import os
import json
import re
import customtkinter as ctk
import subprocess
from tkinter import filedialog
from PIL import Image, ImageOps

# =========================
# PATHS
# =========================

ROOT_DIR = os.path.dirname(
    os.path.dirname(__file__)
)

DATA_DIR = os.path.join(
    ROOT_DIR,
    "data",
    "local-businesses"
)

INDEX_FILE = os.path.join(
    DATA_DIR,
    "local-businesses-index.json"
)

hero_image = None
gallery_images = []

validated = False

# =========================
# APP
# =========================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()

app.title("Local Business Builder")

app.geometry("1700x1020")

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

def auto_git_commit(slug):

    try:

        subprocess.run(
            [
                "git",
                "add",
                "data/local-businesses",
                "tools/local_business_builder_ui.py"
            ],
            cwd=ROOT_DIR,
            check=True
    )

        diff_check = subprocess.run(
            ["git", "diff", "--cached", "--quiet"],
            cwd=ROOT_DIR
        )

        if diff_check.returncode == 0:
            return "No changes to commit"

        subprocess.run(
            ["git", "commit", "-m", f"Add local business {slug}"],
            cwd=ROOT_DIR,
            check=True
        )

        return "✅ Business generated and committed.\nRun:\ngit pull --rebase\ngit push"

    except Exception as e:

        return f"Generated, but Git commit failed: {e}"

# =========================
# IMAGE PICKER
# =========================

def select_hero_image():

    global hero_image

    hero_image = filedialog.askopenfilename(

        title="Select Hero Image",

        filetypes=[
            ("Images", "*.png *.jpg *.jpeg *.webp")
        ]
    )

    if hero_image:

        hero_label.configure(
            text="Hero image selected"
        )

def select_gallery_images():

    global gallery_images

    gallery_images = filedialog.askopenfilenames(

        title="Select Gallery Images",

        filetypes=[
            ("Images", "*.png *.jpg *.jpeg *.webp")
        ]
    )

    gallery_label.configure(
        text=f"{len(gallery_images)} gallery images selected"
    )

# =========================
# VALIDATION
# =========================

def validate_business():

    global validated

    title_en = title_en_entry.get().strip()

    beaches = beaches_entry.get().strip()

    address = address_entry.get().strip()

    if not address:

        status_label.configure(
            text="Missing address",
            text_color="#ff5a5a"
        )

        validated = False
        return

    try:

        float(latitude_entry.get().strip())
        float(longitude_entry.get().strip())

    except ValueError:

        status_label.configure(
            text="Invalid GPS coordinates",
            text_color="#ff5a5a"
        )

        validated = False
        return
    
    

    if not title_en:

        status_label.configure(
            text="Missing Title EN",
            text_color="#ff5a5a"
        )

        validated = False
        return

    if not beaches:

        status_label.configure(
            text="Missing beaches",
            text_color="#ff5a5a"
        )

        validated = False
        return

    if not hero_image:

        status_label.configure(
            text="Select Hero Image",
            text_color="#ff5a5a"
        )

        validated = False
        return

    if len(gallery_images) == 0:

        status_label.configure(
            text="Select Gallery Images",
            text_color="#ff5a5a"
        )

        validated = False
        return

    slug = slugify(title_en)

    business_dir = os.path.join(
        DATA_DIR,
        slug
    )

    if os.path.exists(business_dir):

        status_label.configure(
            text="Business already exists",
            text_color="#ff5a5a"
        )

        validated = False
        return

    validated = True

    slug_preview.configure(
        text=f"Slug: {slug}"
    )

    status_label.configure(
        text="Validation successful",
        text_color="#3ddc84"
    )

# =========================
# GENERATOR
# =========================

def generate_business():

    global validated

    if not validated:

        status_label.configure(
            text="Validate first",
            text_color="#ff5a5a"
        )

        return

    title_en = title_en_entry.get().strip()

    title_ro = title_ro_entry.get().strip()

    slug = slugify(title_en)

    beaches = beaches_entry.get().strip()

    category_en = category_en_entry.get().strip()

    category_ro = category_ro_entry.get().strip()

    phone = phone_entry.get().strip()

    whatsapp = whatsapp_entry.get().strip()

    website = website_entry.get().strip()

    address = address_entry.get().strip()

    latitude = float(
        latitude_entry.get().strip()
    )

    longitude = float(
    longitude_entry.get().strip()
    )

    booking = booking_switch.get()

    hours_en = hours_en_entry.get().strip()

    hours_ro = hours_ro_entry.get().strip()

    description_en = description_en_box.get(
        "1.0",
        "end"
    ).strip()

    description_ro = description_ro_box.get(
        "1.0",
        "end"
    ).strip()

    beaches_list = [

    slugify(beach)

    for beach in beaches.split(",")

    if beach.strip()

    ]

    # =========================
    # CREATE DIRS
    # =========================

    business_dir = os.path.join(
        DATA_DIR,
        slug
    )

    images_dir = os.path.join(
        business_dir,
        "images"
    )

    os.makedirs(
        images_dir,
        exist_ok=True
    )

    # =========================
    # SAVE IMAGES
    # =========================

    # =========================
    # SAVE HERO
    # =========================

    hero = Image.open(hero_image).convert("RGB")

    hero = ImageOps.fit(
        hero,
        (1200, 800),
        Image.LANCZOS
    )

    hero.save(
        os.path.join(images_dir, "hero.webp"),
        "WEBP",
        quality=92
    )

    # =========================
    # SAVE THUMBNAIL
    # =========================

    thumbnail = ImageOps.fit(
        hero,
        (600, 400),
        Image.LANCZOS
    )

    thumbnail.save(
        os.path.join(images_dir, "thumbnail.webp"),
        "WEBP",
        quality=90
    )

    # =========================
    # SAVE GALLERY
    # =========================

    image_names = []

    for index, image_path in enumerate(gallery_images):

        image = Image.open(image_path).convert("RGB")

        image = ImageOps.fit(
            image,
            (1200, 800),
            Image.LANCZOS
        )

        image_name = f"business{index + 1}.webp"

        image.save(
            os.path.join(images_dir, image_name),
            "WEBP",
            quality=92
        )

        image_names.append(image_name)

    # =========================
    # BUSINESS JSON
    # =========================

    business_data = {

        "id": slug,

        "type": "local_business",

        "booking": booking,

        "beaches": beaches_list,

        "titleEn": title_en,

        "titleRo": title_ro,

        "categoryEn": category_en,

        "categoryRo": category_ro,

        "phone": phone,

        "whatsapp": whatsapp,

        "website": website,

        "instagram": "",

        "facebook": "",

        "address": address,

        "lat": latitude,
        "lon": longitude,

        "coordinates": {
            "lat": latitude,
            "lng": longitude
        },

        "hours": {
            "en": hours_en,
            "ro": hours_ro
        },

        "descriptionEn": description_en,

        "descriptionRo": description_ro,

        "heroImage": "hero.webp",

        "thumbnail": "thumbnail.webp",

        "images": image_names

    }

    with open(

        os.path.join(
            business_dir,
            "index.json"
        ),

        "w",

        encoding="utf-8"

    ) as f:

        json.dump(
            business_data,
            f,
            ensure_ascii=False,
            indent=2
        )

    # =========================
    # UPDATE INDEX
    # =========================

    if os.path.exists(INDEX_FILE):

        with open(
            INDEX_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            index_data = json.load(f)

    else:

        index_data = []

    index_data.append({

        "id": slug,

        "type": "local_business",

        "titleEn": title_en,

        "category": category_en,

        "beaches": beaches_list,

        "lat": latitude,

        "lon": longitude,

        "thumbnail": "thumbnail.webp",

        "heroImage": "hero.webp"

    })

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

    git_message = auto_git_commit(slug)

    status_label.configure(
        text=git_message,
        text_color="#3ddc84"
    )

# =========================
# UI
# =========================

title = ctk.CTkLabel(

    app,

    text="Local Business Builder",

    font=("Arial", 30, "bold")
)

title.pack(pady=20)

# =========================
# MAIN FRAME
# =========================

main_frame = ctk.CTkFrame(
    app,
    fg_color="transparent"
)

main_frame.pack(
    fill="both",
    expand=True,
    padx=30,
    pady=10
)

# =========================
# LEFT
# =========================

left_frame = ctk.CTkScrollableFrame(
    main_frame
)

left_frame.pack(
    side="left",
    fill="both",
    expand=True,
    padx=(0, 10)
)

# =========================
# RIGHT
# =========================

right_frame = ctk.CTkScrollableFrame(
    main_frame
)

right_frame.pack(
    side="left",
    fill="both",
    expand=True,
    padx=(10, 0)
)

# =========================
# ENTRY HELPER
# =========================

def create_entry(parent, label_text):

    label = ctk.CTkLabel(
        parent,
        text=label_text
    )

    label.pack(
        anchor="w",
        padx=20,
        pady=(14, 4)
    )

    entry = ctk.CTkEntry(
        parent,
        width=500,
        height=40
    )

    entry.pack(
        padx=20
    )

    return entry

# =========================
# LEFT ENTRIES
# =========================

title_en_entry = create_entry(
    left_frame,
    "Title EN"
)

title_ro_entry = create_entry(
    left_frame,
    "Title RO"
)

beaches_entry = create_entry(
    left_frame,
    "Beaches (comma separated)"
)

category_en_entry = create_entry(
    left_frame,
    "Category EN"
)

category_ro_entry = create_entry(
    left_frame,
    "Category RO"
)

phone_entry = create_entry(
    left_frame,
    "Phone"
)

whatsapp_entry = create_entry(
    left_frame,
    "WhatsApp"
)

website_entry = create_entry(
    left_frame,
    "Website"
)

address_entry = create_entry(
    left_frame,
    "Address"
)

latitude_entry = create_entry(
    left_frame,
    "Latitude"
)

longitude_entry = create_entry(
    left_frame,
    "Longitude"
)

hours_en_entry = create_entry(
    left_frame,
    "Hours EN"
)

hours_ro_entry = create_entry(
    left_frame,
    "Hours RO"
)

# =========================
# RIGHT SIDE
# =========================

desc_en_label = ctk.CTkLabel(
    right_frame,
    text="Description EN"
)

desc_en_label.pack(
    anchor="w",
    padx=20,
    pady=(14, 4)
)

description_en_box = ctk.CTkTextbox(
    right_frame,
    width=500,
    height=170
)

description_en_box.pack(
    padx=20
)

# =========================

desc_ro_label = ctk.CTkLabel(
    right_frame,
    text="Description RO"
)

desc_ro_label.pack(
    anchor="w",
    padx=20,
    pady=(18, 4)
)

description_ro_box = ctk.CTkTextbox(
    right_frame,
    width=500,
    height=170
)

description_ro_box.pack(
    padx=20
)

# =========================
# BOOKING
# =========================

booking_switch = ctk.CTkSwitch(
    right_frame,
    text="Booking Available"
)

booking_switch.pack(
    anchor="w",
    padx=20,
    pady=20
)

# =========================
# IMAGES
# =========================

hero_button = ctk.CTkButton(
    right_frame,
    text="Select Hero Image",
    height=44,
    command=select_hero_image
)

hero_button.pack(
    padx=20,
    pady=(10, 6),
    fill="x"
)

hero_label = ctk.CTkLabel(
    right_frame,
    text="No hero image selected"
)

hero_label.pack(
    anchor="w",
    padx=20
)

gallery_button = ctk.CTkButton(
    right_frame,
    text="Select Gallery Images",
    height=44,
    command=select_gallery_images
)

gallery_button.pack(
    padx=20,
    pady=(16, 6),
    fill="x"
)

gallery_label = ctk.CTkLabel(
    right_frame,
    text="No gallery images selected"
)

gallery_label.pack(
    anchor="w",
    padx=20
)

# =========================
# SLUG PREVIEW
# =========================

slug_preview = ctk.CTkLabel(
    right_frame,
    text="Slug: -"
)

slug_preview.pack(
    anchor="w",
    padx=20,
    pady=(16, 6)
)

# =========================
# BUTTONS
# =========================

validate_button = ctk.CTkButton(

    right_frame,

    text="Validate Business",

    height=50,

    font=("Arial", 16, "bold"),

    fg_color="#1f6aa5",

    command=validate_business
)

validate_button.pack(
    padx=20,
    pady=(18, 10),
    fill="x"
)

# =========================

generate_button = ctk.CTkButton(

    right_frame,

    text="Generate Business",

    height=54,

    font=("Arial", 17, "bold"),

    fg_color="#179c52",

    command=generate_business
)

generate_button.pack(
    padx=20,
    pady=(0, 18),
    fill="x"
)

# =========================
# STATUS
# =========================

status_label = ctk.CTkLabel(
    right_frame,
    text=""
)

status_label.pack(
    pady=(0, 20)
)

# =========================

app.mainloop()