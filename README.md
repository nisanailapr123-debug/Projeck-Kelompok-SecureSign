# SignDoc — Sistem Tanda Tangan Digital
**Kelompok**
1. Ahmad Aly (2488010069)
2. Nazwa Hummaimah Shidqin (2488010039)
3. Nisa Naila (2488010024)

Proyek Akhir (UAS) Kriptografi Modern  
**Tema 1: SignDoc** — Tanda Tangan Digital untuk Dokumen  
Algoritma: **RSA-2048 + SHA-256 (PSS padding)**

<h3>Video Demonstrasi</h3>
<a href="https://youtu.be/i0bSArvkPVE?si=BD0pb1Lw_6M2oTRv">Link YouTube</a>

---

## Cara Menjalankan

### 1. Prasyarat
- Python 3.10+
- XAMPP (MySQL aktif)
- pip

### 2. Install dependensi

```bash
cd signdoc
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate

pip install -r requirements.txt
```

### 3. Buat database MySQL

Buka phpMyAdmin atau MySQL CLI:
```sql
CREATE DATABASE signdoc CHARACTER SET utf8mb4;
```
Database dan tabel dibuat otomatis saat aplikasi pertama dijalankan.

### 4. Konfigurasi (opsional)

Edit `config.py` jika MySQL password berbeda:
```python
MYSQL_PASSWORD = 'password_anda'
```

### 5. Jalankan aplikasi

```bash
python app.py
```

Buka browser: http://localhost:5000

---

## Struktur Folder

```
signdoc/
├── app.py              # Entry point Flask
├── config.py           # Konfigurasi aplikasi
├── database.py         # Inisialisasi & helper database
├── requirements.txt
├── models/             # (opsional, logika di routes)
├── routes/
│   ├── auth.py         # Register, login, logout
│   ├── document.py     # Upload, dashboard, history
│   ├── sign.py         # Tanda tangan dokumen
│   └── verify.py       # Verifikasi signature
├── crypto/
│   ├── keygen.py       # RSA-2048 key pair generation
│   ├── hashing.py      # SHA-256 hashing
│   ├── signing.py      # RSA-PSS signing
│   └── verify.py       # RSA-PSS verification
├── templates/          # HTML Jinja2 templates
├── static/             # CSS & JS
├── uploads/            # File dokumen yang diunggah
└── signatures/         # File .sig
```

---

## Alur Kriptografi

### A. Registrasi
1. User daftar dengan username + password
2. Sistem generate **RSA-2048 key pair**
3. Private key **dienkripsi** dengan password user (AES-256-CBC via PKCS#8)
4. Password di-hash dengan **bcrypt** sebelum disimpan

### B. Tanda Tangan Dokumen
1. Upload dokumen → hitung **SHA-256 hash**
2. Dekripsi private key menggunakan password (dari session)
3. Sign hash menggunakan **RSA-PSS** → signature bytes
4. Signature disimpan di DB + file `.sig`

### C. Verifikasi
1. Upload dokumen + file `.sig`
2. Hitung ulang SHA-256 hash dokumen
3. Cari signature di DB → ambil public key penanda tangan
4. `public_key.verify(signature, hash)` → **VALID** atau **INVALID**

---

## Fitur yang Diimplementasikan

### Wajib ✅
- [x] Registrasi + generate RSA-2048 key pair
- [x] Upload dokumen + hitung SHA-256 hash
- [x] Tanda tangan dengan RSA private key (PSS padding)
- [x] Verifikasi signature (VALID/INVALID + detail)
- [x] Riwayat dokumen per user

### Pengembangan (nilai A) 🌟
- [ ] Multi-signer (dalam pengembangan)
- [ ] QR Code verifikasi (dalam pengembangan)
- [ ] Export laporan verifikasi PDF (dalam pengembangan)
