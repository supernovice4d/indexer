import requests
import time

# Fungsi untuk memuat proxy dari file yang diberikan
def load_proxies(filename):
    try:
        with open(filename, 'r') as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print("File tidak ditemukan. Pastikan nama file yang Anda masukkan benar dan berada di direktori yang sama dengan script ini.")
        return []

# Meminta pengguna memasukkan nama file untuk daftar proxy
filename = input("List proxy: ")

# Meminta pengguna untuk memasukkan jeda antara setiap permintaan
delay = float(input("Tread: "))

# Meminta pengguna untuk memasukkan URL target
url = input("Link: ")

# Meminta pengguna untuk memasukkan kata kunci pencarian
keyword = input("Keywoard: ")

# Headers termasuk referer yang dibangun berdasarkan input pengguna
headers = {
    'Referer': f'https://www.google.com/search?q={keyword}'
}

# Memuat daftar proxy dari file yang diberikan pengguna
proxies_list = load_proxies(filename)

# Fungsi untuk mengirim permintaan menggunakan proxy yang berbeda
def send_request(url, headers, proxy):
    try:
        proxies = {
            'http': proxy,
            'https': proxy
        }
        response = requests.get(url, headers=headers, proxies=proxies)
        print(f"Status Code: {response.status_code} | Proxy: {proxy}")
    except requests.exceptions.RequestException as e:
        print(f"Error with {proxy}: {e}")

# Mengirim permintaan dengan setiap proxy dalam daftar
for proxy in proxies_list:
    send_request(url, headers, proxy)
    time.sleep(delay)  # Menunggu sejumlah waktu yang ditentukan oleh pengguna sebelum mengirim permintaan berikutnya
