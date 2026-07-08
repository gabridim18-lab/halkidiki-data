package com.halkidikiguide.explorer.data.whattodo

import androidx.annotation.DrawableRes
import com.halkidikiguide.explorer.R

// ===== Modelul rămâne neschimbat =====
data class WhatToDoItem(
    val id: String,
    val categoryEn: String = "",
    val categoryRo: String = "",
    val beaches: List<String> = emptyList(),
    val titleEn: String,
    val titleRo: String,
    val address: String,
    val hoursEn: String? = null,
    val hoursRo: String? = null,
    val website: String? = null,
    val facebook: String? = null,
    val instagram: String? = null,
    val phone: String? = null,
    val email: String? = null,
    val price: String? = null,
    val descriptionEn: String = "",
    val descriptionRo: String = "",
    @DrawableRes val images: List<Int> = emptyList()
)

object WhatToDoData {

    // --- Utils ---
    private fun slug(s: String) = s.lowercase().replace("[^a-z0-9]+".toRegex(), "_").trim('_')

    // ===== 1) CATALOG COMPLET — fiecare activitate are categorie + plaje =====
    // (Am pus câteva exemple; continui cu același tipar pentru restul)
    private val catalog: Map<String, WhatToDoItem> = mapOf(
        "magic_park" to WhatToDoItem(
            id = "magic_park",
            categoryEn = "Entertainment",
            categoryRo = "Divertisment",
            beaches = listOf(
                "nea_krini_beach",
                "surfer_beach_angelochori",
                "riviera_virgin_beach",
                "oasis_beach",
                "sand_dunes_beach",
                "nea_iraklia_beach",
                "vergia_beach",
                "sozopoli_beach",
                "mykoniatika_secret_beach",
                "ntouraki_beach",
                "flogita_beach",
            ),
            titleEn = "Magic Park",            titleRo = "Magic Park",            address = "Agias Anastasias 15, Thessaloniki 555 35, Greece",
            hoursEn = "Mon–Sun 18:00–00:00",            hoursRo = "Lun–Dum 18:00–00:00",            website = "http://www.magicpark.gr/",
            facebook = "https://www.facebook.com/magicparkthessaloniki",            phone = "+30 2310 476 771",            price = "13€",
            descriptionEn = "\uD83C\uDFAA Magic Park is the ultimate amusement destination in Northern Greece, spanning over 50,000m² of non-stop fun!\n" +
                    "\n" +
                    "\uD83C\uDFA2 Attractions for All Ages\n" +
                    "\n" +
                    "    Thrill Zone: Heart-pounding roller coasters \uD83C\uDFA2, free-fall towers \uD83E\uDE82, and spinning rides \uD83C\uDF00 for adrenaline junkies\n" +
                    "\n" +
                    "    Family Land: Gentle ferris wheel \uD83C\uDFA1, bumper cars \uD83D\uDE97\uD83D\uDCA5, and classic carousels \uD83D\uDC0E\n" +
                    "\n" +
                    "    Kids' Kingdom: Mini train rides \uD83D\uDE82, interactive playgrounds \uD83C\uDFF0, and fairy-tale themed areas \uD83E\uDDDA\n" +
                    "\n" +
                    "\uD83C\uDF1F Special Features\n" +
                    "\n" +
                    "    \uD83C\uDFAE Arcade City: 100+ modern games with ticket prizes \uD83C\uDFC6\n" +
                    "\n" +
                    "    \uD83C\uDF54 Food Court: Traditional Greek souvlaki \uD83C\uDF62, cotton candy \uD83C\uDF6D, and refreshing frappés ☕\n" +
                    "\n" +
                    "    \uD83C\uDF19 Night Magic: Spectacular light shows ✨ and summer DJ parties \uD83C\uDFA7\n" +
                    "\n" +
                    "\uD83C\uDF9F\uFE0F Practical Info\n" +
                    "\n" +
                    "    \uD83D\uDD52 Hours: Seasonal (typically 10AM-12AM summer, weekends only in winter)\n" +
                    "\n" +
                    "    \uD83D\uDCB6 Tickets: Discounted family packages available\n" +
                    "\n" +
                    "    \uD83C\uDD7F\uFE0F Parking: Free secured lot (500+ spaces)\n" +
                    "\n" +
                    "    ♿ Accessibility: Wheelchair-friendly paths\n" +
                    "\n" +
                    "\uD83D\uDCA1 Pro Tip: Visit on weekdays to avoid crowds!",
            descriptionRo = "\uD83C\uDFAA Magic Park este cel mai mare parc de distracții din nordul Greciei, cu peste 50.000m² de aventuri!\n" +
                    "\n" +
                    "\uD83C\uDFA1 Atracții pentru Toți\n" +
                    "\n" +
                    "    Zona Extreme: Montagne russe fulgerante \uD83C\uDFA2, turnuri de cădere liberă \uD83E\uDE82 și caruseluri rotative \uD83C\uDF00\n" +
                    "\n" +
                    "    Spații Family: Ferris wheel relaxant \uD83C\uDFA1, mașini tampon \uD83D\uDE97\uD83D\uDCA5 și carusele clasice \uD83D\uDC0E\n" +
                    "\n" +
                    "    Lumea Copiilor: Trenulețe colorate \uD83D\uDE82, locuri de joacă interactive \uD83C\uDFF0 și zone tematice de basme \uD83E\uDDDA\n" +
                    "\n" +
                    "✨ Experiențe Unice\n" +
                    "\n" +
                    "    \uD83C\uDFAE Arcade-uri: 100+ jocuri moderne cu premii \uD83C\uDFC6\n" +
                    "\n" +
                    "    \uD83C\uDF74 Zona Gourmet: Souvlaki autentic \uD83C\uDF62, vată de zahăr \uD83C\uDF6D și frappé-uri răcoritoare ☕\n" +
                    "\n" +
                    "    \uD83C\uDF0C Nopți Magice: Spectacole de lumini ✨ și petreceri cu DJ în vară \uD83C\uDFA7\n" +
                    "\n" +
                    "ℹ\uFE0F Informații Utile\n" +
                    "\n" +
                    "    \uD83D\uDD52 Program: Variază pe sezoane (vara 10:00-24:00, iarna doar weekend)\n" +
                    "\n" +
                    "    \uD83D\uDCB0 Bilete: Pachete familie la preț redus\n" +
                    "\n" +
                    "    \uD83C\uDD7F\uFE0F Parcare: Gratuită și supravegheată (500+ locuri)\n" +
                    "\n" +
                    "    ♿ Accesibil: Căi speciale pentru scaune cu rotile\n" +
                    "\n" +
                    "\uD83D\uDCA1 Sfat: Vizitați în zilele lucrătoare pentru a evita cozile!",

            images = listOf(
                R.drawable.what_magicparc,                R.drawable.what_magicpark1,                R.drawable.what_magicpark2,
            )
        ),
        "tenpin_bowling" to WhatToDoItem(
            id = "tenpin_bowling",
            categoryEn = "Entertainment",
            categoryRo = "Divertisment",
            beaches = listOf(
                "nea_krini_beach",
            ),
            titleEn = "TenPin Bowling",            titleRo = "TenPin Bowling",            address = "Mitropolitou Kallidou 112, Kalamaria 551 31, Greece",
            // Compact schedule: Mon–Thu, Fri–Sat, Sun            hoursEn = "Mon–Thu 17:00–01:00, Fri–Sat 17:00–02:00, Sun 17:00–01:00",
            hoursRo = "Lun–Joi 17:00–01:00, Vin–Sâm 17:00–02:00, Dum 17:00–01:00",            website = "http://www.tenpin.gr/",
            phone = "+30 2310 421 412",
            descriptionEn = "🎳 Modern bowling alley in Halkidiki, perfect for families, friends, and groups.\n\n• 🎳 Multiple bowling lanes for casual games or competitive matches\n• 🍹 Full-service bar & snack area with drinks and light bites\n• 🎉 Party & event packages (birthdays, group celebrations)\n• 🌙 Late-night hours (check the current schedule)\n• 🚗 Easy access from Thessaloniki with parking available\n\n⭐ A great choice for a fun evening after the beach or as a rainy-day activity.",
            descriptionRo = "🎳 Sală de bowling modernă din Halkidiki, ideală pentru familii, prieteni și grupuri.\n\n• 🎳 Mai multe piste de bowling pentru jocuri relaxate sau competiții\n• 🍹 Bar complet & zonă de gustări, cu băuturi și snack-uri\n• 🎉 Pachete pentru petreceri și evenimente (zile de naștere, grupuri)\n• 🌙 Program prelungit seara (verifică programul actual)\n• 🚗 Acces facil din Salonic, cu parcare disponibilă\n\n⭐ O alegere excelentă pentru o seară distractivă după plajă sau în zilele mai răcoroase.",

            images = listOf(                R.drawable.what_tenpin,                R.drawable.what_tenpin1,                R.drawable.what_tenpin2,
            )
        ),
        "white_tower" to WhatToDoItem(
            id = "white_tower",
            categoryEn = "History & Landmarks",
            categoryRo = "Istorie și obiective",
            beaches = listOf(
                "nea_krini_beach",
            ),
            titleEn = "White Tower of Thessaloniki",            titleRo = "Turnul Alb din Salonic",
            address = "Thessaloniki 546 21, Greece",            hoursEn = "Winter (Nov 1-Mar 31): Daily 08:30-15:30 | Summer (Apr 1-Oct 31): Daily 08:00-20:00",
            hoursRo = "Sezon de iarnă (1 Noi-31 Mar): Zilnic 08:30-15:30 | Sezon de vară (1 Apr-31 Oct): Zilnic 08:00-20:00",
            website = "http://www.lpth.gr/",            phone = "+30 2310 267832",
            descriptionEn = "🏰 The White Tower (Λευκός Πύργος, Lefkós Pýrgos) is Thessaloniki’s most iconic landmark, located on the city’s waterfront.\n\n• 🏛️ Built in the 16th century during the Ottoman period\n• 🛡️ Originally part of the city’s defensive walls\n• 🩸 Later used as a prison, earning the nickname “Tower of Blood”\n• ⚪ Whitewashed in 1912, when Thessaloniki became part of Greece\n• 🖼️ Today it hosts a museum presenting the city’s history from antiquity to modern times\n• 🌅 Visitors can climb to the top for panoramic views of the Thermaic Gulf and Mount Olympus\n\n⭐ A must-see attraction and one of the best viewpoints in Thessaloniki.",
            descriptionRo = "🏰 Turnul Alb (Λευκός Πύργος, Lefkós Pýrgos) este cel mai emblematic reper al Salonicului, situat pe faleza orașului.\n\n• 🏛️ Construit în secolul al XVI-lea, în perioada otomană\n• 🛡️ A făcut parte inițial din sistemul de fortificații al orașului\n• 🩸 A fost folosit ulterior ca închisoare, primind porecla „Turnul Sângelui”\n• ⚪ A fost văruit în 1912, când Salonicul a devenit parte a Greciei\n• 🖼️ Astăzi găzduiește un muzeu dedicat istoriei orașului, din antichitate până în epoca modernă\n• 🌅 Vizitatorii pot urca până în vârf pentru priveliști panoramice asupra Golfului Thermaic și Muntelui Olimp\n\n⭐ Un obiectiv de neratat și unul dintre cele mai frumoase puncte de belvedere din Salonic.",
              price = "Winter: €4 | Summer: €8 (regular), €4 (reduced)",
            images = listOf(                R.drawable.what_whitetower,
            )
        ),
        "mediterranean_cosmos" to WhatToDoItem(
            id = "mediterranean_cosmos",
            categoryEn = "Shopping & Markets",
            categoryRo = "Cumpărături și piețe",
            beaches = listOf(
                "nea_krini_beach",
                "surfer_beach_angelochori",
                "riviera_virgin_beach",
                "oasis_beach",
                "sand_dunes_beach",
                "nea_iraklia_beach",
                "vergia_beach",
                "sozopoli_beach",
                "mykoniatika_secret_beach",
                "ntouraki_beach",
                "flogita_beach",
            ),
            titleEn = "Mediterranean Cosmos",            titleRo = "Mediterranean Cosmos",
            address = "11th km National Road, A/D Thessalonikis Neon Moudanion, Thessaloniki 570 01, Greece",            hoursEn = "Mon-Fri 10:00-21:00; Sat 10:00-22:00; Sun 10:00-21:00",
            hoursRo = "Lun-Vin 10:00-21:00; Sâm 10:00-22:00; Dum 10:00-21:00",            website = "https://www.mediterranean-cosmos.gr/",
            phone = "+30 231 077 0000",
            descriptionEn = "🛍️ Mediterranean Cosmos is the largest shopping and entertainment center in Northern Greece, offering a complete retail and leisure experience near Thessaloniki.\n\n• 🏬 Over 200 stores, including fashion brands, electronics, bookshops, and lifestyle outlets\n• 🎬 Modern multiplex cinema with the latest movie releases\n• 🎳 Bowling alley and family-friendly entertainment areas\n• 🍽️ Large food court with Greek and international cuisine, cafés, and dessert spots\n• 🎉 Regular events, exhibitions, and seasonal decorations throughout the year\n• 🚗 Easy access with spacious parking facilities\n\n⭐ A perfect destination for shopping, entertainment, and dining in one place.",
            descriptionRo = "🛍️ Mediterranean Cosmos este cel mai mare centru comercial și de divertisment din nordul Greciei, oferind o experiență completă de shopping și relaxare în apropiere de Salonic.\n\n• 🏬 Peste 200 de magazine, incluzând branduri de modă, electronice, librării și magazine de lifestyle\n• 🎬 Cinema multiplex modern, cu cele mai noi lansări de filme\n• 🎳 Bowling și zone de divertisment dedicate familiilor\n• 🍽️ Food court generos, cu bucătărie grecească și internațională, cafenele și deserturi\n• 🎉 Evenimente, expoziții și decoruri sezoniere pe tot parcursul anului\n• 🚗 Acces facil și parcare spațioasă\n\n⭐ O destinație ideală pentru cumpărături, distracție și luat masa într-un singur loc.",
              images = listOf(                R.drawable.what_medcosmos,                R.drawable.what_medcosmos1            )
        ),
        "war_museum_thessaloniki" to WhatToDoItem(            id = "war_museum_thessaloniki",
            categoryEn = "Museums & Culture",
            categoryRo = "Muzee și cultură",
            beaches = listOf(
                "nea_krini_beach",
            ),
            titleEn = "War Museum of Thessaloniki",
            titleRo = "Muzeul de Război din Salonic",            address = "Grigoriou Lampraki 4, Thessaloniki 546 36, Greece",
            hoursEn = "Hours vary by season — check official schedule",            hoursRo = "Programul variază în funcție de sezon — verificați orarul oficial",
            website = "https://warmuseum.gr/",            phone = "+302310249803",
            descriptionEn = "🏛️ Housed in an elegant early-20th-century building, the War Museum of Thessaloniki offers a comprehensive look into Greece’s modern military history.\n\n• ⚔️ Exhibitions covering the Balkan Wars, World War I, World War II, and more recent conflicts\n• 🎖️ Original military uniforms, medals, and personal belongings\n• 📜 Historical documents, photographs, and archival material\n• 🔫 Authentic weapons displayed with clarity and historical context\n• 🏛️ A calm and respectful atmosphere focused on education and remembrance\n\n⭐ A meaningful visit for those interested in modern history and the role of Thessaloniki in shaping Greece’s past.",
            descriptionRo = "🏛️ Găzduit într-o clădire elegantă de la începutul secolului XX, Muzeul de Război din Salonic oferă o perspectivă amplă asupra istoriei militare moderne a Greciei.\n\n• ⚔️ Expoziții dedicate Războaielor Balcanice, Primului și Celui de-al Doilea Război Mondial, precum și conflictelor recente\n• 🎖️ Uniforme militare autentice, medalii și obiecte personale\n• 📜 Documente istorice, fotografii și materiale de arhivă\n• 🔫 Arme originale, prezentate clar și contextualizat\n• 🏛️ O atmosferă sobră și respectuoasă, axată pe educație și memorie\n\n⭐ O vizită valoroasă pentru cei interesați de istoria modernă și de rolul Salonicului în trecutul Greciei.",
                images = listOf(                R.drawable.what_war_museum            )
        ),
        "horse_club" to WhatToDoItem(            id = "horse_club",
            categoryEn = "Adventure & Activities",
            categoryRo = "Aventură și activități",
            beaches = listOf(
                "surfer_beach_angelochori",
                "riviera_virgin_beach",
                "oasis_beach",
                "sand_dunes_beach",
                "nea_iraklia_beach",
                "vergia_beach",
                "sozopoli_beach",
                "mykoniatika_secret_beach",
                "ntouraki_beach",
                "flogita_beach",
            ),
            titleEn = "Horse Club (Thessaloniki Equestrian Center)",
            titleRo = "Horse Club (Centrul Ecvestru Thessaloniki)",            address = "GX6W+FH, Neo Risio 570 01, Greece",
            hoursEn = "Mon Closed; Tue–Sun 09:00–20:00",            hoursRo = "Lun Închis; Mar–Dum 09:00–20:00",
            website = "https://www.horseclub.gr/",            phone = "+30 694 845 0147",
            descriptionEn = "🐎 Thessaloniki Equestrian Center is a modern horseback riding facility offering professional training and outdoor experiences in a natural setting near Thessaloniki.\n\n• 🐎 Riding lessons for all ages and skill levels, from beginners to advanced riders\n• 🌿 Scenic horseback trails through nature and open landscapes\n• 🏆 Competition training, including show jumping and dressage\n• 👧 Summer camps and activities designed especially for children\n• 🏡 Well-maintained stables and facilities with experienced instructors\n\n⭐ An excellent choice for families, sports enthusiasts, and nature lovers seeking an active outdoor experience.",
            descriptionRo = "🐎 Centrul Ecvestru Thessaloniki este o bază modernă de echitație, care oferă antrenament profesionist și experiențe în aer liber, într-un cadru natural din apropierea Salonicului.\n\n• 🐎 Lecții de călărie pentru toate vârstele și nivelurile, de la începători la avansați\n• 🌿 Trasee ecvestre prin natură și peisaje deschise\n• 🏆 Pregătire pentru competiții, inclusiv sărituri peste obstacole și dresaj\n• 👧 Tabere de vară și activități dedicate copiilor\n• 🏡 Grajduri și facilități bine întreținute, cu instructori experimentați\n\n⭐ O alegere excelentă pentru familii, pasionați de sport și iubitori de natură.",

               images = listOf(                R.drawable.what_horseclub,                R.drawable.what_horseclub1,                R.drawable.what_horseclub2,
            )
        ),
        "drivepark" to WhatToDoItem(            id = "drivepark",
            categoryEn = "Entertainment",
            categoryRo = "Divertisment",
            beaches = listOf(
                "nea_krini_beach",
            ),
            titleEn = "Drivepark Go-Kart Circuit",            titleRo = "Drivepark Circuit de Go-Kart",
            address = "GX7R+JP Neo Rysio, Greece",            hoursEn = "Mon-Fri 14:00-23:00; Sat-Sun 10:00-23:00",
            hoursRo = "Lun-Vin 14:00-23:00; Sâm-Dum 10:00-23:00",            website = "http://www.drivepark.gr/",
            phone = "+30 2310 465723",
            descriptionEn = "🏎️ Drivepark Go-Kart Circuit Thessaloniki is a modern racing venue located just 15 km from Thessaloniki, near Nea Mihaniona in Neo Risio.\n\n• 🏁 Professionally designed track with challenging turns and fast straights\n• 🏎️ High-performance go-karts suitable for beginners and experienced drivers\n• 🛡️ Safety equipment and clear rules to ensure a secure racing experience\n• 👨‍🏫 Professional staff providing guidance and supervision\n• 🎉 Ideal for casual rides, competitive races, group events, and celebrations\n• 👨‍👩‍👧 Suitable for families, friends, and motorsport enthusiasts\n\n⭐ A thrilling, adrenaline-filled activity for anyone looking to add excitement to their visit near Thessaloniki.",
            descriptionRo = "🏎️ Drivepark Circuit de Go-Kart Thessaloniki este un complex modern de curse, situat la doar 15 km de Salonic, în apropiere de Nea Mihaniona, în zona Neo Risio.\n\n• 🏁 Traseu proiectat profesionist, cu viraje provocatoare și linii drepte rapide\n• 🏎️ Karte de înaltă performanță, potrivite atât pentru începători, cât și pentru piloți experimentați\n• 🛡️ Echipament de siguranță și reguli clare pentru o experiență sigură\n• 👨‍🏫 Personal profesionist care oferă instrucțiuni și supraveghere\n• 🎉 Ideal pentru plimbări recreative, curse competitive și evenimente de grup\n• 👨‍👩‍👧 Potrivit pentru familii, prieteni și pasionați de motorsport\n\n⭐ O activitate plină de adrenalină, perfectă pentru a adăuga distracție și energie unei zile petrecute lângă Salonic.",
            images = listOf(                R.drawable.what_drivepark
            )
        ),
        "lakkoma_thursday_market" to WhatToDoItem(
            id = "lakkoma_thursday_market",
            categoryEn = "Shopping & Markets",
            categoryRo = "Cumpărături și piețe",
            beaches = listOf(
                "perea_beach",
                "neoi_epivates_beach",
                "tourmpali_beach",
                "agistri_beach",
                "sahara_beach",
                "paralia_iraklia",
                "nea_plagia_beach",
                "nea_moudania_beach",
                "paralia_nea_moudania",
                "gremia",
                "windsurfers_paradise",
                "stavronikita_beach",
                "sani_beach",
                "simantro_beach",
                "paralia_kipsa",
                "chelona_beach",
                "siviri_beach",
                "agios_nikolaos_beach",
                "agios_nikolaos_fourka",
                "aigaiopelagitika_beach",
                "possidi_west_beach",
                "possidi_beach",
                "mola_kaliva_beach",
                "paralia_anemi",
                "paralia_skioni",
                "the_beach",
                "paralia_agias_paraskevis",
                "loutra_agias_paraskevis_beach",
                "pepples_beach_of_st_george",
                "ani_beach",
                "dymitry_beach",
                "cape_sevas",
                "cliff_rocks",
                "agios_nikolaos_kanistro_beach",
                "paralia_panagias",
                "porto_valitsa_bay",
                "paliouri_beach",
                "paralia_chroussou",
                "golden_beach",
                "alonaki_beach",
                "lagoon_beach",
                "paralia_pefkochori",
                "pefkochori_beach",
                "polychrono_beach",
                "kryopigi_beach",
                "kalithea_beach",
                "plage_liosi",
                "plage_moudounou",
                "athytos_beach",
                "plage_vothonas",
                "place_de_ninna",
                "savatianos_beach",
                "wild_sandy_beach",
                "nea_potidea_beach",
                "agios_mamas_beach",
                "kalyves_beach",
                "mikiverna_beach",
                "gerakini_beach",
            ),

            titleEn = "Lakkoma Thursday Street Market (Laiki Agora)",
            titleRo = "Piața de Joi Lakkoma (Laiki Agora)",
            address = "Central area, near the stadium • Plus Code: 4XVW+95 Lakkoma, Greece",
            hoursEn = "Thu 07:00–14:00",
            hoursRo = "Joi 07:00–14:00",
            descriptionEn = "Every Thursday morning, the quiet village of Lakkoma transforms into a lively, colorful market. Locals set up their stalls filled with fresh fruits, vegetables, golden honey, handmade cheeses, and bottles of pure olive oil – all coming straight from nearby farms.\n" +
                    "\n" +
                    "You’ll feel the genuine Greek atmosphere: friendly smiles, local music in the background, and the scent of herbs and roasted nuts drifting through the air. It’s a perfect stop for travelers who want to experience Halkidiki beyond its beaches.\n" +
                    "\n" +
                    "\uD83D\uDCA1 Why visit the Lakkoma market:\n" +
                    "\n" +
                    "To taste fresh, authentic local produce at great prices.\n" +
                    "\n" +
                    "To see everyday Greek life and connect with the locals.\n" +
                    "\n" +
                    "To enjoy a vibrant, traditional scene full of color and flavor.\n" +
                    "\n" +
                    "\uD83D\uDCCD Tip: Visit early in the morning (around 8–11 AM) for the best selection and cooler weather.",
            descriptionRo = "În fiecare joi dimineață, micuța localitate Lakkoma prinde viață odată cu tradiționala piață săptămânală. Străzile se umplu de tarabe colorate, de mirosul fructelor proaspete și de glasurile vânzătorilor care își laudă produsele.\n" +
                    "\n" +
                    "Aici poți găsi de toate: legume și fructe de sezon culese de fermieri locali, miere de pin, brânzeturi de casă, ulei de măsline autentic, condimente aromate și mici suveniruri lucrate manual. Totul într-o atmosferă caldă și autentic grecească, departe de zonele aglomerate de pe coastă.\n" +
                    "\n" +
                    "\uD83D\uDCA1 De ce merită vizitată piața din Lakkoma:\n" +
                    "\n" +
                    "Pentru prospețimea produselor locale și prețurile prietenoase.\n" +
                    "\n" +
                    "Pentru a simți ritmul real al vieții de zi cu zi din Halkidiki.\n" +
                    "\n" +
                    "Pentru fotografii superbe și interacțiuni directe cu localnicii.\n" +
                    "\n" +
                    "\uD83D\uDCCD Sfat: mergi dimineața, între orele 8:00 și 11:00, când piața e mai animată și oferta e bogată.",
            images = listOf(R.drawable.what_lakkoma_market, R.drawable.what_lakkoma_market1)
        ),
        "waterbus_karavakia" to WhatToDoItem(            id = "waterbus_karavakia",
            categoryEn = "Boat Trips & Sea Transport",
            categoryRo = "Excursii cu barca și transport pe mare",
            beaches = listOf(
                "perea_beach",
                "neoi_epivates_beach",
            ),
            titleEn = "Thessaloniki Waterbus (Karavakia)",
            titleRo = "Thessaloniki Waterbus (Karavakia)",            address = "Neoi Epivates Port, Neoi Epivates 57019, Greece",
            hoursEn = "Daily 10:00–22:00 (seasonal, Apr–Oct)",            hoursRo = "Zilnic 10:00–22:00 (sezonier, Apr–Oct)",
            website = "https://www.karavakia.com/",            phone = "+30 697 801 6009",
            descriptionEn = "⛴️ Thessaloniki Waterbus, known locally as “Karavakia”, offers a scenic and relaxing sea connection between the city center and the nearby beach suburbs.\n\n• 🌊 Direct boat routes linking Thessaloniki with Peraia, Nei Epivates, and Nea Krini\n• ⏱️ Approximately 50-minute cruise along the Thermaic Gulf\n• 🏙️ Beautiful views of Thessaloniki’s waterfront, the White Tower, and Mount Olympus on clear days\n• ☀️ Open deck seating, ideal for sightseeing and photos\n• 🍹 Bar service on board for drinks and refreshments\n• 🚤 Popular with both tourists and locals as transport or a mini-cruise experience\n\n⭐ A unique and enjoyable way to travel by sea while discovering Thessaloniki from a different perspective.",
            descriptionRo = "⛴️ Thessaloniki Waterbus, cunoscut sub numele de „Karavakia”, oferă o legătură pe mare relaxantă și pitorească între centrul orașului și zonele de plajă din apropiere.\n\n• 🌊 Rute directe către Peraia, Nei Epivates și Nea Krini\n• ⏱️ Croazieră de aproximativ 50 de minute pe Golful Thermaic\n• 🏙️ Priveliști spectaculoase asupra falezei din Salonic, Turnului Alb și Muntelui Olimp în zilele senine\n• ☀️ Punte deschisă, ideală pentru relaxare și fotografii\n• 🍹 Bar la bord, cu băuturi și gustări\n• 🚤 Preferat atât de turiști, cât și de localnici ca mijloc de transport sau mini-croazieră\n\n⭐ O modalitate specială și plăcută de a călători pe mare și de a vedea Salonicul dintr-o perspectivă diferită.",
               images = listOf(                R.drawable.what_txepi,                R.drawable.what_txepi1,                R.drawable.what_txepi2,
            )
        ),
        "waterland_thermi" to WhatToDoItem(            id = "waterland_thermi",
            categoryEn = "Water Parks",
            categoryRo = "Parcuri acvatice",
            beaches = listOf(
                "perea_beach",
                "neoi_epivates_beach",
            ),
            titleEn = "Waterland (Thermi)",            titleRo = "Waterland (Thermi)",
            address = "Tagarades, Thermi 570 01, Greece",            hoursEn = "Daily 10:00–18:00 (seasonal, May–Sep)",
            hoursRo = "Zilnic 10:00–18:00 (sezonier, Mai–Sep)",            website = "https://www.waterland.gr/",
            phone = "+30 2392 079512",
            descriptionEn = "💦 Waterland in Thermi is one of the largest waterparks in Greece, offering fun and relaxation for all ages just outside Thessaloniki.\n\n• 🎢 Giant water slides with different levels of thrill\n• 🌊 Wave pools and lazy rivers for relaxation and family fun\n• 👶 Dedicated play areas and safe attractions for children\n• 🌴 Relaxation zones with sunbeds and shaded areas\n• 🍔 Restaurants and snack bars with a variety of food options\n• 🎉 Seasonal events, summer parties, and special activities\n\n⭐ A perfect summer destination for families, groups of friends, and anyone looking to cool off and have fun.",
            descriptionRo = "💦 Waterland din Thermi este unul dintre cele mai mari parcuri acvatice din Grecia, oferind distracție și relaxare pentru toate vârstele, în apropiere de Salonic.\n\n• 🎢 Tobogane acvatice uriașe, cu niveluri diferite de adrenalină\n• 🌊 Piscine cu valuri și râuri leneșe pentru relaxare și distracție\n• 👶 Zone de joacă și atracții sigure dedicate copiilor\n• 🌴 Spații de relaxare cu șezlonguri și zone umbrite\n• 🍔 Restaurante și snack baruri cu opțiuni variate de mâncare\n• 🎉 Evenimente sezoniere, petreceri de vară și activități speciale\n\n⭐ O destinație ideală de vară pentru familii, grupuri de prieteni și oricine dorește să se răcorească și să se distreze.",
            images = listOf(                R.drawable.what_waterland,                R.drawable.what_waterland1,
                R.drawable.what_waterland2,            )
        ),
        "noesis_science_center" to WhatToDoItem(            id = "noesis_science_center",
            categoryEn = "Museums & Culture",
            categoryRo = "Muzee și cultură",
            beaches = listOf(
                "perea_beach",
            ),
            titleEn = "Noesis – Thessaloniki Science Center & Technology Museum",
            titleRo = "Noesis – Centrul de Știință și Muzeul Tehnologiei Salonic",            address = "6th km Thessaloniki–Thermi, Thermi 570 01, Greece",
            hoursEn = "Tue–Fri 09:00–15:00; Sat–Sun 11:30–20:00; Mon Closed",            hoursRo = "Mar–Vin 09:00–15:00; Sâm–Dum 11:30–20:00; Lun Închis",
            website = "https://www.noesis.edu.gr/",            phone = "+30 2310 483000",
            descriptionEn = "🔬 NOESIS is a modern science center and technology museum near Thessaloniki, offering interactive experiences that combine education, innovation, and entertainment.\n\n• 🧪 Hands-on interactive exhibitions for all ages\n• 🌌 Planetarium shows exploring space and astronomy\n• 🎥 3D cinema and motion simulator experiences\n• 🏛️ Permanent collections focused on ancient Greek technology, transport, and science\n• 🧠 Temporary exhibitions and educational programs throughout the year\n• 👨‍👩‍👧 Ideal for families, students, and curious minds\n\n⭐ A fascinating destination for learning, discovery, and fun through science and technology.",
            descriptionRo = "🔬 NOESIS este un centru modern de știință și muzeu al tehnologiei, situat în apropiere de Salonic, care îmbină educația, inovația și divertismentul.\n\n• 🧪 Expoziții interactive, potrivite pentru toate vârstele\n• 🌌 Spectacole de planetariu dedicate spațiului și astronomiei\n• 🎥 Cinema 3D și experiențe cu simulator de mișcare\n• 🏛️ Colecții permanente despre tehnologia Greciei antice, transport și știință\n• 🧠 Expoziții temporare și programe educaționale pe tot parcursul anului\n• 👨‍👩‍👧 Ideal pentru familii, elevi, studenți și persoane curioase\n\n⭐ O destinație captivantă pentru învățare, descoperire și distracție prin știință și tehnologie.",

            images = listOf(                R.drawable.what_noesis,                R.drawable.what_noesis1            )
        ),
        "gerovassiliou_winery_agia_triada" to WhatToDoItem(        id = "gerovassiliou_winery_agia_triada",
            categoryEn = "Local Products & Tastings",
            categoryRo = "Produse locale și degustări",
            beaches = listOf(
                "perea_beach",
                "neoi_epivates_beach",
            ),
        titleEn = "Ktima Gerovassiliou Winery near Agia Triada",
            titleRo = "Crama Ktima Gerovassiliou lângă Agia Triada",        address = "Epanomi (slopes near Agia Triada), 57500 Thessaloniki, Greece",
            hoursEn = "Mon, Thu, Fri 10:00–16:00; Wed 13:00–19:00; Sat–Sun 11:00–17:00; Tue Closed",        hoursRo = "Lun, Joi, Vin 10:00–16:00; Mie 13:00–19:00; Sâm–Dum 11:00–17:00; Mar Închis",
            website = "https://www.gerovassiliou.gr/en/visits",        phone = "+30 23920 44567",
            descriptionEn = "🍷 Ktima Gerovassiliou is a renowned family-run winery located on the slopes of Epanomi, near Agia Triada, offering an authentic wine and cultural experience close to Thessaloniki.\n\n• 🌿 Founded in 1981, with vineyards set in a scenic coastal landscape\n• 🏭 Guided tours through the vineyards, modern winery, and aging cellars\n• 🍾 Insight into bottling, maturation processes, and wine production\n• 🏛️ Home to the famous Wine Museum showcasing rare exhibits and tools\n• 🍷 Wine tastings featuring Greek and international varieties, including rare vintages\n• 🧀 Tastings often paired with local products and delicacies\n\n⭐ A must-visit destination for wine lovers, culture enthusiasts, and anyone seeking a refined experience near Thessaloniki.",
            descriptionRo = "🍷 Ktima Gerovassiliou este o cramă de familie renumită, situată pe versanții din Epanomi, aproape de Agia Triada, oferind o experiență autentică de vin și cultură în apropiere de Salonic.\n\n• 🌿 Înființată în 1981, cu podgorii amplasate într-un peisaj natural deosebit\n• 🏭 Tururi ghidate prin vii, crama modernă și spațiile de învechire\n• 🍾 Prezentarea proceselor de îmbuteliere, maturare și producție a vinului\n• 🏛️ Găzduiește celebrul Muzeu al Vinului, cu exponate rare\n• 🍷 Degustări de vinuri grecești și internaționale, inclusiv ediții speciale\n• 🧀 Degustările sunt adesea însoțite de produse și delicatese locale\n\n⭐ O destinație de neratat pentru pasionații de vin, iubitorii de cultură și cei care caută o experiență rafinată lângă Salonic.",
            images = listOf(            R.drawable.what_gerovassiliou1,            R.drawable.what_gerovassiliou2        )
        ),
        "petralona_cave_exploration" to WhatToDoItem(
            id = "petralona_cave_exploration",
            categoryEn = "Museums & Culture",
            categoryRo = "Muzee și cultură",
            beaches = listOf(
                "perea_beach",
                "neoi_epivates_beach",
                "tourmpali_beach",
                "nea_michaniona_beach",
                "agistri_beach",
                "paralia_potami",
                "sahara_beach",
                "delfinia_beach",
                "paralia_iraklia",
                "beach_mykoniatika",
                "nea_plagia_beach",
                "dionisiou_beach",
            ),

            titleEn = "Petralona Cave Exploration & Anthropological Museum",
            titleRo = "Explorarea Peșterii Petralona și Muzeul Antropologic",
            address = "Petralona 630 80, Halkidiki, Greece",
            hoursEn = "Daily 09:00–15:00 (seasonal)",
            hoursRo = "Zilnic 09:00–15:00 (sezonier)",
            phone = "+30 23730 71671",
            descriptionEn = "Nestled at the foot of Mount Katsika near the village of Petralona, this spectacular cave is one of Halkidiki’s most fascinating natural and archaeological sites. Discovered in 1959, the Petralona Cave is famous for its stunning formations of stalactites and stalagmites, and especially for the skull of a prehistoric human, estimated to be over 700,000 years old — one of Europe’s most remarkable paleoanthropological findings.\n" +
                    "\n" +
                    "Visitors can follow a well-designed path through illuminated chambers, discovering the wonders of nature and the deep history of humankind. Knowledgeable guides share stories about the cave’s discovery and the scientific studies that made it world-renowned.\n" +
                    "\n" +
                    "\uD83D\uDCA1 Why visit:\n" +
                    "\n" +
                    "To witness breathtaking underground formations.\n" +
                    "\n" +
                    "To see a site of major archaeological importance.\n" +
                    "\n" +
                    "To enjoy an unforgettable and educational experience for all ages.\n" +
                    "\n" +
                    "\uD83D\uDCCD Tip: Wear comfortable shoes and light clothing — the cave maintains a constant temperature of around 17°C year-round.",
            descriptionRo = "Situată la poalele Muntelui Katsika, în apropiere de satul Petralona, această peșteră spectaculoasă este unul dintre cele mai impresionante situri naturale și arheologice din Halkidiki. Descoperită în 1959, Peștera Petralona este renumită pentru stalactitele și stalagmitele sale uimitoare, dar mai ales pentru descoperirea craniului omului preistoric, vechi de peste 700.000 de ani – una dintre cele mai importante descoperiri paleoantropologice din Europa.\n" +
                    "\n" +
                    "Vizitatorii pot explora un traseu amenajat prin galerii subterane, unde fiecare pas te poartă într-o lume fascinantă a formelor de piatră sculptate de timp. Ghidajele oferă informații interesante despre evoluția omului și istoria naturală a regiunii.\n" +
                    "\n" +
                    "\uD83D\uDCA1 De ce merită vizitată:\n" +
                    "\n" +
                    "Pentru spectaculoasa frumusețe naturală a peșterii.\n" +
                    "\n" +
                    "Pentru importanța arheologică unică în lume.\n" +
                    "\n" +
                    "Pentru experiența educativă și atmosfera misterioasă a subteranului.\n" +
                    "\n" +
                    "\uD83D\uDCCD Sfat: Poartă încălțăminte comodă și haine ușoare – temperatura în interior este constantă, în jur de 17°C tot timpul anului.",
            images = listOf(R.drawable.what_petralona_cave, R.drawable.what_petralona_cave1)
        ),
        "salt_lake_aggelohori" to WhatToDoItem(            id = "salt_lake_aggelohori",
            categoryEn = "Nature & Scenic Spots",
            categoryRo = "Natură și peisaje",
            beaches = listOf(
                "agia_triada_beach",
            ),
            titleEn = "Salt Lake of Aggelohori",            titleRo = "Lacul Sărat Aggelohori",
            address = "Aggelohori, near Epanomi, Thessaloniki, Greece",            hoursEn = "Open-air natural site (accessible anytime, best during daylight)",
            hoursRo = "Sit natural în aer liber (accesibil oricând, recomandat pe timp de zi)",
            descriptionEn = "🦩 The Salt Lake of Aggelohori is a peaceful coastal wetland near Epanomi, forming part of the wider Axios–Loudias–Aliakmonas National Park.\n\n• 🌊 Shallow coastal lagoon with salt flats and surrounding marshlands\n• 🐦 Important stopover for migratory birds, including flamingos, herons, and rare species\n• 📸 Ideal location for birdwatching, nature photography, and quiet exploration\n• 🌾 Natural landscape offering a calm and untouched atmosphere\n• 🌍 Ecologically valuable area with cultural and environmental significance\n\n⭐ A hidden natural gem for nature lovers seeking tranquility and authentic landscapes near Thessaloniki.",
            descriptionRo = "🦩 Lacul Sărat Aggelohori este o zonă umedă de coastă liniștită, situată lângă Epanomi, parte a Parcului Național Axios–Loudias–Aliakmonas.\n\n• 🌊 Lagună de coastă puțin adâncă, cu sărături și zone mlăștinoase\n• 🐦 Punct important de popas pentru păsările migratoare, inclusiv flamingo, stârci și specii rare\n• 📸 Locație ideală pentru observarea păsărilor, fotografie și explorare în natură\n• 🌾 Peisaj natural calm, aproape nealterat\n• 🌍 Zonă cu valoare ecologică și culturală deosebită\n\n⭐ O bijuterie naturală mai puțin cunoscută, perfectă pentru iubitorii de natură și liniște, aproape de Salonic.",
                images = listOf(                R.drawable.what_aggelohori_lake,                R.drawable.what_aggelohori_lake1
            )
        ),
        "lighthouse_angelochori" to WhatToDoItem(
            id = "lighthouse_angelochori",
            categoryEn = "History & Landmarks",
            categoryRo = "Istorie și obiective",
            beaches = listOf(
                "agia_triada_beach",
            ),
            titleEn = "Angelochori Lighthouse",            titleRo = "Farul din Angelochori",            address = "Cape Megalo Embolo, Angelochori, near Nea Michaniona, Thessaloniki, Greece",            hoursEn = "Open-air landmark (accessible anytime, best at sunset)",
            hoursRo = "Monument în aer liber (accesibil oricând, recomandat la apus)",
            descriptionEn = "🗼 The Angelochori Lighthouse is a historic coastal landmark built in 1864 on Cape Megalo Embolo, making it one of the oldest lighthouses in Northern Greece.\n\n• ⚓ Originally guided ships entering the Thermaic Gulf\n• 🗿 Well-preserved stone tower with historical significance\n• 🌊 Located on a quiet cape surrounded by sea and natural scenery\n• 🌅 Stunning panoramic views, especially beautiful at sunset\n• 📸 Ideal spot for photography, walks, and peaceful moments\n\n⭐ A charming seaside landmark offering history, tranquility, and unforgettable views near Thessaloniki.",
            descriptionRo = "🗼 Farul din Angelochori este un reper istoric de coastă, construit în 1864 pe Capul Megalo Embolo, fiind unul dintre cele mai vechi faruri din nordul Greciei.\n\n• ⚓ A ghidat odinioară vasele care intrau în Golful Thermaic\n• 🗿 Turn de piatră bine conservat, cu valoare istorică\n• 🌊 Amplasat pe un promontoriu liniștit, înconjurat de mare și natură\n• 🌅 Priveliști panoramice spectaculoase, mai ales la apus\n• 📸 Loc ideal pentru fotografie, plimbări și momente de relaxare\n\n⭐ Un obiectiv deosebit care îmbină istoria, liniștea și peisajele memorabile, aproape de Salonic.",
                 images = listOf(                R.drawable.what_angelochori_lighthouse,
            )
        ),
        "nea_kallikrateia_tuesday_market" to WhatToDoItem(            id = "nea_kallikrateia_tuesday_market",
            categoryEn = "Shopping & Markets",
            categoryRo = "Cumpărături și piețe",
            beaches = listOf(
                "nea_krini_beach",
                "paralia_nea_potidea",
                "paralia_sani",
                "elani_beach",
                "skala_fourkas_beach",
                "paralia_posidi",
                "nea_skioni_beach",
                "loutra_beach",
                "kanastraio_or_kalogria_cape",
                "kanistro_beach",
                "xenia_beach",
                "glarokavos_beach",
                "hanioti_beach",
                "paralia_afitos",
                "varkes_beach",
                "nea_fokea_beach",
                "paralia_kalivia",
            ),
            titleEn = "Nea Kallikrateia Tuesday Street Market (Laiki Agora)",            titleRo = "Piața Volantă de Marți Nea Kallikrateia (Laiki Agora)",            address = "Central Market area (Agias Paraskevis), Nea Kallikrateia, Halkidiki, Greece",
            hoursEn = "Tue 07:00–14:00",            hoursRo = "Marți 07:00–14:00",
            descriptionEn = "🛒 Every Tuesday morning, the central market of Nea Kallikrateia comes alive with a traditional ‘laiki agora’, offering an authentic taste of local life.\n\n• 🍎 Fresh fruit and vegetables directly from local producers\n• 🫒 Olives, olive oil, cheese, honey, nuts, and herbs\n• 🐟 Fresh fish and seasonal regional products\n• 👕 Clothing, shoes, and household items alongside food stalls\n• 🎶 Lively atmosphere with locals shopping for weekly supplies\n\n⭐ A genuine local experience best enjoyed early in the morning.",
            descriptionRo = "🛒 În fiecare marți dimineața, piața centrală din Nea Kallikrateia prinde viață printr-o ‘laiki agora’ tradițională, oferind o experiență autentică locală.\n\n• 🍎 Fructe și legume proaspete direct de la producători locali\n• 🫒 Măsline, ulei de măsline, brânzeturi, miere, nuci și ierburi aromatice\n• 🐟 Pește proaspăt și produse sezoniere din regiune\n• 👕 Îmbrăcăminte, încălțăminte și articole pentru casă\n• 🎶 Atmosferă animată, cu localnici care își fac cumpărăturile săptămânale\n\n⭐ O experiență locală autentică, ideală de descoperit dimineața devreme.",

                images = listOf(                R.drawable.what_kallikrateia_market,                R.drawable.what_kallikrateia_market1
            )
        ),
        "nea_michaniona_fish_market" to WhatToDoItem(            id = "nea_michaniona_fish_market",
            categoryEn = "Shopping & Markets",
            categoryRo = "Cumpărături și piețe",
            beaches = listOf(
                "agia_triada_beach",
                "hidden_beach",
                "surfer_beach_angelochori",
                "riviera_virgin_beach",
                "nea_michaniona_beach",
                "oasis_beach",
                "sand_dunes_beach",
                "paralia_potami",
                "nea_iraklia_beach",
                "vergia_beach",
                "delfinia_beach",
                "sozopoli_beach",
                "mykoniatika_secret_beach",
                "beach_mykoniatika",
                "ntouraki_beach",
                "flogita_beach",
                "dionisiou_beach",
            ),
            titleEn = "Nea Michaniona Port & Fish Market",            titleRo = "Portul și Piața de Pește din Nea Michaniona",            address = "Port of Nea Michaniona, Thermaic Gulf, Thessaloniki, Greece",
            hoursEn = "Daily early morning & late afternoon (best time: 07:00–10:00 for fresh catch)",            hoursRo = "Zilnic dimineața devreme și după-amiaza (cea mai bună perioadă: 07:00–10:00 pentru captura proaspătă)",
            descriptionEn = "⚓ Nea Michaniona is one of the largest fishing ports in Northern Greece, well known for its lively and authentic fish market.\n\n• 🐟 Fresh daily catch brought in every morning by local fishermen\n• 🦐 Wide variety of seafood, including fish, octopus, shrimp, and mussels\n• 🛒 Direct sales at the port’s market stalls, straight from the boats\n• 🍽️ Popular with locals and tavernas sourcing the freshest ingredients\n• 🌊 Authentic coastal atmosphere reflecting traditional maritime life\n\n⭐ A must-visit spot to experience Greek fishing culture, fresh seafood, and the charm of a traditional seaside town.",
            descriptionRo = "⚓ Nea Michaniona este unul dintre cele mai mari porturi de pescuit din nordul Greciei, renumit pentru piața sa de pește autentică și animată.\n\n• 🐟 Captura zilei adusă în fiecare dimineață de pescarii locali\n• 🦐 Varietate bogată de fructe de mare: pește, caracatiță, creveți, midii\n• 🛒 Vânzare directă la tarabele din port, chiar de lângă ambarcațiuni\n• 🍽️ Frecventată de localnici și taverne în căutare de produse proaspete\n• 🌊 Atmosferă marină autentică, specifică unui oraș pescăresc tradițional\n\n⭐ Un loc de neratat pentru a descoperi cultura pescuitului grecesc, gustul fructelor de mare proaspete și farmecul litoralului local.",

            images = listOf(                R.drawable.what_michaniona_fishmarket,                R.drawable.what_michaniona_fishmarket1,
                R.drawable.what_michaniona_fishmarket2,            )
        ),
        "shipwreck_kyra_panagia" to WhatToDoItem(
            id = "shipwreck_kyra_panagia",
            categoryEn = "Nature & Scenic Spots",
            categoryRo = "Natură și peisaje",
            beaches = listOf(
                "agia_triada_beach",
                "hidden_beach",
                "tourmpali_beach",
                "nea_michaniona_beach",
                "agistri_beach",
                "paralia_potami",
                "sahara_beach",
                "delfinia_beach",
                "paralia_iraklia",
                "beach_mykoniatika",
                "nea_plagia_beach",
                "dionisiou_beach",
            ),
            titleEn = "Shipwreck of Kyra Panagia",            titleRo = "Epava navei „Kyra Panagia”",            address = "Off the coast near Kyra Panagia island, Sithonia, Halkidiki, Greece",            hoursEn = "Accessible by boat tours (seasonal, usually May–October)",
            hoursRo = "Accesibil prin excursii cu barca (sezonier, de obicei mai–octombrie)",            website = "https://www.sailinthassos.com/kyra-panagia-shipwreck-tour/",
            descriptionEn = "🚢 The Kyra Panagia shipwreck rests in shallow turquoise waters near the uninhabited island of Kyra Panagia, off the coast of Sithonia.\n\n• 🌊 Crystal-clear, shallow sea ideal for swimming and snorkeling\n• 🤿 Popular spot for snorkeling and beginner-friendly diving\n• 🐠 Rich marine life surrounding the wreck\n• 📸 Unique scenery combining shipwreck, sea, and wild nature\n• 🚤 Accessible via boat tours from Sithonia and nearby ports\n• 🧭 A blend of adventure, photography, and maritime history\n\n⭐ A spectacular sea attraction for explorers and nature lovers visiting Sithonia.",
            descriptionRo = "🚢 Epava navei Kyra Panagia se află în ape turcoaz puțin adânci, lângă insula nelocuită Kyra Panagia, în largul Sithoniei.\n\n• 🌊 Ape limpezi și puțin adânci, ideale pentru înot și snorkeling\n• 🤿 Loc apreciat pentru snorkeling și scufundări ușoare\n• 🐠 Viață marină bogată în jurul epavei\n• 📸 Peisaj unic, ce îmbină epava, marea și natura sălbatică\n• 🚤 Accesibil prin excursii cu barca din Sithonia și porturile apropiate\n• 🧭 Combinație de aventură, fotografie și istorie maritimă\n\n⭐ O atracție marină spectaculoasă pentru exploratori și iubitorii de natură care vizitează Sithonia.",
            images = listOf(                R.drawable.what_kyra_panagia_wreck,                R.drawable.what_kyra_panagia_wreck1            )
        ),
        "epanomi_seaside_park" to WhatToDoItem(
            id = "epanomi_seaside_park",
            categoryEn = "Nature & Scenic Spots",
            categoryRo = "Natură și peisaje",
            beaches = listOf(
                "agia_triada_beach",
                "hidden_beach",
                "tourmpali_beach",
                "nea_michaniona_beach",
                "agistri_beach",
                "paralia_potami",
                "sahara_beach",
                "delfinia_beach",
                "paralia_iraklia",
                "beach_mykoniatika",
                "nea_plagia_beach",
                "dionisiou_beach",
            ),

            titleEn = "Epanomi Seaside Park",
            titleRo = "Parcul Litoral Epanomi",
            address = "Epanomi, Thermaic Gulf, Thessaloniki, Greece",
            hoursEn = "Open-air park (accessible anytime, best in spring and summer)",
            hoursRo = "Parc în aer liber (accesibil oricând, recomandat primăvara și vara)",
            descriptionEn = "🌊 Epanomi Seaside Park is a coastal recreation area along the Thermaic Gulf, combining sandy stretches, seaside paths, and relaxing open spaces.\n\n• 🏖️ Sandy coastal areas ideal for relaxation and short beach stops\n• 🚶 Walking and cycling paths with sea views\n• 🧺 Picnic spots and open areas for families and groups\n• 🎶 Seasonal cultural and community events\n• 🌿 Close to nearby wetlands and the famous Epanomi shipwreck\n• 🌅 Peaceful atmosphere with beautiful seaside scenery\n\n⭐ A relaxing seaside park that blends leisure, nature, and coastal views near Thessaloniki.",
            descriptionRo = "🌊 Parcul Litoral Epanomi este o zonă de recreere situată pe malul Golfului Thermaic, ce îmbină plaje nisipoase, alei de promenadă și spații de relaxare.\n\n• 🏖️ Zone de plajă potrivite pentru relaxare și opriri scurte la mare\n• 🚶 Aleile pentru plimbări și ciclism, cu priveliști spre mare\n• 🧺 Spații pentru picnic și întâlniri în familie sau cu prietenii\n• 🎶 Evenimente culturale și comunitare organizate sezonier\n• 🌿 Aproape de zone umede și celebra epavă din Epanomi\n• 🌅 Atmosferă liniștită și peisaje maritime plăcute\n\n⭐ Un parc litoral relaxant care îmbină recreerea, natura și priveliștile de coastă, aproape de Salonic.",

              images = listOf(
                R.drawable.what_epanomi_park,
                R.drawable.what_epanomi_park1,
                R.drawable.what_epanomi_park2
            )
        ),
        "epanomi_beacon" to WhatToDoItem(
            id = "epanomi_beacon",
            categoryEn = "History & Landmarks",
            categoryRo = "Istorie și obiective",
            beaches = listOf(
                "agia_triada_beach",
                "hidden_beach",
                "tourmpali_beach",
                "nea_michaniona_beach",
                "agistri_beach",
                "paralia_potami",
                "sahara_beach",
                "delfinia_beach",
                "paralia_iraklia",
                "beach_mykoniatika",
                "nea_plagia_beach",
                "dionisiou_beach",
            ),

            titleEn = "Beacon of Epanomi",
            titleRo = "Farul din apropiere de Epanomi",
            address = "Cape Epanomi, Thermaic Gulf, near Thessaloniki, Greece",
            hoursEn = "Open-air landmark (accessible anytime, best at sunset or sunrise)",
            hoursRo = "Monument în aer liber (accesibil oricând, recomandat la apus sau răsărit)",
            descriptionEn = "🗼 The Beacon of Epanomi stands on a sandy cape extending into the Thermaic Gulf, serving as a scenic coastal landmark.\n\n• ⚓ Originally built as a maritime marker guiding ships along the coast\n• 🌊 Located on a wide sandy cape with open sea views\n• 📸 Panoramic scenery ideal for photography and sunset views\n• 🚶 Perfect area for seaside walks and quiet exploration\n• 🗺️ Close to the Epanomi shipwreck and surrounding coastal attractions\n• 🌅 Calm and peaceful atmosphere by the sea\n\n⭐ A beautiful coastal spot offering space, views, and a relaxed seaside experience near Thessaloniki.",
            descriptionRo = "🗼 Farul din Epanomi este situat pe un promontoriu nisipos ce se întinde în Golful Thermaic, fiind un reper costier pitoresc.\n\n• ⚓ Construit inițial ca punct de orientare pentru navigația maritimă\n• 🌊 Amplasat pe un cap nisipos larg, cu deschidere către mare\n• 📸 Peisaje panoramice ideale pentru fotografie și apusuri spectaculoase\n• 🚶 Zonă potrivită pentru plimbări pe malul mării și explorare liniștită\n• 🗺️ Aproape de epava din Epanomi și alte atracții de coastă\n• 🌅 Atmosferă calmă și relaxantă, în mijlocul naturii\n\n⭐ Un loc deosebit pe litoral, perfect pentru priveliști, liniște și o experiență relaxantă lângă Salonic.",
              images = listOf(
                R.drawable.what_epanomi_beacon,
                R.drawable.what_epanomi_beacon1
            )
        ),
        "farm_partali" to WhatToDoItem(
            id = "farm_partali",
            categoryEn = "Adventure & Activities",
            categoryRo = "Aventură și activități",
            beaches = listOf(
                "agia_triada_beach",
            ),

            titleEn = "Farm Partali",
            titleRo = "Ferma Partali",
            address = "Partali Farm, Epanomi, Thessaloniki, Greece",
            hoursEn = "Open daily 09:00–19:00 (check seasonal schedule for activities)",
            hoursRo = "Deschis zilnic 09:00–19:00 (verificați programul sezonier pentru activități)",
            website = "https://www.farmpartali.com/",
            phone = "+30 23920 43571",
            descriptionEn = "🐄 Farm Partali is a family-friendly agro-tourism destination in Epanomi, offering an authentic glimpse into traditional farming life in Northern Greece.\n\n• 🐑 Farm animals, orchards, and gardens in a natural rural setting\n• 👨‍👩‍👧 Interactive experiences such as feeding animals and hands-on activities\n• 🐎 Horse riding experiences suitable for children and adults\n• 🫒 Olive oil tasting and introduction to local agricultural products\n• 🎨 Seasonal workshops and activities connected to rural traditions\n• 🌿 Calm countryside atmosphere, ideal for relaxation and learning\n\n⭐ A wonderful experience for families, nature lovers, and anyone looking to connect with rural life and local gastronomy near Thessaloniki.",
            descriptionRo = "🐄 Ferma Partali este o destinație agroturistică prietenoasă cu familiile, situată în Epanomi, oferind o experiență autentică a vieții agricole tradiționale din nordul Greciei.\n\n• 🐑 Animale de fermă, livezi și grădini într-un cadru rural natural\n• 👨‍👩‍👧 Experiențe interactive, precum hrănirea animalelor și activități practice\n• 🐎 Experiențe de echitație potrivite pentru copii și adulți\n• 🫒 Degustări de ulei de măsline și prezentarea produselor locale\n• 🎨 Ateliere și activități sezoniere legate de tradițiile rurale\n• 🌿 Atmosferă liniștită de țară, ideală pentru relaxare și învățare\n\n⭐ O experiență minunată pentru familii, iubitorii de natură și cei care doresc să se conecteze cu viața rurală și gastronomia locală, aproape de Salonic.",
            images = listOf(
                R.drawable.what_farm_partali,
                R.drawable.what_farm_partali1
            )
        ),
        "tsantali_winery" to WhatToDoItem(
            id = "tsantali_winery",
            categoryEn = "Local Products & Tastings",
            categoryRo = "Produse locale și degustări",
            beaches = listOf(
                "surfer_beach_angelochori",
                "riviera_virgin_beach",
                "oasis_beach",
                "sand_dunes_beach",
                "nea_iraklia_beach",
                "vergia_beach",
                "sozopoli_beach",
                "mykoniatika_secret_beach",
                "ntouraki_beach",
                "flogita_beach",
            ),

            titleEn = "Tsantali Winery",
            titleRo = "Crama Tsantali",
            address = "Agios Pavlos, Halkidiki, Greece",
            hoursEn = "Mon–Fri 09:00–16:00 (tours by appointment)",
            hoursRo = "Lun–Vin 09:00–16:00 (vizite cu programare)",
            website = "https://www.tsantali.com/",
            phone = "+30 23730 20020",
            descriptionEn = "🍷 Tsantali Winery is one of Greece’s most historic and respected wine producers, with a legacy dating back to 1890, located in Agios Pavlos, Halkidiki.\n\n• 🌿 Vineyards set in the unique terroir of Northern Greece\n• 🏭 Guided tours through cellars, production, and aging areas\n• 🍾 Insight into both traditional and modern winemaking techniques\n• 🏆 Tastings of award-winning Greek wines\n• 🧬 Exploration of the Tsantali family heritage and wine philosophy\n• 🧀 Wine tastings often paired with local flavors\n\n⭐ A refined destination for wine lovers and cultural travelers exploring Halkidiki.",
            descriptionRo = "🍷 Crama Tsantali este unul dintre cei mai vechi și apreciați producători de vin din Grecia, cu o istorie ce începe în anul 1890, situată în Agios Pavlos, Halkidiki.\n\n• 🌿 Podgorii amplasate într-un terroir unic al Greciei de Nord\n• 🏭 Tururi ghidate prin pivnițe, zone de producție și învechire\n• 🍾 Prezentarea tehnicilor de vinificație tradiționale și moderne\n• 🏆 Degustări de vinuri grecești premiate\n• 🧬 Descoperirea moștenirii familiei Tsantali și a filozofiei vinului\n• 🧀 Degustări acompaniate de produse locale\n\n⭐ O destinație rafinată pentru iubitorii de vin și turiștii pasionați de cultură care vizitează Halkidiki.",
            images = listOf(
                R.drawable.what_tsantali_winery,
                R.drawable.what_tsantali_winery1
            )
        ),
        "nea_triglia_monday_market" to WhatToDoItem(
            id = "nea_triglia_monday_market",
            categoryEn = "Shopping & Markets",
            categoryRo = "Cumpărături și piețe",
            beaches = emptyList(),

            titleEn = "Nea Triglia Monday Street Market (Laiki Agora)",
            titleRo = "Piața Volantă de Luni Nea Triglia (Laiki Agora)",
            address = "Central square, next to the school and park, Nea Triglia, Halkidiki, Greece",
            hoursEn = "Mon 07:00–14:00",
            hoursRo = "Luni 07:00–14:00",
            descriptionEn = "🛒 Every Monday morning, Nea Triglia hosts a lively ‘laiki agora’ in the central square, next to the school and the park.\n\n• 🍎 Fresh fruit and vegetables from local farmers\n• 🫒 Olives, olive oil, honey, cheeses, herbs, and seasonal products\n• 🐟 Fresh fish and regional specialties\n• 👕 Clothing, shoes, and household goods alongside food stalls\n• 🤝 Vibrant meeting point for the local community\n\n⭐ A great opportunity to experience authentic Halkidiki life and local flavors.",
            descriptionRo = "🛒 În fiecare luni dimineața, Nea Triglia găzduiește o ‘laiki agora’ animată în piața centrală, lângă școală și parc.\n\n• 🍎 Fructe și legume proaspete de la producători locali\n• 🫒 Măsline, ulei de măsline, miere, brânzeturi, ierburi și produse de sezon\n• 🐟 Pește proaspăt și specialități locale\n• 👕 Îmbrăcăminte, încălțăminte și articole pentru casă\n• 🤝 Punct de întâlnire plin de viață pentru comunitatea locală\n\n⭐ O ocazie excelentă de a descoperi viața autentică din Halkidiki și produsele locale.",
             images = listOf(
                R.drawable.what_triglia_market,
                R.drawable.what_triglia_market1
            )
        ),
        "nea_moudania_wednesday_market" to WhatToDoItem(
            id = "nea_moudania_wednesday_market",
            categoryEn = "Shopping & Markets",
            categoryRo = "Cumpărături și piețe",
            beaches = emptyList(),

            titleEn = "Nea Moudania Wednesday Street Market (Laiki Agora)",
            titleRo = "Piața Volantă de Miercuri Nea Moudania (Laiki Agora)",
            address = "Near KTEL bus station, Nea Moudania, Halkidiki, Greece",
            hoursEn = "Wed 07:00–14:30",
            hoursRo = "Miercuri 07:00–14:30",
            descriptionEn = "🛒 The weekly street market of Nea Moudania, held every Wednesday near the KTEL bus station, is the largest open-air market in Halkidiki.\n\n• 🍎 Fresh fruit and vegetables from local producers\n• 🫒 Olives, olive oil, honey, nuts, herbs, and regional products\n• 🐟 Fish and seafood, including seasonal catches\n• 🧀 Cheeses and other traditional local delicacies\n• 👕 Clothing, footwear, and household goods\n• 🎶 Lively atmosphere attracting both locals and visitors\n\n⭐ A must-see market to experience authentic local life and the vibrant spirit of Halkidiki.",
            descriptionRo = "🛒 Piața săptămânală din Nea Moudania, organizată în fiecare miercuri lângă stația KTEL, este cea mai mare piață în aer liber din Halkidiki.\n\n• 🍎 Fructe și legume proaspete de la producători locali\n• 🫒 Măsline, ulei de măsline, miere, nuci, ierburi și produse regionale\n• 🐟 Pește și fructe de mare, în funcție de sezon\n• 🧀 Brânzeturi și alte delicatese tradiționale\n• 👕 Îmbrăcăminte, încălțăminte și articole pentru casă\n• 🎶 Atmosferă animată, frecventată de localnici și turiști\n\n⭐ O piață de neratat pentru a descoperi viața locală autentică și energia specifică din Halkidiki.",
              images = listOf(
                R.drawable.what_moudania_market,
                R.drawable.what_moudania_market1
            )
        ),
        "simantra_friday_market" to WhatToDoItem(
            id = "simantra_friday_market",
            categoryEn = "Shopping & Markets",
            categoryRo = "Cumpărături și piețe",
            beaches = listOf(
                "paralia_psakoudia",
                "psakoudia_beach",
                "paralia_sargani",
                "paralia_askamnia",
                "red_rocks_of_metamorphosis",
                "nikiti_beach",
                "kastri_beach",
                "agios_ioannis_beach",
                "koviou_beach",
                "kalogria_beach",
                "small_spathies_beach",
                "spathies_beach",
                "paralia_perigiali",
                "elia_beach",
                "lagomandra_beach",
                "nikitis_beach_sithonia",
                "tripotamos_beach",
                "paradisos_beach",
                "neos_marmaras_beach",
                "porto_carras_beach",
                "kohi_beach",
                "diaporti_beach",
                "likithos_beach",
                "azapiko_beach",
                "paralia_alexandra_xenia",
                "paralia_azapiko",
                "paralia_xenia",
                "tristinika_beach",
                "destenika_beach",
                "ema_beach",
                "paralia_toroni",
                "toroni_beach",
                "porto_koufo_beach",
                "marathias_beach",
                "secret_beach",
                "sithonia_cape",
                "kalamitsi_beach",
                "kriaritsi_beach",
                "prassou_beach",
                "tourkolimnionas",
                "skala_sykias_beach",
                "linaraki_beach",
                "valti_beach",
                "agridia_beach",
                "goa_beach",
                "sarti_beach",
                "achlada",
                "heart_shaped_bay",
                "orange_beach",
                "kavourotrypes_beach",
                "mega_portokali_beach",
                "dream_coast_beach",
                "robinson_beach",
                "banana_beach",
                "zografou_beach",
                "koutloumousi_beach",
                "bara_beach",
                "manos_beach",
                "karydi_beach",
                "rocks_on_the_beach",
                "karagatsi_beach",
                "talgo_beach",
                "lagonisi_beach",
                "livrohio",
                "trani_ammouda",
                "beach_of_pirgos",
                "schinias_beach",
                "salonikiou_beach",
                "paralia_salonikiou",
            ),

            titleEn = "Simantra Friday Street Market (Laiki Agora)",
            titleRo = "Piața Volantă de Vineri Simantra (Laiki Agora)",
            address = "Central square, next to St. Athanasios Church, Simantra, Halkidiki, Greece",
            hoursEn = "Fri 07:00–14:00",
            hoursRo = "Vineri 07:00–14:00",
            descriptionEn = "🛒 Every Friday morning, Simantra hosts a traditional ‘laiki agora’ in the central square next to St. Athanasios Church, offering a glimpse into everyday village life in Halkidiki.\n\n• 🍎 Seasonal fruit and vegetables from local producers\n• 🫒 Olives, olive oil, cheese, honey, herbs, and baked goods\n• 🐟 Fresh fish and regional products\n• 👕 Clothing, footwear, and household items\n• 🤝 Lively meeting point for residents and visitors alike\n\n⭐ A charming local market, perfect for experiencing the authentic rhythm of a traditional Halkidiki village.",
            descriptionRo = "🛒 În fiecare vineri dimineața, Simantra găzduiește o ‘laiki agora’ tradițională în piața centrală, lângă Biserica Sf. Atanasios, oferind o perspectivă autentică asupra vieții de zi cu zi din Halkidiki.\n\n• 🍎 Fructe și legume de sezon de la producători locali\n• 🫒 Măsline, ulei de măsline, brânzeturi, miere, ierburi și produse de panificație\n• 🐟 Pește proaspăt și produse regionale\n• 👕 Îmbrăcăminte, încălțăminte și articole pentru casă\n• 🤝 Punct de întâlnire animat pentru localnici și vizitatori\n\n⭐ O piață locală plină de farmec, ideală pentru a descoperi ritmul autentic al unui sat tradițional din Halkidiki.",
             images = listOf(
                R.drawable.what_simantra_market,
                R.drawable.what_simantra_market1
            )
        ),
        "byzantine_museum_chalkidiki" to WhatToDoItem(
            id = "byzantine_museum_chalkidiki",
            categoryEn = "Museums & Culture",
            categoryRo = "Muzee și cultură",
            beaches = listOf(
                "nea_moudania_beach",
                "gremia",
                "windsurfers_paradise",
                "sani_beach",
                "simantro_beach",
                "chelona_beach",
                "siviri_beach",
                "agios_nikolaos_fourka",
                "aigaiopelagitika_beach",
                "possidi_beach",
                "mola_kaliva_beach",
                "paralia_skioni",
                "the_beach",
                "loutra_agias_paraskevis_beach",
                "pepples_beach_of_st_george",
                "dymitry_beach",
                "cape_sevas",
                "agios_nikolaos_kanistro_beach",
                "paralia_panagias",
                "paliouri_beach",
                "paralia_chroussou",
                "alonaki_beach",
                "lagoon_beach",
                "pefkochori_beach",
                "polychrono_beach",
                "kalithea_beach",
                "plage_liosi",
                "athytos_beach",
                "plage_vothonas",
                "savatianos_beach",
                "wild_sandy_beach",
                "agios_mamas_beach",
                "kalyves_beach",
                "gerakini_beach",
            ),

            titleEn = "Byzantine Museum of Chalkidiki",
            titleRo = "Muzeul Bizantin al Halkidiki",
            address = "Agiou Stefanou, Afitos 630 77, Kassandra, Halkidiki, Greece",
            hoursEn = "Tue–Sun 09:00–16:00; Mon Closed",
            hoursRo = "Mar–Dum 09:00–16:00; Lună Închis",
            phone = "+30 23740 22230",
            descriptionEn = "🏛️ The Byzantine Museum of Halkidiki is housed in the historic Stamos Papavasileiou mansion in Afitos, offering insight into the region’s Byzantine and post-Byzantine heritage.\n\n• 🖼️ Collection of Byzantine and post-Byzantine icons\n• 📜 Manuscripts, mosaics, and ecclesiastical objects\n• ⛪ Exhibits highlighting the spiritual and artistic history of Halkidiki\n• 🏛️ Elegant historic architecture in a traditional mansion\n• 🌊 Panoramic views over the Toroneos Gulf from the museum grounds\n• 🏘️ Located in Afitos, one of the most picturesque villages in the region\n\n⭐ A refined cultural stop combining history, art, and beautiful seaside views in Halkidiki.",
            descriptionRo = "🏛️ Muzeul Bizantin al Halkidiki este găzduit în conacul istoric Stamos Papavasileiou din Afitos și oferă o incursiune în patrimoniul bizantin și post-bizantin al regiunii.\n\n• 🖼️ Colecție de icoane bizantine și post-bizantine\n• 📜 Manuscrise, mozaicuri și obiecte bisericești\n• ⛪ Expoziții ce evidențiază istoria spirituală și artistică a Halkidiki\n• 🏛️ Arhitectură elegantă într-un conac tradițional\n• 🌊 Priveliști panoramice asupra Golfului Toroneos\n• 🏘️ Situat în Afitos, una dintre cele mai pitorești localități din regiune\n\n⭐ Un obiectiv cultural rafinat, ce îmbină istoria, arta și peisajele maritime din Halkidiki.",
            images = listOf(
                R.drawable.what_byzantine_museum,
                R.drawable.what_byzantine_museum1
            )
        ),
        "fisheries_museum_moudania" to WhatToDoItem(
            id = "fisheries_museum_moudania",
            categoryEn = "Museums & Culture",
            categoryRo = "Muzee și cultură",
            beaches = listOf(
                "hidden_beach",
                "nea_moudania_beach",
                "gremia",
                "windsurfers_paradise",
                "sani_beach",
                "simantro_beach",
                "chelona_beach",
                "siviri_beach",
                "agios_nikolaos_fourka",
                "aigaiopelagitika_beach",
                "possidi_beach",
                "mola_kaliva_beach",
                "paralia_skioni",
                "the_beach",
                "loutra_agias_paraskevis_beach",
                "pepples_beach_of_st_george",
                "dymitry_beach",
                "cape_sevas",
                "agios_nikolaos_kanistro_beach",
                "paralia_panagias",
                "paliouri_beach",
                "paralia_chroussou",
                "alonaki_beach",
                "lagoon_beach",
                "pefkochori_beach",
                "polychrono_beach",
                "kalithea_beach",
                "plage_liosi",
                "athytos_beach",
                "plage_vothonas",
                "savatianos_beach",
                "wild_sandy_beach",
                "agios_mamas_beach",
                "kalyves_beach",
                "gerakini_beach",
            ),

            titleEn = "Fisheries Museum of Nea Moudania",
            titleRo = "Muzeul de Pescuit din Nea Moudania",
            address = "Nea Moudania 632 00, Halkidiki, Greece",
            hoursEn = "Tue–Sun 09:00–14:00; Mon Closed",
            hoursRo = "Mar–Dum 09:00–14:00; Luni Închis",
            phone = "+30 23730 26166",
            descriptionEn = "⚓ The Fisheries Museum of Nea Moudania is the only museum in Greece dedicated exclusively to the history and traditions of fishing.\n\n• 🎣 Traditional fishing tools, nets, and boat equipment\n• 🗺️ Maps, photographs, and detailed models illustrating fishermen’s daily life\n• 🐟 Exhibits focused on marine biodiversity and coastal ecosystems\n• 🌊 Insights into sustainable fishing practices and maritime heritage\n• 🏛️ Cultural presentation highlighting Halkidiki’s deep connection with the sea\n\n⭐ A unique cultural stop offering a deeper understanding of fishing traditions and the maritime environment of Halkidiki.",
            descriptionRo = "⚓ Muzeul de Pescuit din Nea Moudania este singurul muzeu din Grecia dedicat exclusiv istoriei și tradițiilor pescuitului.\n\n• 🎣 Unelte tradiționale de pescuit, plase și echipamente de bărci\n• 🗺️ Hărți, fotografii și machete ce ilustrează viața pescarilor\n• 🐟 Expoziții despre biodiversitatea marină și ecosistemele costiere\n• 🌊 Prezentarea practicilor de pescuit sustenabil și a patrimoniului maritim\n• 🏛️ O incursiune culturală în legătura profundă dintre Halkidiki și mare\n\n⭐ O oprire culturală unică, ideală pentru a descoperi tradițiile pescărești și importanța mediului maritim din Halkidiki.",

            images = listOf(
                R.drawable.what_moudania_fisheries,
                R.drawable.what_moudania_fisheries1
            )
        ),
        //Kassandra
        "block518_paintball" to WhatToDoItem(
            id = "block518_paintball",
            categoryEn = "Entertainment",
            categoryRo = "Divertisment",
            beaches = listOf(
                "nea_moudania_beach",
                "gremia",
                "windsurfers_paradise",
                "sani_beach",
                "simantro_beach",
                "chelona_beach",
                "siviri_beach",
                "agios_nikolaos_fourka",
                "aigaiopelagitika_beach",
                "possidi_beach",
                "mola_kaliva_beach",
                "paralia_skioni",
                "the_beach",
                "loutra_agias_paraskevis_beach",
                "pepples_beach_of_st_george",
                "dymitry_beach",
                "cape_sevas",
                "agios_nikolaos_kanistro_beach",
                "paralia_panagias",
                "paliouri_beach",
                "paralia_chroussou",
                "alonaki_beach",
                "lagoon_beach",
                "pefkochori_beach",
                "polychrono_beach",
                "kalithea_beach",
                "plage_liosi",
                "athytos_beach",
                "plage_vothonas",
                "savatianos_beach",
                "wild_sandy_beach",
                "agios_mamas_beach",
                "kalyves_beach",
                "gerakini_beach",
            ),

            titleEn = "BLOCK 5.18 Paintball Club Halkidiki",
            titleRo = "BLOCK 5.18 Paintball Club Halkidiki",
            address = "Nea Moudania, Halkidiki, Greece",
            hoursEn = "Open daily 10:00–20:00 (booking required)",
            hoursRo = "Deschis zilnic 10:00–20:00 (rezervare necesară)",
            website = "https://www.facebook.com/block5.18paintballclub/",
            phone = "+30 694 606 9957",
            descriptionEn = "🔫 BLOCK 5.18 Paintball Club in Nea Moudania offers action-packed outdoor fun for adrenaline lovers, groups, and team activities.\n\n• 🏞️ Specially designed outdoor fields with natural and artificial obstacles\n• 🎯 Safe and exciting paintball scenarios for beginners and experienced players\n• 🛡️ Quality equipment and protective gear provided\n• 👨‍🏫 Professional staff ensuring safety and smooth gameplay\n• 👥 Ideal for groups, families, friends, and corporate team-building events\n\n⭐ A thrilling alternative to the beach, perfect for those seeking energy, action, and unforgettable moments in Halkidiki.",
            descriptionRo = "🔫 BLOCK 5.18 Paintball Club din Nea Moudania oferă distracție în aer liber plină de adrenalină pentru iubitorii de acțiune, grupuri și activități de echipă.\n\n• 🏞️ Terenuri exterioare special amenajate, cu obstacole naturale și artificiale\n• 🎯 Scenarii de paintball sigure și captivante, pentru începători și avansați\n• 🛡️ Echipamente de calitate și protecție asigurată\n• 👨‍🏫 Personal profesionist care supraveghează jocurile\n• 👥 Ideal pentru grupuri de prieteni, familii și team-building corporate\n\n⭐ O alternativă plină de energie la plajă, perfectă pentru cei care caută acțiune și experiențe memorabile în Halkidiki.",
              images = listOf(
                R.drawable.what_block518_paintball,
                R.drawable.what_block518_paintball1
            )
        ),
        "agios_mamas_wetland" to WhatToDoItem(
            id = "agios_mamas_wetland",
            categoryEn = "Nature & Scenic Spots",
            categoryRo = "Natură și peisaje",
            beaches = listOf(
                "nea_moudania_beach",
                "gremia",
                "windsurfers_paradise",
                "sani_beach",
                "simantro_beach",
                "chelona_beach",
                "siviri_beach",
                "agios_nikolaos_fourka",
                "aigaiopelagitika_beach",
                "possidi_beach",
                "mola_kaliva_beach",
                "paralia_skioni",
                "the_beach",
                "loutra_agias_paraskevis_beach",
                "pepples_beach_of_st_george",
                "dymitry_beach",
                "cape_sevas",
                "agios_nikolaos_kanistro_beach",
                "paralia_panagias",
                "paliouri_beach",
                "paralia_chroussou",
                "alonaki_beach",
                "lagoon_beach",
                "pefkochori_beach",
                "polychrono_beach",
                "kalithea_beach",
                "plage_liosi",
                "athytos_beach",
                "plage_vothonas",
                "savatianos_beach",
                "wild_sandy_beach",
                "agios_mamas_beach",
                "kalyves_beach",
                "gerakini_beach",
            ),

            titleEn = "Agios Mamas Wetland",
            titleRo = "Zona Umedă Agios Mamas",
            address = "Agios Mamas, Halkidiki, Greece",
            hoursEn = "Open-air natural site (accessible anytime, best during daylight)",
            hoursRo = "Sit natural în aer liber (accesibil oricând, recomandat pe timp de zi)",
            descriptionEn = "🦩 The Agios Mamas Wetland is one of the most important coastal ecosystems in Halkidiki, located near the village of Agios Mamas.\n\n• 🌊 Shallow lagoon and marshland forming a rich natural habitat\n• 🐦 Refuge for over 100 bird species, including flamingos, herons, and rare migratory birds\n• 📸 Ideal location for birdwatching, nature photography, and quiet exploration\n• 🚶 Peaceful walking areas within a landscape that changes with the seasons\n• 🌍 Part of the Natura 2000 network, highlighting its ecological importance\n\n⭐ A serene natural destination for wildlife enthusiasts and nature lovers exploring Halkidiki.",
            descriptionRo = "🦩 Zona umedă Agios Mamas este unul dintre cele mai importante ecosisteme costiere din Halkidiki, situată în apropierea satului Agios Mamas.\n\n• 🌊 Lagună puțin adâncă și zonă mlăștinoasă cu habitat natural bogat\n• 🐦 Adăpostește peste 100 de specii de păsări, inclusiv flamingo, stârci și specii migratoare rare\n• 📸 Locație ideală pentru observarea păsărilor, fotografie și explorare în natură\n• 🚶 Zone potrivite pentru plimbări liniștite într-un peisaj ce se schimbă odată cu anotimpurile\n• 🌍 Parte a rețelei Natura 2000, subliniind importanța sa ecologică\n\n⭐ O destinație naturală liniștită, perfectă pentru iubitorii de faună și peisaje autentice din Halkidiki.",
              images = listOf(
                R.drawable.what_agiosmamas_wetland,
                R.drawable.what_agiosmamas_wetland1
            )
        ),
        "archaeological_area_potidea" to WhatToDoItem(
            id = "archaeological_area_potidea",
            categoryEn = "History & Landmarks",
            categoryRo = "Istorie și obiective",
            beaches = listOf(
                "paralia_nea_moudania",
                "paralia_nea_potidea",
                "stavronikita_beach",
                "paralia_sani",
                "paralia_kipsa",
                "elani_beach",
                "agios_nikolaos_beach",
                "skala_fourkas_beach",
                "possidi_west_beach",
                "paralia_posidi",
                "paralia_anemi",
                "nea_skioni_beach",
                "paralia_agias_paraskevis",
                "loutra_beach",
                "ani_beach",
                "kanastraio_or_kalogria_cape",
                "cliff_rocks",
                "kanistro_beach",
                "porto_valitsa_bay",
                "xenia_beach",
                "golden_beach",
                "glarokavos_beach",
                "paralia_pefkochori",
                "hanioti_beach",
                "kryopigi_beach",
                "paralia_afitos",
                "plage_moudounou",
                "varkes_beach",
                "place_de_ninna",
                "nea_fokea_beach",
                "nea_potidea_beach",
                "paralia_kalivia",
                "mikiverna_beach",
            ),

            titleEn = "Archaeological Area of Potidea",
            titleRo = "Zona Arheologică Potidea",
            address = "Nea Potidea, Kassandra, Halkidiki, Greece",
            hoursEn = "Open-air site (accessible anytime, best during daylight)",
            hoursRo = "Sit în aer liber (accesibil oricând, recomandat pe timp de zi)",
            descriptionEn = "🏛️ The archaeological site of Potidea preserves the remains of an ancient city founded by the Corinthians in 600 BC, located at the narrow isthmus of Kassandra.\n\n• 🏺 Strategic ancient colony with an important role in classical and Byzantine periods\n• 🧱 Visible sections of ancient walls and defensive fortifications\n• 🏘️ Traces of early settlements revealing daily life in antiquity\n• 🌊 Panoramic views over the canal of Nea Potidea\n• 📚 A place where history, archaeology, and landscape come together\n\n⭐ A fascinating cultural stop combining ancient history with impressive seaside views in Halkidiki.",
            descriptionRo = "🏛️ Zona arheologică Potidea păstrează vestigiile orașului antic fondat de corintieni în anul 600 î.Hr., situat pe istmul îngust al Kassandrei.\n\n• 🏺 Colonie strategică cu un rol important în epoca clasică și bizantină\n• 🧱 Fragmente vizibile din zidurile antice și fortificații defensive\n• 🏘️ Urme de așezări ce oferă indicii despre viața din antichitate\n• 🌊 Priveliști panoramice asupra canalului Nea Potidea\n• 📚 Un loc unde istoria, arheologia și peisajul se îmbină armonios\n\n⭐ O oprire culturală captivantă ce îmbină istoria antică cu peisaje maritime impresionante din Halkidiki.",
              images = listOf(
                R.drawable.what_potidea_archaeology,
                R.drawable.what_potidea_archaeology1
            )
        ),
        "magic_bloom_waterpark_potidea" to WhatToDoItem(
            id = "magic_bloom_waterpark_potidea",
            categoryEn = "Water Parks",
            categoryRo = "Parcuri acvatice",
            beaches = listOf(
                "paralia_nea_moudania",
                "paralia_nea_potidea",
                "stavronikita_beach",
                "paralia_sani",
                "paralia_kipsa",
                "elani_beach",
                "agios_nikolaos_beach",
                "skala_fourkas_beach",
                "possidi_west_beach",
                "paralia_posidi",
                "paralia_anemi",
                "nea_skioni_beach",
                "paralia_agias_paraskevis",
                "loutra_beach",
                "ani_beach",
                "kanastraio_or_kalogria_cape",
                "cliff_rocks",
                "kanistro_beach",
                "porto_valitsa_bay",
                "xenia_beach",
                "golden_beach",
                "glarokavos_beach",
                "paralia_pefkochori",
                "hanioti_beach",
                "kryopigi_beach",
                "paralia_afitos",
                "plage_moudounou",
                "varkes_beach",
                "place_de_ninna",
                "nea_fokea_beach",
                "nea_potidea_beach",
                "paralia_kalivia",
                "mikiverna_beach",
            ),

            titleEn = "Magic Bloom – Waterpark Potidea",
            titleRo = "Magic Bloom – Waterpark Potidea",
            address = "Nea Potidea, Kassandra, Halkidiki, Greece",
            hoursEn = "Daily 10:00–19:00 (seasonal, May–September)",
            hoursRo = "Zilnic 10:00–19:00 (sezonier, mai–septembrie)",
            website = "https://www.magicbloom.gr/",
            phone = "+30 23730 43210",
            descriptionEn = "💦 Magic Bloom Waterpark in Nea Potidea is a family-friendly water park offering fun, relaxation, and refreshing activities for all ages.\n\n• 🎢 A variety of waterslides, from thrilling rides to gentle slides\n• 🌊 Pools designed for both adults and children\n• 👶 Safe kids’ play areas with shallow water attractions\n• 🌴 Relaxation zones with sunbeds and shaded areas\n• 🍔 Snack bars and refreshment points throughout the park\n• 🎉 Organized events and activities during the season\n\n⭐ A perfect choice for a full day of fun, cooling off, and family entertainment beyond the beaches of Halkidiki.",
            descriptionRo = "💦 Magic Bloom Waterpark din Nea Potidea este un parc acvatic prietenos cu familiile, oferind distracție, relaxare și activități răcoritoare pentru toate vârstele.\n\n• 🎢 Tobogane acvatice variate, de la cele palpitante la cele pentru relaxare\n• 🌊 Piscine dedicate atât adulților, cât și copiilor\n• 👶 Zone de joacă sigure pentru copii, cu apă puțin adâncă\n• 🌴 Spații de relaxare cu șezlonguri și zone umbrite\n• 🍔 Snack baruri și puncte de servire a băuturilor\n• 🎉 Evenimente și activități organizate pe parcursul sezonului\n\n⭐ O alegere excelentă pentru o zi întreagă de distracție și răcorire, dincolo de plajele din Halkidiki.",
             images = listOf(
                R.drawable.what_magicbloom,
                R.drawable.what_magicbloom1
            )
        ),
        "sani_wetlands" to WhatToDoItem(
            id = "sani_wetlands",
            categoryEn = "Nature & Scenic Spots",
            categoryRo = "Natură și peisaje",
            beaches = listOf(
                "paralia_nea_moudania",
                "paralia_nea_potidea",
                "stavronikita_beach",
                "paralia_sani",
                "paralia_kipsa",
                "elani_beach",
                "agios_nikolaos_beach",
                "skala_fourkas_beach",
                "possidi_west_beach",
                "paralia_posidi",
                "paralia_anemi",
                "nea_skioni_beach",
                "paralia_agias_paraskevis",
                "loutra_beach",
                "ani_beach",
                "kanastraio_or_kalogria_cape",
                "cliff_rocks",
                "kanistro_beach",
                "porto_valitsa_bay",
                "xenia_beach",
                "golden_beach",
                "glarokavos_beach",
                "paralia_pefkochori",
                "hanioti_beach",
                "kryopigi_beach",
                "paralia_afitos",
                "plage_moudounou",
                "varkes_beach",
                "place_de_ninna",
                "nea_fokea_beach",
                "nea_potidea_beach",
                "paralia_kalivia",
                "mikiverna_beach",
            ),

            titleEn = "Sani Wetlands – Natural Park & Reserve",
            titleRo = "Sani Wetlands – Parc natural și rezervație",
            address = "Sani area, north of Stavronikita, Kassandra, Halkidiki, Greece",
            hoursEn = "Open-air natural reserve (accessible anytime, best during daylight)",
            hoursRo = "Rezervație naturală în aer liber (accesibilă oricând, recomandat pe timp de zi)",
            website = "https://www.sani-resort.com/sani-wetlands",
            descriptionEn = "🦩 The Sani Wetlands are a protected natural reserve near Sani, north of Stavronikita, covering over 400 hectares of coastal lagoons, marshes, and meadows.\n\n• 🌊 Extensive wetlands with lagoons, marshlands, and open meadows\n• 🐦 Home to more than 200 bird species, including herons, flamingos, and rare migratory birds\n• 🌿 Part of the Natura 2000 network, highlighting its high ecological value\n• 🚶 Marked trails ideal for peaceful walks through unspoiled nature\n• 📸 Excellent spot for birdwatching, nature photography, and quiet exploration\n\n⭐ A unique eco-destination offering tranquility, wildlife, and pristine landscapes in Halkidiki.",
            descriptionRo = "🦩 Zona umedă Sani este o rezervație naturală protejată, situată lângă Sani, la nord de Stavronikita, ce se întinde pe peste 400 de hectare de lagune costiere, zone mlăștinoase și pajiști.\n\n• 🌊 Zone umede extinse, cu lagune, mlaștini și pajiști naturale\n• 🐦 Adăpostește peste 200 de specii de păsări, inclusiv stârci, flamingo și specii migratoare rare\n• 🌿 Parte a rețelei Natura 2000, cu valoare ecologică deosebită\n• 🚶 Trasee marcate, ideale pentru plimbări liniștite în natură\n• 📸 Locație excelentă pentru observarea păsărilor și fotografie de natură\n\n⭐ O destinație ecologică unică, perfectă pentru iubitorii de natură, liniște și peisaje nealterate din Halkidiki.",

             images = listOf(
                R.drawable.what_sani_wetlands,
                R.drawable.what_sani_wetlands1
            )
        ),
        "stavronikita_tower" to WhatToDoItem(
            id = "stavronikita_tower",
            categoryEn = "History & Landmarks",
            categoryRo = "Istorie și obiective",
            beaches = listOf(
                "paralia_nea_moudania",
                "paralia_nea_potidea",
                "stavronikita_beach",
                "paralia_sani",
                "paralia_kipsa",
                "elani_beach",
                "agios_nikolaos_beach",
                "skala_fourkas_beach",
                "possidi_west_beach",
                "paralia_posidi",
                "paralia_anemi",
                "nea_skioni_beach",
                "paralia_agias_paraskevis",
                "loutra_beach",
                "ani_beach",
                "kanastraio_or_kalogria_cape",
                "cliff_rocks",
                "kanistro_beach",
                "porto_valitsa_bay",
                "xenia_beach",
                "golden_beach",
                "glarokavos_beach",
                "paralia_pefkochori",
                "hanioti_beach",
                "kryopigi_beach",
                "paralia_afitos",
                "plage_moudounou",
                "varkes_beach",
                "place_de_ninna",
                "nea_fokea_beach",
                "nea_potidea_beach",
                "paralia_kalivia",
                "mikiverna_beach",
            ),

            titleEn = "Stavronikita Tower (Sani Tower)",
            titleRo = "Turnul Stavronikita (Turnul Sani)",
            address = "Sani, Kassandra, Halkidiki, Greece",
            hoursEn = "Open-air historical monument (accessible anytime, exterior only)",
            hoursRo = "Monument istoric în aer liber (accesibil oricând, doar exteriorul)",
            descriptionEn = "🏰 The Stavronikita Tower, also known as the Sani Tower, is a well-preserved 14th-century Byzantine tower built by the monks of Mount Athos to protect their landholdings in Kassandra.\n\n• 🏛️ Byzantine defensive tower dating back to the 14th century\n• ⛪ Built by monks from Mount Athos for strategic protection\n• 🧱 One of the best-preserved Byzantine towers in Halkidiki\n• 📏 Rising approximately 8 meters in height\n• 🎶 Cultural landmark hosting music and art events during the Sani Festival\n• 🌅 Unique setting blending history with contemporary culture\n\n⭐ A remarkable historical monument that combines Byzantine heritage with modern cultural life in Sani.",
            descriptionRo = "🏰 Turnul Stavronikita, cunoscut și sub numele de Turnul Sani, este un turn bizantin bine conservat din secolul al XIV-lea, construit de călugării de pe Muntele Athos pentru protejarea moșiilor din Kassandra.\n\n• 🏛️ Turn defensiv bizantin din secolul al XIV-lea\n• ⛪ Construit de călugării athoniți cu scop strategic\n• 🧱 Unul dintre cele mai bine păstrate turnuri bizantine din Halkidiki\n• 📏 Are o înălțime de aproximativ 8 metri\n• 🎶 Reper cultural ce găzduiește evenimente muzicale și artistice în cadrul Festivalului Sani\n• 🌅 Cadru unic ce îmbină istoria cu cultura contemporană\n\n⭐ Un monument istoric deosebit, unde patrimoniul bizantin se întâlnește cu viața culturală modernă din Sani.",
             images = listOf(
                R.drawable.what_stavronikita_tower,
                R.drawable.what_stavronikita_tower1
            )
        ),
        "sani_marina" to WhatToDoItem(
            id = "sani_marina",
            categoryEn = "Shopping & Markets",
            categoryRo = "Cumpărături și piețe",
            beaches = emptyList(),

            titleEn = "Sani Marina",
            titleRo = "Sani Marina",
            address = "Sani Resort, Kassandra, Halkidiki, Greece",
            hoursEn = "Open daily (restaurants, cafes, shops usually 09:00–00:00)",
            hoursRo = "Deschis zilnic (restaurantele, cafenelele și magazinele de obicei 09:00–00:00)",
            website = "https://www.sani-resort.com/sani-marina",
            phone = "+30 23740 99500",
            descriptionEn = "⚓ Sani Marina is a world-class yacht harbor and leisure destination located within Sani Resort, offering an elegant Mediterranean lifestyle experience in Kassandra.\n\n• 🛥️ Modern marina with mooring for luxury yachts and sailing boats\n• 🍽️ Fine dining restaurants featuring Greek and international cuisine\n• ☕ Stylish cafés and seaside lounges along the promenade\n• 🛍️ Boutique shops with fashion, accessories, and lifestyle brands\n• 🎶 Lively atmosphere with evening entertainment and nightlife\n• 🌊 Scenic waterfront promenade with views of the Aegean Sea\n\n⭐ A refined destination for dining, shopping, relaxation, and evening entertainment in Halkidiki.",
            descriptionRo = "⚓ Sani Marina este un port de agrement de clasă internațională și o destinație de lifestyle situată în cadrul Sani Resort, oferind o experiență mediteraneană elegantă în Kassandra.\n\n• 🛥️ Marină modernă cu ancorare pentru iahturi de lux și bărci cu vele\n• 🍽️ Restaurante rafinate cu bucătărie grecească și internațională\n• ☕ Cafenele elegante și lounge-uri pe malul mării\n• 🛍️ Magazine boutique cu modă, accesorii și produse de lifestyle\n• 🎶 Atmosferă animată, cu divertisment și viață de noapte\n• 🌊 Promenadă pitorească pe malul apei, cu priveliști spre Marea Egee\n\n⭐ O destinație rafinată pentru gastronomie, cumpărături, relaxare și distracție de seară în Halkidiki.",
            images = listOf(
                R.drawable.what_sani_marina,
                R.drawable.what_sani_marina1
            )
        ),
        "koutsoupia_siviri_trail" to WhatToDoItem(
            id = "koutsoupia_siviri_trail",
            categoryEn = "Adventure & Activities",
            categoryRo = "Aventură și activități",
            beaches = emptyList(),

            titleEn = "Koutsoupia–Siviri Hiking Trail",
            titleRo = "Traseul de Drumeție Koutsoupia–Siviri",
            address = "Coastal path between Sani and Siviri, Kassandra, Halkidiki, Greece",
            hoursEn = "Open-air hiking trail (accessible anytime; best in spring and autumn)",
            hoursRo = "Traseu de drumeție în aer liber (accesibil oricând; recomandat primăvara și toamna)",
            descriptionEn = "🥾 The Koutsoupia–Siviri Hiking Trail follows a dramatic coastal route between Sani and the village of Siviri, offering some of the most impressive sea views in Kassandra.\n\n• 🌊 Approximately 20 km long trail running along cliffs above the sea\n• 🌲 Passes through pine forests, Mediterranean shrubs, and natural vegetation\n• 👀 Open viewpoints with breathtaking panoramas of the coastline\n• 🌿 Combines rich flora with rugged coastal landscapes\n• 🧭 Best suited for experienced hikers or well-planned excursions\n• ⏳ Shorter sections can be enjoyed as half-day walks\n\n⭐ A spectacular hiking route for nature lovers seeking adventure, scenery, and unspoiled coastal beauty in Halkidiki.",
            descriptionRo = "🥾 Traseul de drumeție Koutsoupia–Siviri urmează un drum spectaculos de coastă între Sani și satul Siviri, oferind unele dintre cele mai frumoase priveliști din Kassandra.\n\n• 🌊 Traseu de aproximativ 20 km, desfășurat de-a lungul falezelor deasupra mării\n• 🌲 Străbate păduri de pini, vegetație mediteraneană și zone naturale\n• 👀 Puncte deschise cu panorame impresionante asupra litoralului\n• 🌿 Îmbină diversitatea florei cu peisaje de coastă dramatice\n• 🧭 Recomandat drumeților cu experiență sau excursiilor bine planificate\n• ⏳ Segmente mai scurte pot fi parcurse ca plimbări de jumătate de zi\n\n⭐ Un traseu spectaculos pentru iubitorii de natură și drumeții care caută aventură și peisaje autentice în Halkidiki.",
            images = listOf(
                R.drawable.what_koutsoupia_siviri,
                R.drawable.what_koutsoupia_siviri1
            )
        ),
        "afytos_village" to  WhatToDoItem(
            id = "afytos_village",
            categoryEn = "Villages & Local Life",
            categoryRo = "Sate și viață locală",
            beaches = emptyList(),

            titleEn = "Afytos Village",
            titleRo = "Satul Afytos",
            address = "Afytos 630 77, Kassandra, Halkidiki, Greece",
            hoursEn = "Accessible anytime (shops & tavernas usually open daily 09:00–00:00 in summer)",
            hoursRo = "Accesibil oricând (magazinele și tavernele sunt deschise zilnic 09:00–00:00 vara)",
            descriptionEn = "🏘️ Afytos is one of the most picturesque villages in Halkidiki, dramatically set on a cliff overlooking the Toroneos Gulf.\n\n• 🪨 Traditional stone houses and charming cobbled streets\n• ⛪ Historic church dating back to the Byzantine era\n• 🏛️ Folklore museum and small art galleries showcasing local culture\n• 🍽️ Numerous tavernas offering local cuisine with panoramic sea views\n• 🎶 Lively central square with a vibrant village atmosphere\n• 🌅 Stunning viewpoints overlooking the coastline and the sea\n\n⭐ A must-see destination combining authentic architecture, culture, and breathtaking seaside views in Halkidiki.",
            descriptionRo = "🏘️ Afytos este unul dintre cele mai pitorești sate din Halkidiki, situat spectaculos pe o stâncă ce domină Golful Toroneos.\n\n• 🪨 Case tradiționale din piatră și străduțe pavate pline de farmec\n• ⛪ Biserică istorică din perioada bizantină\n• 🏛️ Muzeu de folclor și galerii de artă locală\n• 🍽️ Numeroase taverne cu bucătărie tradițională și priveliști panoramice spre mare\n• 🎶 Piață centrală animată, cu atmosferă autentică de sat grecesc\n• 🌅 Puncte de belvedere spectaculoase asupra litoralului\n\n⭐ O destinație de neratat ce îmbină arhitectura autentică, cultura și peisajele maritime impresionante din Halkidiki.",
            images = listOf(
                R.drawable.what_afytos_village,
                R.drawable.what_afytos_village1
            )
        ),
        "kassandria_village" to WhatToDoItem(
            id = "kassandria_village",
            categoryEn = "Villages & Local Life",
            categoryRo = "Sate și viață locală",
            beaches = emptyList(),

            titleEn = "Kassandria Village",
            titleRo = "Satul Kassandria",
            address = "Kassandria 630 77, Kassandra, Halkidiki, Greece",
            hoursEn = "Accessible anytime (shops & cafes usually open daily 09:00–22:00)",
            hoursRo = "Accesibil oricând (magazinele și cafenelele sunt deschise zilnic 09:00–22:00)",
            descriptionEn = "🏘️ Kassandria is the administrative and historical center of the Kassandra peninsula, combining traditional character with everyday local life.\n\n• 🏛️ Neoclassical architecture and traditional village atmosphere\n• ⛪ Church of the Birth of Christ, built in 1850\n• 🛒 Weekly street market offering local products and goods\n• 🏪 Local shops, small museums, cafés, and tavernas\n• 🌿 Surrounded by olive groves and countryside landscapes\n• 📍 Centrally located, close to both coasts of the peninsula\n\n⭐ A vibrant local hub offering history, culture, and an authentic glimpse into everyday life in Kassandra.",
            descriptionRo = "🏘️ Kassandria este centrul administrativ și istoric al peninsulei Kassandra, îmbinând caracterul tradițional cu viața locală de zi cu zi.\n\n• 🏛️ Arhitectură neoclasică și atmosferă autentică de sat\n• ⛪ Biserica Nașterii Domnului, construită în anul 1850\n• 🛒 Piață săptămânală cu produse locale și diverse bunuri\n• 🏪 Magazine locale, mici muzee, cafenele și taverne\n• 🌿 Înconjurată de livezi de măslini și peisaje rurale\n• 📍 Poziție centrală, aproape de ambele coaste ale peninsulei\n\n⭐ Un centru local vibrant, ideal pentru a descoperi istoria, cultura și viața autentică din Kassandra.",
             images = listOf(
                R.drawable.what_kassandria_village,
                R.drawable.what_kassandria_village1
            )
        ),
        "gaia_kallisti" to WhatToDoItem(
            id = "gaia_kallisti",
            categoryEn = "Local Products & Tastings",
            categoryRo = "Produse locale și degustări",
            beaches = emptyList(),

            titleEn = "Gaia Kallisti – Olive Oil & Olives Center",
            titleRo = "Gaia Kallisti – Centru pentru Ulei de Măsline și Măsline",
            address = "Nea Potidea, Kassandra, Halkidiki, Greece",
            hoursEn = "Mon–Sat 09:00–18:00; Sun Closed",
            hoursRo = "Lun–Sâm 09:00–18:00; Duminică Închis",
            website = "https://gaiakallisti.com/",
            phone = "+30 23730 42060",
            descriptionEn = "🫒 Gaia Kallisti is a cultural and gastronomic center dedicated to the olive-growing tradition of Halkidiki, offering an authentic taste of local heritage.\n\n• 🏛️ Exhibitions explaining olive oil production and local traditions\n• 🫒 Tasting of premium extra virgin olive oil\n• 🟢 Discovery of the famous Halkidiki green olives\n• 👨‍🏫 Guided tours, educational programs, and hands-on workshops\n• 🍽️ Experience connecting history, culture, and gastronomy\n\n⭐ A must-visit destination for food lovers and anyone interested in authentic Greek traditions.",
            descriptionRo = "🫒 Gaia Kallisti este un centru cultural și gastronomic dedicat tradiției cultivării măslinilor din Halkidiki, oferind o experiență autentică a patrimoniului local.\n\n• 🏛️ Expoziții despre producția uleiului de măsline și tradițiile locale\n• 🫒 Degustări de ulei de măsline extravirgin de calitate superioară\n• 🟢 Descoperirea celebrelor măsline verzi din Halkidiki\n• 👨‍🏫 Tururi ghidate, programe educaționale și ateliere interactive\n• 🍽️ Experiență ce îmbină istoria, cultura și gastronomia\n\n⭐ O oprire de neratat pentru iubitorii de gastronomie și pentru cei interesați de tradițiile autentice grecești.",
             images = listOf(
                R.drawable.what_gaia_kallisti,
                R.drawable.what_gaia_kallisti1
            )
        ),
        "katergopetra_siviri" to WhatToDoItem(
            id = "katergopetra_siviri",
            categoryEn = "Nature & Scenic Spots",
            categoryRo = "Natură și peisaje",
            beaches = emptyList(),

            titleEn = "Katergopetra Rocks near Siviri",
            titleRo = "Katergopetra lângă Siviri",
            address = "Coastal cliffs, near Siviri, Kassandra, Halkidiki, Greece",
            hoursEn = "Open-air natural site (accessible anytime, best during daylight)",
            hoursRo = "Sit natural în aer liber (accesibil oricând, recomandat pe timp de zi)",
            descriptionEn = "🪨 Katergopetra, located near the seaside village of Siviri, is a striking coastal rock formation shaped by wind and sea over centuries.\n\n• 🌊 Dramatic cliffs and naturally sculpted rock formations\n• 🥾 Easily accessible via the coastal walking path\n• 📸 Popular spot for photography and nature exploration\n• 🌅 Especially impressive at sunset, with warm light reflecting on the rocks\n• 🌿 Unique natural landscape combining sea, stone, and open views\n\n⭐ A beautiful natural landmark ideal for short walks, photography, and enjoying the wild coastal scenery of Halkidiki.",
            descriptionRo = "🪨 Katergopetra, situată lângă satul de coastă Siviri, este o formațiune stâncoasă spectaculoasă modelată de vânt și mare de-a lungul secolelor.\n\n• 🌊 Faleze dramatice și stânci sculptate natural\n• 🥾 Acces facil prin poteca de coastă\n• 📸 Loc apreciat pentru fotografie și explorare în natură\n• 🌅 Deosebit de spectaculoasă la apus, când stâncile capătă nuanțe calde\n• 🌿 Peisaj natural unic ce îmbină marea, piatra și priveliștile deschise\n\n⭐ Un punct natural deosebit, perfect pentru plimbări scurte, fotografie și admirarea peisajului sălbatic din Halkidiki.",
            images = listOf(
                R.drawable.what_katergopetra,
                R.drawable.what_katergopetra1
            )
        ),
        "akti_bondes" to WhatToDoItem(
            id = "akti_bondes",
            categoryEn = "Nature & Scenic Spots",
            categoryRo = "Natură și peisaje",
            beaches = emptyList(),

            titleEn = "Akti Bondes Beach",
            titleRo = "Plaja Akti Bondes",
            address = "Near Nea Skioni, Kassandra, Halkidiki, Greece",
            hoursEn = "Open-air beach (accessible anytime; organized areas usually 09:00–19:00 in summer)",
            hoursRo = "Plajă în aer liber (accesibilă oricând; zonele organizate de obicei 09:00–19:00 vara)",
            descriptionEn = "🏖️ Akti Bondes is a serene beach located near Nea Skioni on the western coast of Kassandra, ideal for relaxed seaside moments.\n\n• 🏝️ Soft sand and clear, shallow waters suitable for families\n• 👨‍👩‍👧 Calm atmosphere, away from large crowds\n• ⛱️ Partly organized with sunbeds and umbrellas\n• 🌿 Natural, unspoiled sections for quiet relaxation\n• 🌅 Beautiful sunset views over the Aegean Sea\n\n⭐ A peaceful beach perfect for families, relaxation, and enjoying tranquil sunsets in Halkidiki.",
            descriptionRo = "🏖️ Akti Bondes este o plajă liniștită situată lângă Nea Skioni, pe coasta vestică a Kassandrei, ideală pentru momente de relaxare la malul mării.\n\n• 🏝️ Nisip fin și ape limpezi, puțin adânci, potrivite pentru familii\n• 👨‍👩‍👧 Atmosferă calmă, departe de aglomerație\n• ⛱️ Zonă parțial organizată cu șezlonguri și umbrele\n• 🌿 Secțiuni naturale, neamenajate, pentru liniște deplină\n• 🌅 Priveliști superbe la apus peste Marea Egee\n\n⭐ O plajă liniștită, perfectă pentru familii, relaxare și apusuri spectaculoase în Halkidiki.",
            images = listOf(
                R.drawable.what_akti_bondes,
                R.drawable.what_akti_bondes1
            )
        ),
        "skeye_paragliding" to WhatToDoItem(
            id = "skeye_paragliding",
            categoryEn = "Adventure & Activities",
            categoryRo = "Aventură și activități",
            beaches = emptyList(),

            titleEn = "Skeye Paragliding Flights",
            titleRo = "Zboruri cu parapanta Skeye",
            address = "Flights from Kassandra & Sithonia locations, Halkidiki, Greece",
            hoursEn = "Daily flights (weather permitting, booking required)",
            hoursRo = "Zboruri zilnice (în funcție de condițiile meteo, cu rezervare prealabilă)",
            website = "https://skeyeparagliding.com/",
            phone = "+30 694 247 7464",
            descriptionEn = "🪂 Skeye Paragliding offers tandem paragliding flights over Halkidiki, delivering an unforgettable bird’s-eye view of beaches, mountains, and turquoise seas.\n\n• 🪂 Tandem flights with experienced, certified pilots\n• 🌊 Panoramic aerial views over the coastline and peninsula\n• 🏖️ Flight locations in selected areas of Kassandra and Sithonia\n• 🧭 Suitable for beginners, no prior experience required\n• 🛡️ High safety standards and professional equipment\n• 🌬️ Flights operated according to weather conditions\n\n⭐ One of the most thrilling outdoor experiences in Halkidiki, perfect for adventure seekers and unforgettable memories.",
            descriptionRo = "🪂 Skeye Paragliding oferă zboruri tandem cu parapanta deasupra Halkidiki, oferind o experiență aeriană spectaculoasă asupra plajelor, munților și apelor turcoaz.\n\n• 🪂 Zboruri tandem alături de piloți profesioniști și certificați\n• 🌊 Priveliști panoramice de sus asupra litoralului și peninsulei\n• 🏖️ Puncte de decolare selectate din Kassandra și Sithonia\n• 🧭 Potrivit și pentru începători, fără experiență anterioară\n• 🛡️ Standarde ridicate de siguranță și echipament profesionist\n• 🌬️ Zborurile se desfășoară în funcție de condițiile meteo\n\n⭐ Una dintre cele mai palpitante experiențe în aer liber din Halkidiki, ideală pentru iubitorii de adrenalină și amintiri de neuitat.",

            images = listOf(
                R.drawable.what_skeye_paragliding,
                R.drawable.what_skeye_paragliding1
            )
        ),
        "siviri_amphitheater" to WhatToDoItem(
            id = "siviri_amphitheater",
            categoryEn = "Entertainment",
            categoryRo = "Divertisment",
            beaches = emptyList(),

            titleEn = "Siviri Amphitheater",
            titleRo = "Amfiteatrul Siviri",
            address = "Siviri, Kassandra, Halkidiki, Greece",
            hoursEn = "Open during events (mainly summer evenings, Kassandra Festival)",
            hoursRo = "Deschis în timpul evenimentelor (mai ales serile de vară, Festivalul Kassandra)",
            website = "https://www.kassandrafestival.gr/",
            phone = "+30 23740 22208",
            descriptionEn = "🎭 The Siviri Amphitheater is an open-air cultural venue set among pine trees on the hills above Siviri, offering a unique artistic experience in nature.\n\n• 🎶 Main stage of the annual Kassandra Festival\n• 🌍 Hosts concerts, theatre plays, dance performances, and international artists\n• 🌲 Natural setting surrounded by pine forest\n• 🔊 Excellent acoustics designed for open-air performances\n• 🌅 Panoramic views over the surrounding landscape\n• 🎟️ One of the most important cultural venues in Northern Greece\n\n⭐ A unique place where culture, music, and nature come together in Halkidiki.",
            descriptionRo = "🎭 Amfiteatrul Siviri este un spațiu cultural în aer liber, amplasat printre pini pe colinele de deasupra satului Siviri, oferind o experiență artistică deosebită în mijlocul naturii.\n\n• 🎶 Scena principală a Festivalului Kassandra\n• 🌍 Găzduiește concerte, piese de teatru, spectacole de dans și artiști internaționali\n• 🌲 Cadru natural, înconjurat de păduri de pini\n• 🔊 Acustică excelentă pentru spectacole în aer liber\n• 🌅 Priveliști panoramice asupra peisajului înconjurător\n• 🎟️ Unul dintre cele mai importante spații culturale din nordul Greciei\n\n⭐ Un loc special unde arta, muzica și natura se îmbină armonios în Halkidiki.",
            images = listOf(
                R.drawable.what_siviri_amphitheater,
                R.drawable.what_siviri_amphitheater1
            )
        ),
        "possidi_lighthouse" to WhatToDoItem(
            id = "possidi_lighthouse",
            categoryEn = "History & Landmarks",
            categoryRo = "Istorie și obiective",
            beaches = emptyList(),

            titleEn = "Possidi Lighthouse",
            titleRo = "Farul Possidi",
            address = "Possidi Cape, Kassandra 630 77, Halkidiki, Greece",
            hoursEn = "Open-air landmark (accessible anytime; exterior visit only)",
            hoursRo = "Monument în aer liber (accesibil oricând; vizitabil doar exteriorul)",
            descriptionEn = "🗼 The Possidi Lighthouse, built in 1864 at the edge of Cape Possidi, is one of the most iconic landmarks of Halkidiki, marking the western tip of Kassandra.\n\n• ⚓ Historic lighthouse that once guided sailors along the Aegean coast\n• 🏜️ Surrounded by sand dunes and a wild coastal landscape\n• 🌊 Open views over the Aegean Sea and the cape\n• 📸 A popular spot for photography, especially at sunset\n• 🚶 Ideal area for walks along the narrow sandy cape\n\n⭐ A picturesque historical landmark combining maritime heritage, nature, and unforgettable sunset views in Halkidiki.",
            descriptionRo = "🗼 Farul Possidi, construit în anul 1864 la extremitatea Capului Possidi, este unul dintre cele mai emblematice repere ale Halkidiki, marcând punctul vestic al Kassandrei.\n\n• ⚓ Far istoric ce a ghidat navele de-a lungul coastei Mării Egee\n• 🏜️ Înconjurat de dune de nisip și peisaj natural sălbatic\n• 🌊 Priveliști deschise asupra mării și capului\n• 📸 Loc popular pentru fotografie, mai ales la apus\n• 🚶 Zonă ideală pentru plimbări pe fâșia îngustă de pământ\n\n⭐ Un reper istoric pitoresc ce îmbină patrimoniul maritim cu natura și apusuri spectaculoase în Halkidiki.",
            images = listOf(
                R.drawable.what_possidi_lighthouse,
                R.drawable.what_possidi_lighthouse1
            )
        ),
        "poseidon_temple_possidi" to WhatToDoItem(
            id = "poseidon_temple_possidi",
            categoryEn = "History & Landmarks",
            categoryRo = "Istorie și obiective",
            beaches = emptyList(),

            titleEn = "Poseidon Temple Archaeological Site - Temporarely Closed",
            titleRo = "Sit Arheologic – Templul lui Poseidon - Inchisa Temporar",
            address = "Possidi Cape, Kassandra, Halkidiki, Greece",
            hoursEn = "Open-air archaeological site (accessible anytime, best during daylight)",
            hoursRo = "Sit arheologic în aer liber (accesibil oricând, recomandat pe timp de zi)",
            descriptionEn = "🏛️ The Archaeological Site of the Temple of Poseidon at Cape Possidi is one of the oldest sanctuaries dedicated to the god of the sea in Northern Greece.\n\n• 🏺 Ancient sanctuary dating back to the 6th century BC\n• ⚓ Once a place of worship for sailors seeking protection at sea\n• 🧱 Remains of temple foundations and ritual altars\n• 🌊 Located on Cape Possidi with dramatic coastal scenery\n• 📸 A unique spot combining archaeology, history, and sea views\n\n⭐ A fascinating ancient site where mythology, maritime history, and natural beauty meet on the coast of Halkidiki.",
            descriptionRo = "🏛️ Situl arheologic al Templului lui Poseidon de la Capul Possidi este unul dintre cele mai vechi sanctuare dedicate zeului mării din nordul Greciei.\n\n• 🏺 Sanctuar antic ce datează din secolul al VI-lea î.Hr.\n• ⚓ Loc de cult frecventat de marinari în căutare de protecție pe mare\n• 🧱 Vestigii ale fundațiilor templului și ale altarelor rituale\n• 🌊 Amplasat pe Capul Possidi, într-un cadru natural spectaculos\n• 📸 Loc deosebit ce îmbină arheologia, istoria și priveliștile maritime\n\n⭐ Un sit antic impresionant, unde mitologia, istoria maritimă și frumusețea naturală se întâlnesc pe litoralul Halkidiki.",
            images = listOf(
                R.drawable.what_poseidon_temple,
                R.drawable.what_poseidon_temple1
            )
        ),
        "cine_poseidi" to WhatToDoItem(
            id = "cine_poseidi",
            categoryEn = "Entertainment",
            categoryRo = "Divertisment",
            beaches = emptyList(),

            titleEn = "Cine Poseidi – Open-Air Cinema",
            titleRo = "Cine Poseidi – Cinema în aer liber",
            address = "Poseidi, Kassandra 630 77, Halkidiki, Greece",
            hoursEn = "Summer season: daily screenings at 21:00 (June–September)",
            hoursRo = "Sezon estival: proiecții zilnice la ora 21:00 (iunie–septembrie)",
            website = "https://short-url.org/1hPk9",
            descriptionEn = "🎬 Cine Poseidi is a traditional open-air cinema located in the seaside village of Poseidi, offering classic Greek summer movie nights under the stars.\n\n• 🌙 Open-air cinema operating during the summer season\n• 🌲 Set among pine trees with a fresh sea breeze\n• 🎥 Large screen and comfortable seating\n• 🍿 Snack bar with refreshments for evening screenings\n• ⭐ Popular with both locals and visitors for relaxed summer nights\n\n⭐ A charming evening experience that captures the authentic atmosphere of Greek summers in Halkidiki.",
            descriptionRo = "🎬 Cine Poseidi este un cinema tradițional în aer liber, situat în satul de coastă Poseidi, oferind seri de film sub cerul înstelat, specifice verilor grecești.\n\n• 🌙 Cinema în aer liber, deschis pe perioada verii\n• 🌲 Amplasat printre pini, cu briza mării în apropiere\n• 🎥 Ecran mare și locuri confortabile\n• 🍿 Snack bar cu gustări și băuturi\n• ⭐ Activitate de seară apreciată de localnici și turiști\n\n⭐ O experiență deosebită de seară, ce surprinde perfect atmosfera autentică a verilor din Halkidiki.",
            images = listOf(
                R.drawable.what_cine_poseidi,
                R.drawable.what_cine_poseidi1
            )
        ),
        "palatia_formations" to WhatToDoItem(
            id = "palatia_formations",
            categoryEn = "Nature & Scenic Spots",
            categoryRo = "Natură și peisaje",
            beaches = emptyList(),

            titleEn = "Natural Formations Palatia",
            titleRo = "Formațiunile Naturale Palatia",
            address = "Palatia area, near Kalandra, Kassandra, Halkidiki, Greece",
            hoursEn = "Open-air natural site (accessible anytime, best during daylight)",
            hoursRo = "Sit natural în aer liber (accesibil oricând, recomandat pe timp de zi)",
            descriptionEn = "🪨 The Natural Formations of Palatia, located near Kalandra on the western coast of Kassandra, are impressive coastal rock formations shaped by the sea and wind over centuries.\n\n• 🌊 Dramatic cliffs and naturally sculpted rock formations\n• 🏞️ Hidden coves and untouched coastal landscapes\n• 🥾 Ideal area for hiking and coastal exploration\n• 📸 Popular spot for photography and nature lovers\n• 🌅 Especially captivating at sunset with panoramic sea views\n\n⭐ A hidden natural gem offering wild beauty, tranquility, and stunning scenery away from the busy resorts of Halkidiki.",
            descriptionRo = "🪨 Formațiunile naturale Palatia, situate lângă Kalandra pe coasta vestică a Kassandrei, sunt formațiuni stâncoase spectaculoase modelate de mare și vânt de-a lungul secolelor.\n\n• 🌊 Faleze dramatice și stânci sculptate natural\n• 🏞️ Golfuri ascunse și peisaje de coastă neatinse\n• 🥾 Zonă ideală pentru drumeții și explorare\n• 📸 Loc apreciat de fotografi și iubitorii de natură\n• 🌅 Deosebit de spectaculoasă la apus, cu priveliști panoramice asupra mării\n\n⭐ O comoară naturală ascunsă, perfectă pentru liniște, explorare și frumusețe autentică, departe de stațiunile aglomerate din Halkidiki.",
            images = listOf(
                R.drawable.what_palatia,
                R.drawable.what_palatia1
            )
        ),
        "mavrobara_turtle_lake" to WhatToDoItem(
            id = "mavrobara_turtle_lake",
            categoryEn = "Nature & Scenic Spots",
            categoryRo = "Natură și peisaje",
            beaches = emptyList(),

            titleEn = "Mavrobara – Turtle Lake",
            titleRo = "Mavrobara – Lacul Țestoaselor",
            address = "Near Polychrono, Kassandra, Halkidiki, Greece",
            hoursEn = "Open-air natural site (accessible anytime; best in spring and autumn)",
            hoursRo = "Sit natural în aer liber (accesibil oricând; recomandat primăvara și toamna)",
            descriptionEn = "🐢 Mavrobara is a unique freshwater lake located above the village of Polychrono in Kassandra, officially designated as a protected natural monument.\n\n• 💧 Rare freshwater ecosystem surrounded by lush vegetation\n• 🐢 Home to two protected turtle species: Emys orbicularis and Mauremys caspica\n• 🐦 Quiet habitat for birds and other wildlife\n• 🥾 Peaceful hiking paths suitable for families and nature lovers\n• 🌿 High ecological value and tranquil natural setting\n\n⭐ A hidden natural gem offering calm walks, wildlife observation, and authentic nature in Halkidiki.",
            descriptionRo = "🐢 Mavrobara este un lac de apă dulce unic, situat deasupra satului Polychrono din Kassandra, declarat monument natural protejat.\n\n• 💧 Ecosistem rar de apă dulce, înconjurat de vegetație bogată\n• 🐢 Adăpostește două specii protejate de țestoase: Emys orbicularis și Mauremys caspica\n• 🐦 Habitat liniștit pentru păsări și faună sălbatică\n• 🥾 Trasee ușoare pentru plimbări, potrivite pentru familii și iubitori de natură\n• 🌿 Valoare ecologică ridicată și cadru natural relaxant\n\n⭐ O comoară naturală ascunsă, ideală pentru liniște, observarea faunei și plimbări în natură autentică din Halkidiki.",
            images = listOf(
                R.drawable.what_mavrobara,
                R.drawable.what_mavrobara1
            )
        ),
        "kriopigi_cold_fountain" to WhatToDoItem(
            id = "kriopigi_cold_fountain",
            categoryEn = "Nature & Scenic Spots",
            categoryRo = "Natură și peisaje",
            beaches = emptyList(),

            titleEn = "Kriopigi Cold Fountain",
            titleRo = "Izvorul Rece Kriopigi",
            address = "Kriopigi, Kassandra, Halkidiki, Greece",
            hoursEn = "Accessible anytime (public outdoor site)",
            hoursRo = "Accesibil oricând (loc public în aer liber)",
            website = "https://short-url.org/1d5sU",
            descriptionEn = "💧 The Cold Fountain of Kriopigi is a historic natural spring located in the heart of the traditional village of Kriopigi, known since ancient times.\n\n• 🏺 Ancient spring that supplied fresh drinking water to locals and travelers\n• 🌳 Surrounded by plane trees and traditional stone-paved alleys\n• 🚶 Pleasant stop during village walks and exploration\n• 🏘️ Authentic village atmosphere and local meeting point\n• ❄️ Cool, pure spring water, especially refreshing in summer\n\n⭐ A charming historical spot offering refreshment and a glimpse into the traditional life of Kriopigi.",
            descriptionRo = "💧 Izvorul Rece din Kriopigi este un izvor natural istoric situat în inima satului tradițional Kriopigi, cunoscut încă din antichitate.\n\n• 🏺 Izvor vechi ce a furnizat apă potabilă localnicilor și călătorilor\n• 🌳 Înconjurat de platani și alei pavate cu piatră\n• 🚶 Oprire plăcută în timpul plimbărilor prin sat\n• 🏘️ Punct de întâlnire cu atmosferă autentică locală\n• ❄️ Apă rece și pură, extrem de răcoritoare vara\n\n⭐ Un loc fermecător ce oferă răcoare, istorie și o experiență autentică a satului Kriopigi.",
              images = listOf(
                R.drawable.what_kriopigi_fountain,
                R.drawable.what_kriopigi_fountain1
            )
        ),
        "solina_church" to WhatToDoItem(
            id = "solina_church",
            categoryEn = "History & Landmarks",
            categoryRo = "Istorie și obiective",
            beaches = emptyList(),

            titleEn = "Early Christian Church of Solina",
            titleRo = "Biserica Paleocreștină din Solina",
            address = "Solina area, Kassandra, Halkidiki, Greece",
            hoursEn = "Open-air archaeological site (accessible anytime, best during daylight)",
            hoursRo = "Sit arheologic în aer liber (accesibil oricând, recomandat pe timp de zi)",
            descriptionEn = "⛪ The Early Christian Church of Solina, located near Kassandra, is one of the region’s most important archaeological sites from the early Byzantine period.\n\n• 🏛️ Dates back to the 5th–6th century AD\n• 🧱 Remains of a three-aisled basilica\n• 🖼️ Preserved mosaic floors and marble architectural elements\n• ✝️ Reflects the early spread of Christianity in Halkidiki\n• 📜 Valuable insight into early Byzantine religious architecture\n\n⭐ An impressive archaeological site offering a glimpse into the spiritual and architectural heritage of early Christian Halkidiki.",
            descriptionRo = "⛪ Biserica Paleocreștină din Solina, situată lângă Kassandra, este unul dintre cele mai importante situri arheologice ale regiunii din perioada bizantină timpurie.\n\n• 🏛️ Datează din secolele V–VI d.Hr.\n• 🧱 Vestigii ale unei bazilici cu trei nave\n• 🖼️ Podele din mozaic și elemente arhitecturale din marmură\n• ✝️ Mărturie a răspândirii timpurii a creștinismului în Halkidiki\n• 📜 Informații valoroase despre arhitectura religioasă bizantină timpurie\n\n⭐ Un sit arheologic deosebit, ce oferă o incursiune în patrimoniul spiritual și arhitectural al Halkidiki din epoca creștină timpurie.",
            images = listOf(
                R.drawable.what_solina_church,
                R.drawable.what_solina_church1
            )
        ),
        "dionysus_nymphs_sanctuary" to WhatToDoItem(
            id = "dionysus_nymphs_sanctuary",
            categoryEn = "History & Landmarks",
            categoryRo = "Istorie și obiective",
            beaches = emptyList(),

            titleEn = "Sanctuary of Dionysus and the Nymphs",
            titleRo = "Sanctuarul lui Dionysos și al Nimfelor",
            address = "Kassandra peninsula, Halkidiki, Greece (near Afytos)",
            hoursEn = "Open-air archaeological site (accessible anytime, best during daylight)",
            hoursRo = "Sit arheologic în aer liber (accesibil oricând, recomandat pe timp de zi)",
            descriptionEn = "🏛️ The Sanctuary of Dionysus and the Nymphs, located near Afytos in Kassandra, is an ancient worship site dedicated to the god of wine and ecstasy and to the nature spirits known as the Nymphs.\n\n• 🍷 Sacred site linked to Dionysus, god of wine, fertility, and ritual celebration\n• 🌿 Dedicated also to the Nymphs, protectors of nature and water sources\n• 🪨 Rock-carved spaces, niches, and ancient ritual areas\n• 🏺 Votive inscriptions revealing strong religious traditions of antiquity\n• 🌄 Harmoniously integrated into the natural landscape of Halkidiki\n\n⭐ A unique archaeological site where mythology, spirituality, and nature come together in Kassandra.",
            descriptionRo = "🏛️ Sanctuarul lui Dionysos și al Nimfelor, situat lângă Afytos, în Kassandra, este un vechi loc de cult dedicat zeului vinului și extazului, precum și spiritelor naturii – Nimfele.\n\n• 🍷 Loc sacru asociat cu Dionysos, zeul vinului, fertilității și ritualurilor\n• 🌿 Dedicat și Nimfelor, protectoarele naturii și ale izvoarelor\n• 🪨 Spații, nișe și zone rituale săpate direct în stâncă\n• 🏺 Inscripții votive ce reflectă tradițiile religioase ale antichității\n• 🌄 Îmbinare armonioasă între sit arheologic și peisaj natural\n\n⭐ Un sit arheologic deosebit, unde mitologia, spiritualitatea și natura se întâlnesc în inima Kassandrei.",
            images = listOf(
                R.drawable.what_dionysus_sanctuary,
                R.drawable.what_dionysus_sanctuary1
            )
        ),
        "ammon_zeus_sanctuary" to WhatToDoItem(
            id = "ammon_zeus_sanctuary",
            categoryEn = "History & Landmarks",
            categoryRo = "Istorie și obiective",
            beaches = emptyList(),

            titleEn = "Sanctuary of Ammon Zeus",
            titleRo = "Sanctuarul lui Ammon Zeus",
            address = "Kallithea, Kassandra, Halkidiki, Greece",
            hoursEn = "Open-air archaeological site (accessible anytime, best during daylight)",
            hoursRo = "Sit arheologic în aer liber (accesibil oricând, recomandat pe timp de zi)",
            descriptionEn = "🏛️ The Sanctuary of Ammon Zeus in Kallithea is one of the most significant archaeological sites in Halkidiki, uniquely located right next to the sea.\n\n• 🏺 Ancient sanctuary dating back to the 4th century BC\n• ⚡ Dedicated to Ammon Zeus, a fusion of the Greek god Zeus and the Egyptian god Ammon\n• 🧱 Excavated remains of temple foundations, altars, and inscriptions\n• ✝️ Important religious center in antiquity\n• 🌊 Exceptional seaside setting, just steps from Kallithea Beach\n\n⭐ A remarkable archaeological site where ancient history meets the seaside landscape of Halkidiki.",
            descriptionRo = "🏛️ Sanctuarul lui Ammon Zeus din Kallithea este unul dintre cele mai importante situri arheologice din Halkidiki, amplasat chiar lângă mare.\n\n• 🏺 Sanctuar antic ce datează din secolul al IV-lea î.Hr.\n• ⚡ Dedicat zeului Ammon Zeus, o fuziune între Zeus și zeul egiptean Ammon\n• 🧱 Vestigii ale fundațiilor templului, altare și inscripții\n• ✝️ Centru religios important al antichității\n• 🌊 Cadru unic pe litoral, în imediata apropiere a plajei Kallithea\n\n⭐ Un sit arheologic deosebit, unde istoria antică se îmbină perfect cu peisajul marin al Halkidiki.",
            images = listOf(
                R.drawable.what_ammon_zeus,
                R.drawable.what_ammon_zeus1
            )
        ),
        "nea_fokea_tower" to WhatToDoItem(
            id = "nea_fokea_tower",
            categoryEn = "Museums & Culture",
            categoryRo = "Muzee și cultură",
            beaches = emptyList(),

            titleEn = "St. Paul's Byzantine Tower of Nea Fokea",
            titleRo = "Turnul Bizantin Sf. Pavel din Nea Fokea",
            address = "Nea Fokea, Kassandra, Halkidiki, Greece",
            hoursEn = "Accessible anytime (exterior visit only)",
            hoursRo = "Accesibil oricând (vizitabil doar exteriorul)",
            descriptionEn = "🏰 The Byzantine Tower of Nea Fokea, also known as St. Paul’s Tower, is a well-preserved 15th-century defensive tower built in 1407 by the monks of Mount Athos.\n\n• 🏛️ Byzantine tower standing 28 meters tall\n• ⛪ Built by Athonite monks to protect coastal lands\n• ✝️ Traditionally linked to the Apostle Paul, who preached in the area\n• 🧱 One of the best-preserved Byzantine towers in Halkidiki\n• 🌊 Dominates the village seafront and is visible from afar\n\n⭐ A striking historical landmark combining Byzantine heritage, religious tradition, and coastal scenery in Nea Fokea.",
            descriptionRo = "🏰 Turnul Bizantin din Nea Fokea, cunoscut și ca Turnul Sfântului Pavel, este un turn defensiv bine conservat din secolul al XV-lea, construit în anul 1407 de călugării de pe Muntele Athos.\n\n• 🏛️ Turn bizantin cu o înălțime de 28 de metri\n• ⛪ Construit de călugării athoniți pentru protejarea zonei de coastă\n• ✝️ Asociat tradițional cu Apostolul Pavel, care a predicat în această regiune\n• 🧱 Unul dintre cele mai bine păstrate turnuri bizantine din Halkidiki\n• 🌊 Reper impunător ce domină litoralul satului, vizibil de la distanță\n\n⭐ Un monument istoric impresionant, ce îmbină patrimoniul bizantin, tradiția religioasă și peisajul marin din Nea Fokea.",
            images = listOf(
                R.drawable.what_nea_fokea_tower,
                R.drawable.what_nea_fokea_tower1
            )
        ),
        "kladi_olive_oil" to WhatToDoItem(
            id = "kladi_olive_oil",
            categoryEn = "Local Products & Tastings",
            categoryRo = "Produse locale și degustări",
            beaches = listOf(
                "paralia_psakoudia",
                "paralia_sargani",
                "paralia_askamnia",
                "nikiti_beach",
                "kastri_beach",
                "koviou_beach",
                "kalogria_beach",
                "spathies_beach",
                "paralia_perigiali",
                "lagomandra_beach",
                "nikitis_beach_sithonia",
                "paradisos_beach",
                "neos_marmaras_beach",
                "kohi_beach",
                "diaporti_beach",
                "azapiko_beach",
                "paralia_alexandra_xenia",
                "paralia_xenia",
                "tristinika_beach",
                "ema_beach",
                "paralia_toroni",
                "porto_koufo_beach",
                "marathias_beach",
                "sithonia_cape",
                "kalamitsi_beach",
                "prassou_beach",
                "tourkolimnionas",
                "linaraki_beach",
                "valti_beach",
                "goa_beach",
                "sarti_beach",
                "heart_shaped_bay",
                "orange_beach",
                "mega_portokali_beach",
                "dream_coast_beach",
                "banana_beach",
                "zografou_beach",
                "bara_beach",
                "manos_beach",
                "rocks_on_the_beach",
                "karagatsi_beach",
                "lagonisi_beach",
                "livrohio",
                "beach_of_pirgos",
                "schinias_beach",
                "paralia_salonikiou",
            ),

            titleEn = "Kladi Olive Oil",
            titleRo = "Kladi Olive Oil",
            address = "Epar.Od. Nikitis-Sartis, Nikiti 630 88, Sithonia, Halkidiki, Greece",
            hoursEn = "Mon–Sat 09:00–14:00 and 17:00-21:00; Sun 17:00-21:00",
            hoursRo = "Lun–Sâm 09:00–14:00 si 17:00-21:00 ; Duminică 17:00-21:00",
            facebook = "https://www.facebook.com/kladi2016",
            instagram = "https://www.instagram.com/kladi_serafim_evoo/",
            email = "kladiserafim@gmail.com",
            phone = "+30 6977394175",
            descriptionEn = "🫒 Kladi Olive Oil in Nikiti is a boutique producer and shop dedicated to premium extra virgin olive oil from Sithonia, offering an authentic taste of local tradition.\n\n• 🏺 High-quality extra virgin olive oil produced locally in Sithonia\n• 👨‍🏫 Guided tastings and introductions to olive oil flavors\n• ⚙️ Insight into the olive oil extraction and production process\n• 💚 Information about health benefits in Mediterranean cuisine\n• 🎁 Elegant packaging, ideal for gifts or souvenirs\n\n⭐ A refined gastronomic stop for food lovers seeking authentic flavors and a taste of Halkidiki to take home.",
            descriptionRo = "🫒 Kladi Olive Oil din Nikiti este un producător și magazin boutique dedicat uleiului de măsline extravirgin premium din Sithonia, oferind o experiență autentică a tradiției locale.\n\n• 🏺 Ulei de măsline extravirgin de înaltă calitate, produs local\n• 👨‍🏫 Degustări ghidate și prezentarea aromelor uleiului de măsline\n• ⚙️ Informații despre procesul de extracție și producție\n• 💚 Beneficiile uleiului de măsline în bucătăria mediteraneană\n• 🎁 Ambalaje elegante, perfecte pentru cadouri sau suveniruri\n\n⭐ O oprire gastronomică rafinată pentru iubitorii de gusturi autentice și pentru cei care vor să ducă acasă un strop din Halkidiki.",
             images = listOf(
                R.drawable.what_kladi_oliveoil,
                R.drawable.what_kladi_oliveoil1
            )
        ),
        "ormylia_monday_market" to WhatToDoItem(
            id = "ormylia_monday_market",
            categoryEn = "Shopping & Markets",
            categoryRo = "Cumpărături și piețe",
            beaches = listOf(
                "metamorfossi_beach",
                "paralia_kastri",
                "isla_beach",
                "paralia_elia",
                "great_lagomanda_coast",
                "peaceful_beach",
                "koutsoupia_beach",
                "foresta_sithonia",
                "aretes_beach",
                "luka_beach",
                "lagoon_in_porto_koufo",
                "mamba_beach",
                "klimataria_beach",
                "sykias_beach",
                "platania",
                "platanitsi_beach",
                "paralia_armenistis",
                "porto_paradiso",
                "fava_beach",
                "livari_beach",
                "latoura_beach",
                "paralia_agios_nikolaos",
                "irini_beach",
            ),

            titleEn = "Ormylia Monday Street Market (Laiki Agora)",
            titleRo = "Piața Volantă de Luni Ormylia (Laiki Agora)",
            address = "Central square, next to St. George Church, Ormylia, Halkidiki, Greece",
            hoursEn = "Mon 07:00–14:00",
            hoursRo = "Luni 07:00–14:00",
            descriptionEn = "🛒 Every Monday morning, Ormylia hosts a traditional ‘laiki agora’ in the central square, right next to the Church of St. George, offering an authentic local experience.\n\n• 🍎 Seasonal fruit and vegetables from local farmers\n• 🫒 Olives, olive oil, cheese, honey, herbs, and baked goods\n• 🐟 Fresh fish and regional products\n• 👕 Clothing, shoes, and household items\n• 🤝 Lively meeting point for the local community\n\n⭐ A vibrant weekly market where visitors can experience everyday life and local traditions in Halkidiki.",
            descriptionRo = "🛒 În fiecare luni dimineața, Ormylia găzduiește o ‘laiki agora’ tradițională în piața centrală, chiar lângă Biserica Sfântul Gheorghe, oferind o experiență locală autentică.\n\n• 🍎 Fructe și legume de sezon de la producători locali\n• 🫒 Măsline, ulei de măsline, brânzeturi, miere, ierburi și produse de panificație\n• 🐟 Pește proaspăt și produse regionale\n• 👕 Îmbrăcăminte, încălțăminte și articole pentru casă\n• 🤝 Punct de întâlnire animat pentru comunitatea locală\n\n⭐ O piață săptămânală plină de viață, ideală pentru a descoperi viața de zi cu zi și tradițiile din Halkidiki.",
            images = listOf(
                R.drawable.what_ormylia_market,
                R.drawable.what_ormylia_market1
            )
        ),
        "nikiti_friday_market" to WhatToDoItem(
            id = "nikiti_friday_market",
            categoryEn = "Shopping & Markets",
            categoryRo = "Cumpărături și piețe",
            beaches = listOf(
                "paralia_pirgos",
                "xiropotamos_beach",
                "paralia_ouranoupoli",
                "komitsa_beach",
                "ierissos_beach",
                "stratoni_beach",
                "proti_ammoudia_beach",
                "paralia_stavros",
                "platani_beach",
                "nea_vrasna_beach",
            ),

            titleEn = "Nikiti Friday Street Market (Laiki Agora)",
            titleRo = "Piața Volantă de Vineri Nikiti (Laiki Agora)",
            address = "Old Town center, Nikiti, Sithonia, Halkidiki, Greece",
            hoursEn = "Fri 07:00–14:00",
            hoursRo = "Vineri 07:00–14:00",
            descriptionEn = "🛒 Every Friday morning, Nikiti hosts a lively ‘laiki agora’ in the old town center, offering an authentic taste of local life in Sithonia.\n\n• 🍎 Seasonal fruits and vegetables from local farmers\n• 🐟 Fresh fish and seafood, depending on availability\n• 🫒 Olives, olive oil, honey, cheese, herbs, and baked goods\n• 👕 Clothing, footwear, and household items\n• 🤝 Lively atmosphere with locals and visitors alike\n\n⭐ A vibrant weekly market perfect for discovering local flavors and the everyday rhythm of Sithonia.",
            descriptionRo = "🛒 În fiecare vineri dimineața, Nikiti găzduiește o ‘laiki agora’ animată în centrul vechi al satului, oferind o experiență autentică a vieții locale din Sithonia.\n\n• 🍎 Fructe și legume de sezon de la fermieri locali\n• 🐟 Pește proaspăt și fructe de mare, în funcție de disponibilitate\n• 🫒 Măsline, ulei de măsline, miere, brânzeturi, ierburi și produse de panificație\n• 👕 Îmbrăcăminte, încălțăminte și articole pentru casă\n• 🤝 Atmosferă animată, cu localnici și vizitatori\n\n⭐ O piață săptămânală plină de viață, ideală pentru a descoperi aromele locale și ritmul autentic al Sithoniei.",
            images = listOf(
                R.drawable.what_nikiti_market,
                R.drawable.what_nikiti_market1
            )
        ),
        "agios_nikolaos_thursday_market" to WhatToDoItem(
            id = "agios_nikolaos_thursday_market",
            categoryEn = "Shopping & Markets",
            categoryRo = "Cumpărături și piețe",
            beaches = listOf(
                "ladhario_beach",
                "paralia_pirgos",
                "develiki_beach",
                "tripiti_beach",
                "paralia_ouranoupoli",
                "ouranoupolis_beach",
                "nea_roda_beach",
                "ierissos_beach",
                "kakoudia_beach",
                "babylon_beach",
                "proti_ammoudia_beach",
                "olympiada_beach",
                "milies_beach",
                "platani_beach",
                "vrasna_beach",
            ),

            titleEn = "Agios Nikolaos Thursday Street Market (Laiki Agora)",
            titleRo = "Piața Volantă de Joi Agios Nikolaos (Laiki Agora)",
            address = "Central square, next to St. Nicholas Church, Agios Nikolaos, Sithonia, Halkidiki, Greece",
            hoursEn = "Thu 07:00–14:00",
            hoursRo = "Joi 07:00–14:00",
            descriptionEn = "🛒 Every Thursday morning, Agios Nikolaos hosts a traditional ‘laiki agora’ in the central square, next to the Church of St. Nicholas, offering an authentic local experience in Sithonia.\n\n• 🍎 Seasonal fruit and vegetables from local farmers\n• 🫒 Olives, olive oil, cheese, honey, herbs, and baked goods\n• 🐟 Fresh fish and regional products\n• 👕 Clothing, shoes, and household items\n• 🤝 Lively meeting point for locals and visitors\n\n⭐ A vibrant weekly market where travelers can experience everyday life and local traditions in Sithonia.",
            descriptionRo = "🛒 În fiecare joi dimineața, Agios Nikolaos găzduiește o ‘laiki agora’ tradițională în piața centrală, lângă Biserica Sfântul Nicolae, oferind o experiență locală autentică în Sithonia.\n\n• 🍎 Fructe și legume de sezon de la producători locali\n• 🫒 Măsline, ulei de măsline, brânzeturi, miere, ierburi și produse de panificație\n• 🐟 Pește proaspăt și produse regionale\n• 👕 Îmbrăcăminte, încălțăminte și articole pentru casă\n• 🤝 Punct de întâlnire animat pentru localnici și vizitatori\n\n⭐ O piață săptămânală plină de viață, ideală pentru a descoperi viața de zi cu zi și tradițiile locale din Sithonia.",
               images = listOf(
                R.drawable.what_agiosnikolaos_market,
                R.drawable.what_agiosnikolaos_market1
            )
        ),
        "neosmarmaras_thursday_market" to WhatToDoItem(
            id = "neosmarmaras_thursday_market",
            categoryEn = "Shopping & Markets",
            categoryRo = "Cumpărături și piețe",
            beaches = emptyList(),

            titleEn = "Neos Marmaras Thursday Street Market (Laiki Agora)",
            titleRo = "Piața Volantă de Joi Neos Marmaras (Laiki Agora)",
            address = "By the port, on the coastal road, Neos Marmaras, Sithonia, Halkidiki, Greece",
            hoursEn = "Thu 07:00–14:00",
            hoursRo = "Joi 07:00–14:00",
            descriptionEn = "🛒 Every Thursday morning, Neos Marmaras comes alive with its weekly ‘laiki agora’, held by the port along the coastal road, offering a vibrant seaside market experience.\n\n• 🍎 Seasonal fruit and vegetables from local producers\n• 🫒 Olives, olive oil, cheese, honey, herbs, and traditional baked goods\n• 🐟 Fresh fish and regional products\n• 👕 Clothing, footwear, and household items\n• 🌊 Picturesque seaside location by the harbor\n\n⭐ One of the most lively and scenic weekly markets in Sithonia, combining local flavors with a beautiful coastal setting.",
            descriptionRo = "🛒 În fiecare joi dimineața, Neos Marmaras prinde viață cu ‘laiki agora’ săptămânală, organizată lângă port, pe strada de coastă, oferind o experiență de piață animată pe malul mării.\n\n• 🍎 Fructe și legume de sezon de la producători locali\n• 🫒 Măsline, ulei de măsline, brânzeturi, miere, ierburi și produse de panificație tradiționale\n• 🐟 Pește proaspăt și produse regionale\n• 👕 Îmbrăcăminte, încălțăminte și articole pentru casă\n• 🌊 Amplasare pitorească pe malul mării, lângă port\n\n⭐ Una dintre cele mai frumoase și animate piețe săptămânale din Sithonia, ce îmbină aromele locale cu farmecul litoralului.",
            images = listOf(
                R.drawable.what_neosmarmaras_market,
                R.drawable.what_neosmarmaras_market1
            )
        ),
        "sikia_saturday_market" to WhatToDoItem(
            id = "sikia_saturday_market",
            categoryEn = "Shopping & Markets",
            categoryRo = "Cumpărături și piețe",
            beaches = emptyList(),

            titleEn = "Sikiá Saturday Street Market (Laiki Agora)",
            titleRo = "Piața Volantă de Sâmbătă Sikiá (Laiki Agora)",
            address = "Central square, next to the Primary School, Sikiá, Sithonia, Halkidiki, Greece",
            hoursEn = "Sat 07:00–14:00",
            hoursRo = "Sâmbătă 07:00–14:00",
            descriptionEn = "🛒 Every Saturday morning, Sikiá hosts its weekly ‘laiki agora’ in the central square, right next to the primary school, offering a true taste of village life in Sithonia.\n\n• 🍎 Fresh seasonal fruits and vegetables from local farmers\n• 🫒 Olives, olive oil, honey, cheese, herbs, and homemade baked goods\n• 🐟 Fresh fish and regional products\n• 👕 Clothing, footwear, and household items\n• 🤝 Lively village atmosphere with authentic local charm\n\n⭐ A traditional weekly market where visitors can experience the authentic rhythm and flavors of Sithonia.",
            descriptionRo = "🛒 În fiecare sâmbătă dimineața, Sikiá găzduiește ‘laiki agora’ săptămânală în piața centrală, chiar lângă școala primară, oferind o experiență autentică de viață locală în Sithonia.\n\n• 🍎 Fructe și legume proaspete de sezon de la producători locali\n• 🫒 Măsline, ulei de măsline, miere, brânzeturi, ierburi și produse de panificație de casă\n• 🐟 Pește proaspăt și produse regionale\n• 👕 Îmbrăcăminte, încălțăminte și articole pentru casă\n• 🤝 Atmosferă animată de sat, cu farmec tradițional\n\n⭐ O piață săptămânală tradițională, ideală pentru a descoperi aromele și ritmul autentic al Sithoniei.",
            images = listOf(
                R.drawable.what_sikia_market,
                R.drawable.what_sikia_market1
            )
        ),
        "sophronios_basilica" to WhatToDoItem(
            id = "sophronios_basilica",
            categoryEn = "History & Landmarks",
            categoryRo = "Istorie și obiective",
            beaches = listOf(
                "paralia_psakoudia",
                "paralia_sargani",
                "paralia_askamnia",
                "nikiti_beach",
                "kastri_beach",
                "koviou_beach",
                "kalogria_beach",
                "spathies_beach",
                "paralia_perigiali",
                "lagomandra_beach",
                "nikitis_beach_sithonia",
                "paradisos_beach",
                "neos_marmaras_beach",
                "kohi_beach",
                "diaporti_beach",
                "azapiko_beach",
                "paralia_alexandra_xenia",
                "paralia_xenia",
                "tristinika_beach",
                "ema_beach",
                "paralia_toroni",
                "porto_koufo_beach",
                "marathias_beach",
                "sithonia_cape",
                "kalamitsi_beach",
                "prassou_beach",
                "tourkolimnionas",
                "linaraki_beach",
                "valti_beach",
                "goa_beach",
                "sarti_beach",
                "heart_shaped_bay",
                "orange_beach",
                "mega_portokali_beach",
                "dream_coast_beach",
                "banana_beach",
                "zografou_beach",
                "bara_beach",
                "manos_beach",
                "rocks_on_the_beach",
                "karagatsi_beach",
                "lagonisi_beach",
                "livrohio",
                "beach_of_pirgos",
                "schinias_beach",
                "paralia_salonikiou",
            ),

            titleEn = "Paleochristian Basilica of Sophronios",
            titleRo = "Bazilica Paleocreștină a lui Sofronie",
            address = "Nikiti, Sithonia, Halkidiki, Greece",
            hoursEn = "Open-air archaeological site (accessible anytime, best during daylight)",
            hoursRo = "Sit arheologic în aer liber (accesibil oricând, recomandat pe timp de zi)",
            descriptionEn = "⛪ The Paleochristian Basilica of Sophronios in Nikiti dates back to the 5th century AD and is one of the oldest Christian monuments in Halkidiki.\n\n• 🏛️ Early Christian basilica from the 5th century AD\n• ✝️ Dedicated to Bishop Sophronios\n• 🧱 Ruins of a three-aisled structure\n• 🖼️ Preserved mosaic floors and marble decorations\n• 🏺 Archaeological finds revealing early Christian art and architecture\n\n⭐ A significant archaeological site illustrating the spread of Christianity in Halkidiki during the early Byzantine era.",
            descriptionRo = "⛪ Bazilica Paleocreștină a lui Sofronie din Nikiti datează din secolul al V-lea d.Hr. și este unul dintre cele mai vechi monumente creștine din Halkidiki.\n\n• 🏛️ Bazilică creștină timpurie din secolul al V-lea d.Hr.\n• ✝️ Dedicată episcopului Sofronie\n• 🧱 Ruinele unei structuri cu trei nave\n• 🖼️ Podele din mozaic și decorațiuni din marmură\n• 🏺 Descoperiri arheologice ce ilustrează arta și arhitectura creștină timpurie\n\n⭐ Un sit arheologic important ce evidențiază răspândirea creștinismului în Halkidiki în perioada bizantină timpurie.",
            images = listOf(
                R.drawable.what_sophronios_basilica,
                R.drawable.what_sophronios_basilica1
            )
        ),
        "aquata_waterpark" to WhatToDoItem(
            id = "aquata_waterpark",
            categoryEn = "Water Parks",
            categoryRo = "Parcuri acvatice",
            beaches = listOf(
                "paralia_psakoudia",
                "paralia_sargani",
                "paralia_askamnia",
                "nikiti_beach",
                "kastri_beach",
                "koviou_beach",
                "kalogria_beach",
                "spathies_beach",
                "paralia_perigiali",
                "lagomandra_beach",
                "nikitis_beach_sithonia",
                "paradisos_beach",
                "neos_marmaras_beach",
                "kohi_beach",
                "diaporti_beach",
                "azapiko_beach",
                "paralia_alexandra_xenia",
                "paralia_xenia",
                "tristinika_beach",
                "ema_beach",
                "paralia_toroni",
                "porto_koufo_beach",
                "marathias_beach",
                "sithonia_cape",
                "kalamitsi_beach",
                "prassou_beach",
                "tourkolimnionas",
                "linaraki_beach",
                "valti_beach",
                "goa_beach",
                "sarti_beach",
                "heart_shaped_bay",
                "orange_beach",
                "mega_portokali_beach",
                "dream_coast_beach",
                "banana_beach",
                "zografou_beach",
                "bara_beach",
                "manos_beach",
                "rocks_on_the_beach",
                "karagatsi_beach",
                "lagonisi_beach",
                "livrohio",
                "beach_of_pirgos",
                "schinias_beach",
                "paralia_salonikiou",
            ),

            titleEn = "Aquata Waterpark",
            titleRo = "Aquata Waterpark",
            address = "Egialou 1, Nikiti 630 88, Sithonia, Halkidiki, Greece",
            hoursEn = "Daily 10:00–19:00 (summer season)",
            hoursRo = "Zilnic 10:00–19:00 (sezon estival)",
            website = "https://www.aquatawaterpark.com/",
            phone = "+30 23750 22244",
            descriptionEn = "💦 Aquata Waterpark in Nikiti is a family-friendly water attraction offering fun, relaxation, and refreshing activities for all ages in the heart of Sithonia.\n\n• 🎢 A variety of water slides, from thrilling rides to gentle attractions\n• 🌊 Pools and wave areas suitable for both adults and children\n• 👶 Safe children’s play zones with shallow water features\n• 🌴 Sunbathing and relaxation areas with shaded spots\n• ☕ Cafés and snack bars available throughout the park\n\n⭐ An ideal destination for a full day of water fun, relaxation, and family entertainment in Sithonia.",
            descriptionRo = "💦 Aquata Waterpark din Nikiti este un parc acvatic prietenos cu familiile, oferind distracție, relaxare și activități răcoritoare pentru toate vârstele, în inima Sithoniei.\n\n• 🎢 Tobogane acvatice variate, de la cele palpitante la cele pentru relaxare\n• 🌊 Piscine și zone cu valuri potrivite pentru adulți și copii\n• 👶 Zone de joacă sigure pentru copii, cu apă puțin adâncă\n• 🌴 Spații de relaxare și plajă cu zone umbrite\n• ☕ Cafenele și snack baruri disponibile în incinta parcului\n\n⭐ O destinație excelentă pentru o zi întreagă de distracție acvatică și relaxare în Sithonia.",
            images = listOf(
                R.drawable.what_aquata_waterpark,
                R.drawable.what_aquata_waterpark1
            )
        ),
                "psalida_tower" to WhatToDoItem(
            id = "psalida_tower",
            categoryEn = "Museums & Culture",
            categoryRo = "Muzee și cultură",
            beaches = listOf(
                "paralia_psakoudia",
                "paralia_sargani",
                "paralia_askamnia",
                "nikiti_beach",
                "kastri_beach",
                "koviou_beach",
                "kalogria_beach",
                "spathies_beach",
                "paralia_perigiali",
                "lagomandra_beach",
                "nikitis_beach_sithonia",
                "paradisos_beach",
                "neos_marmaras_beach",
                "kohi_beach",
                "diaporti_beach",
                "azapiko_beach",
                "paralia_alexandra_xenia",
                "paralia_xenia",
                "tristinika_beach",
                "ema_beach",
                "paralia_toroni",
                "porto_koufo_beach",
                "marathias_beach",
                "sithonia_cape",
                "kalamitsi_beach",
                "prassou_beach",
                "tourkolimnionas",
                "linaraki_beach",
                "valti_beach",
                "goa_beach",
                "sarti_beach",
                "heart_shaped_bay",
                "orange_beach",
                "mega_portokali_beach",
                "dream_coast_beach",
                "banana_beach",
                "zografou_beach",
                "bara_beach",
                "manos_beach",
                "rocks_on_the_beach",
                "karagatsi_beach",
                "lagonisi_beach",
                "livrohio",
                "beach_of_pirgos",
                "schinias_beach",
                "paralia_salonikiou",
            ),

            titleEn = "Byzantine Tower of Psalida",
            titleRo = "Turnul Bizantin Psalida",
            address = "Near Agios Nikolaos, Sithonia, Halkidiki, Greece",
            hoursEn = "Accessible anytime (exterior visit only)",
            hoursRo = "Accesibil oricând (vizitabil doar exteriorul)",
                    descriptionEn = "🏰 The Byzantine Tower of Psalida, located near Agios Nikolaos in Sithonia, is a historic defensive structure dating back to the Byzantine period.\n\n• 🏛️ Part of a network of Byzantine fortifications protecting coastal routes\n• ⛪ Linked to the protection of monastic properties in the region\n• 🧱 Ruins of a medieval tower set among olive groves\n• 📜 Insight into the medieval history of Halkidiki\n• 📸 Quiet location ideal for photography and exploration\n\n⭐ A peaceful historical site offering a glimpse into the Byzantine past of Sithonia.",
                    descriptionRo = "🏰 Turnul Bizantin Psalida, situat lângă Agios Nikolaos, în Sithonia, este o structură defensivă istorică ce datează din perioada bizantină.\n\n• 🏛️ Parte a unei rețele de fortificații bizantine ce protejau rutele de coastă\n• ⛪ Asociat cu apărarea proprietăților mănăstirești din zonă\n• 🧱 Ruinele unui turn medieval, înconjurate de livezi de măslini\n• 📜 Oferă o perspectivă asupra istoriei medievale a Halkidiki\n• 📸 Loc liniștit, ideal pentru explorare și fotografie\n\n⭐ Un sit istoric discret, perfect pentru cei interesați de trecutul bizantin al Sithoniei.",
                    images = listOf(
                R.drawable.what_unknown_fortress,
                R.drawable.what_unknown_fortress1
            )
        ),
        "nikiti_old_settlement" to WhatToDoItem(
            id = "nikiti_old_settlement",
            categoryEn = "History & Landmarks",
            categoryRo = "Istorie și obiective",
            beaches = listOf(
                "psakoudia_beach",
                "metamorfossi_beach",
                "red_rocks_of_metamorphosis",
                "paralia_kastri",
                "agios_ioannis_beach",
                "isla_beach",
                "small_spathies_beach",
                "paralia_elia",
                "elia_beach",
                "great_lagomanda_coast",
                "tripotamos_beach",
                "peaceful_beach",
                "porto_carras_beach",
                "koutsoupia_beach",
                "likithos_beach",
                "foresta_sithonia",
                "paralia_azapiko",
                "aretes_beach",
                "destenika_beach",
                "luka_beach",
                "toroni_beach",
                "lagoon_in_porto_koufo",
                "secret_beach",
                "mamba_beach",
                "kriaritsi_beach",
                "klimataria_beach",
                "skala_sykias_beach",
                "sykias_beach",
                "agridia_beach",
                "platania",
                "achlada",
                "platanitsi_beach",
                "kavourotrypes_beach",
                "paralia_armenistis",
                "robinson_beach",
                "porto_paradiso",
                "koutloumousi_beach",
                "fava_beach",
                "karydi_beach",
                "livari_beach",
                "talgo_beach",
                "latoura_beach",
                "trani_ammouda",
                "paralia_agios_nikolaos",
                "salonikiou_beach",
                "irini_beach",
            ),

            titleEn = "Nikiti Old Settlement",
            titleRo = "Satul Vechi Nikiti",
            address = "Old Town, Nikiti 630 88, Sithonia, Halkidiki, Greece",
            hoursEn = "Accessible anytime (cafes, tavernas, and shops usually open daily 09:00–00:00 in summer)",
            hoursRo = "Accesibil oricând (cafenelele, tavernele și magazinele deschise zilnic 09:00–00:00 vara)",
            descriptionEn = "🏘️ The Old Settlement of Nikiti is a beautifully preserved traditional village dating back to the 14th century, set on the hillside above the modern town.\n\n• 🪨 Traditional stone houses and narrow cobbled streets\n• ⛪ Church of Agios Nikitas, built in 1867\n• 🏛️ Well-preserved local architecture and historical atmosphere\n• 🍽️ Taverns and cafés offering authentic local flavors\n• 🌅 Panoramic views over the surrounding area\n• 🌙 Especially charming in the evening, with a romantic ambiance\n\n⭐ A must-visit destination in Sithonia, combining history, architecture, and a unique village atmosphere.",
            descriptionRo = "🏘️ Satul Vechi Nikiti este un sat tradițional bine conservat, datând din secolul al XIV-lea, situat pe colina de deasupra orașului modern.\n\n• 🪨 Case tradiționale din piatră și străduțe înguste pavate\n• ⛪ Biserica Agios Nikitas, construită în anul 1867\n• 🏛️ Arhitectură locală bine păstrată și atmosferă istorică\n• 🍽️ Taverne și cafenele cu arome locale autentice\n• 🌅 Priveliști frumoase asupra zonei înconjurătoare\n• 🌙 Deosebit de fermecător seara, cu o atmosferă romantică\n\n⭐ O destinație de neratat în Sithonia, ce îmbină istoria, arhitectura și farmecul autentic al satului grecesc.",
            images = listOf(
                R.drawable.what_nikiti_oldsettlement,
                R.drawable.what_nikiti_oldsettlement1
            )
        ),
        "panoramic_rest_point" to WhatToDoItem(
            id = "panoramic_rest_point",
            categoryEn = "Nature & Scenic Spots",
            categoryRo = "Natură și peisaje",
            beaches = listOf(
                "psakoudia_beach",
                "metamorfossi_beach",
                "red_rocks_of_metamorphosis",
                "paralia_kastri",
                "agios_ioannis_beach",
                "isla_beach",
                "small_spathies_beach",
                "paralia_elia",
                "elia_beach",
                "great_lagomanda_coast",
                "tripotamos_beach",
                "peaceful_beach",
                "porto_carras_beach",
                "koutsoupia_beach",
                "likithos_beach",
                "foresta_sithonia",
                "paralia_azapiko",
                "aretes_beach",
                "destenika_beach",
                "luka_beach",
                "toroni_beach",
                "lagoon_in_porto_koufo",
                "secret_beach",
                "mamba_beach",
                "kriaritsi_beach",
                "klimataria_beach",
                "skala_sykias_beach",
                "sykias_beach",
                "agridia_beach",
                "platania",
                "achlada",
                "platanitsi_beach",
                "kavourotrypes_beach",
                "paralia_armenistis",
                "robinson_beach",
                "porto_paradiso",
                "koutloumousi_beach",
                "fava_beach",
                "karydi_beach",
                "livari_beach",
                "talgo_beach",
                "latoura_beach",
                "trani_ammouda",
                "paralia_agios_nikolaos",
                "salonikiou_beach",
                "irini_beach",
            ),

            titleEn = "Panoramic & Rest Point of View",
            titleRo = "Punct Panoramic și de Odihnă",
            address = "Epar.Od. Nikitis-Sartis 42, Sithonia 630 88, Halkidiki, Greece",
            hoursEn = "Accessible anytime",
            hoursRo = "Accesibil oricând",
            descriptionEn = "🌄 The Panoramic & Rest Point on the Nikiti–Sarti provincial road offers breathtaking views over the Toroneos Gulf and the green hills of Sithonia.\n\n• 🌊 Wide panoramic views over the sea and coastline\n• 🌲 Overlooks the lush hills and natural landscape of Sithonia\n• 🪑 Benches and shaded areas for rest and relaxation\n• 📸 Ideal stop for photography and scenic breaks during the drive\n• 🌅 Especially popular at sunset, with warm colors over sea and mountains\n\n⭐ A peaceful scenic stop perfect for relaxation, photos, and enjoying the natural beauty of Sithonia.",
            descriptionRo = "🌄 Punctul Panoramic și de Odihnă de pe drumul provincial Nikiti–Sarti oferă priveliști spectaculoase asupra Golfului Toroneos și a colinelor verzi ale Sithoniei.\n\n• 🌊 Priveliști panoramice largi asupra mării și litoralului\n• 🌲 Deschidere către colinele verzi și peisajul natural al Sithoniei\n• 🪑 Bănci și zone umbrite pentru odihnă și relaxare\n• 📸 Oprire ideală pentru fotografii și pauze de drum\n• 🌅 Deosebit de apreciat la apus, cu nuanțe calde peste mare și munți\n\n⭐ Un loc liniștit și pitoresc, perfect pentru relaxare, fotografii și admirarea naturii din Sithonia.",
            images = listOf(
                R.drawable.what_panoramic_rest,
                R.drawable.what_panoramic_rest1
            )
        ),
        "neos_marmaras_village" to WhatToDoItem(
            id = "neos_marmaras_village",
            categoryEn = "Villages & Local Life",
            categoryRo = "Sate și viață locală",
            beaches = listOf(
                "psakoudia_beach",
                "metamorfossi_beach",
                "red_rocks_of_metamorphosis",
                "paralia_kastri",
                "agios_ioannis_beach",
                "isla_beach",
                "small_spathies_beach",
                "paralia_elia",
                "elia_beach",
                "great_lagomanda_coast",
                "tripotamos_beach",
                "peaceful_beach",
                "porto_carras_beach",
                "koutsoupia_beach",
                "likithos_beach",
                "foresta_sithonia",
                "paralia_azapiko",
                "aretes_beach",
                "destenika_beach",
                "luka_beach",
                "toroni_beach",
                "lagoon_in_porto_koufo",
                "secret_beach",
                "mamba_beach",
                "kriaritsi_beach",
                "klimataria_beach",
                "skala_sykias_beach",
                "sykias_beach",
                "agridia_beach",
                "platania",
                "achlada",
                "platanitsi_beach",
                "kavourotrypes_beach",
                "paralia_armenistis",
                "robinson_beach",
                "porto_paradiso",
                "koutloumousi_beach",
                "fava_beach",
                "karydi_beach",
                "livari_beach",
                "talgo_beach",
                "latoura_beach",
                "trani_ammouda",
                "paralia_agios_nikolaos",
                "salonikiou_beach",
                "irini_beach",
            ),

            titleEn = "Neos Marmaras",
            titleRo = "Neos Marmaras",
            address = "Neos Marmaras 630 81, Sithonia, Halkidiki, Greece",
            hoursEn = "Accessible anytime (shops & tavernas usually open daily 09:00–00:00 in summer)",
            hoursRo = "Accesibil oricând (magazinele și tavernele sunt deschise zilnic 09:00–00:00 vara)",
            descriptionEn = "🏖️ Neos Marmaras is the largest and most cosmopolitan town in Sithonia, built on three hills and stretching along a lively waterfront on the Toroneos Gulf.\n\n• 🏘️ Scenic old town with traditional streets and local character\n• 🍽️ Wide selection of tavernas, cafés, shops, and vibrant nightlife\n• 🌊 Beautiful waterfront promenade and marina atmosphere\n• 🏖️ Easy access to nearby beaches such as Paradisos and Porto Carras\n• 🚤 Boat trips and sea excursions around the Toroneos Gulf\n• 🌅 Stunning views over the hills, town, and coastline\n\n⭐ A must-visit destination combining culture, leisure, and seaside beauty in the heart of Sithonia.",
            descriptionRo = "🏖️ Neos Marmaras este cel mai mare și cosmopolit oraș din Sithonia, construit pe trei coline și desfășurat de-a lungul unei faleze animate pe Golful Toroneos.\n\n• 🏘️ Parte veche pitorească, cu străzi tradiționale și farmec local\n• 🍽️ Gamă largă de taverne, cafenele, magazine și viață de noapte\n• 🌊 Faleză animată și atmosferă de port turistic\n• 🏖️ Acces facil la plajele din apropiere, precum Paradisos și Porto Carras\n• 🚤 Excursii cu barca și activități pe mare în Golful Toroneos\n• 🌅 Priveliști spectaculoase asupra colinelor, orașului și mării\n\n⭐ O destinație de neratat ce îmbină cultura, distracția și frumusețea litoralului în inima Sithoniei.",
            images = listOf(
                R.drawable.what_neos_marmaras,
                R.drawable.what_neos_marmaras1
            )
        ),
        "toroni_archaeological_site" to WhatToDoItem(
            id = "toroni_archaeological_site",
            categoryEn = "History & Landmarks",
            categoryRo = "Istorie și obiective",
            beaches = listOf(
                "psakoudia_beach",
                "metamorfossi_beach",
                "red_rocks_of_metamorphosis",
                "paralia_kastri",
                "agios_ioannis_beach",
                "isla_beach",
                "small_spathies_beach",
                "paralia_elia",
                "elia_beach",
                "great_lagomanda_coast",
                "tripotamos_beach",
                "peaceful_beach",
                "porto_carras_beach",
                "koutsoupia_beach",
                "likithos_beach",
                "foresta_sithonia",
                "paralia_azapiko",
                "aretes_beach",
                "destenika_beach",
                "luka_beach",
                "toroni_beach",
                "lagoon_in_porto_koufo",
                "secret_beach",
                "mamba_beach",
                "kriaritsi_beach",
                "klimataria_beach",
                "skala_sykias_beach",
                "sykias_beach",
                "agridia_beach",
                "platania",
                "achlada",
                "platanitsi_beach",
                "kavourotrypes_beach",
                "paralia_armenistis",
                "robinson_beach",
                "porto_paradiso",
                "koutloumousi_beach",
                "fava_beach",
                "karydi_beach",
                "livari_beach",
                "talgo_beach",
                "latoura_beach",
                "trani_ammouda",
                "paralia_agios_nikolaos",
                "salonikiou_beach",
                "irini_beach",
            ),

            titleEn = "Archaeological Site of Toroni",
            titleRo = "Sit Arheologic Toroni",
            address = "Toroni, Sithonia 630 72, Halkidiki, Greece",
            hoursEn = "Open-air archaeological site (accessible anytime, best during daylight)",
            hoursRo = "Sit arheologic în aer liber (accesibil oricând, recomandat pe timp de zi)",
            descriptionEn = "🏛️ The Archaeological Site of Toroni preserves the remains of one of the most powerful ancient cities in Halkidiki, with origins dating back to the 8th century BC.\n\n• 🏺 Ancient city with a long and important historical presence\n• 🧱 Remains of city walls, residential areas, and fortifications\n• ⛪ Early Christian basilicas revealing later phases of the settlement\n• 🏰 Acropolis with defensive structures overlooking the sea\n• 🌊 Stunning coastal views over the Aegean Sea\n\n⭐ A remarkable archaeological site offering a journey through ancient history combined with breathtaking seaside scenery in Sithonia.",
            descriptionRo = "🏛️ Situl Arheologic Toroni păstrează vestigiile unuia dintre cele mai puternice orașe antice din Halkidiki, cu origini ce datează din secolul al VIII-lea î.Hr.\n\n• 🏺 Oraș antic cu o istorie îndelungată și importantă\n• 🧱 Fragmente din zidurile orașului, locuințe și fortificații\n• ⛪ Bazilici paleocreștine ce reflectă etapele târzii ale așezării\n• 🏰 Acropola cu structuri defensive, situată deasupra mării\n• 🌊 Priveliști spectaculoase asupra Mării Egee\n\n⭐ Un sit arheologic deosebit ce oferă o incursiune în istoria antică și peisaje de coastă impresionante din Sithonia.",
            images = listOf(
                R.drawable.what_toroni_archaeological,
                R.drawable.what_toroni_archaeological1
            )
        ),
        "porto_koufo" to WhatToDoItem(
            id = "porto_koufo",
            categoryEn = "Nature & Scenic Spots",
            categoryRo = "Natură și peisaje",
            beaches = emptyList(),

            titleEn = "Porto Koufo",
            titleRo = "Porto Koufo",
            address = "Porto Koufo, Sithonia 630 72, Halkidiki, Greece",
            hoursEn = "Accessible anytime",
            hoursRo = "Accesibil oricând",
            descriptionEn = "⚓ Porto Koufo, located on the southwestern coast of Sithonia, is the deepest natural harbor in Greece and one of the safest anchorages in the Aegean Sea.\n\n• 🌊 Dramatic, fjord-like bay offering shelter from winds\n• 📜 Known since antiquity and described by historian Thucydides\n• ⚓ Used historically as a strategic naval base\n• 🐟 Peaceful fishing village atmosphere\n• 🍽️ Excellent tavernas serving fresh fish and seafood\n• 🥾 Hiking trails and panoramic viewpoints around the bay\n\n⭐ A unique destination combining history, natural beauty, and authentic seaside charm in Sithonia.",
            descriptionRo = "⚓ Porto Koufo, situat pe coasta sud-vestică a Sithoniei, este cel mai adânc port natural din Grecia și unul dintre cele mai sigure adăposturi maritime din Marea Egee.\n\n• 🌊 Golf spectaculos, asemănător unui fiord, ferit de vânturi\n• 📜 Cunoscut încă din antichitate și descris de istoricul Tucidide\n• ⚓ Folosit de-a lungul timpului ca bază navală strategică\n• 🐟 Atmosferă liniștită de sat pescăresc\n• 🍽️ Taverne renumite pentru pește și fructe de mare proaspete\n• 🥾 Trasee de drumeție și puncte panoramice în împrejurimi\n\n⭐ O destinație aparte ce îmbină istoria, natura și farmecul autentic al litoralului din Sithonia.",

            images = listOf(
                R.drawable.what_porto_koufo,
                R.drawable.what_porto_koufo1
            )
        ),
        "porto_koufo_cannons" to WhatToDoItem(
            id = "porto_koufo_cannons",
            categoryEn = "History & Landmarks",
            categoryRo = "Istorie și obiective",
            beaches = emptyList(),

            titleEn = "Cannons of Porto Koufo",
            titleRo = "Tunurile din Porto Koufo",
            address = "Porto Koufo, Sithonia 630 72, Halkidiki, Greece",
            hoursEn = "Accessible anytime (open-air historical site)",
            hoursRo = "Accesibil oricând (sit istoric în aer liber)",
            descriptionEn = "🪖 The Cannons of Porto Koufo stand as a reminder of the strategic importance of this deep natural harbor.\n\n• ⚓ Porto Koufo’s bay was heavily fortified during World War II\n• 🛡️ German coastal artillery installations controlled naval access to the Aegean Sea\n• 🧱 Remains of gun emplacements can still be seen on the surrounding hills\n• 📜 A tangible link to the wartime history of Halkidiki\n• 🌊 Elevated positions offer stunning panoramic views over the fjord-like harbor\n\n⭐ A fascinating historical site that combines military heritage with breathtaking coastal scenery.",
            descriptionRo = "🪖 Tunurile din Porto Koufo sunt o mărturie a importanței strategice a acestui port natural adânc.\n\n• ⚓ Golful Porto Koufo a fost puternic fortificat în timpul celui de-Al Doilea Război Mondial\n• 🛡️ Artileria de coastă germană controla accesul naval către Marea Egee\n• 🧱 Rămășițele pozițiilor de artilerie pot fi observate și astăzi pe dealurile din jur\n• 📜 Un martor autentic al istoriei militare din Halkidiki\n• 🌊 Punctele înalte oferă priveliști panoramice spectaculoase asupra golfului asemănător unui fiord\n\n⭐ Un obiectiv istoric interesant ce îmbină patrimoniul militar cu peisaje de coastă impresionante.",
             images = listOf(
                R.drawable.what_porto_koufo_cannons,
                R.drawable.what_porto_koufo_cannons1
            )
        ),
        "lemos_beach" to WhatToDoItem(
            id = "lemos_beach",
            categoryEn = "Nature & Scenic Spots",
            categoryRo = "Natură și peisaje",
            beaches = emptyList(),

            titleEn = "Lemos Beach",
            titleRo = "Plaja Lemos",
            address = "Near Porto Koufo, Sithonia 630 72, Halkidiki, Greece",
            hoursEn = "Accessible anytime (no organized facilities)",
            hoursRo = "Accesibil oricând (fără facilități organizate)",
            website = "https://www.halkidikitravel.com/beaches/lemos-beach",
            descriptionEn = "🏝️ Lemos Beach, located close to Porto Koufo, is a rare double-sided sandy strip surrounded by turquoise waters on both sides.\n\n• 🌊 Unique natural ‘isthmus beach’ connecting the mainland with a small peninsula\n• 🏖️ Two calm bays with crystal-clear waters on each side\n• 🌿 Completely unspoiled, with no organized facilities\n• 🏊 Ideal for swimming, snorkeling, and quiet relaxation\n• 📸 Perfect spot for photography thanks to its dramatic landscape\n\n⭐ One of Sithonia’s hidden gems, offering raw natural beauty and a truly unique seaside experience.",
            descriptionRo = "🏝️ Plaja Lemos, situată în apropiere de Porto Koufo, este o fâșie rară de nisip mărginită de ape turcoaz pe ambele părți.\n\n• 🌊 ‘Plajă istm’ naturală ce leagă țărmul de o mică peninsulă\n• 🏖️ Două golfuri diferite, cu ape calme și cristaline\n• 🌿 Complet neamenajată, fără facilități organizate\n• 🏊 Ideală pentru înot, snorkeling și relaxare liniștită\n• 📸 Loc perfect pentru fotografie datorită peisajului dramatic\n\n⭐ Una dintre comorile ascunse ale Sithoniei, ce oferă frumusețe naturală pură și o experiență deosebită la malul mării.",
            images = listOf(
                R.drawable.what_lemos_beach,
                R.drawable.what_lemos_beach1
            )
        ),
        "prehistoric_tumulus" to WhatToDoItem(
            id = "prehistoric_tumulus",
            categoryEn = "History & Landmarks",
            categoryRo = "Istorie și obiective",
            beaches = emptyList(),

            titleEn = "Archaeological Site – Prehistoric Tumulus",
            titleRo = "Sit Arheologic – Tumulus Preistoric",
            address = "Halkidiki, Greece (exact location near ancient settlement areas)",
            hoursEn = "Open-air archaeological site (accessible anytime, best during daylight)",
            hoursRo = "Sit arheologic în aer liber (accesibil oricând, recomandat pe timp de zi)",
            descriptionEn = "🏺 The Prehistoric Tumulus in Halkidiki is an ancient burial mound dating back to prehistoric times, offering insight into the earliest human presence in the region.\n\n• 🏞️ Prehistoric burial mound used for collective or elite graves\n• 🏺 Archaeological finds including pottery, tools, and burial artifacts\n• 📜 Evidence of early settlements and ancient belief systems\n• 🌿 Quiet site set within the natural landscape of Halkidiki\n• 🧭 A place reflecting the deep roots of human history in the area\n\n⭐ A discreet yet meaningful archaeological landmark connecting visitors to Halkidiki’s prehistoric past.",
            descriptionRo = "🏺 Tumulusul preistoric din Halkidiki este un mormânt tumular antic, ce datează din epoca preistorică, oferind o perspectivă asupra celor mai timpurii comunități umane din regiune.\n\n• 🏞️ Mormânt preistoric folosit pentru înmormântări colective sau ale elitelor\n• 🏺 Descoperiri arheologice precum ceramică, unelte și obiecte funerare\n• 📜 Dovezi ale așezărilor timpurii și ale credințelor străvechi\n• 🌿 Sit liniștit, integrat în peisajul natural al Halkidiki\n• 🧭 Un loc ce reflectă rădăcinile profunde ale istoriei umane din zonă\n\n⭐ Un reper arheologic discret, dar valoros, ce conectează vizitatorii cu trecutul preistoric al Halkidiki.",
            images = listOf(
                R.drawable.what_prehistoric_tumulus,
                R.drawable.what_prehistoric_tumulus1
            )
        ),
        "iron_age_settlement" to WhatToDoItem(
            id = "iron_age_settlement",
            categoryEn = "History & Landmarks",
            categoryRo = "Istorie și obiective",
            beaches = emptyList(),

            titleEn = "Archaeological Site – Iron Age Settlement",
            titleRo = "Sit Arheologic – Așezare din Epoca Fierului",
            address = "Halkidiki, Greece (near prehistoric tumulus sites)",
            hoursEn = "Open-air archaeological site (accessible anytime, best during daylight)",
            hoursRo = "Sit arheologic în aer liber (accesibil oricând, recomandat pe timp de zi)",
            descriptionEn = "🏺 The Iron Age Settlement in Halkidiki dates back to the early 1st millennium BC and represents an important phase in the region’s ancient history.\n\n• 🏘️ Stone foundations of houses revealing organized community life\n• 🏺 Pottery, storage pits, and everyday household artifacts\n• 🔨 Metal tools illustrating early technological development\n• ⚱️ Evidence of burial practices and social structure\n• 📜 Marks the transition from prehistoric to historic times\n• 🌿 Demonstrates continuous human presence and cultural evolution\n\n⭐ An important archaeological site offering insight into Iron Age life and the early development of settlements in Halkidiki.",
            descriptionRo = "🏺 Așezarea din Epoca Fierului din Halkidiki datează din prima parte a mileniului I î.Hr. și reprezintă o etapă importantă din istoria antică a regiunii.\n\n• 🏘️ Fundații de piatră ale locuințelor, ce indică o comunitate bine organizată\n• 🏺 Ceramică, gropi de depozitare și obiecte de uz cotidian\n• 🔨 Unelte metalice ce reflectă progresul tehnologic\n• ⚱️ Dovezi ale practicilor funerare și ale structurii sociale\n• 📜 Ilustrează tranziția de la epoca preistorică la cea istorică\n• 🌿 Confirmă continuitatea locuirii și evoluția culturală\n\n⭐ Un sit arheologic valoros ce oferă o perspectivă clară asupra vieții și culturii din Epoca Fierului în Halkidiki.",
             images = listOf(
                R.drawable.what_iron_age_settlement,
                R.drawable.what_iron_age_settlement1
            )
        ),
        "goa_beach_cave" to WhatToDoItem(
            id = "goa_beach_cave",
            categoryEn = "Nature & Scenic Spots",
            categoryRo = "Natură și peisaje",
            beaches = emptyList(),

            titleEn = "Goa Beach & Cave",
            titleRo = "Plaja și Peștera Goa",
            address = "Goa Beach, near Sarti, Sithonia 630 72, Halkidiki, Greece",
            hoursEn = "Accessible anytime (best during daylight; swimming recommended in calm seas)",
            hoursRo = "Accesibil oricând (recomandat pe timp de zi; înotul recomandat doar pe mare calmă)",
            website = "https://www.halkidikitravel.com/beaches/goa-beach",
            descriptionEn = "🏝️ Goa Beach, located near Sarti, is a hidden gem of Sithonia, famous for its turquoise waters, fine sand, and dramatic rock formations.\n\n• 🌊 Crystal-clear turquoise waters ideal for swimming\n• 🏖️ Fine sand combined with rocky coastal scenery\n• 🪨 Impressive cliffs shaping the beach’s wild character\n• 🕳️ Small natural sea cave carved into the rocks, accessible by swimming or paddling\n• 🌿 Secluded and less crowded, perfect for peaceful escapes\n• 📸 Excellent spot for photography and exploration\n\n⭐ A unique blend of relaxation and adventure, Goa Beach is perfect for nature lovers seeking unspoiled coastal beauty in Sithonia.",
            descriptionRo = "🏝️ Plaja Goa, situată lângă Sarti, este o adevărată comoară ascunsă a Sithoniei, renumită pentru apele turcoaz, nisipul fin și formațiunile stâncoase spectaculoase.\n\n• 🌊 Ape limpezi, ideale pentru înot\n• 🏖️ Nisip fin îmbinat cu peisaj stâncos sălbatic\n• 🪨 Faleze impresionante ce definesc caracterul plajei\n• 🕳️ Mică peșteră marină naturală, accesibilă înot sau cu caiacul\n• 🌿 Retrasă și mai puțin aglomerată, perfectă pentru relaxare\n• 📸 Loc excelent pentru fotografie și explorare\n\n⭐ Un amestec de relaxare și aventură, Plaja Goa este ideală pentru iubitorii de natură care caută frumusețe de coastă nealterată în Sithonia.",
             images = listOf(
                R.drawable.what_goa_beach,
                R.drawable.what_goa_beach1
            )
        ),
        "sarti_village" to WhatToDoItem(
            id = "sarti_village",
            categoryEn = "Villages & Local Life",
            categoryRo = "Sate și viață locală",
            beaches = emptyList(),

            titleEn = "Sarti Village",
            titleRo = "Satul Sarti",
            address = "Sarti 630 72, Sithonia, Halkidiki, Greece",
            hoursEn = "Accessible anytime (shops & tavernas usually open daily 09:00–00:00 in summer)",
            hoursRo = "Accesibil oricând (magazinele și tavernele sunt deschise zilnic 09:00–00:00 vara)",
            descriptionEn = "🏖️ Sarti is a lively seaside village on the eastern coast of Sithonia, well known for its long sandy beach and stunning views of Mount Athos.\n\n• 🌊 Long sandy beach with crystal-clear waters and panoramic views\n• 🏔️ Unique sight of Mount Athos rising above the sea\n• 🏘️ Charming old village with traditional streets and local character\n• 🍽️ Wide choice of tavernas, cafés, beach bars, and summer nightlife\n• 🏄 Water sports, beach activities, and boat excursions\n• 🏨 Hotels and guesthouses for all budgets\n\n⭐ A vibrant summer destination that perfectly blends beach life, authentic Greek charm, and breathtaking scenery, ideal for families and young travelers alike.",
            descriptionRo = "🏖️ Sarti este un sat de coastă animat, situat pe țărmul estic al Sithoniei, renumit pentru plaja sa lungă cu nisip și priveliștile spectaculoase asupra Muntelui Athos.\n\n• 🌊 Plajă întinsă cu nisip fin și ape limpezi\n• 🏔️ Priveliști unice către Muntele Athos\n• 🏘️ Sat vechi pitoresc, cu străzi tradiționale și farmec local\n• 🍽️ Numeroase taverne, cafenele, beach baruri și viață de noapte de vară\n• 🏄 Sporturi nautice, activități pe plajă și excursii cu barca\n• 🏨 Hoteluri și pensiuni pentru toate bugetele\n\n⭐ O destinație de vară vibrantă ce îmbină perfect relaxarea la plajă, farmecul autentic grecesc și peisaje spectaculoase, ideală pentru familii și tineri.",
            images = listOf(
                R.drawable.what_sarti_village,
                R.drawable.what_sarti_village1
            )
        ),
        "diaporos_island" to WhatToDoItem(
            id = "diaporos_island",
            categoryEn = "Nature & Scenic Spots",
            categoryRo = "Natură și peisaje",
            beaches = emptyList(),

            titleEn = "Diaporos Island",
            titleRo = "Insula Diaporos",
            address = "Diaporos Island, opposite Vourvourou, Sithonia 630 78, Halkidiki, Greece",
            hoursEn = "Accessible anytime (by boat or kayak; best visited in summer daylight)",
            hoursRo = "Accesibil oricând (cu barca sau caiacul; recomandat vara, pe timp de zi)",
            descriptionEn = "🏝️ Diaporos Island, located across from Vourvourou in Sithonia, is a stunning natural paradise famous for its turquoise waters, hidden coves, and sandy beaches.\n\n• 🌊 Crystal-clear turquoise water and shallow natural lagoons\n• 🛶 Accessible only by boat, kayak, or SUP\n• 🏖️ Secluded sandy beaches and unspoiled bays like Kryftos and Myrsini\n• 🐠 Excellent conditions for swimming and snorkeling\n• 👨‍👩‍👧 Calm, shallow waters suitable for families\n• 🌿 Wild, untouched landscape with a peaceful atmosphere\n\n⭐ Often called the \"Blue Lagoon\" of Halkidiki, Diaporos is a true hidden gem of Sithonia, perfect for relaxation and exploration.",
            descriptionRo = "🏝️ Insula Diaporos, situată în fața stațiunii Vourvourou din Sithonia, este un paradis natural spectaculos, renumit pentru apele sale turcoaz, golfurile ascunse și plajele cu nisip.\n\n• 🌊 Apă limpede, de culoare turcoaz, și lagune naturale puțin adânci\n• 🛶 Accesibilă doar cu barca, caiacul sau SUP-ul\n• 🏖️ Plaje retrase și golfuri neatinse precum Kryftos și Myrsini\n• 🐠 Condiții excelente pentru înot și snorkeling\n• 👨‍👩‍👧 Ape calme, ideale pentru familii\n• 🌿 Peisaj sălbatic, aproape neatins, cu atmosferă liniștită\n\n⭐ Supranumită „Laguna Albastră” a Halkidiki, Diaporos rămâne o adevărată comoară ascunsă a Sithoniei, perfectă pentru relaxare și explorare.",
            images = listOf(
                R.drawable.what_diaporos_island,
                R.drawable.what_diaporos_island1
            )
        ),
        "prosphorion_tower" to WhatToDoItem(
            id = "prosphorion_tower",
            categoryEn = "Museums & Culture",
            categoryRo = "Muzee și cultură",
            beaches = listOf(
                "ladhario_beach",
                "develiki_beach",
                "tripiti_beach",
                "ouranoupolis_beach",
                "nea_roda_beach",
                "kakoudia_beach",
                "babylon_beach",
                "olympiada_beach",
                "milies_beach",
                "vrasna_beach",
            ),

            titleEn = "Byzantine Tower of Prosphorion",
            titleRo = "Turnul Bizantin Prosphorion",
            address = "Ouranoupoli, Athos, Halkidiki 630 75, Greece",
            hoursEn = "Tue–Sun 10:00–17:00; Mon Closed",
            hoursRo = "Mar–Dum 10:00–17:00; Luni Închis",
            website = "https://www.ouranoupoli.com/tower-of-prosphorion/",
            phone = "+30 23770 71248",
            descriptionEn = "🏰 The Byzantine Tower of Prosphorion, located at the entrance of Ouranoupoli, is the largest and best-preserved medieval tower in Halkidiki, standing as a powerful symbol of the region’s Byzantine past.\n\n• 🕍 Built in the 14th century and originally owned by the Vatopedi Monastery of Mount Athos\n• 🛡️ Served as a defensive fortress and storage tower\n• 🏛️ Houses a small museum with archaeological exhibits\n• 🌊 Offers panoramic views over the sea and Ammouliani Island\n• 📍 Landmark of Ouranoupoli and gateway to Mount Athos\n\n⭐ A must-see historical monument that connects visitors with the Byzantine heritage and spiritual legacy of the area.",
            descriptionRo = "🏰 Turnul Bizantin Prosphorion, situat la intrarea în Ouranoupoli, este cel mai mare și mai bine conservat turn medieval din Halkidiki, fiind un simbol puternic al trecutului bizantin al regiunii.\n\n• 🕍 Construit în secolul al XIV-lea și aparținând inițial Mănăstirii Vatopedi de pe Muntele Athos\n• 🛡️ A servit ca fortăreață defensivă și turn de depozitare\n• 🏛️ Găzduiește un mic muzeu cu descoperiri arheologice\n• 🌊 Oferă priveliști panoramice asupra mării și insulei Ammouliani\n• 📍 Reper emblematic al localității Ouranoupoli și poartă de acces spre Athos\n\n⭐ Un obiectiv istoric de neratat, ce leagă vizitatorii de patrimoniul bizantin și moștenirea spirituală a zonei.",
            images = listOf(
                R.drawable.what_prosphorion_tower,
                R.drawable.what_prosphorion_tower1
            )
        ),
        "megali_panagia_wednesday_market" to WhatToDoItem(
            id = "megali_panagia_wednesday_market",
            categoryEn = "Shopping & Markets",
            categoryRo = "Cumpărături și piețe",
            beaches = listOf(
                "xiropotamos_beach",
                "komitsa_beach",
                "stratoni_beach",
                "paralia_stavros",
                "nea_vrasna_beach",
            ),

            titleEn = "Megali Panagia Wednesday Street Market (Laiki Agora)",
            titleRo = "Piața Volantă de Miercuri Megali Panagia (Laiki Agora)",
            address = "Central square, next to the Primary School, Megali Panagia, Halkidiki, Greece",
            hoursEn = "Wed 07:00–14:00",
            hoursRo = "Miercuri 07:00–14:00",
            descriptionEn = "🛒 Every Wednesday morning, the village of Megali Panagia comes alive with a traditional ‘laiki agora’ held in the central square, next to the primary school.\n\n• 🍎 Fresh seasonal fruits and vegetables from local farmers\n• 🫒 Olives, olive oil, honey, cheese, herbs, and local fish\n• 🥖 Homemade baked goods and traditional products\n• 👕 Stalls selling clothes, shoes, and household items\n• 🎶 Lively local atmosphere with authentic village vibes\n\n⭐ A perfect place to experience everyday life in Halkidiki and discover fresh local products directly from producers.",
            descriptionRo = "🛒 În fiecare miercuri dimineața, satul Megali Panagia prinde viață datorită ‘laiki agora’ tradiționale, organizată în piața centrală, lângă școala primară.\n\n• 🍎 Fructe și legume proaspete de sezon, direct de la fermieri locali\n• 🫒 Măsline, ulei de măsline, miere, brânzeturi, ierburi și pește local\n• 🥖 Produse de panificație de casă și specialități tradiționale\n• 👕 Tarabe cu haine, încălțăminte și articole pentru casă\n• 🎶 Atmosferă animată, specifică vieții autentice de sat\n\n⭐ Un loc ideal pentru a descoperi viața de zi cu zi din Halkidiki și produse locale autentice.",
            images = listOf(
                R.drawable.what_megalipanagia_market,
                R.drawable.what_megalipanagia_market1
            )
        ),
        "arnea_wednesday_market" to WhatToDoItem(
            id = "arnea_wednesday_market",
            categoryEn = "Shopping & Markets",
            categoryRo = "Cumpărături și piețe",
            beaches = emptyList(),

            titleEn = "Arnea Wednesday Street Market (Laiki Agora)",
            titleRo = "Piața Volantă de Miercuri Arnea (Laiki Agora)",
            address = "Central square, next to St. Stephen’s Church, Arnea, Halkidiki, Greece",
            hoursEn = "Wed 07:00–14:00",
            hoursRo = "Miercuri 07:00–14:00",
            descriptionEn = "🛒 Every Wednesday morning, the mountain village of Arnea hosts a traditional ‘laiki agora’ in the central square, right next to St. Stephen’s Church.\n\n• 🍎 Seasonal fruits and vegetables from local farmers\n• 🫒 Olives, olive oil, cheese, honey, herbs, fish, and baked goods\n• 👕 Stalls with clothing, shoes, and household items\n• ⛪ Picturesque setting beside St. Stephen’s Church\n• 🏔️ Authentic atmosphere of a traditional mountain village\n\n⭐ A lively local market where visitors can experience genuine Halkidiki culture, traditions, and flavors.",
            descriptionRo = "🛒 În fiecare miercuri dimineața, satul de munte Arnea găzduiește o ‘laiki agora’ tradițională în piața centrală, chiar lângă Biserica Sf. Ștefan.\n\n• 🍎 Fructe și legume de sezon, direct de la fermieri locali\n• 🫒 Măsline, ulei de măsline, brânzeturi, miere, ierburi, pește și produse de panificație\n• 👕 Tarabe cu îmbrăcăminte, încălțăminte și articole gospodărești\n• ⛪ Cadru pitoresc lângă Biserica Sf. Ștefan\n• 🏔️ Atmosferă autentică de sat tradițional de munte\n\n⭐ O piață locală plină de viață, unde vizitatorii pot descoperi cultura, tradițiile și aromele autentice din Halkidiki.",
            images = listOf(
                R.drawable.what_arnea_market,
                R.drawable.what_arnea_market1
            )
        ),
        "zygos_monastery" to WhatToDoItem(
            id = "zygos_monastery",
            categoryEn = "History & Landmarks",
            categoryRo = "Istorie și obiective",
            beaches = listOf(
                "ladhario_beach",
                "develiki_beach",
                "tripiti_beach",
                "ouranoupolis_beach",
                "nea_roda_beach",
                "kakoudia_beach",
                "babylon_beach",
                "olympiada_beach",
                "milies_beach",
                "vrasna_beach",
            ),

            titleEn = "Monastery of Zygos (Frangokastro)",
            titleRo = "Mănăstirea Zygos (Frangokastro)",
            address = "Near Ouranoupoli, Mount Athos border, Halkidiki 630 75, Greece",
            hoursEn = "Open-air archaeological site (accessible during daylight)",
            hoursRo = "Sit arheologic în aer liber (accesibil pe timp de zi)",
            website = "https://www.mountathosarea.org/portfolio-items/zygos-monastery/",
            descriptionEn = "⛪ The Monastery of Zygos, also known as Frangokastro, is a ruined Byzantine monastery located just outside the border of Mount Athos, near Ouranoupoli.\n\n• 🕍 Built in the 10th century and abandoned in the 12th century\n• 🚪 One of the few Athonite monasteries accessible to both men and women\n• 🛡️ Impressive ruins including defensive walls, towers, and church remains\n• 📍 Located outside the Athonite monastic state, near the Mount Athos border\n• 📜 Offers insight into early monastic life on Mount Athos\n\n⭐ A rare and fascinating historical site that allows all visitors to explore the origins of Athonite monasticism.",
            descriptionRo = "⛪ Mănăstirea Zygos, cunoscută și sub numele de Frangokastro, este o mănăstire bizantină în ruină, situată chiar la granița Muntelui Athos, lângă Ouranoupoli.\n\n• 🕍 Construită în secolul al X-lea și abandonată în secolul al XII-lea\n• 🚪 Una dintre puținele mănăstiri athonite accesibile atât bărbaților, cât și femeilor\n• 🛡️ Ruine impresionante cu ziduri de apărare, turnuri și rămășițe de biserică\n• 📍 Situată în afara statului monastic athonit, la limita Muntelui Athos\n• 📜 Oferă o perspectivă rară asupra vieții monahale timpurii de pe Athos\n\n⭐ Un obiectiv istoric deosebit, ce permite tuturor vizitatorilor să descopere originile monahismului athonit.",
            images = listOf(
                R.drawable.what_zygos_monastery,
                R.drawable.what_zygos_monastery1
            )
        ),
        "ammouliani_island" to WhatToDoItem(
            id = "ammouliani_island",
            categoryEn = "Nature & Scenic Spots",
            categoryRo = "Natură și peisaje",
            beaches = listOf(
                "ladhario_beach",
                "develiki_beach",
                "tripiti_beach",
                "ouranoupolis_beach",
                "nea_roda_beach",
                "kakoudia_beach",
                "babylon_beach",
                "olympiada_beach",
                "milies_beach",
                "vrasna_beach",
            ),

            titleEn = "Ammouliani Island",
            titleRo = "Insula Ammouliani",
            address = "Ammouliani 630 75, Halkidiki, Greece (ferry from Tripiti port, near Ouranoupoli)",
            hoursEn = "Accessible anytime (ferry connection daily from Tripiti)",
            hoursRo = "Accesibil oricând (ferry zilnic din portul Tripiti)",
            website = "https://www.visitammouliani.com/",
            descriptionEn = "🏝️ Ammouliani is the only inhabited island of Halkidiki, located opposite Mount Athos and easily accessible by ferry from Tripiti.\n\n• 🏖️ Golden sandy beaches such as Alikes, Megali Ammos, and Karagatsia\n• 🌊 Crystal-clear waters ideal for swimming and relaxation\n• 🍽️ Traditional tavernas serving fresh seafood and local dishes\n• 🚤 Boat trips to the nearby Drenia islets\n• 🏘️ Authentic Greek village atmosphere with a laid-back vibe\n\n⭐ A peaceful island escape, perfect for families, couples, and nature lovers seeking clear waters and authentic Greek charm.",
            descriptionRo = "🏝️ Ammouliani este singura insulă locuită din Halkidiki, situată vizavi de Muntele Athos și ușor accesibilă cu ferry din portul Tripiti.\n\n• 🏖️ Plaje cu nisip auriu precum Alikes, Megali Ammos și Karagatsia\n• 🌊 Ape cristaline, ideale pentru înot și relaxare\n• 🍽️ Taverne tradiționale cu fructe de mare proaspete și preparate locale\n• 🚤 Excursii cu barca către insulițele Drenia din apropiere\n• 🏘️ Atmosferă autentică de sat grecesc, liniștită și primitoare\n\n⭐ O evadare insulară liniștită, ideală pentru familii, cupluri și iubitorii de natură care caută ape limpezi și farmec grecesc autentic.",
             images = listOf(
                R.drawable.what_ammouliani_island,
                R.drawable.what_ammouliani_island1
            )
        ),
        "goat_island" to WhatToDoItem(
            id = "goat_island",
            categoryEn = "Nature & Scenic Spots",
            categoryRo = "Natură și peisaje",
            beaches = listOf(
                "ladhario_beach",
                "develiki_beach",
                "tripiti_beach",
                "ouranoupolis_beach",
                "nea_roda_beach",
                "kakoudia_beach",
                "babylon_beach",
                "olympiada_beach",
                "milies_beach",
                "vrasna_beach",
            ),

            titleEn = "Goat Island (near Ammouliani)",
            titleRo = "Insula Caprelor (lângă Ammouliani)",
            address = "Off the coast of Ammouliani, Drenia island group, Halkidiki 630 75, Greece",
            hoursEn = "Accessible anytime (by boat or kayak from Ammouliani)",
            hoursRo = "Accesibil oricând (cu barca sau caiacul din Ammouliani)",
            descriptionEn = "🏝️ Goat Island, part of the Drenia islet group near Ammouliani, is a small uninhabited island known for its pristine nature and turquoise waters.\n\n• 🌊 Crystal-clear turquoise water and sandy coves\n• 🚤 Accessible only by boat or kayak from Ammouliani\n• 🐐 Named after the goats that once freely roamed the island\n• 🐠 Ideal for swimming and snorkeling in calm waters\n• 🧺 Perfect spot for quiet picnics in nature\n• 🌿 Secluded and untouched landscape with a peaceful atmosphere\n\n⭐ A hidden gem of the Ammouliani area, ideal for visitors seeking tranquility, natural beauty, and off-the-beaten-path exploration.",
            descriptionRo = "🏝️ Insula Caprelor, parte a grupului de insulițe Drenia de lângă Ammouliani, este o mică insulă nelocuită, renumită pentru natura sa neatinsă și apele turcoaz.\n\n• 🌊 Ape limpezi de culoare turcoaz și golfuri cu nisip\n• 🚤 Accesibilă doar cu barca sau caiacul din Ammouliani\n• 🐐 Denumită după caprele care cutreierau odinioară insula\n• 🐠 Ideală pentru înot și snorkeling în ape liniștite\n• 🧺 Loc perfect pentru picnicuri în mijlocul naturii\n• 🌿 Peisaj retras, aproape neatins, cu atmosferă liniștită\n\n⭐ O adevărată comoară ascunsă a zonei Ammouliani, ideală pentru cei care caută liniște, frumusețe naturală și explorare autentică.",
            images = listOf(
                R.drawable.what_goat_island,
                R.drawable.what_goat_island1
            )
        ),
        "akanthos_archaeological_site" to WhatToDoItem(
            id = "akanthos_archaeological_site",
            categoryEn = "History & Landmarks",
            categoryRo = "Istorie și obiective",
            beaches = listOf(
                "paralia_pirgos",
                "xiropotamos_beach",
                "paralia_ouranoupoli",
                "komitsa_beach",
                "ierissos_beach",
                "stratoni_beach",
                "proti_ammoudia_beach",
                "paralia_stavros",
                "platani_beach",
                "nea_vrasna_beach",
            ),

            titleEn = "Archaeological Site of Akanthos",
            titleRo = "Sit Arheologic Akanthos",
            address = "Near Ierissos, Halkidiki 630 75, Greece",
            hoursEn = "Open-air archaeological site (accessible anytime, best during daylight)",
            hoursRo = "Sit arheologic în aer liber (accesibil oricând, recomandat pe timp de zi)",
            descriptionEn = "🏛️ The Archaeological Site of Akanthos, located near Ierissos, preserves the remains of one of the most important ancient cities of Halkidiki, founded in the 7th century BC by colonists from Andros.\n\n• 🏺 Founded in the 7th century BC by settlers from Andros\n• 🧱 Remains of fortification walls, acropolis sections, and ancient houses\n• ⚰️ Ancient cemeteries (necropolises) discovered on site\n• 🪙 Thousands of inscriptions and coins uncovered during excavations\n• ⚓ Major center of trade and political influence in antiquity\n• 🌊 Panoramic views over the Aegean Sea\n\n⭐ A fascinating open-air site where history, archaeology, and sea views come together, offering insight into ancient life in Halkidiki.",
            descriptionRo = "🏛️ Situl Arheologic Akanthos, situat lângă Ierissos, păstrează ruinele unuia dintre cele mai importante orașe antice din Halkidiki, fondat în secolul al VII-lea î.Hr. de coloniști din Andros.\n\n• 🏺 Fondat în secolul al VII-lea î.Hr. de coloniști din Andros\n• 🧱 Ziduri de fortificație, părți din acropolă și locuințe antice\n• ⚰️ Necropole descoperite în urma săpăturilor arheologice\n• 🪙 Mii de inscripții și monede antice\n• ⚓ Centru important de comerț și influență politică în Antichitate\n• 🌊 Priveliști panoramice asupra Mării Egee\n\n⭐ Un sit arheologic impresionant, unde istoria se îmbină perfect cu peisajele spectaculoase ale Halkidiki.",
            images = listOf(
                R.drawable.what_akanthos,
                R.drawable.what_akanthos1
            )
        ),
        "stageira_archaeological_site" to WhatToDoItem(
            id = "stageira_archaeological_site",
            categoryEn = "History & Landmarks",
            categoryRo = "Istorie și obiective",
            beaches = listOf(
                "paralia_pirgos",
                "xiropotamos_beach",
                "paralia_ouranoupoli",
                "komitsa_beach",
                "ierissos_beach",
                "stratoni_beach",
                "proti_ammoudia_beach",
                "paralia_stavros",
                "platani_beach",
                "nea_vrasna_beach",
            ),

            titleEn = "Archaeological Site of Stageira",
            titleRo = "Sit Arheologic Stageira",
            address = "Olympiada, Halkidiki 630 75, Greece",
            hoursEn = "Open daily 08:00–20:00 (summer); reduced hours in winter",
            hoursRo = "Deschis zilnic 08:00–20:00 (vara); program redus iarna",
            phone = "+30 23760 22245",
            descriptionEn = "🏛️ The Archaeological Site of Stageira, located near Olympiada, is the birthplace of the great philosopher Aristotle and one of the most important ancient cities of Halkidiki.\n\n• 🏺 Founded in the 7th century BC by colonists from Andros and Chalkis\n• 🧠 Birthplace of Aristotle, one of the greatest philosophers in history\n• 🧱 Remains of fortification walls, towers, public buildings, and houses\n• 🌊 Set on a peninsula with stunning views over the Aegean Sea\n• 🚶 Ideal for walking while combining history and nature\n\n⭐ A remarkable archaeological site where ancient history, philosophy, and breathtaking coastal scenery come together.",
            descriptionRo = "🏛️ Situl Arheologic Stageira, situat lângă Olympiada, este locul de naștere al marelui filosof Aristotel și unul dintre cele mai importante orașe antice din Halkidiki.\n\n• 🏺 Fondat în secolul al VII-lea î.Hr. de coloniști din Andros și Chalkis\n• 🧠 Locul de naștere al lui Aristotel, unul dintre cei mai mari filosofi ai lumii\n• 🧱 Ziduri de fortificație, turnuri, clădiri publice și locuințe antice\n• 🌊 Așezat pe o peninsulă cu priveliști spectaculoase asupra Mării Egee\n• 🚶 Perfect pentru plimbări ce îmbină istoria cu natura\n\n⭐ Un sit arheologic impresionant, unde patrimoniul istoric se împletește armonios cu frumusețea naturală a litoralului.",
            images = listOf(
                R.drawable.what_stageira,
                R.drawable.what_stageira1
            )
        ),
        "aristotle_tomb" to WhatToDoItem(
            id = "aristotle_tomb",
            categoryEn = "History & Landmarks",
            categoryRo = "Istorie și obiective",
            beaches = listOf(
                "paralia_pirgos",
                "xiropotamos_beach",
                "paralia_ouranoupoli",
                "komitsa_beach",
                "ierissos_beach",
                "stratoni_beach",
                "proti_ammoudia_beach",
                "paralia_stavros",
                "platani_beach",
                "nea_vrasna_beach",
            ),

            titleEn = "Tomb of Aristotle",
            titleRo = "Mormântul lui Aristotel",
            address = "Άκανθος, Stagira 570 14, Grecia",
            hoursEn = "Open-air archaeological site (accessible anytime, best during daylight)",
            hoursRo = "Sit arheologic în aer liber (accesibil oricând, recomandat pe timp de zi)",
            descriptionEn = "🏛️ The Tomb of Aristotle, discovered in 1996 near Stageira in Olympiada, is believed to mark the burial place of the renowned philosopher and stands as a powerful symbol of his legacy.\n\n• 🧠 Associated with Aristotle, one of the greatest philosophers in history\n• 🏺 Discovered in 1996 near ancient Stageira\n• 🔘 Remains of a circular structure with an altar\n• 🌊 Panoramic views over the bay, matching ancient historical descriptions\n• 📜 Considered a symbolic monument despite ongoing scholarly debate\n\n⭐ A meaningful cultural landmark that honors Aristotle’s enduring influence and connects visitors with the philosophical heritage of Halkidiki.",
            descriptionRo = "🏛️ Mormântul lui Aristotel, descoperit în 1996 lângă Stageira, în Olympiada, este considerat locul de înmormântare al renumitului filosof și un simbol puternic al moștenirii sale.\n\n• 🧠 Asociat cu Aristotel, unul dintre cei mai mari filosofi ai istoriei\n• 🏺 Descoperit în 1996, în apropierea vechii Stageira\n• 🔘 Rămășițele unei structuri circulare cu altar\n• 🌊 Priveliști panoramice asupra golfului, conforme descrierilor istorice antice\n• 📜 Considerat un monument simbolic, în ciuda dezbaterilor academice\n\n⭐ Un reper cultural deosebit, care onorează influența durabilă a lui Aristotel și leagă vizitatorii de patrimoniul filosofic al Halkidiki.",
            images = listOf(
                R.drawable.what_aristotle_tomb,
                R.drawable.what_aristotle_tomb1
            )
        ),
        // TODO: adaugă aici toate celelalte activități o singură dată
    )

        // ===== 2) MAPARE — doar liste de ID-uri pe plajă =====
        private val beachRefs: Map<String, List<String>> = mapOf(
    // Nea Krini Beach
    "nea_krini_beach" to listOf(
    "magic_park",
    "tenpin_bowling",
    "white_tower",
    "mediterranean_cosmos",
    "war_museum_thessaloniki",
    "drivepark",
    "nea_kallikrateia_tuesday_market"
    ),
    // Perea Beach
    "perea_beach" to listOf(
    "waterbus_karavakia",
    "waterland_thermi",
    "noesis_science_center",
    "gerovassiliou_winery_agia_triada",
    "petralona_cave_exploration",
    "lakkoma_thursday_market"
    ),
    // Neoi Epivates Beach
    "neoi_epivates_beach" to listOf(
    "waterbus_karavakia",
    "waterland_thermi",
    "gerovassiliou_winery_agia_triada",
    "petralona_cave_exploration",
    "lakkoma_thursday_market"
    ),
    // Agia Triada Beach
    "agia_triada_beach" to listOf(
    "shipwreck_kyra_panagia",
    "epanomi_seaside_park",
    "epanomi_beacon",
    "farm_partali",
    "lighthouse_angelochori",
    "salt_lake_aggelohori",
    "nea_michaniona_fish_market"
    ),
    // Hidden Beach
    "hidden_beach" to listOf(
    "fisheries_museum_moudania",
    "shipwreck_kyra_panagia",
    "epanomi_seaside_park",
    "epanomi_beacon",
    "nea_michaniona_fish_market"
    ),
    // Surfer Beach ANGELOCHORI
    "surfer_beach_angelochori" to listOf(
    "magic_park",
    "mediterranean_cosmos",
    "horse_club",
    "tsantali_winery",
    "nea_michaniona_fish_market"
    ),
    // Tourmpali Beach
    "tourmpali_beach" to listOf(
    "petralona_cave_exploration",
    "shipwreck_kyra_panagia",
    "epanomi_seaside_park",
    "epanomi_beacon",
    "lakkoma_thursday_market"
    ),
    // Riviera Virgin Beach
    "riviera_virgin_beach" to listOf(
    "magic_park",
    "mediterranean_cosmos",
    "horse_club",
    "tsantali_winery",
    "nea_michaniona_fish_market"
    ),
    // Nea Michaniona Beach
    "nea_michaniona_beach" to listOf(
    "petralona_cave_exploration",
    "shipwreck_kyra_panagia",
    "epanomi_seaside_park",
    "epanomi_beacon",
    "nea_michaniona_fish_market"
    ),
    // Oasis Beach
    "oasis_beach" to listOf(
    "magic_park",
    "mediterranean_cosmos",
    "horse_club",
    "tsantali_winery",
    "nea_michaniona_fish_market"
    ),
    // AGISTRI BEACH
    "agistri_beach" to listOf(
    "petralona_cave_exploration",
    "shipwreck_kyra_panagia",
    "epanomi_seaside_park",
    "epanomi_beacon",
    "lakkoma_thursday_market"
    ),
    // Sand Dunes Beach
    "sand_dunes_beach" to listOf(
    "magic_park",
    "mediterranean_cosmos",
    "horse_club",
    "tsantali_winery",
    "nea_michaniona_fish_market"
    ),
    // Paralia Potami
    "paralia_potami" to listOf(
    "petralona_cave_exploration",
    "shipwreck_kyra_panagia",
    "epanomi_seaside_park",
    "epanomi_beacon",
    "nea_michaniona_fish_market"
    ),
    // Nea Iraklia Beach
    "nea_iraklia_beach" to listOf(
    "magic_park",
    "mediterranean_cosmos",
    "horse_club",
    "tsantali_winery",
    "nea_michaniona_fish_market"
    ),
    // Sahara Beach
    "sahara_beach" to listOf(
    "petralona_cave_exploration",
    "shipwreck_kyra_panagia",
    "epanomi_seaside_park",
    "epanomi_beacon",
    "lakkoma_thursday_market"
    ),
    // Vergia Beach
    "vergia_beach" to listOf(
    "magic_park",
    "mediterranean_cosmos",
    "horse_club",
    "tsantali_winery",
    "nea_michaniona_fish_market"
    ),
    // Delfinia Beach
    "delfinia_beach" to listOf(
    "petralona_cave_exploration",
    "shipwreck_kyra_panagia",
    "epanomi_seaside_park",
    "epanomi_beacon",
    "nea_michaniona_fish_market"
    ),
    // Sozopoli Beach
    "sozopoli_beach" to listOf(
    "magic_park",
    "mediterranean_cosmos",
    "horse_club",
    "tsantali_winery",
    "nea_michaniona_fish_market"
    ),
    // Paralia Iraklia
    "paralia_iraklia" to listOf(
    "petralona_cave_exploration",
    "shipwreck_kyra_panagia",
    "epanomi_seaside_park",
    "epanomi_beacon",
    "lakkoma_thursday_market"
    ),
    // Mykoniatika Secret Beach
    "mykoniatika_secret_beach" to listOf(
    "magic_park",
    "mediterranean_cosmos",
    "horse_club",
    "tsantali_winery",
    "nea_michaniona_fish_market"
    ),
    // Beach Mykoniatika
    "beach_mykoniatika" to listOf(
    "petralona_cave_exploration",
    "shipwreck_kyra_panagia",
    "epanomi_seaside_park",
    "epanomi_beacon",
    "nea_michaniona_fish_market"
    ),
    // Ntouraki Beach
    "ntouraki_beach" to listOf(
    "magic_park",
    "mediterranean_cosmos",
    "horse_club",
    "tsantali_winery",
    "nea_michaniona_fish_market"
    ),
    // Nea Plagia Beach
    "nea_plagia_beach" to listOf(
    "petralona_cave_exploration",
    "shipwreck_kyra_panagia",
    "epanomi_seaside_park",
    "epanomi_beacon",
    "lakkoma_thursday_market"
    ),
    // Flogita Beach
    "flogita_beach" to listOf(
    "magic_park",
    "mediterranean_cosmos",
    "horse_club",
    "tsantali_winery",
    "nea_michaniona_fish_market"
    ),
    // Dionisiou Beach
    "dionisiou_beach" to listOf(
    "petralona_cave_exploration",
    "shipwreck_kyra_panagia",
    "epanomi_seaside_park",
    "epanomi_beacon",
    "nea_michaniona_fish_market"
    ),
    // Nea Moudania Beach
    "nea_moudania_beach" to listOf(
    "byzantine_museum_chalkidiki",
    "fisheries_museum_moudania",
    "block518_paintball",
    "agios_mamas_wetland",
    "lakkoma_thursday_market"
    ),
    // Paralia Nea Moudania
    "paralia_nea_moudania" to listOf(
    "archaeological_area_potidea",
    "magic_bloom_waterpark_potidea",
    "sani_wetlands",
    "stavronikita_tower",
    "lakkoma_thursday_market"
    ),
    // Gremia
    "gremia" to listOf(
    "byzantine_museum_chalkidiki",
    "fisheries_museum_moudania",
    "block518_paintball",
    "agios_mamas_wetland",
    "lakkoma_thursday_market"
    ),
    // Paralia Nea Potidea
    "paralia_nea_potidea" to listOf(
    "archaeological_area_potidea",
    "magic_bloom_waterpark_potidea",
    "sani_wetlands",
    "stavronikita_tower",
    "nea_kallikrateia_tuesday_market"
    ),
    // Windsurfers Paradise
    "windsurfers_paradise" to listOf(
    "byzantine_museum_chalkidiki",
    "fisheries_museum_moudania",
    "block518_paintball",
    "agios_mamas_wetland",
    "lakkoma_thursday_market"
    ),
    // Stavronikita Beach
    "stavronikita_beach" to listOf(
    "archaeological_area_potidea",
    "magic_bloom_waterpark_potidea",
    "sani_wetlands",
    "stavronikita_tower",
    "lakkoma_thursday_market"
    ),
    // Sani Beach
    "sani_beach" to listOf(
    "byzantine_museum_chalkidiki",
    "fisheries_museum_moudania",
    "block518_paintball",
    "agios_mamas_wetland",
    "lakkoma_thursday_market"
    ),
    // Paralia Sani
    "paralia_sani" to listOf(
    "archaeological_area_potidea",
    "magic_bloom_waterpark_potidea",
    "sani_wetlands",
    "stavronikita_tower",
    "nea_kallikrateia_tuesday_market"
    ),
    // Simantro Beach
    "simantro_beach" to listOf(
    "byzantine_museum_chalkidiki",
    "fisheries_museum_moudania",
    "block518_paintball",
    "agios_mamas_wetland",
    "lakkoma_thursday_market"
    ),
    // Paralia Kipsa
    "paralia_kipsa" to listOf(
    "archaeological_area_potidea",
    "magic_bloom_waterpark_potidea",
    "sani_wetlands",
    "stavronikita_tower",
    "lakkoma_thursday_market"
    ),
    // Chelona Beach
    "chelona_beach" to listOf(
    "byzantine_museum_chalkidiki",
    "fisheries_museum_moudania",
    "block518_paintball",
    "agios_mamas_wetland",
    "lakkoma_thursday_market"
    ),
    // Elani Beach
    "elani_beach" to listOf(
    "archaeological_area_potidea",
    "magic_bloom_waterpark_potidea",
    "sani_wetlands",
    "stavronikita_tower",
    "nea_kallikrateia_tuesday_market"
    ),
    // Siviri Beach
    "siviri_beach" to listOf(
    "byzantine_museum_chalkidiki",
    "fisheries_museum_moudania",
    "block518_paintball",
    "agios_mamas_wetland",
    "lakkoma_thursday_market"
    ),
    // Agios Nikolaos Beach
    "agios_nikolaos_beach" to listOf(
    "archaeological_area_potidea",
    "magic_bloom_waterpark_potidea",
    "sani_wetlands",
    "stavronikita_tower",
    "lakkoma_thursday_market"
    ),
    // Agios Nikolaos Fourka
    "agios_nikolaos_fourka" to listOf(
    "byzantine_museum_chalkidiki",
    "fisheries_museum_moudania",
    "block518_paintball",
    "agios_mamas_wetland",
    "lakkoma_thursday_market"
    ),
    // Skala Fourkas Beach
    "skala_fourkas_beach" to listOf(
    "archaeological_area_potidea",
    "magic_bloom_waterpark_potidea",
    "sani_wetlands",
    "stavronikita_tower",
    "nea_kallikrateia_tuesday_market"
    ),
    // Aigaiopelagitika Beach
    "aigaiopelagitika_beach" to listOf(
    "byzantine_museum_chalkidiki",
    "fisheries_museum_moudania",
    "block518_paintball",
    "agios_mamas_wetland",
    "lakkoma_thursday_market"
    ),
    // Possidi West Beach
    "possidi_west_beach" to listOf(
    "archaeological_area_potidea",
    "magic_bloom_waterpark_potidea",
    "sani_wetlands",
    "stavronikita_tower",
    "lakkoma_thursday_market"
    ),
    // Possidi Beach
    "possidi_beach" to listOf(
    "byzantine_museum_chalkidiki",
    "fisheries_museum_moudania",
    "block518_paintball",
    "agios_mamas_wetland",
    "lakkoma_thursday_market"
    ),
    // Paralia Posidi
    "paralia_posidi" to listOf(
    "archaeological_area_potidea",
    "magic_bloom_waterpark_potidea",
    "sani_wetlands",
    "stavronikita_tower",
    "nea_kallikrateia_tuesday_market"
    ),

            // Mola Kaliva Beach
            "mola_kaliva_beach" to listOf(
                "byzantine_museum_chalkidiki",
                "fisheries_museum_moudania",
                "block518_paintball",
                "agios_mamas_wetland",
                "lakkoma_thursday_market"
            ),
            // Paralia Anemi
            "paralia_anemi" to listOf(
                "archaeological_area_potidea",
                "magic_bloom_waterpark_potidea",
                "sani_wetlands",
                "stavronikita_tower",
                "lakkoma_thursday_market"
            ),
            // Paralia Skioni
            "paralia_skioni" to listOf(
                "byzantine_museum_chalkidiki",
                "fisheries_museum_moudania",
                "block518_paintball",
                "agios_mamas_wetland",
                "lakkoma_thursday_market"
            ),
            // Nea Skioni Beach
            "nea_skioni_beach" to listOf(
                "archaeological_area_potidea",
                "magic_bloom_waterpark_potidea",
                "sani_wetlands",
                "stavronikita_tower",
                "nea_kallikrateia_tuesday_market"
            ),
            // The Beach
            "the_beach" to listOf(
                "byzantine_museum_chalkidiki",
                "fisheries_museum_moudania",
                "block518_paintball",
                "agios_mamas_wetland",
                "lakkoma_thursday_market"
            ),
            // Paralia Agias Paraskevis
            "paralia_agias_paraskevis" to listOf(
                "archaeological_area_potidea",
                "magic_bloom_waterpark_potidea",
                "sani_wetlands",
                "stavronikita_tower",
                "lakkoma_thursday_market"
            ),
            // Loutra Agias Paraskevis Beach
            "loutra_agias_paraskevis_beach" to listOf(
                "byzantine_museum_chalkidiki",
                "fisheries_museum_moudania",
                "block518_paintball",
                "agios_mamas_wetland",
                "lakkoma_thursday_market"
            ),
            // Loutra Beach
            "loutra_beach" to listOf(
                "archaeological_area_potidea",
                "magic_bloom_waterpark_potidea",
                "sani_wetlands",
                "stavronikita_tower",
                "nea_kallikrateia_tuesday_market"
            ),
            // Pepples Beach of St George
            "pepples_beach_of_st_george" to listOf(
                "byzantine_museum_chalkidiki",
                "fisheries_museum_moudania",
                "block518_paintball",
                "agios_mamas_wetland",
                "lakkoma_thursday_market"
            ),
            // Ani Beach
            "ani_beach" to listOf(
                "archaeological_area_potidea",
                "magic_bloom_waterpark_potidea",
                "sani_wetlands",
                "stavronikita_tower",
                "lakkoma_thursday_market"
            ),
            // Dymitry Beach
            "dymitry_beach" to listOf(
                "byzantine_museum_chalkidiki",
                "fisheries_museum_moudania",
                "block518_paintball",
                "agios_mamas_wetland",
                "lakkoma_thursday_market"
            ),
            // Kanastraio or Kalogria Cape
            "kanastraio_or_kalogria_cape" to listOf(
                "archaeological_area_potidea",
                "magic_bloom_waterpark_potidea",
                "sani_wetlands",
                "stavronikita_tower",
                "nea_kallikrateia_tuesday_market"
            ),
            // Cape Sevas
            "cape_sevas" to listOf(
                "byzantine_museum_chalkidiki",
                "fisheries_museum_moudania",
                "block518_paintball",
                "agios_mamas_wetland",
                "lakkoma_thursday_market"
            ),
            // Cliff Rocks
            "cliff_rocks" to listOf(
                "archaeological_area_potidea",
                "magic_bloom_waterpark_potidea",
                "sani_wetlands",
                "stavronikita_tower",
                "lakkoma_thursday_market"
            ),
            // Agios Nikolaos Kanistro Beach
            "agios_nikolaos_kanistro_beach" to listOf(
                "byzantine_museum_chalkidiki",
                "fisheries_museum_moudania",
                "block518_paintball",
                "agios_mamas_wetland",
                "lakkoma_thursday_market"
            ),
            // Kanistro Beach
            "kanistro_beach" to listOf(
                "archaeological_area_potidea",
                "magic_bloom_waterpark_potidea",
                "sani_wetlands",
                "stavronikita_tower",
                "nea_kallikrateia_tuesday_market"
            ),
            // Paralia Panagias
            "paralia_panagias" to listOf(
                "byzantine_museum_chalkidiki",
                "fisheries_museum_moudania",
                "block518_paintball",
                "agios_mamas_wetland",
                "lakkoma_thursday_market"
            ),
            // Porto Valitsa Bay
            "porto_valitsa_bay" to listOf(
                "archaeological_area_potidea",
                "magic_bloom_waterpark_potidea",
                "sani_wetlands",
                "stavronikita_tower",
                "lakkoma_thursday_market"
            ),
            // Paliouri Beach
            "paliouri_beach" to listOf(
                "byzantine_museum_chalkidiki",
                "fisheries_museum_moudania",
                "block518_paintball",
                "agios_mamas_wetland",
                "lakkoma_thursday_market"
            ),
            // Xenia Beach
            "xenia_beach" to listOf(
                "archaeological_area_potidea",
                "magic_bloom_waterpark_potidea",
                "sani_wetlands",
                "stavronikita_tower",
                "nea_kallikrateia_tuesday_market"
            ),
            // Paralia Chroussou
            "paralia_chroussou" to listOf(
                "byzantine_museum_chalkidiki",
                "fisheries_museum_moudania",
                "block518_paintball",
                "agios_mamas_wetland",
                "lakkoma_thursday_market"
            ),
            // Golden Beach
            "golden_beach" to listOf(
                "archaeological_area_potidea",
                "magic_bloom_waterpark_potidea",
                "sani_wetlands",
                "stavronikita_tower",
                "lakkoma_thursday_market"
            ),
            // Alonaki Beach
            "alonaki_beach" to listOf(
                "byzantine_museum_chalkidiki",
                "fisheries_museum_moudania",
                "block518_paintball",
                "agios_mamas_wetland",
                "lakkoma_thursday_market"
            ),
            // Glarokavos Beach
            "glarokavos_beach" to listOf(
                "archaeological_area_potidea",
                "magic_bloom_waterpark_potidea",
                "sani_wetlands",
                "stavronikita_tower",
                "nea_kallikrateia_tuesday_market"
            ),
            // Lagoon Beach
            "lagoon_beach" to listOf(
                "byzantine_museum_chalkidiki",
                "fisheries_museum_moudania",
                "block518_paintball",
                "agios_mamas_wetland",
                "lakkoma_thursday_market"
            ),
            // Paralia Pefkochori
            "paralia_pefkochori" to listOf(
                "archaeological_area_potidea",
                "magic_bloom_waterpark_potidea",
                "sani_wetlands",
                "stavronikita_tower",
                "lakkoma_thursday_market"
            ),
            // Pefkochori Beach
            "pefkochori_beach" to listOf(
                "byzantine_museum_chalkidiki",
                "fisheries_museum_moudania",
                "block518_paintball",
                "agios_mamas_wetland",
                "lakkoma_thursday_market"
            ),
            // Hanioti Beach
            "hanioti_beach" to listOf(
                "archaeological_area_potidea",
                "magic_bloom_waterpark_potidea",
                "sani_wetlands",
                "stavronikita_tower",
                "nea_kallikrateia_tuesday_market"
            ),
            // Polychrono Beach
            "polychrono_beach" to listOf(
                "byzantine_museum_chalkidiki",
                "fisheries_museum_moudania",
                "block518_paintball",
                "agios_mamas_wetland",
                "lakkoma_thursday_market"
            ),
            // Kryopigi Beach
            "kryopigi_beach" to listOf(
                "archaeological_area_potidea",
                "magic_bloom_waterpark_potidea",
                "sani_wetlands",
                "stavronikita_tower",
                "lakkoma_thursday_market"
            ),
            // Kalithea Beach
            "kalithea_beach" to listOf(
                "byzantine_museum_chalkidiki",
                "fisheries_museum_moudania",
                "block518_paintball",
                "agios_mamas_wetland",
                "lakkoma_thursday_market"
            ),
            // Paralia Afitos
            "paralia_afitos" to listOf(
                "archaeological_area_potidea",
                "magic_bloom_waterpark_potidea",
                "sani_wetlands",
                "stavronikita_tower",
                "nea_kallikrateia_tuesday_market"
            ),
            // Plage Liosi
            "plage_liosi" to listOf(
                "byzantine_museum_chalkidiki",
                "fisheries_museum_moudania",
                "block518_paintball",
                "agios_mamas_wetland",
                "lakkoma_thursday_market"
            ),
            // Plage Moudounou
            "plage_moudounou" to listOf(
                "archaeological_area_potidea",
                "magic_bloom_waterpark_potidea",
                "sani_wetlands",
                "stavronikita_tower",
                "lakkoma_thursday_market"
            ),
            // Athytos Beach
            "athytos_beach" to listOf(
                "byzantine_museum_chalkidiki",
                "fisheries_museum_moudania",
                "block518_paintball",
                "agios_mamas_wetland",
                "lakkoma_thursday_market"
            ),
            // Varkes Beach
            "varkes_beach" to listOf(
                "archaeological_area_potidea",
                "magic_bloom_waterpark_potidea",
                "sani_wetlands",
                "stavronikita_tower",
                "nea_kallikrateia_tuesday_market"
            ),
            // Plage Vothonas
            "plage_vothonas" to listOf(
                "byzantine_museum_chalkidiki",
                "fisheries_museum_moudania",
                "block518_paintball",
                "agios_mamas_wetland",
                "lakkoma_thursday_market"
            ),
            // Place de Ninna
            "place_de_ninna" to listOf(
                "archaeological_area_potidea",
                "magic_bloom_waterpark_potidea",
                "sani_wetlands",
                "stavronikita_tower",
                "lakkoma_thursday_market"
            ),
            // Savatianos Beach
            "savatianos_beach" to listOf(
                "byzantine_museum_chalkidiki",
                "fisheries_museum_moudania",
                "block518_paintball",
                "agios_mamas_wetland",
                "lakkoma_thursday_market"
            ),
            // Nea Fokea Beach
            "nea_fokea_beach" to listOf(
                "archaeological_area_potidea",
                "magic_bloom_waterpark_potidea",
                "sani_wetlands",
                "stavronikita_tower",
                "nea_kallikrateia_tuesday_market"
            ),
            // Wild Sandy Beach
            "wild_sandy_beach" to listOf(
                "byzantine_museum_chalkidiki",
                "fisheries_museum_moudania",
                "block518_paintball",
                "agios_mamas_wetland",
                "lakkoma_thursday_market"
            ),
            // Nea Potidea Beach
            "nea_potidea_beach" to listOf(
                "archaeological_area_potidea",
                "magic_bloom_waterpark_potidea",
                "sani_wetlands",
                "stavronikita_tower",
                "lakkoma_thursday_market"
            ),
            // Agios Mamas Beach
            "agios_mamas_beach" to listOf(
                "byzantine_museum_chalkidiki",
                "fisheries_museum_moudania",
                "block518_paintball",
                "agios_mamas_wetland",
                "lakkoma_thursday_market"
            ),
            // Paralia Kalivia
            "paralia_kalivia" to listOf(
                "archaeological_area_potidea",
                "magic_bloom_waterpark_potidea",
                "sani_wetlands",
                "stavronikita_tower",
                "nea_kallikrateia_tuesday_market"
            ),
            // Kalyves Beach
            "kalyves_beach" to listOf(
                "byzantine_museum_chalkidiki",
                "fisheries_museum_moudania",
                "block518_paintball",
                "agios_mamas_wetland",
                "lakkoma_thursday_market"
            ),
            // Mikiverna Beach
            "mikiverna_beach" to listOf(
                "archaeological_area_potidea",
                "magic_bloom_waterpark_potidea",
                "sani_wetlands",
                "stavronikita_tower",
                "lakkoma_thursday_market"
            ),
            // Gerakini Beach
            "gerakini_beach" to listOf(
                "byzantine_museum_chalkidiki",
                "fisheries_museum_moudania",
                "block518_paintball",
                "agios_mamas_wetland",
                "lakkoma_thursday_market"
            ),
            // Paralia Psakoudia
            "paralia_psakoudia" to listOf(
                "kladi_olive_oil",
                "sophronios_basilica",
                "aquata_waterpark",
                "psalida_tower",
                "simantra_friday_market"
            ),
            // Psakoudia Beach
            "psakoudia_beach" to listOf(
                "nikiti_old_settlement",
                "panoramic_rest_point",
                "neos_marmaras_village",
                "toroni_archaeological_site",
                "simantra_friday_market"
            ),
            // Paralia Sargani
            "paralia_sargani" to listOf(
                "kladi_olive_oil",
                "sophronios_basilica",
                "aquata_waterpark",
                "psalida_tower",
                "simantra_friday_market"
            ),
            // Metamorfossi Beach
            "metamorfossi_beach" to listOf(
                "nikiti_old_settlement",
                "panoramic_rest_point",
                "neos_marmaras_village",
                "toroni_archaeological_site",
                "ormylia_monday_market"
            ),
            // Paralia Askamnia
            "paralia_askamnia" to listOf(
                "kladi_olive_oil",
                "sophronios_basilica",
                "aquata_waterpark",
                "psalida_tower",
                "simantra_friday_market"
            ),
            // Red Rocks Of Metamorphosis
            "red_rocks_of_metamorphosis" to listOf(
                "nikiti_old_settlement",
                "panoramic_rest_point",
                "neos_marmaras_village",
                "toroni_archaeological_site",
                "simantra_friday_market"
            ),
            // Nikiti Beach
            "nikiti_beach" to listOf(
                "kladi_olive_oil",
                "sophronios_basilica",
                "aquata_waterpark",
                "psalida_tower",
                "simantra_friday_market"
            ),
            // Paralia Kastri
            "paralia_kastri" to listOf(
                "nikiti_old_settlement",
                "panoramic_rest_point",
                "neos_marmaras_village",
                "toroni_archaeological_site",
                "ormylia_monday_market"
            ),
            // Kastri Beach
            "kastri_beach" to listOf(
                "kladi_olive_oil",
                "sophronios_basilica",
                "aquata_waterpark",
                "psalida_tower",
                "simantra_friday_market"
            ),
            // Agios Ioannis Beach
            "agios_ioannis_beach" to listOf(
                "nikiti_old_settlement",
                "panoramic_rest_point",
                "neos_marmaras_village",
                "toroni_archaeological_site",
                "simantra_friday_market"
            ),
            // Koviou Beach
            "koviou_beach" to listOf(
                "kladi_olive_oil",
                "sophronios_basilica",
                "aquata_waterpark",
                "psalida_tower",
                "simantra_friday_market"
            ),
            // Isla Beach
            "isla_beach" to listOf(
                "nikiti_old_settlement",
                "panoramic_rest_point",
                "neos_marmaras_village",
                "toroni_archaeological_site",
                "ormylia_monday_market"
            ),
            // Kalogria Beach
            "kalogria_beach" to listOf(
                "kladi_olive_oil",
                "sophronios_basilica",
                "aquata_waterpark",
                "psalida_tower",
                "simantra_friday_market"
            ),
            // Small Spathies Beach
            "small_spathies_beach" to listOf(
                "nikiti_old_settlement",
                "panoramic_rest_point",
                "neos_marmaras_village",
                "toroni_archaeological_site",
                "simantra_friday_market"
            ),
            // Spathies Beach
            "spathies_beach" to listOf(
                "kladi_olive_oil",
                "sophronios_basilica",
                "aquata_waterpark",
                "psalida_tower",
                "simantra_friday_market"
            ),
            // Paralia Elia
            "paralia_elia" to listOf(
                "nikiti_old_settlement",
                "panoramic_rest_point",
                "neos_marmaras_village",
                "toroni_archaeological_site",
                "ormylia_monday_market"
            ),
            // Paralia Perigiali
            "paralia_perigiali" to listOf(
                "kladi_olive_oil",
                "sophronios_basilica",
                "aquata_waterpark",
                "psalida_tower",
                "simantra_friday_market"
            ),
            // Elia Beach
            "elia_beach" to listOf(
                "nikiti_old_settlement",
                "panoramic_rest_point",
                "neos_marmaras_village",
                "toroni_archaeological_site",
                "simantra_friday_market"
            ),
            // Lagomandra Beach
            "lagomandra_beach" to listOf(
                "kladi_olive_oil",
                "sophronios_basilica",
                "aquata_waterpark",
                "psalida_tower",
                "simantra_friday_market"
            ),
            // Great Lagomanda Coast
            "great_lagomanda_coast" to listOf(
                "nikiti_old_settlement",
                "panoramic_rest_point",
                "neos_marmaras_village",
                "toroni_archaeological_site",
                "ormylia_monday_market"
            ),
            // Nikitis Beach Sithonia
            "nikitis_beach_sithonia" to listOf(
                "kladi_olive_oil",
                "sophronios_basilica",
                "aquata_waterpark",
                "psalida_tower",
                "simantra_friday_market"
            ),

            // Tripotamos Beach
            "tripotamos_beach" to listOf(
                "nikiti_old_settlement",
                "panoramic_rest_point",
                "neos_marmaras_village",
                "toroni_archaeological_site",
                "simantra_friday_market"
            ),
            // Paradisos Beach
            "paradisos_beach" to listOf(
                "kladi_olive_oil",
                "sophronios_basilica",
                "aquata_waterpark",
                "psalida_tower",
                "simantra_friday_market"
            ),
            // Peaceful Beach
            "peaceful_beach" to listOf(
                "nikiti_old_settlement",
                "panoramic_rest_point",
                "neos_marmaras_village",
                "toroni_archaeological_site",
                "ormylia_monday_market"
            ),
            // Neos Marmaras Beach
            "neos_marmaras_beach" to listOf(
                "kladi_olive_oil",
                "sophronios_basilica",
                "aquata_waterpark",
                "psalida_tower",
                "simantra_friday_market"
            ),
            // Porto Carras Beach
            "porto_carras_beach" to listOf(
                "nikiti_old_settlement",
                "panoramic_rest_point",
                "neos_marmaras_village",
                "toroni_archaeological_site",
                "simantra_friday_market"
            ),
            // Kohi Beach
            "kohi_beach" to listOf(
                "kladi_olive_oil",
                "sophronios_basilica",
                "aquata_waterpark",
                "psalida_tower",
                "simantra_friday_market"
            ),
            // Koutsoupia Beach
            "koutsoupia_beach" to listOf(
                "nikiti_old_settlement",
                "panoramic_rest_point",
                "neos_marmaras_village",
                "toroni_archaeological_site",
                "ormylia_monday_market"
            ),
            // Diaporti Beach
            "diaporti_beach" to listOf(
                "kladi_olive_oil",
                "sophronios_basilica",
                "aquata_waterpark",
                "psalida_tower",
                "simantra_friday_market"
            ),
            // Likithos Beach
            "likithos_beach" to listOf(
                "nikiti_old_settlement",
                "panoramic_rest_point",
                "neos_marmaras_village",
                "toroni_archaeological_site",
                "simantra_friday_market"
            ),
            // Azapiko Beach
            "azapiko_beach" to listOf(
                "kladi_olive_oil",
                "sophronios_basilica",
                "aquata_waterpark",
                "psalida_tower",
                "simantra_friday_market"
            ),
            // Foresta Sithonia
            "foresta_sithonia" to listOf(
                "nikiti_old_settlement",
                "panoramic_rest_point",
                "neos_marmaras_village",
                "toroni_archaeological_site",
                "ormylia_monday_market"
            ),
            // Paralia Alexandra-Xenia
            "paralia_alexandra_xenia" to listOf(
                "kladi_olive_oil",
                "sophronios_basilica",
                "aquata_waterpark",
                "psalida_tower",
                "simantra_friday_market"
            ),
            // Paralia Azapiko
            "paralia_azapiko" to listOf(
                "nikiti_old_settlement",
                "panoramic_rest_point",
                "neos_marmaras_village",
                "toroni_archaeological_site",
                "simantra_friday_market"
            ),
            // Paralia Xenia
            "paralia_xenia" to listOf(
                "kladi_olive_oil",
                "sophronios_basilica",
                "aquata_waterpark",
                "psalida_tower",
                "simantra_friday_market"
            ),
            // Aretes Beach
            "aretes_beach" to listOf(
                "nikiti_old_settlement",
                "panoramic_rest_point",
                "neos_marmaras_village",
                "toroni_archaeological_site",
                "ormylia_monday_market"
            ),
            // Tristinika Beach
            "tristinika_beach" to listOf(
                "kladi_olive_oil",
                "sophronios_basilica",
                "aquata_waterpark",
                "psalida_tower",
                "simantra_friday_market"
            ),
            // Destenika Beach
            "destenika_beach" to listOf(
                "nikiti_old_settlement",
                "panoramic_rest_point",
                "neos_marmaras_village",
                "toroni_archaeological_site",
                "simantra_friday_market"
            ),
            // Ema Beach
            "ema_beach" to listOf(
                "kladi_olive_oil",
                "sophronios_basilica",
                "aquata_waterpark",
                "psalida_tower",
                "simantra_friday_market"
            ),
            // Luka Beach
            "luka_beach" to listOf(
                "nikiti_old_settlement",
                "panoramic_rest_point",
                "neos_marmaras_village",
                "toroni_archaeological_site",
                "ormylia_monday_market"
            ),
            // Paralia Toroni
            "paralia_toroni" to listOf(
                "kladi_olive_oil",
                "sophronios_basilica",
                "aquata_waterpark",
                "psalida_tower",
                "simantra_friday_market"
            ),
            // Toroni Beach
            "toroni_beach" to listOf(
                "nikiti_old_settlement",
                "panoramic_rest_point",
                "neos_marmaras_village",
                "toroni_archaeological_site",
                "simantra_friday_market"
            ),
            // Porto Koufo Beach
            "porto_koufo_beach" to listOf(
                "kladi_olive_oil",
                "sophronios_basilica",
                "aquata_waterpark",
                "psalida_tower",
                "simantra_friday_market"
            ),
            // Lagoon in Porto Koufo
            "lagoon_in_porto_koufo" to listOf(
                "nikiti_old_settlement",
                "panoramic_rest_point",
                "neos_marmaras_village",
                "toroni_archaeological_site",
                "ormylia_monday_market"
            ),
            // Marathias Beach
            "marathias_beach" to listOf(
                "kladi_olive_oil",
                "sophronios_basilica",
                "aquata_waterpark",
                "psalida_tower",
                "simantra_friday_market"
            ),
            // Secret Beach
            "secret_beach" to listOf(
                "nikiti_old_settlement",
                "panoramic_rest_point",
                "neos_marmaras_village",
                "toroni_archaeological_site",
                "simantra_friday_market"
            ),
            // Sithonia Cape
            "sithonia_cape" to listOf(
                "kladi_olive_oil",
                "sophronios_basilica",
                "aquata_waterpark",
                "psalida_tower",
                "simantra_friday_market"
            ),
            // Mamba Beach
            "mamba_beach" to listOf(
                "nikiti_old_settlement",
                "panoramic_rest_point",
                "neos_marmaras_village",
                "toroni_archaeological_site",
                "ormylia_monday_market"
            ),
            // Kalamitsi Beach
            "kalamitsi_beach" to listOf(
                "kladi_olive_oil",
                "sophronios_basilica",
                "aquata_waterpark",
                "psalida_tower",
                "simantra_friday_market"
            ),
            // Kriaritsi Beach
            "kriaritsi_beach" to listOf(
                "nikiti_old_settlement",
                "panoramic_rest_point",
                "neos_marmaras_village",
                "toroni_archaeological_site",
                "simantra_friday_market"
            ),
            // Prassou Beach
            "prassou_beach" to listOf(
                "kladi_olive_oil",
                "sophronios_basilica",
                "aquata_waterpark",
                "psalida_tower",
                "simantra_friday_market"
            ),
            // Klimataria Beach
            "klimataria_beach" to listOf(
                "nikiti_old_settlement",
                "panoramic_rest_point",
                "neos_marmaras_village",
                "toroni_archaeological_site",
                "ormylia_monday_market"
            ),
            // Tourkolimnionas
            "tourkolimnionas" to listOf(
                "kladi_olive_oil",
                "sophronios_basilica",
                "aquata_waterpark",
                "psalida_tower",
                "simantra_friday_market"
            ),
            // Skala Sykias Beach
            "skala_sykias_beach" to listOf(
                "nikiti_old_settlement",
                "panoramic_rest_point",
                "neos_marmaras_village",
                "toroni_archaeological_site",
                "simantra_friday_market"
            ),
            // Linaraki Beach
            "linaraki_beach" to listOf(
                "kladi_olive_oil",
                "sophronios_basilica",
                "aquata_waterpark",
                "psalida_tower",
                "simantra_friday_market"
            ),
            // Sykias Beach
            "sykias_beach" to listOf(
                "nikiti_old_settlement",
                "panoramic_rest_point",
                "neos_marmaras_village",
                "toroni_archaeological_site",
                "ormylia_monday_market"
            ),
            // Valti Beach
            "valti_beach" to listOf(
                "kladi_olive_oil",
                "sophronios_basilica",
                "aquata_waterpark",
                "psalida_tower",
                "simantra_friday_market"
            ),
            // Agridia Beach
            "agridia_beach" to listOf(
                "nikiti_old_settlement",
                "panoramic_rest_point",
                "neos_marmaras_village",
                "toroni_archaeological_site",
                "simantra_friday_market"
            ),
            // Goa Beach
            "goa_beach" to listOf(
                "kladi_olive_oil",
                "sophronios_basilica",
                "aquata_waterpark",
                "psalida_tower",
                "simantra_friday_market"
            ),
            // Platania
            "platania" to listOf(
                "nikiti_old_settlement",
                "panoramic_rest_point",
                "neos_marmaras_village",
                "toroni_archaeological_site",
                "ormylia_monday_market"
            ),
            // Sarti Beach
            "sarti_beach" to listOf(
                "kladi_olive_oil",
                "sophronios_basilica",
                "aquata_waterpark",
                "psalida_tower",
                "simantra_friday_market"
            ),
            // Achlada
            "achlada" to listOf(
                "nikiti_old_settlement",
                "panoramic_rest_point",
                "neos_marmaras_village",
                "toroni_archaeological_site",
                "simantra_friday_market"
            ),
            // Heart-Shaped Bay
            "heart_shaped_bay" to listOf(
                "kladi_olive_oil",
                "sophronios_basilica",
                "aquata_waterpark",
                "psalida_tower",
                "simantra_friday_market"
            ),
            // Platanitsi Beach
            "platanitsi_beach" to listOf(
                "nikiti_old_settlement",
                "panoramic_rest_point",
                "neos_marmaras_village",
                "toroni_archaeological_site",
                "ormylia_monday_market"
            ),
            // Orange Beach
            "orange_beach" to listOf(
                "kladi_olive_oil",
                "sophronios_basilica",
                "aquata_waterpark",
                "psalida_tower",
                "simantra_friday_market"
            ),
            // Kavourotrypes Beach
            "kavourotrypes_beach" to listOf(
                "nikiti_old_settlement",
                "panoramic_rest_point",
                "neos_marmaras_village",
                "toroni_archaeological_site",
                "simantra_friday_market"
            ),
            // Mega Portokali Beach
            "mega_portokali_beach" to listOf(
                "kladi_olive_oil",
                "sophronios_basilica",
                "aquata_waterpark",
                "psalida_tower",
                "simantra_friday_market"
            ),
            // Paralia Armenistis
            "paralia_armenistis" to listOf(
                "nikiti_old_settlement",
                "panoramic_rest_point",
                "neos_marmaras_village",
                "toroni_archaeological_site",
                "ormylia_monday_market"
            ),
            // Dream Coast Beach
            "dream_coast_beach" to listOf(
                "kladi_olive_oil",
                "sophronios_basilica",
                "aquata_waterpark",
                "psalida_tower",
                "simantra_friday_market"
            ),
            // Robinson Beach
            "robinson_beach" to listOf(
                "nikiti_old_settlement",
                "panoramic_rest_point",
                "neos_marmaras_village",
                "toroni_archaeological_site",
                "simantra_friday_market"
            ),
            // Banana Beach
            "banana_beach" to listOf(
                "kladi_olive_oil",
                "sophronios_basilica",
                "aquata_waterpark",
                "psalida_tower",
                "simantra_friday_market"
            ),
            // Porto Paradiso
            "porto_paradiso" to listOf(
                "nikiti_old_settlement",
                "panoramic_rest_point",
                "neos_marmaras_village",
                "toroni_archaeological_site",
                "ormylia_monday_market"
            ),
            // Zografou Beach
            "zografou_beach" to listOf(
                "kladi_olive_oil",
                "sophronios_basilica",
                "aquata_waterpark",
                "psalida_tower",
                "simantra_friday_market"
            ),
            // Koutloumousi Beach
            "koutloumousi_beach" to listOf(
                "nikiti_old_settlement",
                "panoramic_rest_point",
                "neos_marmaras_village",
                "toroni_archaeological_site",
                "simantra_friday_market"
            ),
            // Bara Beach
            "bara_beach" to listOf(
                "kladi_olive_oil",
                "sophronios_basilica",
                "aquata_waterpark",
                "psalida_tower",
                "simantra_friday_market"
            ),
            // Fava Beach
            "fava_beach" to listOf(
                "nikiti_old_settlement",
                "panoramic_rest_point",
                "neos_marmaras_village",
                "toroni_archaeological_site",
                "ormylia_monday_market"
            ),
            // Manos Beach
            "manos_beach" to listOf(
                "kladi_olive_oil",
                "sophronios_basilica",
                "aquata_waterpark",
                "psalida_tower",
                "simantra_friday_market"
            ),
            // Karydi Beach
            "karydi_beach" to listOf(
                "nikiti_old_settlement",
                "panoramic_rest_point",
                "neos_marmaras_village",
                "toroni_archaeological_site",
                "simantra_friday_market"
            ),
            // Rocks on the Beach
            "rocks_on_the_beach" to listOf(
                "kladi_olive_oil",
                "sophronios_basilica",
                "aquata_waterpark",
                "psalida_tower",
                "simantra_friday_market"
            ),
            // Livari Beach
            "livari_beach" to listOf(
                "nikiti_old_settlement",
                "panoramic_rest_point",
                "neos_marmaras_village",
                "toroni_archaeological_site",
                "ormylia_monday_market"
            ),
            // Karagatsi Beach
            "karagatsi_beach" to listOf(
                "kladi_olive_oil",
                "sophronios_basilica",
                "aquata_waterpark",
                "psalida_tower",
                "simantra_friday_market"
            ),
            // Talgo Beach
            "talgo_beach" to listOf(
                "nikiti_old_settlement",
                "panoramic_rest_point",
                "neos_marmaras_village",
                "toroni_archaeological_site",
                "simantra_friday_market"
            ),
            // Lagonisi Beach
            "lagonisi_beach" to listOf(
                "kladi_olive_oil",
                "sophronios_basilica",
                "aquata_waterpark",
                "psalida_tower",
                "simantra_friday_market"
            ),
            // Latoura Beach
            "latoura_beach" to listOf(
                "nikiti_old_settlement",
                "panoramic_rest_point",
                "neos_marmaras_village",
                "toroni_archaeological_site",
                "ormylia_monday_market"
            ),
            // Livrohio
            "livrohio" to listOf(
                "kladi_olive_oil",
                "sophronios_basilica",
                "aquata_waterpark",
                "psalida_tower",
                "simantra_friday_market"
            ),
            // Trani Ammouda
            "trani_ammouda" to listOf(
                "nikiti_old_settlement",
                "panoramic_rest_point",
                "neos_marmaras_village",
                "toroni_archaeological_site",
                "simantra_friday_market"
            ),
            // Beach of Pirgos
            "beach_of_pirgos" to listOf(
                "kladi_olive_oil",
                "sophronios_basilica",
                "aquata_waterpark",
                "psalida_tower",
                "simantra_friday_market"
            ),
            // Paralia Agios Nikolaos
            "paralia_agios_nikolaos" to listOf(
                "nikiti_old_settlement",
                "panoramic_rest_point",
                "neos_marmaras_village",
                "toroni_archaeological_site",
                "ormylia_monday_market"
            ),
            // Schinias Beach
            "schinias_beach" to listOf(
                "kladi_olive_oil",
                "sophronios_basilica",
                "aquata_waterpark",
                "psalida_tower",
                "simantra_friday_market"
            ),
            // Salonikiou Beach
            "salonikiou_beach" to listOf(
                "nikiti_old_settlement",
                "panoramic_rest_point",
                "neos_marmaras_village",
                "toroni_archaeological_site",
                "simantra_friday_market"
            ),
            // Paralia Salonikiou
            "paralia_salonikiou" to listOf(
                "kladi_olive_oil",
                "sophronios_basilica",
                "aquata_waterpark",
                "psalida_tower",
                "simantra_friday_market"
            ),
            // Irini Beach
            "irini_beach" to listOf(
                "nikiti_old_settlement",
                "panoramic_rest_point",
                "neos_marmaras_village",
                "toroni_archaeological_site",
                "ormylia_monday_market"
            ),
            // Ladhario Beach
            "ladhario_beach" to listOf(
                "prosphorion_tower",
                "zygos_monastery",
                "ammouliani_island",
                "goat_island",
                "agios_nikolaos_thursday_market"
            ),
            // Paralia Pirgos
            "paralia_pirgos" to listOf(
                "akanthos_archaeological_site",
                "stageira_archaeological_site",
                "aristotle_tomb",
                "nikiti_friday_market",
                "agios_nikolaos_thursday_market"
            ),
            // Develiki Beach
            "develiki_beach" to listOf(
                "prosphorion_tower",
                "zygos_monastery",
                "ammouliani_island",
                "goat_island",
                "agios_nikolaos_thursday_market"
            ),
            // Xiropotamos Beach
            "xiropotamos_beach" to listOf(
                "akanthos_archaeological_site",
                "stageira_archaeological_site",
                "aristotle_tomb",
                "nikiti_friday_market",
                "megali_panagia_wednesday_market"
            ),
            // Tripiti Beach
            "tripiti_beach" to listOf(
                "prosphorion_tower",
                "zygos_monastery",
                "ammouliani_island",
                "goat_island",
                "agios_nikolaos_thursday_market"
            ),
            // Paralia Ouranoupoli
            "paralia_ouranoupoli" to listOf(
                "akanthos_archaeological_site",
                "stageira_archaeological_site",
                "aristotle_tomb",
                "nikiti_friday_market",
                "agios_nikolaos_thursday_market"
            ),
            // Ouranoupolis Beach
            "ouranoupolis_beach" to listOf(
                "prosphorion_tower",
                "zygos_monastery",
                "ammouliani_island",
                "goat_island",
                "agios_nikolaos_thursday_market"
            ),
            // Komitsa Beach
            "komitsa_beach" to listOf(
                "akanthos_archaeological_site",
                "stageira_archaeological_site",
                "aristotle_tomb",
                "nikiti_friday_market",
                "megali_panagia_wednesday_market"
            ),
            // Nea Roda Beach
            "nea_roda_beach" to listOf(
                "prosphorion_tower",
                "zygos_monastery",
                "ammouliani_island",
                "goat_island",
                "agios_nikolaos_thursday_market"
            ),
            // Ierissos Beach
            "ierissos_beach" to listOf(
                "akanthos_archaeological_site",
                "stageira_archaeological_site",
                "aristotle_tomb",
                "nikiti_friday_market",
                "agios_nikolaos_thursday_market"
            ),
            // Kakoudia Beach
            "kakoudia_beach" to listOf(
                "prosphorion_tower",
                "zygos_monastery",
                "ammouliani_island",
                "goat_island",
                "agios_nikolaos_thursday_market"
            ),
            // Stratoni Beach
            "stratoni_beach" to listOf(
                "akanthos_archaeological_site",
                "stageira_archaeological_site",
                "aristotle_tomb",
                "nikiti_friday_market",
                "megali_panagia_wednesday_market"
            ),
            // Babylon Beach
            "babylon_beach" to listOf(
                "prosphorion_tower",
                "zygos_monastery",
                "ammouliani_island",
                "goat_island",
                "agios_nikolaos_thursday_market"
            ),
            // Proti Ammoudia Beach
            "proti_ammoudia_beach" to listOf(
                "akanthos_archaeological_site",
                "stageira_archaeological_site",
                "aristotle_tomb",
                "nikiti_friday_market",
                "agios_nikolaos_thursday_market"
            ),
            // Olympiada Beach
            "olympiada_beach" to listOf(
                "prosphorion_tower",
                "zygos_monastery",
                "ammouliani_island",
                "goat_island",
                "agios_nikolaos_thursday_market"
            ),
            // Paralia Stavros
            "paralia_stavros" to listOf(
                "akanthos_archaeological_site",
                "stageira_archaeological_site",
                "aristotle_tomb",
                "nikiti_friday_market",
                "megali_panagia_wednesday_market"
            ),
            // Milies Beach
            "milies_beach" to listOf(
                "prosphorion_tower",
                "zygos_monastery",
                "ammouliani_island",
                "goat_island",
                "agios_nikolaos_thursday_market"
            ),
            // Platani Beach
            "platani_beach" to listOf(
                "akanthos_archaeological_site",
                "stageira_archaeological_site",
                "aristotle_tomb",
                "nikiti_friday_market",
                "agios_nikolaos_thursday_market"
            ),
            // Vrasna Beach
            "vrasna_beach" to listOf(
                "prosphorion_tower",
                "zygos_monastery",
                "ammouliani_island",
                "goat_island",
                "agios_nikolaos_thursday_market"
            ),
            // Nea Vrasna Beach
            "nea_vrasna_beach" to listOf(
                "akanthos_archaeological_site",
                "stageira_archaeological_site",
                "aristotle_tomb",
                "nikiti_friday_market",
                "megali_panagia_wednesday_market"
            ),
    )



    // ===== 3) API public — rămâne același pentru ecran =====
    fun itemsForBeach(beachName: String): List<WhatToDoItem> =
        beachRefs[slug(beachName)]?.mapNotNull(catalog::get).orEmpty()

    // (opțional) toate item-urile, de ex. pt. search global
    fun allItems(): List<WhatToDoItem> = catalog.values.toList()
}