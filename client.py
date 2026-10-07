import socket

#1. Inisialisasi socket yang sama dengan server 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#2. Tentukan target server yang ingin dituju
HOST = 'localhost'
PORT = 5000

print(f"[*] Menghubungkan ke server {HOST}:{PORT}...")
client_socket.connect((HOST,PORT))

#3. Siapkan pesan yang ingin dikirim
pesan = "halo server, ini pesan dari client!"
print(f"[Mengirim Request]: {pesan}")

#4. Kirim pesan ke server (harus diubah menjadi bytes dulu)
client_socket.send(pesan.encode('utf-8'))

#5. Menerima tanggapan/respons dari server
respons = client_socket.recv(1024).decode('utf-8')
print(f"[Menerima Response]: {respons}")

#6. Tutup koneksi setelah selesai
client_socket.close()
print("[*] Selesai.")
