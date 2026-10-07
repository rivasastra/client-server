import socket

#1.  Inisialisasi socket (menggunakan IPv4 dan TCP)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#2. Tentukan alamat IP dan PORT 
# 'localhost' berarti server berjalan di komputer anda sendiri
# PORT 5000 adalah pintu masuk komunikasi
HOST = 'localhost'
PORT = 5000

server_socket.bind((HOST, PORT))

#3. server mulai mendengarkan permintaan (maksimal antrean 1 client)
server_socket.listen(1)
print(f"[*] Server berjalan dan menunggu koneksi di  {HOST}:{PORT}...")

while True:
    #4. Menerima koneksi dari client
    client_socket, client_address = server_socket.accept()
    print(f"[+] Terhubung dengan client dari: {client_address}")

    #5. Membaca pesan yang dikirim oleh client (maksimal 1024 bytes)
    data = client_socket.recv(1024).decode('utf-8')
    if not data:
        break

    print(f"[Request diterima]: {data}")

    #6. Memproses data (mengubah ke huruf kapital)
    respons = data.upper()

    #7. Mengirimkan respons balik ke client
    client_socket.send(respons.encode('utf-8'))
    print(f"[Response dikirim]: {respons}")

    #8. Tutup koneksi dengan client ini
    client_socket.close()
    print("[-] Koneksi dengan client ditutup. \n")