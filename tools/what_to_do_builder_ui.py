import os
import json
import shutil
import subprocess
import re
from pathlib import Path

import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image

# =========================
# CONFIG
# =========================

BASE_DIR = Path(__file__).resolve().parent.parent

WHAT_TO_DO_DIR = BASE_DIR / "data" / "what-to-do"
INDEX_FILE = WHAT_TO_DO_DIR / "what-to-do-index.json"

IMAGE_SIZE = (1200, 800)

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

selected_images = []

# =========================
# HELPERS
# =========================
def slugify(text):

    text = text.strip().lower()

    text = re.sub(
        r"[^\w\s-]",
        "",
        text
    )

    text = re.sub(
        r"[\s_]+",
        "-",
        text
    )

    return text.strip("-")


def ensure_index_exists():
    WHAT_TO_DO_DIR.mkdir(parents=True, exist_ok=True)

    if not INDEX_FILE.exists():
        with open(INDEX_FILE, "w", encoding="utf-8") as f:
            json.dump([], f, indent=2, ensure_ascii=False)


def process_images(item_id, image_paths):

    images_dir = WHAT_TO_DO_DIR / item_id / "images"

    images_dir.mkdir(parents=True, exist_ok=True)

    generated = []

    for i, image_path in enumerate(image_paths, start=1):

        image = Image.open(image_path).convert("RGB")

        image = image.resize(IMAGE_SIZE)

        output_name = f"{item_id}{i}.webp"

        output_path = images_dir / output_name

        image.save(output_path, "WEBP", quality=90)

        generated.append(output_name)

    return generated


def git_commit(commit_message):
    try:
        subprocess.run(["git", "add", "."], cwd=BASE_DIR)

        subprocess.run(
            ["git", "commit", "-m", commit_message],
            cwd=BASE_DIR
        )

        messagebox.showinfo(
            "Success",
            "Generated and committed successfully!"
        )

    except Exception as e:
        messagebox.showerror("Git Error", str(e))


def unescape_kotlin_string(value):
    return (
        value
        .replace(r"\n", "\n")
        .replace(r"\"", '"')
        .replace(r"\\", "\\")
    )


def extract_kotlin_string(text, field_name):
    pattern = rf'{field_name}\s*=\s*"((?:\\.|[^"\\])*)"'
    match = re.search(pattern, text, re.DOTALL)

    if not match:
        return ""

    return unescape_kotlin_string(match.group(1)).strip()


def extract_kotlin_list(text, field_name):
    pattern = rf'{field_name}\s*=\s*listOf\s*\((.*?)\)'
    match = re.search(pattern, text, re.DOTALL)

    if not match:
        return []

    list_body = match.group(1)

    values = re.findall(
        r'"((?:\\.|[^"\\])*)"',
        list_body,
        re.DOTALL
    )

    return [
        unescape_kotlin_string(value).strip()
        for value in values
        if value.strip()
    ]


def extract_kotlin_number(text, field_name):
    pattern = rf'{field_name}\s*=\s*(-?\d+(?:\.\d+)?)'
    match = re.search(pattern, text)

    if not match:
        return ""

    return match.group(1).strip()


def set_entry_value(entry, value):
    entry.delete(0, "end")
    entry.insert(0, value or "")


def set_textbox_value(textbox, value):
    textbox.delete("1.0", "end")
    textbox.insert("1.0", value or "")


# =========================
# KOTLIN IMPORT
# =========================

def convert_kotlin_item():
    kotlin_text = kotlin_import_text.get("1.0", "end").strip()

    if not kotlin_text:
        messagebox.showerror(
            "Convert",
            "Paste one complete Kotlin WhatToDoItem first."
        )
        return

    item_id = extract_kotlin_string(kotlin_text, "id")
    title_en = extract_kotlin_string(kotlin_text, "titleEn")
    title_ro = extract_kotlin_string(kotlin_text, "titleRo")
    category_en = extract_kotlin_string(kotlin_text, "categoryEn")
    category_ro = extract_kotlin_string(kotlin_text, "categoryRo")
    address = extract_kotlin_string(kotlin_text, "address")
    hours_en = extract_kotlin_string(kotlin_text, "hoursEn")
    hours_ro = extract_kotlin_string(kotlin_text, "hoursRo")
    website = extract_kotlin_string(kotlin_text, "website")
    facebook = extract_kotlin_string(kotlin_text, "facebook")
    phone = extract_kotlin_string(kotlin_text, "phone")
    price = extract_kotlin_string(kotlin_text, "price")
    description_en = extract_kotlin_string(kotlin_text, "descriptionEn")
    description_ro = extract_kotlin_string(kotlin_text, "descriptionRo")

    beaches = extract_kotlin_list(kotlin_text, "beaches")

    lat = extract_kotlin_number(kotlin_text, "lat")
    lon = extract_kotlin_number(kotlin_text, "lon")

    set_entry_value(id_entry, item_id)
    set_entry_value(title_en_entry, title_en)
    set_entry_value(title_ro_entry, title_ro)
    set_entry_value(category_en_entry, category_en)
    set_entry_value(category_ro_entry, category_ro)
    set_entry_value(address_entry, address)
    set_entry_value(price_entry, price)
    set_entry_value(hours_en_entry, hours_en)
    set_entry_value(hours_ro_entry, hours_ro)
    set_entry_value(website_entry, website)
    set_entry_value(facebook_entry, facebook)
    set_entry_value(lat_entry, lat)
    set_entry_value(lon_entry, lon)
    set_entry_value(phone_entry, phone)

    set_textbox_value(description_en_text, description_en)
    set_textbox_value(description_ro_text, description_ro)
    set_textbox_value(beaches_text, "\n".join(beaches))

    missing = []

    if not item_id:
        missing.append("ID")

    if not title_en:
        missing.append("Title EN")

    if not category_en:
        missing.append("Category EN")

    if not category_ro:
        missing.append("Category RO")

    if not beaches:
        missing.append("Related Beaches")

    if missing:
        messagebox.showwarning(
            "Convert completed with warnings",
            "The form was filled, but these fields were not found:\n\n"
            + "\n".join(f"• {field}" for field in missing)
        )
    else:
        messagebox.showinfo(
            "Convert",
            "Kotlin item converted successfully.\n\nNow select images, validate, then generate."
        )


# =========================
# IMAGE PICKER
# =========================

def pick_images():
    global selected_images
    files = filedialog.askopenfilenames(
        title="Select Images",
        filetypes=[
            ("Images", "*.png *.jpg *.jpeg *.webp")
        ]
    )

    selected_images = list(files)

    images_label.configure(
        text=f"{len(selected_images)} images selected"
    )


# =========================
# GENERATE
# =========================

def generate_item():
    ensure_index_exists()

    item_id = id_entry.get().strip()

    beaches = [
        x.strip()
        for x in beaches_text.get("1.0", "end")
        .strip()
        .splitlines()
        if x.strip()
    ]

    title_en = title_en_entry.get().strip()
    title_ro = title_ro_entry.get().strip()
    category_en = category_en_entry.get().strip()
    category_ro = category_ro_entry.get().strip()

    address = address_entry.get().strip()

    hours_en = hours_en_entry.get().strip()
    hours_ro = hours_ro_entry.get().strip()

    website = website_entry.get().strip()
    facebook = facebook_entry.get().strip()
    lat = lat_entry.get().strip()
    lon = lon_entry.get().strip()
    phone = phone_entry.get().strip()
    price = price_entry.get().strip()

    description_en = description_en_text.get("1.0", "end").strip()
    description_ro = description_ro_text.get("1.0", "end").strip()

    required_errors = validate_required_fields(show_success=False)

    if required_errors:
        messagebox.showerror(
            "Generate blocked",
            "Please fix these fields before generating:\n\n"
            + "\n".join(f"• {error}" for error in required_errors)
        )
        return

    images = process_images(item_id, selected_images)

    item_folder = WHAT_TO_DO_DIR / item_id
    item_folder.mkdir(parents=True, exist_ok=True)
    item_data = {
        "id": item_id,
        "type": "what_to_do",
        "beaches": beaches,
        "titleEn": title_en,
        "titleRo": title_ro,
        "categoryEn": category_en,
        "categoryRo": category_ro,
        "address": address,
        "hoursEn": hours_en,
        "hoursRo": hours_ro,
        "website": website,
        "facebook": facebook,
        "coordinates": {
         "lat": float(lat) if lat else 0,
         "lon": float(lon) if lon else 0
        },
        "phone": phone,
        "price": price,
        "descriptionEn": description_en,
        "descriptionRo": description_ro,
        "images": images
    }

    with open(
        item_folder / "index.json",
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(item_data, f, indent=2, ensure_ascii=False)

    with open(INDEX_FILE, "r", encoding="utf-8") as f:

        current_index = json.load(f)

    current_index = [

        x for x in current_index

        if x.get("id") != item_id

    ]

    current_index.append({

        "id": item_id,

        "type": "what_to_do",

        "beaches": beaches

    })

    with open(INDEX_FILE, "w", encoding="utf-8") as f:

        json.dump(
         current_index,
         f,
         indent=2,
         ensure_ascii=False
        )

    git_commit(f"Add what to do item {item_id}")


# =========================
# VALIDATE
# =========================

def validate_required_fields(show_success=True):

    errors = []

    item_id = id_entry.get().strip()

    beaches = [
        x.strip()
        for x in beaches_text.get("1.0", "end")
        .strip()
        .splitlines()
        if x.strip()
    ]

    required_entries = [
        ("ID", item_id),
        ("Title EN", title_en_entry.get().strip()),
        ("Title RO", title_ro_entry.get().strip()),
        ("Category EN", category_en_entry.get().strip()),
        ("Category RO", category_ro_entry.get().strip()),
        ("Related Beaches", beaches),
        ("Address", address_entry.get().strip()),
        ("Hours EN", hours_en_entry.get().strip()),
        ("Hours RO", hours_ro_entry.get().strip()),
        ("Website", website_entry.get().strip()),
        ("Phone", phone_entry.get().strip()),
        ("Description EN", description_en_text.get("1.0", "end").strip()),
        ("Description RO", description_ro_text.get("1.0", "end").strip()),
    ]

    for label, value in required_entries:
        if not value:
            errors.append(f"{label} missing")

    if not selected_images:
        errors.append("No images selected")

    if errors and show_success:
        messagebox.showerror(
            "Validation failed",
            "Please fix these fields:\n\n"
            + "\n".join(f"• {error}" for error in errors)
        )

    elif show_success:
        messagebox.showinfo(
            "Validation",
            "Everything looks good!"
        )

    return errors


def validate_data():
    validate_required_fields(show_success=True)


# =========================
# UI
# =========================

app = ctk.CTk()
app.geometry("1450x1080")
app.title("What To Do Builder")

main = ctk.CTkScrollableFrame(app)
main.pack(fill="both", expand=True, padx=20, pady=20)

# =========================
# KOTLIN IMPORT
# =========================

import_frame = ctk.CTkFrame(main)
import_frame.pack(fill="x", pady=10)

ctk.CTkLabel(
    import_frame,
    text="Paste Kotlin Item Here"
).pack(anchor="w", padx=10, pady=(10, 0))

ctk.CTkLabel(
    import_frame,
    text="Paste one complete WhatToDoItem(...) object, then press Convert."
).pack(anchor="w", padx=10, pady=(0, 10))

kotlin_import_text = ctk.CTkTextbox(import_frame, height=180)
kotlin_import_text.pack(fill="x", padx=10, pady=10)

convert_button = ctk.CTkButton(
    import_frame,
    text="Convert",
    height=45,
    command=convert_kotlin_item
)
convert_button.pack(anchor="w", padx=10, pady=(0, 10))

# =========================
# ROW 1
# =========================
row1 = ctk.CTkFrame(main)
row1.pack(fill="x", pady=10)

left1 = ctk.CTkFrame(row1)
left1.pack(side="left", fill="both", expand=True, padx=10)

right1 = ctk.CTkFrame(row1)
right1.pack(side="left", fill="both", expand=True, padx=10)

ctk.CTkLabel(left1, text="ID").pack(anchor="w", padx=10)
id_entry = ctk.CTkEntry(left1)
id_entry.pack(fill="x", padx=10, pady=10)

ctk.CTkLabel(left1, text="Title EN").pack(anchor="w", padx=10)
title_en_entry = ctk.CTkEntry(left1)
title_en_entry.pack(fill="x", padx=10, pady=10)

ctk.CTkLabel(left1, text="Title RO").pack(anchor="w", padx=10)
title_ro_entry = ctk.CTkEntry(left1)
title_ro_entry.pack(fill="x", padx=10, pady=10)

ctk.CTkLabel(left1, text="Category EN").pack(anchor="w", padx=10)
category_en_entry = ctk.CTkEntry(left1)
category_en_entry.pack(fill="x", padx=10, pady=10)

ctk.CTkLabel(left1, text="Category RO").pack(anchor="w", padx=10)
category_ro_entry = ctk.CTkEntry(left1)
category_ro_entry.pack(fill="x", padx=10, pady=10)

ctk.CTkLabel(right1, text="Related Beaches (one per line)").pack(anchor="w", padx=10, pady=(10,0))
beaches_text = ctk.CTkTextbox(right1, height=90)
beaches_text.pack(fill="x", padx=10, pady=10)
ctk.CTkLabel(right1, text="Address").pack(anchor="w", padx=10)
address_entry = ctk.CTkEntry(right1)
address_entry.pack(fill="x", padx=10, pady=10)

ctk.CTkLabel(right1, text="Price").pack(anchor="w", padx=10)
price_entry = ctk.CTkEntry(right1)
price_entry.pack(fill="x", padx=10, pady=10)

# =========================
# ROW 2
# =========================

row2 = ctk.CTkFrame(main)
row2.pack(fill="x", pady=10)

left2 = ctk.CTkFrame(row2)
left2.pack(side="left", fill="both", expand=True, padx=10)

right2 = ctk.CTkFrame(row2)
right2.pack(side="left", fill="both", expand=True, padx=10)

ctk.CTkLabel(left2, text="Hours EN").pack(anchor="w", padx=10, pady=(10,0))
hours_en_entry = ctk.CTkEntry(left2)
hours_en_entry.pack(fill="x", padx=10, pady=10)

ctk.CTkLabel(left2, text="Hours RO").pack(anchor="w", padx=10)
hours_ro_entry = ctk.CTkEntry(left2)
hours_ro_entry.pack(fill="x", padx=10, pady=10)

ctk.CTkLabel(left2, text="Website").pack(anchor="w", padx=10)
website_entry = ctk.CTkEntry(left2)
website_entry.pack(fill="x", padx=10, pady=10)
ctk.CTkLabel(left2, text="Facebook").pack(anchor="w", padx=10)
facebook_entry = ctk.CTkEntry(left2)
facebook_entry.pack(fill="x", padx=10, pady=10)

ctk.CTkLabel(right2, text="Latitude").pack(anchor="w", padx=10, pady=(10,0))

lat_entry = ctk.CTkEntry(right2)

lat_entry.pack(fill="x", padx=10, pady=10)

ctk.CTkLabel(right2, text="Longitude").pack(anchor="w", padx=10)

lon_entry = ctk.CTkEntry(right2)

lon_entry.pack(fill="x", padx=10, pady=10)

ctk.CTkLabel(right2, text="Phone").pack(anchor="w", padx=10)
phone_entry = ctk.CTkEntry(right2)
phone_entry.pack(fill="x", padx=10, pady=10)

images_button = ctk.CTkButton(
    right2,
    text="Select Images",
    command=pick_images
)
images_button.pack(padx=10, pady=20)

images_label = ctk.CTkLabel(
    right2,
    text="No images selected"
)
images_label.pack(padx=10, pady=(0,10))

# =========================
# ROW 3
# =========================

row3 = ctk.CTkFrame(main)
row3.pack(fill="x", pady=10)
left3 = ctk.CTkFrame(row3)
left3.pack(side="left", fill="both", expand=True, padx=10)

right3 = ctk.CTkFrame(row3)
right3.pack(side="left", fill="both", expand=True, padx=10)

ctk.CTkLabel(left3, text="Description EN").pack(anchor="w", padx=10, pady=(10,0))
description_en_text = ctk.CTkTextbox(left3, height=150)
description_en_text.pack(fill="both", expand=True, padx=10, pady=10)

ctk.CTkLabel(right3, text="Description RO").pack(anchor="w", padx=10, pady=(10,0))
description_ro_text = ctk.CTkTextbox(right3, height=150)
description_ro_text.pack(fill="both", expand=True, padx=10, pady=10)

# =========================
# BUTTONS
# =========================

buttons = ctk.CTkFrame(main)
buttons.pack(fill="x", pady=20)

validate_button = ctk.CTkButton(
    buttons,
    text="Validate",
    height=50,
    command=validate_data
)
validate_button.pack(side="left", padx=10, pady=10)

generate_button = ctk.CTkButton(
    buttons,
    text="Generate + Git Commit",
    height=50,
    command=generate_item
)
generate_button.pack(side="left", padx=10, pady=10)

app.mainloop()
