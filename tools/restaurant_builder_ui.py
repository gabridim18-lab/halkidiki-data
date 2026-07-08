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

def slugify(text: str):

    text = text.strip().lower()

    text = re.sub(r"[^\w\s-]", "", text)

    text = re.sub(r"[\s_]+", "-", text)

    return text.strip("-")

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


def make_short_text(text: str, limit: int = 135):

    clean = " ".join(
        text.strip().split()
    )

    if len(clean) <= limit:
        return clean

    return clean[:limit].rsplit(" ", 1)[0] + "..."



# =========================================
# GOOGLE BUSINESS PROFILE DETAILS
# =========================================

GOOGLE_PROFILE_FIELDS = {
    "Accessibility": "accessibility",
    "Service options": "serviceOptions",
    "Highlights": "highlights",
    "Popular for": "popularFor",
    "Offerings": "offerings",
    "Dining options": "diningOptions",
    "Amenities": "amenities",
    "Atmosphere": "atmosphere",
    "Crowd": "crowd",
    "Planning": "planning",
    "Payments": "payments",
    "Children": "children",
    "Parking": "parking",
    "Pets": "pets"
}

GOOGLE_CHECK_OPTIONS = {
    "accessibility": [
        "Wheelchair-accessible entrance",
        "Wheelchair-accessible seating",
        "Wheelchair-accessible toilet"
    ],
    "serviceOptions": [
        "Outdoor seating",
        "No-contact delivery",
        "Delivery",
        "Takeaway",
        "Dine-in"
    ],
    "highlights": [
        "Great dessert",
        "Great wine list",
        "Great beer selection",
        "Live music"
    ],
    "popularFor": [
        "Breakfast",
        "Lunch",
        "Dinner",
        "Solo dining"
    ],
    "offerings": [
        "Alcohol",
        "Beer",
        "Coffee",
        "Cocktails",
        "Late-night food",
        "Private dining room",
        "Quick bite",
        "Small plates",
        "Spirits",
        "Wine"
    ],
    "diningOptions": [
        "Breakfast",
        "Lunch",
        "Dinner",
        "Catering",
        "Dessert",
        "Seating",
        "Table service"
    ],
    "amenities": [
        "Toilet",
        "Wi-Fi"
    ],
    "atmosphere": [
        "Casual",
        "Cosy",
        "Quiet",
        "Romantic",
        "Trendy"
    ],
    "crowd": [
        "Groups",
        "Tourists",
        "Family friendly"
    ],
    "planning": [
        "Lunch reservations recommended",
        "Dinner reservations recommended",
        "Accepts reservations"
    ],
    "payments": [
        "Credit cards",
        "Debit cards",
        "NFC mobile payments"
    ],
    "children": [
        "Good for kids",
        "High chairs",
        "Kids menu"
    ],
    "parking": [
        "Free of charge street parking",
        "Free parking lot",
        "Plenty of parking"
    ],
    "pets": [
        "Dogs allowed"
    ]
}

def normalize_google_item(text: str):
    return (
        text
        .replace("", "")
        .replace("✓", "")
        .replace("✔", "")
        .strip()
    )

def parse_google_business_details(raw_text: str):
    """
    Accepts copied Google Business Profile blocks like:

    Accessibility
      Wheelchair-accessible entrance

    Service options
      Outdoor seating
      Dine-in

    Returns JSON-ready grouped arrays:
    {
      "accessibility": ["Wheelchair-accessible entrance"],
      "serviceOptions": ["Outdoor seating", "Dine-in"]
    }
    """

    result = {
        key: []
        for key in GOOGLE_PROFILE_FIELDS.values()
    }

    current_key = None

    for line in raw_text.splitlines():

        clean = normalize_google_item(line)

        if not clean:
            continue

        if clean in GOOGLE_PROFILE_FIELDS:
            current_key = GOOGLE_PROFILE_FIELDS[clean]
            continue

        if current_key:
            if clean not in result[current_key]:
                result[current_key].append(clean)

    return result


DAYS_EN = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

DAYS_RO = {
    "Monday": "Luni",
    "Tuesday": "Marți",
    "Wednesday": "Miercuri",
    "Thursday": "Joi",
    "Friday": "Vineri",
    "Saturday": "Sâmbătă",
    "Sunday": "Duminică"
}

def normalize_time_text(value: str):

    return (
        value
        .replace("\u202f", " ")
        .replace("\xa0", " ")
        .replace("–", "-")
        .replace("—", "-")
        .replace("−", "-")
        .replace(".", ":")
        .strip()
    )

def convert_single_time_to_24(value: str, default_meridiem=None):

    value = normalize_time_text(value).lower()

    match = re.search(
        r"(\d{1,2})(?::(\d{2}))?\s*(am|pm)?",
        value
    )

    if not match:
        return ""

    hour = int(match.group(1))
    minute = int(match.group(2) or "0")
    meridiem = match.group(3) or default_meridiem

    if meridiem == "pm" and hour != 12:
        hour += 12

    if meridiem == "am" and hour == 12:
        hour = 0

    return f"{hour:02d}:{minute:02d}"

def convert_time_range_to_24(value: str):

    clean = normalize_time_text(value).lower()

    match = re.search(
        r"(\d{1,2}(?::\d{2})?\s*(?:am|pm)?)\s*-\s*(\d{1,2}(?::\d{2})?\s*(?:am|pm)?)",
        clean
    )

    if not match:
        return "", ""

    start_raw = match.group(1).strip()
    end_raw = match.group(2).strip()

    end_meridiem_match = re.search(r"\b(am|pm)\b", end_raw)
    start_meridiem_match = re.search(r"\b(am|pm)\b", start_raw)

    default_start_meridiem = None

    if not start_meridiem_match and end_meridiem_match:
        default_start_meridiem = end_meridiem_match.group(1)

    start = convert_single_time_to_24(
        start_raw,
        default_start_meridiem
    )

    end = convert_single_time_to_24(
        end_raw,
        None
    )

    return start, end

def parse_opening_hours(raw_text: str):

    raw = normalize_time_text(raw_text)

    if not raw:
        return []

    day_pattern = "|".join(DAYS_EN)

    matches = list(
        re.finditer(
            rf"\b({day_pattern})\b",
            raw,
            flags=re.IGNORECASE
        )
    )

    schedule_by_day = {}

    for index, match in enumerate(matches):

        day = match.group(1).capitalize()

        start = match.end()

        end = (
            matches[index + 1].start()
            if index + 1 < len(matches)
            else len(raw)
        )

        value = raw[start:end]
        value = re.sub(r"[;\n\t]+", " ", value)
        value = " ".join(value.split())

        if re.search(r"\bclosed\b", value, flags=re.IGNORECASE):

            schedule_by_day[day] = {
                "day": day,
                "dayRo": DAYS_RO[day],
                "closed": True,
                "open": "",
                "close": "",
                "labelEn": "Closed",
                "labelRo": "Închis"
            }

            continue

        open_time, close_time = convert_time_range_to_24(value)

        if open_time and close_time:

            schedule_by_day[day] = {
                "day": day,
                "dayRo": DAYS_RO[day],
                "closed": False,
                "open": open_time,
                "close": close_time,
                "labelEn": f"{open_time}–{close_time}",
                "labelRo": f"{open_time}–{close_time}"
            }

    return [
        schedule_by_day[day]
        for day in DAYS_EN
        if day in schedule_by_day
    ]

def make_hours_summary(schedule, lang="en"):

    parts = []

    for item in schedule:

        day = item["day"] if lang == "en" else item["dayRo"]
        label = item["labelEn"] if lang == "en" else item["labelRo"]

        parts.append(
            f"{day}: {label}"
        )

    return "; ".join(parts)

def parse_coordinates(value: str):

    clean = value.strip()

    if not clean:
        return None, None

    match = re.search(
        r"(-?\d+(?:\.\d+)?)\s*,\s*(-?\d+(?:\.\d+)?)",
        clean
    )

    if not match:
        raise ValueError(
            "GPS Coordinates must look like: 40.568494593811025, 22.95579049272589"
        )

    lat = float(match.group(1))
    lon = float(match.group(2))

    if lat < -90 or lat > 90:
        raise ValueError("Latitude must be between -90 and 90")

    if lon < -180 or lon > 180:
        raise ValueError("Longitude must be between -180 and 180")

    return lat, lon


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

        self.minsize(1200, 760)

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

        self.hero_image = None

        self.business_images = []

        self.menu_images = []

        self.preview_img = None

        self.last_slug = None

        self.zone_beaches = {
            "Thessaloniki": [
                "thessaloniki",
                "nea-krini-beach",
                "perea-beach",
                "neoi-epivates-beach",
                "agia-triada-beach",
                "hidden-beach",
                "surfer-beach-angelochori",
                "tourmpali-beach",
                "riviera-virgin-beach",
                "nea-michaniona-beach",
                "oasis-beach",
                "agistri-beach",
                "paralia-potami",
                "nea-iraklia-beach",
                "sahara-beach",
                "vergia-beach",
                "delfinia-beach",
                "sozopoli-beach",
                "paralia-iraklia",
                "mykoniatika-secret-beach",
                "beach-mykoniatika",
                "ntouraki-beach",
                "nea-plagia-beach",
                "flogita-beach",
                "dionisiou-beach"
            ],
            "Kassandra": [
                "nea-moudania-beach",
                "paralia-nea-moudania",
                "gremia-beach",
                "paralia-nea-potidea",
                "windsurfers-paradise",
                "stavronikita-beach",
                "paralia-sani",
                "simantro-beach",
                "paralia-kipsa",
                "chelona-beach",
                "elani-beach",
                "siviri-beach",
                "agios-nikolaos-beach",
                "agios-nikolaos-fourka",
                "skala-fourkas-beach",
                "aigaiopelagitika-beach",
                "possidi-west-beach",
                "possidi-beach",
                "paralia-posidi",
                "mola-kaliva-beach",
                "paralia-anemi",
                "paralia-skioni",
                "nea-skioni-beach",
                "the-beach",
                "paralia-agias-paraskevis",
                "loutra-agias-paraskevis-beach",
                "loutra-beach",
                "pebbles-beach-of-st-george",
                "ani-beach",
                "dymitry-beach",
                "kanastraio-or-kalogria-cape",
                "cape-sevas",
                "cliff-rocks",
                "agios-nikolaos-kanistro-beach",
                "kanistro-beach",
                "paralia-panagias",
                "porto-valitsa-bay",
                "paliouri-beach",
                "xenia-beach",
                "paralia-chroussou",
                "golden-beach",
                "alonaki-beach",
                "glarokavos-beach",
                "lagoon-beach",
                "paralia-pefkochori",
                "pefkochori-beach",
                "hanioti-beach",
                "polychrono-beach",
                "kryopigi-beach",
                "kalithea-beach",
                "paralia-afitos",
                "plage-liosi",
                "plage-moudounou",
                "athytos-beach",
                "varkes-beach",
                "plage-vothonas",
                "place-de-ninna",
                "nea-fokea-beach",
                "savatianos-beach",
                "wild-sandy-beach",
                "nea-potidea-beach",
                "paralia-kalivia",
                "kalyves-beach"
            ],
            "Sithonia": [
                "trikorfo-beach",
                "paralia-psakoudia",
                "psakoudia-beach",
                "paralia-sargani",
                "metamorfossi-beach",
                "paralia-askamnia",
                "red-rocks-of-metamorphosis",
                "nikiti-beach",
                "paralia-kastri",
                "kastri-beach",
                "agios-ioannis-beach",
                "koviou-beach",
                "isla-beach",
                "kalogria-beach",
                "small-spathies-beach",
                "spathies-beach",
                "paralia-elia",
                "paralia-perigiali",
                "elia-beach",
                "lagomandra-beach",
                "nikitis-beach-sithonia",
                "tripotamos-beach",
                "paradisos-beach",
                "peaceful-beach",
                "neos-marmaras-beach",
                "porto-carras-beach",
                "kohi-beach",
                "koutsoupia-beach",
                "diaporti-beach",
                "likithos-beach",
                "azapiko-beach",
                "foresta-sithonia",
                "paralia-alexandra-xenia",
                "paralia-azapiko",
                "aretes-beach",
                "tristinika-beach",
                "ema-beach",
                "luka-beach",
                "paralia-toroni",
                "porto-koufo-beach",
                "lagoon-in-porto-koufo",
                "marathias-beach",
                "secret-beach",
                "sithonia-cape",
                "mamba-beach",
                "kalamitsi-beach",
                "kriaritsi-beach",
                "prassou-beach",
                "klimataria-beach",
                "tourkolimnionas",
                "skala-sykias-beach",
                "linaraki-beach",
                "sykias-beach",
                "valti-beach",
                "agridia-beach",
                "goa-beach",
                "platania",
                "sarti-beach",
                "achlada",
                "heart-shaped-bay",
                "platanitsi-beach",
                "orange-beach",
                "kavourotrypes-beach",
                "mega-portokali-beach",
                "paralia-armenistis",
                "dream-coast-beach",
                "robinson-beach",
                "banana-beach",
                "porto-paradiso",
                "zografou-beach",
                "koutloumousi-beach",
                "bara-beach",
                "fava-beach",
                "manos-beach",
                "karydi-beach",
                "rocks-on-the-beach",
                "livari-beach",
                "karagatsi-beach",
                "talgo-beach",
                "private-beach",
                "lagonisi-beach",
                "latoura-beach",
                "livrohio-beach",
                "trani-ammouda",
                "paralia-agios-nikolaos",
                "schinias-beach",
                "salonikiou-beach",
                "paralia-salonikiou",
                "irini-beach"
            ],
            "Olympiada": [
                "ladhario-beach",
                "paralia-pirgos",
                "develiki-beach",
                "xiropotamos-beach",
                "tripiti-beach",
                "paralia-ouranoupoli",
                "ouranoupolis-beach",
                "komitsa-beach",
                "nea-roda-beach",
                "ierissos-beach",
                "kakoudia-beach",
                "stratoni-beach",
                "proti-ammoudia-beach",
                "olympiada-beach",
                "paralia-stavros",
                "milies-beach",
                "platani-beach",
                "vrasna-beach",
                "nea-vrasna-beach"
            ]
        }

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

        left = ttk.Frame(
            root,
            width=930
        )

        left.pack(
            side="left",
            fill="both",
            expand=False,
            padx=(0, 10)
        )

        left.pack_propagate(False)

        # =========================================
        # RIGHT - SCROLLABLE PANEL
        # =========================================

        right_outer = ttk.Frame(
            root,
            width=450
        )

        right_outer.pack(
            side="right",
            fill="y"
        )

        right_outer.pack_propagate(False)

        right_canvas = tk.Canvas(
            right_outer,
            width=430,
            highlightthickness=0
        )

        right_scrollbar = ttk.Scrollbar(
            right_outer,
            orient="vertical",
            command=right_canvas.yview
        )

        right_canvas.configure(
            yscrollcommand=right_scrollbar.set
        )

        right_scrollbar.pack(
            side="right",
            fill="y"
        )

        right_canvas.pack(
            side="left",
            fill="y",
            expand=False
        )

        right = ttk.Frame(right_canvas)

        right_window = right_canvas.create_window(
            (0, 0),
            window=right,
            anchor="nw"
        )

        def _right_configure(event):
            right_canvas.configure(
                scrollregion=right_canvas.bbox("all")
            )

        def _canvas_configure(event):
            right_canvas.itemconfigure(
                right_window,
                width=event.width
            )

        right.bind(
            "<Configure>",
            _right_configure
        )

        right_canvas.bind(
            "<Configure>",
            _canvas_configure
        )

        def _mousewheel(event):
            right_canvas.yview_scroll(
                int(-1 * (event.delta / 120)),
                "units"
            )

        right_canvas.bind_all(
            "<MouseWheel>",
            _mousewheel
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
            fill="x",
            expand=False
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
                sticky="w",
                pady=5
            )

            form.grid_columnconfigure(
                1,
                weight=0
            )

        # =========================================
        # VARIABLES
        # =========================================

        self.var_title_en = tk.StringVar()
        self.var_title_ro = tk.StringVar()

        self.var_slug = tk.StringVar()

        self.var_zone = tk.StringVar(
            value="Kassandra"
        )

        self.var_beach_slug = tk.StringVar()

        self.var_type = tk.StringVar(
            value="restaurant"
        )

        self.var_featured = tk.BooleanVar()

        self.var_display_address = tk.StringVar()

        self.var_gps_coordinates = tk.StringVar()

        self.var_opening_hours = tk.StringVar()

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

        zone_box = ttk.Combobox(
            form,
            textvariable=self.var_zone,
            values=[
                "Thessaloniki",
                "Kassandra",
                "Sithonia",
                "Olympiada"
            ],
            state="readonly"
        )

        row(
            "Zone",
            zone_box,
            3
        )

        beach_box = ttk.Combobox(
            form,
            textvariable=self.var_beach_slug,
            values=[
                "pefkochori-beach",
                "hanioti-beach",
                "polychrono-beach",
                "kalithea-beach",
                "afytos-beach",
                "possidi-beach",
                "sani-beach",
                "nikiti-beach",
                "kalogria-beach",
                "lagomandra-beach",
                "kavourotrypes-beach",
                "sarti-beach",
                "toroni-beach",
                "vourvourou-beach",
                "olympiada-beach"
            ],
            state="readonly"
        )

        row(
            "Beach",
            beach_box,
            4
        )

        self.beach_box = beach_box

        zone_box.bind(
            "<<ComboboxSelected>>",
            self.update_beaches
        )

        self.update_beaches()

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
            5
        )

        ttk.Checkbutton(

            form,

            text="Featured",

            variable=self.var_featured

        ).grid(
            row=6,
            column=1,
            sticky="w"
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
            "GPS Coordinates",
            ttk.Entry(
                form,
                textvariable=self.var_gps_coordinates
            ),
            8
        )

        ttk.Label(
            form,
            text="Opening Hours"
        ).grid(
            row=9,
            column=0,
            sticky="nw",
            padx=(0, 10),
            pady=5
        )

        self.txt_opening_hours = tk.Text(
            form,
            height=4,
            width=72
        )

        self.txt_opening_hours.grid(
            row=10,
            column=1,
            sticky="w",
            pady=5
        )

        row(
            "Website",
            ttk.Entry(
                form,
                textvariable=self.var_website
            ),
            11
        )

        row(
            "Facebook",
            ttk.Entry(
                form,
                textvariable=self.var_facebook
            ),
            13
        )

        row(
            "Instagram",
            ttk.Entry(
                form,
                textvariable=self.var_instagram
            ),
            14
        )

        row(
            "Phone",
            ttk.Entry(
                form,
                textvariable=self.var_phone
            ),
            15
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
            16
        )

        row(
            "Rating",
            ttk.Entry(
                form,
                textvariable=self.var_rating
            ),
            17
        )

        row(
            "Sunbed Price",
            ttk.Entry(
                form,
                textvariable=self.var_sunbed_price
            ),
            18
        )

        ttk.Checkbutton(

            form,

            text="Consumation Included",

            variable=self.var_consumation

        ).grid(
            row=19,
            column=1,
            sticky="w"
        )

        # =========================================
        # DESCRIPTIONS
        # =========================================

        bottom_area = ttk.Frame(left)

        bottom_area.pack(
            fill="both",
            expand=True,
            pady=(10, 0)
        )

        bottom_area.grid_columnconfigure(0, weight=1)
        bottom_area.grid_columnconfigure(1, weight=1)
        bottom_area.grid_rowconfigure(0, weight=1)

        desc_frame = ttk.LabelFrame(

            bottom_area,

            text="Descriptions",

            padding=8

        )

        desc_frame.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(0, 5)
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
            height=7
        )

        self.txt_ro = tk.Text(
            desc_frame,
            height=7
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
        # GOOGLE BUSINESS PROFILE DETAILS
        # =========================================

        google_frame = ttk.LabelFrame(

            bottom_area,

            text="Extra Google Text (optional)",

            padding=8

        )

        google_frame.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=(5, 0)
        )

        self.txt_google_details = tk.Text(
            google_frame,
            height=7
        )

        self.txt_google_details.pack(
            fill="both",
            expand=True
        )

        ttk.Button(

            google_frame,

            text="📋 Auto Select Options",

            command=self.auto_select_google_options

        ).pack(
            pady=(8,0)
        )

        ttk.Label(
            google_frame,
            text="Optional: paste full Google sections here only when needed. Main common options are now checkboxes on the right."
        ).pack(
            anchor="w",
            pady=(6, 0)
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
        # CUISINE TYPES
        # =========================================

        cuisine_box = ttk.LabelFrame(
            right,
            text="Cuisine Types",
            padding=10
        )

        cuisine_box.pack(
            fill="x",
            pady=(0, 10)
        )

        self.cuisine_vars = {}

        cuisine_types = [

            "seafood",
            "greek",
            "mediterranean",
            "international",
            "italian",
            "pizza",
            "burger",
            "steakhouse",
            "asian",
            "sushi"

        ]

        for cuisine in cuisine_types:

            var = tk.BooleanVar()

            self.cuisine_vars[cuisine] = var

            ttk.Checkbutton(

                cuisine_box,

                text=cuisine,

                variable=var

            ).pack(
                anchor="w"
            )

        # =========================================
        # GOOGLE PROFILE CHECKBOXES
        # =========================================

        google_checks_box = ttk.LabelFrame(
            right,
            text="Google Business Essentials",
            padding=10
        )

        google_checks_box.pack(
            fill="x",
            pady=(0, 10)
        )

        self.google_check_vars = {}

        def add_google_group(title, key, options):

            group = ttk.LabelFrame(
                google_checks_box,
                text=title,
                padding=6
            )

            group.pack(
                fill="x",
                pady=(0, 8)
            )

            self.google_check_vars[key] = {}

            for option in options:

                var = tk.BooleanVar()

                self.google_check_vars[key][option] = var

                ttk.Checkbutton(
                    group,
                    text=option,
                    variable=var
                ).pack(
                    anchor="w"
                )

        add_google_group(
            "Accessibility",
            "accessibility",
            GOOGLE_CHECK_OPTIONS["accessibility"]
        )

        add_google_group(
            "Service",
            "serviceOptions",
            GOOGLE_CHECK_OPTIONS["serviceOptions"]
        )

        add_google_group(
            "Highlights",
            "highlights",
            GOOGLE_CHECK_OPTIONS["highlights"]
        )

        add_google_group(
            "Popular For",
            "popularFor",
            GOOGLE_CHECK_OPTIONS["popularFor"]
        )

        add_google_group(
            "Food & Drinks",
            "offerings",
            GOOGLE_CHECK_OPTIONS["offerings"]
        )

        add_google_group(
            "Dining",
            "diningOptions",
            GOOGLE_CHECK_OPTIONS["diningOptions"]
        )

        add_google_group(
            "Atmosphere",
            "atmosphere",
            GOOGLE_CHECK_OPTIONS["atmosphere"]
        )

        add_google_group(
            "Planning",
            "planning",
            GOOGLE_CHECK_OPTIONS["planning"]
        )

        add_google_group(
            "Payments",
            "payments",
            GOOGLE_CHECK_OPTIONS["payments"]
        )

        add_google_group(
            "Children",
            "children",
            GOOGLE_CHECK_OPTIONS["children"]
        )

        add_google_group(
            "Parking",
            "parking",
            GOOGLE_CHECK_OPTIONS["parking"]
        )

        add_google_group(
            "Pets",
            "pets",
            GOOGLE_CHECK_OPTIONS["pets"]
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

            text="Select Hero Image",

            command=self.pick_hero_image

        ).pack(
            fill="x",
            pady=5
        )

        self.hero_label = ttk.Label(
            image_box,
            text="No hero image selected"
        )

        self.hero_label.pack(
            anchor="w"
        )

        ttk.Button(

            image_box,

            text="Select Gallery Images",

            command=self.pick_business_images

        ).pack(
            fill="x",
            pady=10
        )

        self.business_label = ttk.Label(
            image_box,
            text="0 gallery images selected"
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

    def update_beaches(self, event=None):

        beaches = self.zone_beaches.get(
            self.var_zone.get(),
            []
        )

        self.beach_box["values"] = beaches

        if beaches:
            self.var_beach_slug.set(
                beaches[0]
            )
    
    def auto_slug(self):

        title = self.var_title_en.get()

        self.var_slug.set(
            slugify(title)
        )

    def auto_select_google_options(self):

            raw = self.txt_google_details.get(
                "1.0",
                tk.END
            ).strip()

            if not raw:

                messagebox.showwarning(
                    "Google Text",
                    "Paste Google Business text first."
                )

                return

            parsed = parse_google_business_details(raw)

            for group in self.google_check_vars.values():

                for var in group.values():

                    var.set(False)

            found = 0

            for group_key, values in parsed.items():

                if group_key not in self.google_check_vars:

                    continue

                for item in values:

                    if item in self.google_check_vars[group_key]:

                        self.google_check_vars[group_key][item].set(True)

                        found += 1

            messagebox.showinfo(
                "Done",
                f"✓ {found} Google options detected."
            )

    # =========================================
    # PICK HERO IMAGE
    # =========================================

    def pick_hero_image(self):

        file = filedialog.askopenfilename(

            title="Select Hero Image",

            filetypes=[
                ("Images", "*.jpg *.jpeg *.png *.webp")
            ]

        )

        if not file:
            return

        self.hero_image = file

        self.hero_label.config(
            text=Path(file).name
        )

        self.load_preview(file)



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

        try:

            lat, lon = parse_coordinates(
                self.var_gps_coordinates.get()
            )

        except ValueError as e:

            messagebox.showerror(
                "GPS Coordinates Error",
                str(e)
            )

            return

        raw_opening_hours = self.txt_opening_hours.get(
            "1.0",
            tk.END
        ).strip()

        opening_hours = parse_opening_hours(
            raw_opening_hours
        )

        hours_en = make_hours_summary(
            opening_hours,
            "en"
        )

        hours_ro = make_hours_summary(
            opening_hours,
            "ro"
        )

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
    # HERO IMAGE
    # =========================================

        hero_url = ""

        if self.hero_image:

            hero_name = f"{slug}-hero.webp"

            hero_dst = (
                images_folder
                / hero_name
            )

            ensure_1200x800_webp(
                self.hero_image,
                hero_dst
            )

            hero_url = (
                f"{REPO_RAW_BASE}/data/restaurants/{slug}/images/{hero_name}"
            )

        # =========================================
        # GALLERY IMAGES
        # =========================================

        gallery_urls = []

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

            gallery_urls.append(

                f"{REPO_RAW_BASE}/data/restaurants/{slug}/images/{name}"

            )

        business_urls = []

        if hero_url:
            business_urls.append(hero_url)

        business_urls.extend(gallery_urls)

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
        # CUISINE TYPES
        # =========================================

        cuisine_types = []

        for key, value in self.cuisine_vars.items():

            if value.get():

                cuisine_types.append(key)

        # =========================================
        # GOOGLE BUSINESS PROFILE DETAILS
        # =========================================

        self.auto_select_google_options()

        google_raw = self.txt_google_details.get(
            "1.0",
            tk.END
        ).strip()

        google_details = parse_google_business_details(
            google_raw
        )

        # Merge manual checkbox selections with optional pasted Google text
        for group_key, options in self.google_check_vars.items():

            for option, var in options.items():

                if var.get() and option not in google_details[group_key]:

                    google_details[group_key].append(option)

        # =========================================
        # JSON
        # =========================================

        data = {

            "id": slug,

            "zone":
                self.var_zone.get(),

            "beachSlug":
                slugify(
                    self.var_beach_slug.get()
                ),

            "type":
                self.var_type.get(),

            "featured":
                self.var_featured.get(),

            "titleEn":
                self.var_title_en.get(),

            "titleRo":
                self.var_title_ro.get(),

            "displayAddress":
                self.var_display_address.get(),

            "gpsCoordinates":
                self.var_gps_coordinates.get().strip(),

            "lat":
                lat,

            "lon":
                lon,

            "openingHoursRaw":
                raw_opening_hours,

            "openingHours":
                opening_hours,

            "hoursEn":
                hours_en,

            "hoursRo":
                hours_ro,

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

            "heroImage":
                hero_url,

            "images":
                business_urls,

            "galleryImages":
                gallery_urls,

            "menuImages":
                menu_urls,

            "googleBusinessRaw":
                google_raw,

            "accessibility":
                google_details["accessibility"],

            "serviceOptions":
                google_details["serviceOptions"],

            "highlights":
                google_details["highlights"],

            "popularFor":
                google_details["popularFor"],

            "offerings":
                google_details["offerings"],

            "diningOptions":
                google_details["diningOptions"],

            "amenities":
                google_details["amenities"],

            "atmosphere":
                google_details["atmosphere"],

            "crowd":
                google_details["crowd"],

            "planning":
                google_details["planning"],

            "payments":
                google_details["payments"],

            "children":
                google_details["children"],

            "parking":
                google_details["parking"],

            "pets":
                google_details["pets"],

            "sunbedPrice":
                self.var_sunbed_price.get(),

            "sunbedConsumationIncluded":
                self.var_consumation.get(),

            "musicStyles":
                music,

            "features":
                features,

            "cuisineTypes":
                cuisine_types

        }

        save_json(
            folder / "index.json",
            data
        )

        # =========================================
        # UPDATE INDEX
        # =========================================

        main_image = hero_url

        if not main_image and business_urls:
            main_image = business_urls[0]

        index_item = {

            "id": slug,

            "zone":
                self.var_zone.get(),

            "beachSlug":
                slugify(
                    self.var_beach_slug.get()
                ),

            "type":
                self.var_type.get(),

            "featured":
                self.var_featured.get(),

            "titleEn":
                self.var_title_en.get(),

            "titleRo":
                self.var_title_ro.get(),

            "image":
                main_image,

            "heroImage":
                hero_url,

            "lat":
                lat,

            "lon":
                lon,

            "rating":
                float(self.var_rating.get()),

            "price":
                self.var_price.get(),

            "shortEn":
                make_short_text(
                    self.txt_en.get(
                        "1.0",
                        tk.END
                    )
                ),

            "shortRo":
                make_short_text(
                    self.txt_ro.get(
                        "1.0",
                        tk.END
                    )
                ),

            "features":
                features,

            "cuisineTypes":
                cuisine_types

        }

        if self.index_path.exists():

            index_data = json.loads(

                self.index_path.read_text(
                    encoding="utf-8"
                )

            )

        else:

            index_data = []

        updated = False

        for i, item in enumerate(index_data):

            if item.get("id") == slug:

                index_data[i] = index_item
                updated = True
                break

        if not updated:

            index_data.append(index_item)

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