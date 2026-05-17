# restaurant_builder_ui_v2.py

import re
import json
import shutil
import subprocess
import tkinter as tk

from tkinter import ttk, filedialog, messagebox
from pathlib import Path

from PIL import Image, ImageTk

# =========================================
# CONFIG
# =========================================

REPO_RAW_BASE = "https://raw.githubusercontent.com/gabridim18-lab/halkidiki-data/main"

# =========================================
# HELPERS
# =========================================

def slugify(text: str) -> str:

    text = text.strip().lower()

    text = re.sub(r"[^\w\s-]", "", text)

    text = re.sub(r"[\s-]+", "_", text)

    return text.strip("_")

def save_json(path: Path, data: dict):

    path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    path.write_text(

        json.dumps(
            data,
            ensure_ascii=False,
            indent=2
        ),

        encoding="utf-8"
    )

def ensure_1200x800_webp(src_path, dst_path):

    dst_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with Image.open(src_path) as im:

        im = im.convert("RGB")

        target_w = 1200
        target_h = 800

        src_w, src_h = im.size

        src_ratio = src_w / src_h
        target_ratio = target_w / target_h

        # crop center

        if src_ratio > target_ratio:

            new_w = int(src_h * target_ratio)

            left = (src_w - new_w) // 2

            im = im.crop(
                (left, 0, left + new_w, src_h)
            )

        else:

            new_h = int(src_w / target_ratio)

            top = (src_h - new_h) // 2

            im = im.crop(
                (0, top, src_w, top + new_h)
            )

        im = im.resize(
            (target_w, target_h),
            Image.LANCZOS
        )

        im.save(
            dst_path,
            format="WEBP",
            quality=82,
            method=6
        )

def run_cmd(cmd, cwd):

    try:

        p = subprocess.run(

            cmd,

            cwd=str(cwd),

            capture_output=True,

            text=True,

            shell=False

        )

        output = (

            (p.stdout or "")
            +
            ("\n" + p.stderr if p.stderr else "")

        )

        return p.returncode == 0, output

    except Exception as e:

        return False, str(e)

# =========================================
# APP
# =========================================

class App(tk.Tk):

    def __init__(self):

        super().__init__()

        self.title(
            "Restaurant Builder PRO"
        )

        self.geometry("1450x900")

        self.minsize(1200, 800)

        self.repo_root = Path.cwd()

        self.rest_root = (
            self.repo_root
            / "data"
            / "restaurants"
        )

        self.index_path = (
            self.rest_root
            / "restaurants-index.json"
        )

        self.business_images = []

        self.menu_images = []

        self.preview_img = None

        self.last_slug = None

        self.build_ui()

    # =========================================

    def build_ui(self):

        root = ttk.Frame(
            self,
            padding=10
        )

        root.pack(
            fill="both",
            expand=True
        )

        # =========================================
        # LEFT
        # =========================================

        left = ttk.Frame(root)

        left.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(0, 10)
        )

        # =========================================
        # RIGHT
        # =========================================

        right = ttk.Frame(root)

        right.pack(
            side="right",
            fill="y"
        )

        # =========================================
        # FORM
        # =========================================

        form = ttk.LabelFrame(
            left,
            text="Business Details",
            padding=10
        )

        form.pack(
            fill="both",
            expand=True
        )

        def row(label, widget, r):

            ttk.Label(
                form,
                text=label
            ).grid(
                row=r,
                column=0,
                sticky="w",
                padx=(0, 10),
                pady=5
            )

            widget.grid(
                row=r,
                column=1,
                sticky="ew",
                pady=5
            )

            form.grid_columnconfigure(
                1,
                weight=1
            )

        # =========================================
        # VARIABLES
        # =========================================

        self.var_title_en = tk.StringVar()
        self.var_title_ro = tk.StringVar()

        self.var_slug = tk.StringVar()

        self.var_beach_slug = tk.StringVar()

        self.var_type = tk.StringVar(
            value="restaurant"
        )

        self.var_featured = tk.BooleanVar()

        self.var_address = tk.StringVar()

        self.var_display_address = tk.StringVar()

        self.var_hours_en = tk.StringVar()

        self.var_hours_ro = tk.StringVar()

        self.var_website = tk.StringVar()

        self.var_facebook = tk.StringVar()

        self.var_instagram = tk.StringVar()

        self.var_phone = tk.StringVar()

        self.var_price = tk.StringVar(
            value="$$"
        )

        self.var_rating = tk.StringVar(
            value="4.5"
        )

        self.var_sunbed_price = tk.StringVar()

        self.var_consumation = tk.BooleanVar()

        # =========================================
        # ROWS
        # =========================================

        row(
            "Title EN",
            ttk.Entry(
                form,
                textvariable=self.var_title_en
            ),
            0
        )

        row(
            "Title RO",
            ttk.Entry(
                form,
                textvariable=self.var_title_ro
            ),
            1
        )

        slug_frame = ttk.Frame(form)

        ttk.Entry(
            slug_frame,
            textvariable=self.var_slug
        ).pack(
            side="left",
            fill="x",
            expand=True
        )

        ttk.Button(

            slug_frame,

            text="Create Slug",

            command=self.auto_slug

        ).pack(
            side="left",
            padx=8
        )

        row(
            "Slug",
            slug_frame,
            2
        )

        row(
            "Related Beach",
            ttk.Entry(
                form,
                textvariable=self.var_beach_slug
            ),
            3
        )

        # =========================================
        # TYPE
        # =========================================

        type_box = ttk.Combobox(

            form,

            textvariable=self.var_type,

            values=[
                "restaurant",
                "beach_bar"
            ],

            state="readonly"

        )

        row(
            "Type",
            type_box,
            4
        )

        ttk.Checkbutton(

            form,

            text="Featured",

            variable=self.var_featured

        ).grid(
            row=5,
            column=1,
            sticky="w"
        )

        row(
            "Address",
            ttk.Entry(
                form,
                textvariable=self.var_address
            ),
            6
        )

        row(
            "Display Address",
            ttk.Entry(
                form,
                textvariable=self.var_display_address
            ),
            7
        )

        row(
            "Hours EN",
            ttk.Entry(
                form,
                textvariable=self.var_hours_en
            ),
            8
        )

        row(
            "Hours RO",
            ttk.Entry(
                form,
                textvariable=self.var_hours_ro
            ),
            9
        )

        row(
            "Website",
            ttk.Entry(
                form,
                textvariable=self.var_website
            ),
            10
        )

        row(
            "Facebook",
            ttk.Entry(
                form,
                textvariable=self.var_facebook
            ),
            11
        )

        row(
            "Instagram",
            ttk.Entry(
                form,
                textvariable=self.var_instagram
            ),
            12
        )

        row(
            "Phone",
            ttk.Entry(
                form,
                textvariable=self.var_phone
            ),
            13
        )

        price_box = ttk.Combobox(

            form,

            textvariable=self.var_price,

            values=[
                "$",
                "$$",
                "$$$"
            ],

            state="readonly"

        )

        row(
            "Price",
            price_box,
            14
        )

        row(
            "Rating",
            ttk.Entry(
                form,
                textvariable=self.var_rating
            ),
            15
        )

        row(
            "Sunbed Price",
            ttk.Entry(
                form,
                textvariable=self.var_sunbed_price
            ),
            16
        )

        ttk.Checkbutton(

            form,

            text="Consumation Included",

            variable=self.var_consumation

        ).grid(
            row=17,
            column=1,
            sticky="w"
        )

        # =========================================
        # DESCRIPTIONS
        # =========================================

        desc_frame = ttk.LabelFrame(

            left,

            text="Descriptions",

            padding=10

        )

        desc_frame.pack(
            fill="both",
            expand=True,
            pady=(10, 0)
        )

        desc_frame.grid_columnconfigure(
            0,
            weight=1
        )

        desc_frame.grid_columnconfigure(
            1,
            weight=1
        )

        ttk.Label(
            desc_frame,
            text="Description EN"
        ).grid(
            row=0,
            column=0,
            sticky="w"
        )

        ttk.Label(
            desc_frame,
            text="Description RO"
        ).grid(
            row=0,
            column=1,
            sticky="w"
        )

        self.txt_en = tk.Text(
            desc_frame,
            height=10
        )

        self.txt_ro = tk.Text(
            desc_frame,
            height=10
        )

        self.txt_en.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=(0, 5)
        )

        self.txt_ro.grid(
            row=1,
            column=1,
            sticky="nsew",
            padx=(5, 0)
        )

        # =========================================
        # RIGHT SIDE
        # =========================================

        # =========================================
        # MUSIC
        # =========================================

        music_box = ttk.LabelFrame(
            right,
            text="Music Styles",
            padding=10
        )

        music_box.pack(
            fill="x",
            pady=(0, 10)
        )

        self.music_vars = {}

        music_styles = [

            "chill",
            "lounge",
            "party",
            "live_music",
            "dj_sets"

        ]

        for style in music_styles:

            var = tk.BooleanVar()

            self.music_vars[style] = var

            ttk.Checkbutton(

                music_box,

                text=style,

                variable=var

            ).pack(
                anchor="w"
            )

        # =========================================
        # FEATURES
        # =========================================

        feature_box = ttk.LabelFrame(
            right,
            text="Features",
            padding=10
        )

        feature_box.pack(
            fill="x",
            pady=(0, 10)
        )

        self.feature_vars = {}

        features = [

            "sunbeds",
            "cocktails",
            "restaurant",
            "parking",
            "sea_view",
            "sunset_view",
            "family_friendly",
            "pet_friendly",
            "pool",
            "events"

        ]

        for feature in features:

            var = tk.BooleanVar()

            self.feature_vars[feature] = var

            ttk.Checkbutton(

                feature_box,

                text=feature,

                variable=var

            ).pack(
                anchor="w"
            )

        # =========================================
        # IMAGES
        # =========================================

        image_box = ttk.LabelFrame(
            right,
            text="Images",
            padding=10
        )

        image_box.pack(
            fill="both",
            expand=True
        )

        ttk.Button(

            image_box,

            text="Select Business Images",

            command=self.pick_business_images

        ).pack(
            fill="x",
            pady=5
        )

        self.business_label = ttk.Label(
            image_box,
            text="0 images selected"
        )

        self.business_label.pack(
            anchor="w"
        )

        ttk.Button(

            image_box,

            text="Select Menu Images",

            command=self.pick_menu_images

        ).pack(
            fill="x",
            pady=10
        )

        self.menu_label = ttk.Label(
            image_box,
            text="0 menu images selected"
        )

        self.menu_label.pack(
            anchor="w"
        )

        ttk.Label(
            image_box,
            text="Preview"
        ).pack(
            anchor="w",
            pady=(20, 5)
        )

        self.preview_label = ttk.Label(
            image_box
        )

        self.preview_label.pack()

        # =========================================
        # BUTTONS
        # =========================================

        bottom = ttk.Frame(root)

        bottom.pack(
            fill="x",
            pady=(10, 0)
        )

        ttk.Button(

            bottom,

            text="GENERATE FILES",

            command=self.generate

        ).pack(
            side="right"
        )

        ttk.Button(

            bottom,

            text="Git Add + Commit",

            command=self.git_commit

        ).pack(
            side="right",
            padx=10
        )

    # =========================================
    # AUTO SLUG
    # =========================================

    def auto_slug(self):

        title = self.var_title_en.get()

        self.var_slug.set(
            slugify(title)
        )

    # =========================================
    # PICK BUSINESS IMAGES
    # =========================================

    def pick_business_images(self):

        files = filedialog.askopenfilenames(

            title="Select Business Images",

            filetypes=[
                ("Images", "*.jpg *.jpeg *.png *.webp")
            ]

        )

        if not files:
            return

        self.business_images = list(files)

        self.business_label.config(
            text=f"{len(files)} images selected"
        )

        self.load_preview(files[0])

    # =========================================
    # PICK MENU IMAGES
    # =========================================

    def pick_menu_images(self):

        files = filedialog.askopenfilenames(

            title="Select Menu Images",

            filetypes=[
                ("Images", "*.jpg *.jpeg *.png *.webp")
            ]

        )

        if not files:
            return

        self.menu_images = list(files)

        self.menu_label.config(
            text=f"{len(files)} menu images selected"
        )

    # =========================================
    # PREVIEW
    # =========================================

    def load_preview(self, path):

        with Image.open(path) as im:

            im.thumbnail((350, 220))

            self.preview_img = ImageTk.PhotoImage(im)

            self.preview_label.configure(
                image=self.preview_img
            )

    # =========================================
    # GENERATE
    # =========================================

    def generate(self):

        slug = self.var_slug.get().strip()

        if not slug:

            messagebox.showerror(
                "Error",
                "Slug required"
            )

            return

        if slug == self.var_beach_slug.get():

            messagebox.showerror(
                "Error",
                "Business slug cannot be identical to beach slug"
            )

            return

        folder = (
            self.rest_root
            / slug
        )

        images_folder = (
            folder
            / "images"
        )

        images_folder.mkdir(
            parents=True,
            exist_ok=True
        )

      
    # =========================================
    # BUSINESS IMAGES
    # =========================================

        business_urls = []

        for i, image in enumerate(self.business_images):

            name = f"{slug}{i+1}.webp"

            dst = (
                images_folder
                / name
            )

            ensure_1200x800_webp(
                image,
                dst
            )

            business_urls.append(

                f"{REPO_RAW_BASE}/data/restaurants/{slug}/images/{name}"

            )

        # =========================================
        # MENU IMAGES
        # =========================================

        menu_urls = []

        for i, image in enumerate(self.menu_images):

            name = f"menu{i+1}.webp"

            dst = (
                images_folder
                / name
            )

            ensure_1200x800_webp(
                image,
                dst
            )

            menu_urls.append(

                f"{REPO_RAW_BASE}/data/restaurants/{slug}/images/{name}"

            )

        # =========================================
        # MUSIC
        # =========================================

        music = []

        for key, value in self.music_vars.items():

            if value.get():

                music.append(key)

        # =========================================
        # FEATURES
        # =========================================

        features = []

        for key, value in self.feature_vars.items():

            if value.get():

                features.append(key)

        # =========================================
        # JSON
        # =========================================

        data = {

            "id": slug,

            "beachSlug":
                self.var_beach_slug.get(),

            "type":
                self.var_type.get(),

            "featured":
                self.var_featured.get(),

            "titleEn":
                self.var_title_en.get(),

            "titleRo":
                self.var_title_ro.get(),

            "address":
                self.var_address.get(),

            "displayAddress":
                self.var_display_address.get(),

            "hoursEn":
                self.var_hours_en.get(),

            "hoursRo":
                self.var_hours_ro.get(),

            "website":
                self.var_website.get(),

            "facebook":
                self.var_facebook.get(),

            "instagram":
                self.var_instagram.get(),

            "phone":
                self.var_phone.get(),

            "price":
                self.var_price.get(),

            "rating":
                float(self.var_rating.get()),

            "descriptionEn":
                self.txt_en.get(
                    "1.0",
                    tk.END
                ).strip(),

            "descriptionRo":
                self.txt_ro.get(
                    "1.0",
                    tk.END
                ).strip(),

            "images":
                business_urls,

            "menuImages":
                menu_urls,

            "sunbedPrice":
                self.var_sunbed_price.get(),

            "sunbedConsumationIncluded":
                self.var_consumation.get(),

            "musicStyles":
                music,

            "features":
                features

        }

        save_json(
            folder / "index.json",
            data
        )

        # =========================================
        # UPDATE INDEX
        # =========================================

        if self.index_path.exists():

            index_data = json.loads(

                self.index_path.read_text(
                    encoding="utf-8"
                )

            )

        else:

            index_data = []

        found = False

        for item in index_data:

            if item["id"] == slug:

                found = True

        if not found:

          index_data.append({

    "id": slug,

    "type":
        self.var_type.get(),

    "beachSlug":
        self.var_beach_slug.get().strip().lower()

})

        save_json(
            self.index_path,
            index_data
        )

        self.last_slug = slug

        messagebox.showinfo(

            "Success",

            f"{slug} generated successfully!"

        )

    # =========================================
    # GIT COMMIT
    # =========================================

    def git_commit(self):

        if not self.last_slug:

            messagebox.showerror(
                "Error",
                "Generate first"
            )

            return

        ok, out = run_cmd(
            ["git", "add", "."],
            self.repo_root
        )

        if not ok:

            messagebox.showerror(
                "Git Error",
                out
            )

            return

        ok, out = run_cmd(

            [

                "git",

                "commit",

                "-m",

                f"Add restaurant {self.last_slug}"

            ],

            self.repo_root

        )

        if not ok:

            messagebox.showerror(
                "Git Error",
                out
            )

            return

        messagebox.showinfo(

            "Done",

            "Commit created successfully.\n\n"
            "Now run:\n\n"
            "git pull --rebase\n"
            "git push"

        )

# =========================================
# START
# =========================================

if __name__ == "__main__":

    app = App()

    app.mainloop()