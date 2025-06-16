# 🎧 Analisis Musik Spotify Top 50 Indonesia 🇮🇩

Selamat datang di proyek eksploratif ini! 🚀  
Di sini, saya menganalisis *Spotify Top 50 Indonesia* menggunakan Python dan Spotify Web API untuk menggali wawasan musik berdasarkan fitur audio. Proyek ini mencakup pengumpulan data, ekstraksi fitur audio, clustering, hingga visualisasi interaktif.  

---

## 🔍 Deskripsi Proyek

🎵 **Apa yang saya lakukan di sini?**

- Mengambil data dari playlist **Spotify Top 50 Indonesia** secara otomatis.
- Mengekstrak fitur audio seperti:
  - `danceability` 💃
  - `energy` ⚡
  - `valence` 😊
  - `tempo` 🕒
  - `loudness` 🔊
  - `speechiness` 🎙️
- Melakukan **standarisasi** data menggunakan `StandardScaler`.
- Melakukan **clustering** menggunakan algoritma `KMeans`.
- Visualisasi hasil dengan `PCA` dalam bentuk scatter plot 🎯.
- Menyimpan hasil analisis ke dalam file `.csv`.

---

## 🧠 Teknologi yang Digunakan

- Python 🐍
- Spotipy (Spotify Web API wrapper) 🎧
- Pandas & NumPy 📊
- Scikit-learn 🤖
- Matplotlib & Seaborn 📈

---

## 📂 Struktur Output

- File CSV hasil klasterisasi disimpan di:


---

## 📸 Preview Visualisasi

<img src="https://github.com/username/repo-name/blob/main/preview.png" alt="Clustering Result" width="600"/>

---

## ✨ Insight

Dengan cluster ini, kita bisa mengetahui pola lagu-lagu populer di Indonesia:
- Apakah lagu cenderung ceria atau mellow?
- Apakah dominan dance/beat cepat atau slow?
- Dan sebagainya…

---

## 📌 Catatan

- Token dari Spotify akan kedaluwarsa setiap 1 jam.
- Pastikan kamu sudah mendaftar Spotify Developer Account untuk mendapatkan `client_id` dan `client_secret`.

---

## 🤝 Kontribusi

Jika kamu tertarik untuk mengembangkan atau menyempurnakan analisis ini, feel free to fork atau kirim pull request ya! 💬

---

## 🪪 Author

**M. Fahri Ramadhan**  
Mahasiswa Fakultas Ilmu Komputer – Universitas Sriwijaya  


---

## ⭐ Give it a Star

Jika kamu merasa proyek ini bermanfaat, jangan lupa kasih ⭐ ya!

