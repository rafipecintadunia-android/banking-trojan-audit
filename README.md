# Android Banking Trojan - Security Audit & C2 Simulation

Repositori ini mendokumentasikan hasil audit keamanan, rekayasa balik (*reverse engineering*), dan analisis struktur payload dari sampel Android Banking Trojan (`base.apk`). Proyek ini bertujuan untuk memahami pola serangan, analisis izin berbahaya, serta simulasi infrastruktur Command and Control (C2).

---

## 🛠️ Tech Stack & Tools
* **Lingkungan Analisis:** Termux (Android)
* **Reverse Engineering:** Apktool, OpenJDK 21, AAPT2
* **Bahasa Pemrograman:** Python (untuk modul C2 & simulasi)
* **Kontrol Versi:** Git & GitHub

---

## 📂 Struktur Repositori
```text
banking-trojan-audit/
│
├── smali/                 # Kode smali hasil decode (analisis logika & smali hooking)
├── res/                   # Sumber daya aplikasi (layout, drawable, strings)
├── unknown/               # Aset internal dan file terkompresi (termasuk .png & .jpg)
├── AndroidManifest.xml    # Berkas konfigurasi izin & komponen utama aplikasi
└── README.md              # Dokumentasi proyek
