
from numpy import random
import numpy as np
import pandas as pd

random.seed(42)

tekli_kusur_orani = 0.24
coklu_kusur_orani = 0.06

uretim_gunuv1 = pd.to_datetime("2026-10-26 08:00:00")
uretim_gunuv2 = pd.to_datetime("2026-10-26 20:00:00")

parca_idleri = []
uretim_saatleri = []
kontrol_saatleri = []
kontrol_sureleri = []
kontrol_baslangiclari = []
kontrolcu_musait_saati = None

for cevrim_no in range(1, 26):
    for makina_no in ["IM01", "IM02"]:
        for goz_no in range(1, 7):

            if cevrim_no <= 12:
                vardiya = "A"
                uretim_gunu = uretim_gunuv1
                vardiya_cevrimi = cevrim_no
            else:
                vardiya = "B"
                uretim_gunu = uretim_gunuv2
                vardiya_cevrimi = cevrim_no - 12

            uretim_saati = uretim_gunu + pd.Timedelta(
                seconds=48 * (vardiya_cevrimi - 1)
            )

            kontrol_suresi = round(np.random.uniform(10, 30), 2)

            if kontrolcu_musait_saati is None:
                kontrol_baslangici = uretim_saati
            else:
                kontrol_baslangici = max(
                    uretim_saati,
                    kontrolcu_musait_saati
                )

            kontrol_saati = kontrol_baslangici + pd.Timedelta(
                seconds=kontrol_suresi
            )

            kontrolcu_musait_saati = kontrol_saati

            parca_id = (
                f"CH-{makina_no}-C{cevrim_no:03d}-G{goz_no}-{vardiya}"
            )

            parca_idleri.append(parca_id)
            uretim_saatleri.append(uretim_saati)
            kontrol_saatleri.append(kontrol_saati)
            kontrol_sureleri.append(kontrol_suresi)
            kontrol_baslangiclari.append(kontrol_baslangici)

tablo = pd.DataFrame({
    "Parça ID": parca_idleri,
    "Makina No": [p.split("-")[1] for p in parca_idleri],
    "Çevrim No": [int(p.split("-")[2][1:]) for p in parca_idleri],
    "Göz No": [int(p.split("-")[3][1:]) for p in parca_idleri],
    "Vardiya": [p.split("-")[4] for p in parca_idleri],
    "Üretim Saati": uretim_saatleri,
    "Kontrol Başlangıcı": kontrol_baslangiclari,
    "Kontrol Süresi (sn)": kontrol_sureleri,
    "Kontrol Saati": kontrol_saatleri,
    "Çizik-darbe": [False] * len(parca_idleri),
    "Yüzeyde iz": [False] * len(parca_idleri),
    "Toz-kir-yabancı cisim": [False] * len(parca_idleri),
    "Çapak": [False] * len(parca_idleri),
    "Eksik baskı": [False] * len(parca_idleri),
    "Leke": [False] * len(parca_idleri),
    "Buğulanma": [False] * len(parca_idleri),
    "Çatlak/kırık": [False] * len(parca_idleri),
    "Parça sesi": [False] * len(parca_idleri),
    "Silik markalama": [False] * len(parca_idleri)
})

cok_kusurlu_parca = np.random.choice(
    tablo["Parça ID"],
    size=int(len(tablo) * coklu_kusur_orani),
    replace=False
)

kusur_listesi = [
    "Çizik-darbe",
    "Yüzeyde iz",
    "Toz-kir-yabancı cisim",
    "Çapak",
    "Eksik baskı",
    "Leke",
    "Buğulanma",
    "Çatlak/kırık",
    "Parça sesi",
    "Silik markalama"
]

for parca_id in cok_kusurlu_parca:
    kusur_sayisi = np.random.randint(2, 4)
    kusur_turleri = random.choice(
        kusur_listesi,
        size=kusur_sayisi,
        replace=False
    )
    for kusur in kusur_turleri:
        tablo.loc[tablo["Parça ID"] == parca_id, kusur] = True

tekli_kusurlu_parca = np.setdiff1d(
    tablo["Parça ID"],
    cok_kusurlu_parca
)

tekli_kusurlu_parca = np.random.choice(
    tekli_kusurlu_parca,
    size=int(len(tablo) * tekli_kusur_orani),
    replace=False
)

for parca_id in tekli_kusurlu_parca:
    kusur_turleri = random.choice(
        kusur_listesi,
        size=1,
        replace=False
    )
    for kusur in kusur_turleri:
        tablo.loc[tablo["Parça ID"] == parca_id, kusur] = True

tablo.to_excel("kalite_kontrol_veri_seti.xlsx", index=False)

print(tablo)
