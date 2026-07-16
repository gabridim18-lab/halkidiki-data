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


DAY_ALIASES = {
    "monday": 0, "mon": 0, "luni": 0, "lun": 0,
    "tuesday": 1, "tue": 1, "tues": 1, "marti": 1, "marți": 1, "mar": 1,
    "wednesday": 2, "wed": 2, "miercuri": 2, "mie": 2,
    "thursday": 3, "thu": 3, "thur": 3, "thurs": 3, "joi": 3,
    "friday": 4, "fri": 4, "vineri": 4, "vin": 4,
    "saturday": 5, "sat": 5, "sambata": 5, "sâmbătă": 5, "sam": 5, "sâm": 5,
    "sunday": 6, "sun": 6, "duminica": 6, "duminică": 6, "dum": 6,
}

DAY_NAMES_EN = [
    "Monday", "Tuesday", "Wednesday", "Thursday",
    "Friday", "Saturday", "Sunday"
]

DAY_NAMES_RO = [
    "Luni", "Marți", "Miercuri", "Joi",
    "Vineri", "Sâmbătă", "Duminică"
]


def parse_coordinates(raw_value):
    """Extract latitude and longitude from a pasted pair or Google Maps URL."""

    value = raw_value.strip().replace("−", "-")

    patterns = [
        r"@\s*(-?\d{1,2}(?:\.\d+)?)\s*,\s*(-?\d{1,3}(?:\.\d+)?)",
        r"!3d\s*(-?\d{1,2}(?:\.\d+)?)\s*!4d\s*(-?\d{1,3}(?:\.\d+)?)",
        r"(?:q|query|destination)=\s*(-?\d{1,2}(?:\.\d+)?)\s*%2C\s*(-?\d{1,3}(?:\.\d+)?)",
        r"(?:q|query|destination)=\s*(-?\d{1,2}(?:\.\d+)?)\s*,\s*(-?\d{1,3}(?:\.\d+)?)",
        r"(-?\d{1,2}(?:\.\d+)?)\s*[,;]\s*(-?\d{1,3}(?:\.\d+)?)",
        r"(-?\d{1,2}(?:\.\d+)?)\s+(-?\d{1,3}(?:\.\d+)?)",
    ]

    for pattern in patterns:
        match = re.search(pattern, value, flags=re.IGNORECASE)

        if not match:
            continue

        latitude = float(match.group(1))
        longitude = float(match.group(2))

        if -90 <= latitude <= 90 and -180 <= longitude <= 180:
            return latitude, longitude

    raise ValueError(
        "Use coordinates like 40.123456, 23.123456 or paste a Google Maps link"
    )


def normalize_time_value(value):
    """Normalize copied opening-hour values to a clean, compact format."""

    value = value.strip()
    value = value.replace("\u202f", " ").replace("\u00a0", " ")
    value = re.sub(r"\s+", " ", value)

    status_key = value.casefold().strip(" .")

    closed_values = {
        "closed", "inchis", "închis", "closed all day",
        "inchis toata ziua", "închis toată ziua"
    }
    always_open_values = {
        "open 24 hours", "open 24 hrs", "24 hours", "24 hrs", "24/7",
        "deschis nonstop", "deschis non-stop", "nonstop", "non-stop"
    }

    if status_key in closed_values:
        return "closed"

    if status_key in always_open_values:
        return "24h"

    def convert_ampm(match):
        hour = int(match.group(1))
        minute = int(match.group(2) or 0)
        meridiem = match.group(3).lower()

        if meridiem == "pm" and hour != 12:
            hour += 12
        elif meridiem == "am" and hour == 12:
            hour = 0

        return f"{hour:02d}:{minute:02d}"

    value = re.sub(
        r"\b(\d{1,2})(?::(\d{2}))?\s*([ap]\.?m\.?)\b",
        convert_ampm,
        value,
        flags=re.IGNORECASE
    )

    value = re.sub(
        r"\b(\d):([0-5]\d)\b",
        lambda match: f"0{match.group(1)}:{match.group(2)}",
        value
    )

    value = re.sub(r"\s*(?:-|–|—|to|până la|pana la)\s*", "–", value, flags=re.IGNORECASE)
    value = re.sub(r"\s*[,;]\s*", ", ", value)

    return value.strip(" ,")


def format_hours(raw_value):
    """Create English and Romanian schedules from one pasted weekly program."""

    value = raw_value.strip()

    if not value:
        return "", ""

    value = value.replace("\r", "\n")
    value = value.replace("\u202f", " ").replace("\u00a0", " ")

    day_pattern = "|".join(
        sorted((re.escape(day) for day in DAY_ALIASES), key=len, reverse=True)
    )

    # Handles copied text where all days arrive on a single line.
    value = re.sub(
        rf"(?i)(?<!^)(?<!\n)\s+(?=({day_pattern})\b\s*:?)",
        "\n",
        value
    )

    lines = [
        re.sub(r"\s+", " ", line).strip()
        for line in value.split("\n")
        if line.strip()
    ]

    parsed = {}
    extras = []
    index = 0

    while index < len(lines):
        line = lines[index]
        match = re.match(
            rf"(?i)^({day_pattern})\b\s*:?\s*(.*)$",
            line
        )

        if not match:
            extras.append(normalize_time_value(line))
            index += 1
            continue

        day_key = match.group(1).casefold()
        day_index = DAY_ALIASES[day_key]
        day_value = match.group(2).strip()

        if not day_value and index + 1 < len(lines):
            next_line = lines[index + 1]
            next_is_day = re.match(rf"(?i)^({day_pattern})\b", next_line)

            if not next_is_day:
                day_value = next_line
                index += 1

        parsed[day_index] = normalize_time_value(day_value) if day_value else ""
        index += 1

    if not parsed:
        cleaned = "\n".join(extras)
        return cleaned, cleaned

    lines_en = []
    lines_ro = []

    for day_index in range(7):
        if day_index not in parsed:
            continue

        day_value = parsed[day_index]

        if day_value == "closed":
            value_en = "Closed"
            value_ro = "Închis"
        elif day_value == "24h":
            value_en = "Open 24 hours"
            value_ro = "Deschis non-stop"
        else:
            value_en = day_value
            value_ro = day_value

        lines_en.append(f"{DAY_NAMES_EN[day_index]}: {value_en}")
        lines_ro.append(f"{DAY_NAMES_RO[day_index]}: {value_ro}")

    if extras:
        lines_en.extend(extras)
        lines_ro.extend(extras)

    return "\n".join(lines_en), "\n".join(lines_ro)


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

        parse_coordinates(
            coordinates_entry.get().strip()
        )

    except ValueError:

        status_label.configure(
            text="Invalid GPS coordinates. Use: latitude, longitude",
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

    category = category_entry.get().strip()

    phone = phone_entry.get().strip()

    whatsapp = whatsapp_entry.get().strip()

    website = website_entry.get().strip()

    address = address_entry.get().strip()

    latitude, longitude = parse_coordinates(
        coordinates_entry.get().strip()
    )

    booking = booking_switch.get()

    hours_raw = hours_box.get(
        "1.0",
        "end"
    ).strip()

    hours_en, hours_ro = format_hours(hours_raw)

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

        "categoryEn": category,

        "categoryRo": category,

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

        "category": category,

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

category_entry = create_entry(
    left_frame,
    "Category (same for EN and RO)"
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

coordinates_entry = create_entry(
    left_frame,
    "GPS Coordinates (latitude, longitude or Google Maps link)"
)

hours_label = ctk.CTkLabel(
    left_frame,
    text="Opening Hours (paste the complete weekly program)"
)

hours_label.pack(
    anchor="w",
    padx=20,
    pady=(14, 4)
)

hours_box = ctk.CTkTextbox(
    left_frame,
    width=500,
    height=150
)

hours_box.pack(
    padx=20
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