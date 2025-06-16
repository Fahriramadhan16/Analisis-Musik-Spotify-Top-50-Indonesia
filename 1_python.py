# ====================
# IMPORT LIBRARY
# ====================
import os
import time
import spotipy
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from spotipy.oauth2 import SpotifyOAuth
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# ====================
# KONFIGURASI SPOTIFY API
# ====================
client_id = 'd65b2042799b4ae289c6ce459708971d'
client_secret = '139fab950a0f4f1fb2803d1c39d6f818'
redirect_uri = 'http://127.0.0.1:8888/callback'
scope = 'playlist-read-private playlist-read-collaborative user-library-read'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    scope = 'playlist-read-private playlist-read-collaborative user-library-read user-read-private',
    cache_path='.cache',
    show_dialog=True,
    open_browser=True
))
print("✅ Berhasil autentikasi ke Spotify API.")

# ====================
# AMBIL DATA PLAYLIST PUBLIK (Top 50 Indonesia)
# ====================
playlist_id = '1fynbnF3droFlHnH8ln2Uc'
try:
    results = sp.playlist_tracks(playlist_id, market='ID')
    tracks = results['items']
    print(f"🎵 Jumlah lagu ditemukan: {len(tracks)}")
except Exception as e:
    print("❌ Gagal mengambil data dari playlist:", e)
    exit()

# ====================
# EKSTRAKSI TRACK DAN FITUR AUDIO
# ====================
songs = []
ids = []
for item in tracks:
    track = item.get('track')
    if track and track.get('id'):
        ids.append(track['id'])
        songs.append({
            'id': track['id'],
            'name': track['name'],
            'artist': track['artists'][0]['name']
        })

# Ambil fitur audio (max 100 per request)
features = []
for i in range(0, len(ids), 50):
    batch = ids[i:i+50]
    try:
        audio_feats = sp.audio_features(batch)
        features.extend([f for f in audio_feats if f])
    except Exception as e:
        print(f"⚠️ Gagal mengambil fitur audio batch {i}-{i+len(batch)}: {e}")
    time.sleep(0.3)  # delay 300ms antar batch
        
        
# Gabungkan data lagu dan fitur
data = []
for song, feat in zip(songs, features):
    if feat and feat.get('danceability') is not None:
        song.update({
            'danceability': feat['danceability'],
            'energy': feat['energy'],
            'valence': feat['valence'],
            'tempo': feat['tempo'],
            'loudness': feat['loudness'],
            'speechiness': feat['speechiness']
        })
        data.append(song)

df = pd.DataFrame(data)
if df.empty:
    print("❌ Tidak ada data lagu yang valid untuk dianalisis.")
    exit()

print("\n📊 Cuplikan data:\n", df[['name', 'artist', 'danceability', 'energy']].head())

# ====================
# CLUSTERING DATA
# ====================
fitur_audio = ['danceability', 'energy', 'valence', 'tempo', 'loudness', 'speechiness']
X = StandardScaler().fit_transform(df[fitur_audio])
df['cluster'] = KMeans(n_clusters=3, init='k-means++', n_init=10, random_state=42).fit_predict(X)

# ====================
# REDUKSI DIMENSI (PCA) & VISUALISASI
# ====================
pca = PCA(n_components=2)
pca_result = pca.fit_transform(X)
df['PCA1'], df['PCA2'] = pca_result[:, 0], pca_result[:, 1]

sns.set_style('whitegrid')
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='PCA1', y='PCA2', hue='cluster', palette='Set2', s=100)
plt.title("🎶 Clustering Fitur Lagu – Spotify Top 50 Indonesia")
plt.xlabel("PCA Komponen 1")
plt.ylabel("PCA Komponen 2")
plt.tight_layout()
plt.show()

# ====================
# ANALISIS CLUSTER
# ====================
print("\n📌 Rata-rata fitur per cluster:")
print(df.groupby('cluster')[fitur_audio].mean().round(2))

# ====================
# SIMPAN HASIL KE CSV
# ====================
output_dir = 'D:/DataSpotify'
output_file = 'spotify_top50_audio_clusters.csv'

# Buat folder jika belum ada
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Simpan CSV
full_path = os.path.join(output_dir, output_file)
df.to_csv(full_path, index=False)

print(f"\n✅ Data berhasil disimpan ke: {full_path}")

if os.path.exists('.cache'):
    os.remove('.cache')