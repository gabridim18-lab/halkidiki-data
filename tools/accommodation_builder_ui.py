import re
import json
import subprocess
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from pathlib import Path
from PIL import Image, ImageTk

REPO_RAW_BASE = "https://raw.githubusercontent.com/gabridim18-lab/halkidiki-data/main"

# ---- helpers ----
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

        # crop center to cover
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

def parse_float(s: str, default=0.0):
    try:
        return float(s.strip())
    except:
        return default

def parse_int(s: str, default=0):
    try:
        return int(s.strip())
    except:
        return default

def run_cmd(cmd, cwd: Path):
    """
    Rulează o comandă (listă de stringuri) în folderul repo-ului.
    Returnează (ok: bool, output: str).
    """
    try:
        p = subprocess.run(
            cmd,
            cwd=str(cwd),
            capture_output=True,
            text=True,
            shell=False
        )
        out = (p.stdout or "") + ("\n" + p.stderr if p.stderr else "")
        return (p.returncode == 0), out.strip()
    except Exception as e:
        return False, str(e)

# ---- UI ----
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Accommodation Builder (Halkidiki Data)")
        self.geometry("1100x720")
        self.minsize(1000, 650)

        self.repo_root = Path.cwd()
        self.acc_root = self.repo_root / "data" / "accommodations"
        self.index_path = self.acc_root / "index.json"

        if not self.index_path.exists():
            messagebox.showerror(
                "Repo not found",
                "Nu găsesc data/accommodations/index.json.\n\n"
                "Rulează aplicația din ROOT-ul repo-ului halkidiki-data (folderul care conține data/)."
            )
            self.destroy()
            return

        self.main_index = load_json(self.index_path)

        self.image_files = []
        self.preview_imgtk = None
        self.last_generated_slug = None

        self._build_ui()

    def _build_ui(self):
        root = ttk.Frame(self, padding=12)
        root.pack(fill="both", expand=True)

        # layout: left form, right images/preview
        left = ttk.Frame(root)
        left.pack(side="left", fill="both", expand=True, padx=(0, 10))

        right = ttk.Frame(root)
        right.pack(side="right", fill="both", expand=False)

        # --- FORM ---
        form = ttk.LabelFrame(left, text="Accommodation details", padding=10)
        form.pack(fill="both", expand=True)

        # row helper
        def row(label, widget, r):
            ttk.Label(form, text=label).grid(row=r, column=0, sticky="w", padx=(0,8), pady=4)
            widget.grid(row=r, column=1, sticky="ew", pady=4)
            form.grid_columnconfigure(1, weight=1)

        self.var_title_en = tk.StringVar()
        self.var_title_ro = tk.StringVar()
        self.var_beachslug = tk.StringVar()
        self.var_zone = tk.StringVar(value="Sithonia")
        self.var_slug = tk.StringVar()

        self.var_address = tk.StringVar()
        self.var_phone = tk.StringVar()
        self.var_email = tk.StringVar()
        self.var_website = tk.StringVar()

        self.var_category = tk.StringVar(value="family_friendly")
        self.var_rating = tk.StringVar(value="9.5")
        self.var_rating_scale = tk.StringVar(value="10")
        self.var_featured = tk.BooleanVar(value=False)

        self.var_guests = tk.StringVar(value="4")
        self.var_size = tk.StringVar(value="60")
        self.var_view = tk.StringVar(value="Garden view")
        self.var_bedrooms = tk.StringVar(value="2")

        self.var_owner_id = tk.StringVar()
        self.var_owner_code = tk.StringVar()

        self.var_lat = tk.StringVar()
        self.var_lon = tk.StringVar()
        self.var_dist_override = tk.StringVar()  # optional

        # booleans
        self.var_pet = tk.BooleanVar(value=False)
        self.var_pool = tk.BooleanVar(value=False)
        self.var_wifi = tk.BooleanVar(value=True)
        self.var_parking = tk.BooleanVar(value=True)
        self.var_ac = tk.BooleanVar(value=True)
        self.var_kitchen = tk.BooleanVar(value=True)
        self.var_washer = tk.BooleanVar(value=True)
        self.var_balcony = tk.BooleanVar(value=True)
        self.var_bbq = tk.BooleanVar(value=False)

        # widgets
        row("Title EN", ttk.Entry(form, textvariable=self.var_title_en), 0)
        row("Title RO", ttk.Entry(form, textvariable=self.var_title_ro), 1)
        row("BeachSlug (ex: Lagonisi Beach)", ttk.Entry(form, textvariable=self.var_beachslug), 2)

        zone_cb = ttk.Combobox(form, textvariable=self.var_zone, values=["Thessaloniki","Kassandra","Sithonia","Olympiada"], state="readonly")
        row("Zone", zone_cb, 3)

        slug_frame = ttk.Frame(form)
        slug_entry = ttk.Entry(slug_frame, textvariable=self.var_slug)
        slug_entry.pack(side="left", fill="x", expand=True)
        ttk.Button(slug_frame, text="Auto from Title EN", command=self.autofill_slug).pack(side="left", padx=8)
        row("Slug/ID", slug_frame, 4)

        row("Address", ttk.Entry(form, textvariable=self.var_address), 5)

        contact = ttk.Frame(form)
        ttk.Entry(contact, textvariable=self.var_phone, width=18).pack(side="left")
        ttk.Label(contact, text="  Email").pack(side="left")
        ttk.Entry(contact, textvariable=self.var_email, width=25).pack(side="left", padx=(6,0))
        row("Phone + Email", contact, 6)

        row("Website", ttk.Entry(form, textvariable=self.var_website), 7)

        cat_cb = ttk.Combobox(
            form, textvariable=self.var_category,
            values=["family_friendly","perfect_for_groups","couples_retreat","escape_relax","explorers_choice"],
            state="readonly"
        )
        row("Category", cat_cb, 8)

        rline = ttk.Frame(form)
        ttk.Entry(rline, textvariable=self.var_rating, width=10).pack(side="left")
        ttk.Label(rline, text="  Rating scale").pack(side="left")
        ttk.Entry(rline, textvariable=self.var_rating_scale, width=10).pack(side="left", padx=(6,0))
        ttk.Checkbutton(rline, text="Featured", variable=self.var_featured).pack(side="left", padx=12)
        row("Rating", rline, 9)

        facts = ttk.Frame(form)
        ttk.Label(facts, text="Guests").pack(side="left")
        ttk.Entry(facts, textvariable=self.var_guests, width=6).pack(side="left", padx=(6,12))
        ttk.Label(facts, text="SizeSqm").pack(side="left")
        ttk.Entry(facts, textvariable=self.var_size, width=6).pack(side="left", padx=(6,12))
        ttk.Label(facts, text="Bedrooms").pack(side="left")
        ttk.Entry(facts, textvariable=self.var_bedrooms, width=6).pack(side="left", padx=(6,12))
        row("Quick facts", facts, 10)

        row("View", ttk.Entry(form, textvariable=self.var_view), 11)

        owner = ttk.Frame(form)
        ttk.Entry(owner, textvariable=self.var_owner_id, width=18).pack(side="left")
        ttk.Label(owner, text="  Code").pack(side="left")
        ttk.Entry(owner, textvariable=self.var_owner_code, width=10).pack(side="left", padx=(6,0))
        row("Owner", owner, 12)

        geo = ttk.Frame(form)
        ttk.Label(geo, text="Lat").pack(side="left")
        ttk.Entry(geo, textvariable=self.var_lat, width=14).pack(side="left", padx=(6,12))
        ttk.Label(geo, text="Lon").pack(side="left")
        ttk.Entry(geo, textvariable=self.var_lon, width=14).pack(side="left", padx=(6,12))
        row("Geo", geo, 13)

        row("Distance override (meters, optional)", ttk.Entry(form, textvariable=self.var_dist_override), 14)

        # amenities checkboxes
        amen = ttk.LabelFrame(form, text="Amenities", padding=8)
        amen.grid(row=15, column=0, columnspan=2, sticky="ew", pady=(10,6))
        for c in range(4):
            amen.grid_columnconfigure(c, weight=1)

        checks = [
            ("PetFriendly", self.var_pet),
            ("Pool", self.var_pool),
            ("WiFi", self.var_wifi),
            ("Parking", self.var_parking),
            ("AirConditioning", self.var_ac),
            ("Kitchen", self.var_kitchen),
            ("Washer", self.var_washer),
            ("Balcony", self.var_balcony),
            ("BBQ", self.var_bbq),
        ]
        for i, (label, var) in enumerate(checks):
            ttk.Checkbutton(amen, text=label, variable=var).grid(row=i//3, column=i%3, sticky="w", padx=6, pady=2)

        # descriptions
        desc_frame = ttk.LabelFrame(left, text="Descriptions", padding=10)
        desc_frame.pack(fill="both", expand=True, pady=(10,0))

        ttk.Label(desc_frame, text="Description EN").grid(row=0, column=0, sticky="w")
        ttk.Label(desc_frame, text="Description RO").grid(row=0, column=1, sticky="w", padx=(10,0))
        desc_frame.grid_columnconfigure(0, weight=1)
        desc_frame.grid_columnconfigure(1, weight=1)
        desc_frame.grid_rowconfigure(1, weight=1)

        self.txt_desc_en = tk.Text(desc_frame, height=8, wrap="word")
        self.txt_desc_ro = tk.Text(desc_frame, height=8, wrap="word")
        self.txt_desc_en.grid(row=1, column=0, sticky="nsew")
        self.txt_desc_ro.grid(row=1, column=1, sticky="nsew", padx=(10,0))

        # --- RIGHT PANE (IMAGES) ---
        img_box = ttk.LabelFrame(right, text="Images", padding=10)
        img_box.pack(fill="both", expand=True)

        ttk.Button(img_box, text="Select source images…", command=self.pick_images).pack(fill="x")
        ttk.Label(img_box, text="(jpg/png/webp; will be converted to 1200x800 WEBP)").pack(anchor="w", pady=(6,10))

        self.lbl_count = ttk.Label(img_box, text="Selected: 0 images")
        self.lbl_count.pack(anchor="w")

        self.list_images = tk.Listbox(img_box, height=12)
        self.list_images.pack(fill="both", expand=True, pady=8)
        self.list_images.bind("<<ListboxSelect>>", self.on_select_preview)

        ttk.Label(img_box, text="Preview").pack(anchor="w", pady=(6,2))
        self.lbl_preview = ttk.Label(img_box)
        self.lbl_preview.pack()

        # --- bottom actions ---
        actions = ttk.Frame(root)
        actions.pack(fill="x", pady=(12,0))

        ttk.Button(actions, text="Generate files", command=self.generate).pack(side="right")
        self.btn_git_commit = ttk.Button(actions, text="Git Add + Commit", command=self.git_add_commit, state="disabled")
        self.btn_git_commit.pack(side="right", padx=8)
        ttk.Button(actions, text="Validate", command=self.validate_only).pack(side="right", padx=8)

        self.lbl_status = ttk.Label(actions, text="")
        self.lbl_status.pack(side="left")

    def autofill_slug(self):
        title = self.var_title_en.get().strip()
        if not title:
            messagebox.showwarning("Missing", "Completează Title EN înainte.")
            return
        self.var_slug.set(slugify(title))

    def pick_images(self):
        files = filedialog.askopenfilenames(
            title="Select images",
            filetypes=[("Images", "*.jpg *.jpeg *.png *.webp")]
        )
        if not files:
            return
        self.image_files = list(files)
        self.list_images.delete(0, tk.END)
        for f in self.image_files:
            self.list_images.insert(tk.END, f)
        self.lbl_count.config(text=f"Selected: {len(self.image_files)} images")
        self.lbl_status.config(text="")

        # auto preview first
        self.list_images.selection_clear(0, tk.END)
        self.list_images.selection_set(0)
        self.on_select_preview()

    def on_select_preview(self, event=None):
        if not self.image_files:
            return
        sel = self.list_images.curselection()
        if not sel:
            return
        path = self.image_files[sel[0]]
        try:
            with Image.open(path) as im:
                im = im.convert("RGB")
                im.thumbnail((360, 240))
                self.preview_imgtk = ImageTk.PhotoImage(im)
                self.lbl_preview.configure(image=self.preview_imgtk)
        except Exception as e:
            self.lbl_preview.configure(image="")
            self.preview_imgtk = None

    def validate_only(self):
        ok, msg = self._validate()
        if ok:
            messagebox.showinfo("OK", "Validare OK ✅")
        else:
            messagebox.showerror("Validation error", msg)

    def _validate(self):
        if not self.var_title_en.get().strip():
            return False, "Title EN este obligatoriu."
        if not self.var_title_ro.get().strip():
            return False, "Title RO este obligatoriu."
        if not self.var_beachslug.get().strip():
            return False, "BeachSlug este obligatoriu."
        if not self.var_zone.get().strip():
            return False, "Zone este obligatoriu."
        slug = self.var_slug.get().strip()
        if not slug:
            slug = slugify(self.var_title_en.get())
            self.var_slug.set(slug)
        if not re.match(r"^[a-z0-9_]+$", slug):
            return False, "Slug invalid. Folosește litere mici, cifre și _."
        if (self.acc_root / slug).exists():
            return False, f"Există deja folderul pentru slug: {slug}"
        if not self.image_files:
            return False, "Selectează cel puțin o imagine."
        return True, ""

    def generate(self):
        ok, msg = self._validate()
        if not ok:
            messagebox.showerror("Validation error", msg)
            return

        acc_id = self.var_slug.get().strip()

        # load index fresh (avoid stale)
        main_index = load_json(self.index_path)

        acc_dir = self.acc_root / acc_id
        images_dir = acc_dir / "images"
        acc_index_path = acc_dir / "index.json"
        images_dir.mkdir(parents=True, exist_ok=True)

        # process images
        out_files = []
        for i, src in enumerate(self.image_files):
            suffix = "" if i == 0 else str(i)
            dst_name = f"{acc_id}{suffix}.webp"
            dst = images_dir / dst_name
            ensure_1200x800_webp(Path(src), dst)
            out_files.append(dst_name)

        image_urls = [f"{REPO_RAW_BASE}/data/accommodations/{acc_id}/images/{name}" for name in out_files]

        # descriptions
        description_en = self.txt_desc_en.get("1.0", "end").strip()
        description_ro = self.txt_desc_ro.get("1.0", "end").strip()

        acc_json = {
            "id": acc_id,
            "beachSlug": self.var_beachslug.get().strip(),
            "zone": self.var_zone.get().strip(),

            "titleEn": self.var_title_en.get().strip(),
            "titleRo": self.var_title_ro.get().strip(),

            "address": self.var_address.get().strip(),
            "phone": self.var_phone.get().strip(),
            "email": self.var_email.get().strip(),
            "website": self.var_website.get().strip(),

            "category": self.var_category.get().strip(),
            "rating": parse_float(self.var_rating.get(), 0.0),
            "ratingScale": parse_float(self.var_rating_scale.get(), 10.0),
            "featured": bool(self.var_featured.get()),

            "guests": parse_int(self.var_guests.get(), 0),
            "sizeSqm": parse_int(self.var_size.get(), 0),
            "view": self.var_view.get().strip(),
            "bedrooms": parse_int(self.var_bedrooms.get(), 0),

            "petFriendly": bool(self.var_pet.get()),
            "pool": bool(self.var_pool.get()),
            "wifi": bool(self.var_wifi.get()),
            "parking": bool(self.var_parking.get()),
            "airConditioning": bool(self.var_ac.get()),
            "kitchen": bool(self.var_kitchen.get()),
            "washer": bool(self.var_washer.get()),
            "balcony": bool(self.var_balcony.get()),
            "bbq": bool(self.var_bbq.get()),

            "ownerId": self.var_owner_id.get().strip(),
            "ownerCode": self.var_owner_code.get().strip(),

            "lat": parse_float(self.var_lat.get(), 0.0),
            "lon": parse_float(self.var_lon.get(), 0.0),

            "descriptionEn": description_en,
            "descriptionRo": description_ro,

            "images": image_urls
        }

        dist = self.var_dist_override.get().strip()
        if dist:
            acc_json["distanceMetersOverride"] = parse_int(dist, 0)

        save_json(acc_index_path, acc_json)

        # update main index
        if acc_id not in main_index["items"]:
            main_index["items"].append(acc_id)
            save_json(self.index_path, main_index)

        self.lbl_status.config(text=f"✅ Generated: data/accommodations/{acc_id}/ (and updated index.json)")
        self.last_generated_slug = acc_id
        self.btn_git_commit.config(state="normal")

        messagebox.showinfo(
            "Success",
            "Fișiere generate cu succes ✅\n\n"
            f"Slug: {acc_id}\n\n"
            "Acum în Git Bash rulează:\n"
            "git add data/accommodations\n"
            f'git commit -m \"Add accommodation {acc_id}\"\n'
            "git push"
        )


    def git_add_commit(self):
        slug = self.last_generated_slug
        if not slug:
            messagebox.showwarning("Nothing to commit", "Nu există o cazare generată în sesiunea asta. Apasă mai întâi Generate files.")
            return

        # 1) git add
        ok, out = run_cmd(["git", "add", "data/accommodations"], self.repo_root)
        if not ok:
            messagebox.showerror("Git add failed", out or "Unknown error")
            return

        # 2) git commit
        msg = f"Add accommodation {slug}"
        ok, out = run_cmd(["git", "commit", "-m", msg], self.repo_root)
        if not ok:
            # dacă nu ai schimbări, git commit returnează eroare "nothing to commit"
            messagebox.showerror("Git commit failed", out or "Unknown error")
            return

        messagebox.showinfo("Committed", f"✅ Commit created:\n{msg}\n\nAcum rulează manual:\n\ngit push")


if __name__ == "__main__":
    app = App()
    app.mainloop()
