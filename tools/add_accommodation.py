import re
import json
from pathlib import Path
from PIL import Image

REPO_RAW_BASE = "https://raw.githubusercontent.com/gabridim18-lab/halkidiki-data/main"

def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s-]+", "_", text)
    return text.strip("_")

def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))

def save_json(path: Path, data: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

def ensure_1200x800_webp(src_path: Path, dst_path: Path):
    dst_path.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(src_path) as im:
        im = im.convert("RGB")

        target_w, target_h = 1200, 800
        src_w, src_h = im.size

        src_ratio = src_w / src_h
        target_ratio = target_w / target_h

        # crop center to match aspect ratio
        if src_ratio > target_ratio:
            new_w = int(src_h * target_ratio)
            left = (src_w - new_w) // 2
            im = im.crop((left, 0, left + new_w, src_h))
        else:
            new_h = int(src_w / target_ratio)
            top = (src_h - new_h) // 2
            im = im.crop((0, top, src_w, top + new_h))

        im = im.resize((target_w, target_h), Image.LANCZOS)
        im.save(dst_path, format="WEBP", quality=82, method=6)

def ask_bool(label: str) -> bool:
    return input(f"{label}? (y/n): ").strip().lower() == "y"

def main():
    repo_root = Path.cwd()
    acc_root = repo_root / "data" / "accommodations"
    index_path = acc_root / "index.json"

    if not index_path.exists():
        raise SystemExit("Nu găsesc data/accommodations/index.json. Rulează scriptul din root-ul repo-ului.")

    main_index = load_json(index_path)
    if "schemaVersion" not in main_index or "items" not in main_index:
        raise SystemExit("index.json nu are schemaVersion + items.")

    print("\n=== Add new accommodation ===\n")

    title_en = input("Title EN: ").strip()
    title_ro = input("Title RO: ").strip()
    beach_slug = input("BeachSlug (ex: Lagonisi Beach): ").strip()
    zone = input("Zone (Thessaloniki/Kassandra/Sithonia/Olympiada): ").strip()

    slug_in = input("Slug/ID (ENTER ca să îl generez din Title EN): ").strip()
    acc_id = slug_in if slug_in else slugify(title_en)
    print("=> ID/Slug:", acc_id)

    address = input("Address: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()
    website = input("Website: ").strip()

    category = input("Category (family_friendly / perfect_for_groups / couples_retreat / escape_relax / explorers_choice): ").strip()
    rating = float(input("Rating (ex 9.4): ").strip() or "0")
    rating_scale = float(input("RatingScale (ex 10): ").strip() or "10")
    featured = input("Featured? (y/n): ").strip().lower() == "y"

    guests = int(input("Guests: ").strip() or "0")
    size_sqm = int(input("SizeSqm: ").strip() or "0")
    view = input("View (ex Garden view): ").strip()
    bedrooms = int(input("Bedrooms: ").strip() or "0")

    pet_friendly = ask_bool("PetFriendly")
    pool = ask_bool("Pool")
    wifi = ask_bool("WiFi")
    parking = ask_bool("Parking")
    air_conditioning = ask_bool("AirConditioning")
    kitchen = ask_bool("Kitchen")
    washer = ask_bool("Washer")
    balcony = ask_bool("Balcony")
    bbq = ask_bool("BBQ")

    owner_id = input("OwnerId: ").strip()
    owner_code = input("OwnerCode: ").strip()

    lat = float(input("Lat: ").strip() or "0")
    lon = float(input("Lon: ").strip() or "0")

    dist_override = input("DistanceMetersOverride (ENTER dacă nu): ").strip()
    distance_m = int(dist_override) if dist_override else None

    print("\nIntroduce Description EN (termină cu o linie goală):")
    desc_en_lines = []
    while True:
        line = input()
        if not line.strip():
            break
        desc_en_lines.append(line)
    description_en = "\n".join(desc_en_lines).strip()

    print("\nIntroduce Description RO (termină cu o linie goală):")
    desc_ro_lines = []
    while True:
        line = input()
        if not line.strip():
            break
        desc_ro_lines.append(line)
    description_ro = "\n".join(desc_ro_lines).strip()

    images_folder = Path(input("\nPath folder imagini SURSA (jpg/png/webp): ").strip('"').strip())
    if not images_folder.exists():
        raise SystemExit("Folderul cu imagini nu există.")

    acc_dir = acc_root / acc_id
    images_dir = acc_dir / "images"
    acc_index_path = acc_dir / "index.json"
    images_dir.mkdir(parents=True, exist_ok=True)

    src_files = []
    for ext in ("*.jpg", "*.jpeg", "*.png", "*.webp"):
        src_files.extend(sorted(images_folder.glob(ext)))

    if not src_files:
        raise SystemExit("Nu am găsit imagini în folderul sursă (jpg/jpeg/png/webp).")

    out_files = []
    for i, src in enumerate(src_files):
        suffix = "" if i == 0 else str(i)
        dst_name = f"{acc_id}{suffix}.webp"
        dst = images_dir / dst_name
        ensure_1200x800_webp(src, dst)
        out_files.append(dst_name)

    image_urls = [f"{REPO_RAW_BASE}/data/accommodations/{acc_id}/images/{name}" for name in out_files]

    acc_json = {
        "id": acc_id,
        "beachSlug": beach_slug,
        "zone": zone,
        "titleEn": title_en,
        "titleRo": title_ro,
        "address": address,
        "phone": phone,
        "email": email,
        "website": website,
        "category": category,
        "rating": rating,
        "ratingScale": rating_scale,
        "featured": featured,
        "guests": guests,
        "sizeSqm": size_sqm,
        "view": view,
        "bedrooms": bedrooms,
        "petFriendly": pet_friendly,
        "pool": pool,
        "wifi": wifi,
        "parking": parking,
        "airConditioning": air_conditioning,
        "kitchen": kitchen,
        "washer": washer,
        "balcony": balcony,
        "bbq": bbq,
        "ownerId": owner_id,
        "ownerCode": owner_code,
        "lat": lat,
        "lon": lon,
        "descriptionEn": description_en,
        "descriptionRo": description_ro,
        "images": image_urls
    }

    if distance_m is not None:
        acc_json["distanceMetersOverride"] = distance_m

    save_json(acc_index_path, acc_json)
    print("✅ Scris:", acc_index_path)

    items = main_index["items"]
    if acc_id not in items:
        items.append(acc_id)
        save_json(index_path, main_index)
        print("✅ Actualizat:", index_path)
    else:
        print("ℹ️ Slug deja există în index.json, nu am modificat.")

    print("\nDONE. Următorul pas:")
    print("git add data/accommodations")
    print(f'git commit -m \"Add accommodation {acc_id}\"')
    print("git push")

if __name__ == "__main__":
    main()