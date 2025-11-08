# Cyber security 
Nama Project: < Cyber security Testing>

## latihan OWASP Juice Shop, port scanner sederhana, dll)

## Tujuan
- Menunjukkan pemahaman dasar Linux, Python, dan tooling keamanan
- Menyimpan bukti praktis (script, writeup, report) untuk portofolio
- Menunjukkan kemampuan dokumentasi teknik

## Struktur Repository
/
├─ README.md
├─ docs/
├─ scripts/
├─ labs/
└─ reports/

## Cara Menjalankan (Examples)
### Prasyarat
- Python 3.8+
- Virtual environment (venv)
- Nmap, Wireshark (opsional untuk analisis), Git

### Setup cepat
```bash
# clone repo
git clone <repo-url>
cd <repo-folder>

# buat virtualenv dan install deps
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# jalankan script contoh
python3 scripts/simple_port_scanner.py --host 127.0.0.1 --ports 1-1024
