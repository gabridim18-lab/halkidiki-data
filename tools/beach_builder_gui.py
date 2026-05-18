import json
import shutil
import subprocess
from pathlib import Path

from PIL import Image
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText

ROOT = Path(__file__).resolve().parent.parent

OUTPUT_BEACHES = ROOT / "data" / "beaches"
INDEX_FILE = OUTPUT_BEACHES / "beaches-index.json"

selected_images = []

# -----------------------------------
# WINDOW
# -----------------------------------

root = tk.Tk()
root.title("Halkidiki Explorer - Beach Builder")
root.geometry("1100x850")
root.configure(bg="#f5f7fb")

# -----------------------------------
# TITLE
# -----------------------------------
label = tk.Label(
    root,
    text="Beach JSON",
    font=("Arial", 18, "bold"),
    bg="#f5f7fb"
)

label.pack(pady=12)

# -----------------------------------
# JSON INPUT
# -----------------------------------

json_input = ScrolledText(
    root,
    width=130,
    height=28,
    font=("Consolas", 11)
)

json_input.pack(padx=20, pady=10)

# -----------------------------------
# IMAGE LIST
# -----------------------------------

images_label = tk.Label(
    root,
    text="Selected Images",
    font=("Arial", 14, "bold"),
    bg="#f5f7fb"
)
images_label.pack(pady=(15, 5))

images_box = tk.Listbox(
    root,
    width=90,
    height=6,
    font=("Arial", 11)
)

images_box.pack(pady=5)

# -----------------------------------
# SELECT IMAGES
# -----------------------------------

def select_images():

    global selected_images

    files = filedialog.askopenfilenames(
        title="Select beach images",
        filetypes=[
            (
                "Images",
                "*.png *.jpg *.jpeg *.webp"
            )
        ]
    )

    if not files:
        return

    selected_images = list(files)

    images_box.delete(0, tk.END)

    for image in selected_images:
        images_box.insert(tk.END, Path(image).name)

# -----------------------------------
# VALIDATE
# -----------------------------------

def validate_json():

    try:

        raw = json_input.get("1.0", tk.END)

        beach = json.loads(raw)

        required = [
            "id",
            "slug",
            "name",
            "zone",
            "coordinates",
            "images",
            "recommendationRating"
        ]

        for field in required:

            if field not in beach:

                messagebox.showerror(
                    "Validation Error",
                    f"Missing field: {field}"
                )

                return

        if "lat" not in beach["coordinates"]:
            messagebox.showerror(
                "Validation Error",
                "Missing coordinates.lat"
            )
            return

        if "lon" not in beach["coordinates"]:
            messagebox.showerror(
                "Validation Error",
                "Missing coordinates.lon"
            )
            return

        if len(selected_images) == 0:

            messagebox.showerror(
                "Validation Error",
                "No images selected"
            )

            return

        messagebox.showinfo(
            "Validation",
            "Beach validated successfully"
        )

    except Exception as e:

        messagebox.showerror(
            "JSON Error",
            str(e)
        )

# -----------------------------------
# BUILD BEACH
# -----------------------------------

def build_beach():

    try:

        raw = json_input.get("1.0", tk.END)

        beach = json.loads(raw)

        slug = beach["slug"]

        beach_folder = OUTPUT_BEACHES / slug
        images_folder = beach_folder / "images"

        beach_folder.mkdir(
            parents=True,
            exist_ok=True
        )

        images_folder.mkdir(
            parents=True,
            exist_ok=True
        )

        # -----------------------------
        # WRITE index.json
        # -----------------------------

        with open(
            beach_folder / "index.json",
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                beach,
                f,
                ensure_ascii=False,
                indent=2
            )

        # -----------------------------
        # COPY IMAGES
        # -----------------------------

        for image_path in selected_images:

            image_path = Path(image_path)

            img = Image.open(image_path)

            img = img.convert("RGB")

            img = img.resize(
                 (1200, 800)
            )

            output_name = (
                image_path.stem + ".webp"
            )

            output_path = (
                images_folder / output_name
            )

            img.save(
                output_path,
                "WEBP",
                quality=88
            )
            
        # -----------------------------
        # LOAD beaches-index.json
        # -----------------------------

        if INDEX_FILE.exists():

            with open(
                INDEX_FILE,
                "r",
                encoding="utf-8"
            ) as f:

                index_data = json.load(f)

        else:

            index_data = []

        # -----------------------------
        # REMOVE EXISTING ID
        # -----------------------------

        index_data = [
            item
            for item in index_data
            if item["id"] != beach["id"]
        ]
        
        # -----------------------------
        # CREATE INDEX ENTRY
        # -----------------------------

        index_entry = {

            "id": beach["id"],

            "zone": beach["zone"],

            "name": beach["name"],

            "previewImage": beach["images"][0],

            "coordinates": beach["coordinates"],

            "rating": beach[
                "recommendationRating"
            ],

            "waterTemperature": beach[
                "water"
            ][
                "averageTemperature"
            ],

            "suitableForChildren": beach[
                "suitableForChildren"
            ]

        }

        index_data.append(index_entry)
        
        # -----------------------------
        # SAVE beaches-index.json
        # -----------------------------

        with open(
            INDEX_FILE,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                index_data,
                f,
                ensure_ascii=False,
                indent=2
            )

        # -----------------------------
        # GIT ADD + COMMIT
        # -----------------------------

        subprocess.run(
            ["git", "add", "."],
            cwd=ROOT
        )

        subprocess.run(
            [
                "git",
                "commit",
                "-m",
                f"Added beach {slug}"
            ],
            cwd=ROOT
        )

        # -----------------------------
        # SUCCESS
        # -----------------------------

        messagebox.showinfo(
            "SUCCESS",
            "Beach generated successfully.\n\nReady for git push."
        )

    except Exception as e:

        messagebox.showerror(
            "Build Error",
            str(e)
        )

# -----------------------------------
# BUTTONS
# -----------------------------------

buttons_frame = tk.Frame(
    root,
    bg="#f5f7fb"
)

buttons_frame.pack(pady=25)

select_btn = tk.Button(
    buttons_frame,
    text="Select Images",
    command=select_images,
    width=18,
    height=2,
    bg="#2f6fed",
    fg="white",
    font=("Arial", 11, "bold")
)

select_btn.grid(row=0, column=0, padx=10)

validate_btn = tk.Button(
    buttons_frame,
    text="Validate",
    command=validate_json,
    width=18,
    height=2,
    bg="#0d9b63",
    fg="white",
    font=("Arial", 11, "bold")
)

validate_btn.grid(row=0, column=1, padx=10)
build_btn = tk.Button(
    buttons_frame,
    text="Build Beach",
    command=build_beach,
    width=18,
    height=2,
    bg="#ff8a00",
    fg="white",
    font=("Arial", 11, "bold")
)

build_btn.grid(row=0, column=2, padx=10)

# -----------------------------------
# START
# -----------------------------------

root.mainloop()