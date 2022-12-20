#Library Yang Dipakai Pada Program (cgitb, pdb, pygame, sys)
from cgitb import text
from pdb import Restart
import pygame
from pygame.locals import QUIT
import sys

#Array initialState (Kondisi Awal Puzzle) Dengan Array 2 Dimensi Dengan Nol(0) Sebagai Kotak Kosong
initialState = [[2, 8, 3], [1, 6, 4], [7, 0, 5]]


pygame.init()#Inisialisasi Pygame
pygame.display.set_caption("8 PUZZLE | BY : Yunomi99")#Mengubah uPygame Window Name
clock = pygame.time.Clock()#Inisialisasi Pygame Clock
screen = pygame.display.set_mode((300,300))#Membuka Layar Baru pygame
blank = pygame.Surface([100,100])#Membuat Kotak dengan Ukuran 100x100px
hor = pygame.Surface([4, 300])#Variabel Untuk Membuat Persegi Panjang Dengan Ukuran 4x300 Pixel Sebagai Garis Pembatas Horizontal Antar Kotak
ver = pygame.Surface([300, 4])#Variabel Untuk Membuat Persegi Panjang Dengan Ukuran 300x4 Pixel Sebagai Garis Pembatas Vertikal Antar Kotak
myFont1 = pygame.font.SysFont("verdana",20)#Menentukan Font dan Ukuran Font Yang Dipakai Untuk Angka Pada Setiap Kotak
myFont2 = pygame.font.SysFont("verdana",12)#Menentukan Font dan Ukuran Font Yang Dipakai Untuk Pesan Kemenangan

#Fungsi Menemukan Angka Nol/Blank Cell Untuk Bisa Dipindahkan
def findZero():#Inisialisasi Awal dengan Nama Fungsi
    for i in range(3):#Pengulangan Kolom Untuk mencari Angka 0 Pada Kolom
        for j in range(3):#Pengulangan Kolom Untuk mencari Angka 0 Pada Kolom
            if initialState[i][j]==0:#Kondisi Untuk Membandingan Data Yang Terbaca Apakah 0 Atau Tidak
                findZero.iPos= i#Jika Terdeteksi Nol Maka Posisi Kolom Pada Matrik Disimpan Dalam Variabel finZero.iPos
                findZero.jPos= j#Jika Terdeteksi Nol Maka Posisi Baris Pada Matrik Disimpan Dalam Variabel finZero.jPos

#Fungsi Menampilkan Tampilan Puzzle
def displayPuzzle():#Inisialisasi Awal dengan Nama Fungsi
    findZero()#Memanggil Fungsi finZero() Untuk Mendapatkan Posisi Angka 0
    #Variabel Pengisi Kotak Dengan Data Angka Sesuai Dengan Kolom Dan Baris Array initialState
    text00 = myFont1.render(str(initialState[0][0]), True, (0, 0, 0))#Menyimpan Data Pada Varibel Menggukan myFont1 Pada Kordinat [i][j] Dengan Warna Hitam
    text01 = myFont1.render(str(initialState[1][0]), True, (0, 0, 0))#Menyimpan Data Pada Varibel Menggukan myFont1 Pada Kordinat [i][j] Dengan Warna Hitam
    text02 = myFont1.render(str(initialState[2][0]), True, (0, 0, 0))#Menyimpan Data Pada Varibel Menggukan myFont1 Pada Kordinat [i][j] Dengan Warna Hitam
    text10 = myFont1.render(str(initialState[0][1]), True, (0, 0, 0))#Menyimpan Data Pada Varibel Menggukan myFont1 Pada Kordinat [i][j] Dengan Warna Hitam
    text11 = myFont1.render(str(initialState[1][1]), True, (0, 0, 0))#Menyimpan Data Pada Varibel myFont1 Pada Kordinat [i][j] Dengan Warna Hitam
    text12 = myFont1.render(str(initialState[2][1]), True, (0, 0, 0))#Menyimpan Data Pada Varibel myFont1 Pada Kordinat [i][j] Dengan Warna Hitam
    text20 = myFont1.render(str(initialState[0][2]), True, (0, 0, 0))#Menyimpan Data Pada Varibel myFont1 Pada Kordinat [i][j] Dengan Warna Hitam
    text21 = myFont1.render(str(initialState[1][2]), True, (0, 0, 0))#Menyimpan Data Pada Varibel myFont1 Pada Kordinat [i][j] Dengan Warna Hitam
    text22 = myFont1.render(str(initialState[2][2]), True, (0, 0, 0))#Menyimpan Data Pada Varibel myFont1 Pada Kordinat [i][j] Dengan Warna Hitam
    
    
    screen.fill((255,255,255))#Mewarnai Screen Menjadi Warna Putih
    
    x=0+(findZero.jPos*100)#Menentukan Koordinat Kotak Kosong Pada Layar Secara Horixzontal(x) 
    y=0+(findZero.iPos*100)#Menentukan Koordinat Kotak Kosong Pada Layar Secara Vertikal(y)

    #Semua Fungsi Dengan screen.blit Artinya Menampilkan Data Gambar dan text Yang Dibuat Sebelumnya Dalam Variabel Ke Layar
    screen.blit(blank,(x,y))#Menampilkan Kotak Kosong (blank) Pada Koordiat Sesuai Posisi 0
    screen.blit(hor,(-2,0))#Menampilkan Garis Horizontal Pada Koordinat (x,y) Sesuai Angka Dalam Kurung
    screen.blit(hor,(98,0))#Menampilkan Garis Horizontal Pada Koordinat (x,y) Sesuai Angka Dalam Kurung
    screen.blit(hor,(198,0))#Menampilkan Garis Horizontal Pada Koordinat (x,y) Sesuai Angka Dalam Kurung
    screen.blit(hor,(298,0))#Menampilkan Garis Horizontal Pada Koordinat (x,y) Sesuai Angka Dalam Kurung
    screen.blit(ver,(0,-2))#Menampilkan Garis Vertikal Pada Koordinat (x,y) Sesuai Angka Dalam Kurung
    screen.blit(ver,(0,98))#Menampilkan Garis Vertikal Pada Koordinat (x,y) Sesuai Angka Dalam Kurung
    screen.blit(ver,(0,198))#Menampilkan Garis Vertikal Pada Koordinat (x,y) Sesuai Angka Dalam Kurung
    screen.blit(ver,(0,298))#Menampilkan Garis Vertikal Pada Koordinat (x,y) Sesuai Angka Dalam Kurung
    screen.blit(text00, (40, 40))#Menampilkan Text Pada Koordinat (x,y) Sesuai Angka Dalam Kurung
    screen.blit(text01, (40, 140))#Menampilkan Text Pada Koordinat (x,y) Sesuai Angka Dalam Kurung
    screen.blit(text02, (40, 240))#Menampilkan Text Pada Koordinat (x,y) Sesuai Angka Dalam Kurung
    screen.blit(text10, (140, 40))#Menampilkan Text Pada Koordinat (x,y) Sesuai Angka Dalam Kurung
    screen.blit(text11, (140, 140))#Menampilkan Text Pada Koordinat (x,y) Sesuai Angka Dalam Kurung
    screen.blit(text12, (140, 240))#Menampilkan Text Pada Koordinat (x,y) Sesuai Angka Dalam Kurung
    screen.blit(text20, (240, 40))#Menampilkan Text Pada Koordinat (x,y) Sesuai Angka Dalam Kurung
    screen.blit(text21, (240, 140))#Menampilkan Text Pada Koordinat (x,y) Sesuai Angka Dalam Kurung
    screen.blit(text22, (240, 240))#Menampilkan Text Pada Koordinat (x,y) Sesuai Angka Dalam Kurung

#Fungsi Menampilkan Pesan Kemenangan
def winScreen():#Inisialisasi Awal dengan Nama Fungsi
    winText1 = myFont2.render("Selamat!!!", True, (255, 0, 0))#Menyimpan Data Pada Varibel myFont2 Pada Kordinat [i][j] Dengan Warna Merah
    winText2 = myFont2.render("Kamu Berhasil, Puzzle Telah Terpecahkan.", True, (255, 0, 0))#Menyimpan Data Pada Varibel myFont2 Pada Kordinat [i][j] Dengan Warna Merah
    winText3 = myFont2.render("Restart Y/N?", True, (255, 0, 0))#Menyimpan Data Pada Varibel myFont2 Pada Kordinat [i][j] Dengan Warna Merah

    screen.fill((0,255,0))#Mengubah Warna Screen Menjadi Warna Putih

    screen.blit(winText1, (115, 120))#Menampilkan Text Pada Koordinat (x,y) Sesuai Angka Dalam Kurung
    screen.blit(winText2, (30, 140))#Menampilkan Text Pada Koordinat (x,y) Sesuai Angka Dalam Kurung
    screen.blit(winText3, (110, 160))#Menampilkan Text Pada Koordinat (x,y) Sesuai Angka Dalam Kurung
    

#Fungsi Membandingkan Array Yang Terbentuk Dan goalState
def comparePos():#Inisialisasi Awal dengan Nama Fungsi
    global clearedState#Mengenalkan Variabel clearedState Dalam Fungsi Sebagai Global Variabel
    #Kondisi Ketika initialState Sama Dengan goalState (Membandingan Setiap Kolom dan Baris) dari [0][0] sampi [2][2]
    if initialState[0][0] == 1 and initialState[0][1] == 2 and initialState[0][2] == 3 and \
        initialState[1][0] == 8 and initialState[1][1] == 0 and initialState[1][2] == 4 and \
        initialState[2][0] == 7 and initialState[2][1] == 6 and initialState[2][2] == 5:
        clearedState = True#Mengubah Kondisi Pemecahan Puzzle Menjadi True Ketika Sudah Sesuai Semua
    else:
        clearedState = False#Kondisi Apabila Belum Terpecahkan Tetap False

#Fungsi Membaca Tombol Pada Keyboard lalu Mengupdate Array initialState Sesuai Masukan Keyboard
def updatePos():#Inisialisasi Awal dengan Nama Fungsi
    global clearedState#Mengenalkan Variabel clearedState Dalam Fungsi Sebagai Global Variabel
    for event in pygame.event.get():#Perulangan Pembacaan Perubahan Pada Window Dan Sistem Pygame (Contoh: Saat menekan Tombol)
            #Kondisi Jika Menekan Quit/Keluar
            if event.type == QUIT:#Ketika Mengklik Silang Pada Window Game
                pygame.quit()#Fungsi Menghentikan Program Pygame Ui
                sys.exit()#Fungsi Menghentikan Program Python
            elif  event.type == pygame.KEYDOWN:#Kondisi Jika Menekan Tombol Keyboard 
                if event.key == pygame.K_RIGHT:#Kondisi Ketika Menekan Panah Kanan Menggeser Kotak Kosong Kekanan
                    #Memindahkan Kotak Kosong Pada Array initialState Sesuai Perubahan Dan Perintah Masukan Keyboard Dengan Cara Swap Data Kekanan
                    if findZero.jPos != 2:
                        initialState[findZero.iPos][findZero.jPos]=initialState[findZero.iPos][findZero.jPos+1]
                        initialState[findZero.iPos][findZero.jPos+1]=0
                elif event.key == pygame.K_LEFT:#Kondisi Ketika Menekan Panah Kiri Menggeser Kotak Kosong Kekiri
                    #Memindahkan Kotak Kosong Pada Array initialState Sesuai Perubahan Dan Perintah Masukan Keyboard Dengan Cara Swap Data Kekiri
                    if findZero.jPos != 0:
                        initialState[findZero.iPos][findZero.jPos]=initialState[findZero.iPos][findZero.jPos-1]
                        initialState[findZero.iPos][findZero.jPos-1]=0
                elif event.key == pygame.K_UP:#Kondisi Ketika Menekan Panah Atas Untuk Menggeser Kotak Kosong Keatas
                    #Memindahkan Kotak Kosong Pada Array initialState Sesuai Perubahan Dan Perintah Masukan Keyboard Dengan Cara Swap Data Keatas
                    if findZero.iPos != 0: 
                        initialState[findZero.iPos][findZero.jPos]=initialState[findZero.iPos-1][findZero.jPos]
                        initialState[findZero.iPos-1][findZero.jPos]=0
                elif event.key == pygame.K_DOWN:#Kondisi Ketika Menekan Panah Bawah Untuk Menggeser Kotak Kosong Kebawah
                    #Memindahkan Kotak Kosong Pada Array initialState Sesuai Perubahan Dan Perintah Masukan Keyboard Dengan Cara Swap Data Kebawah
                    if findZero.iPos != 2: 
                        initialState[findZero.iPos][findZero.jPos]=initialState[findZero.iPos+1][findZero.jPos]
                        initialState[findZero.iPos+1][findZero.jPos]=0
                elif event.key == pygame.K_y:#Kondisi Ketika Menekan Huruf Y Untuk Mengulang Game
                    if clearedState == True:#Kondisi Hanya Berjalan Ketika Puzzle Susdah Selesai
                        clearedState = False#Reset Data Variabel Penentu Keberhasilan Pemecahan Tabel Ke kondisi sebelum Dipecahkan (False)
                        #Mengembalikan Semua Data Kesemula (initialState) = [[2, 8, 3], [1, 6, 4], [7, 0, 5]] Secara Satu-persatu
                        initialState[0][0] = 2 
                        initialState[0][1] = 8
                        initialState[0][2] = 3
                        initialState[1][0] = 1
                        initialState[1][1] = 6
                        initialState[1][2] = 4
                        initialState[2][0] = 7
                        initialState[2][1] = 0
                        initialState[2][2] = 5
                elif event.key == pygame.K_n:#Kondisi Ketika Menekan Huruf N Untuk Menghentikan Game
                    if clearedState == True:#Kondisi Hanya Berjalan Ketika Puzzle Susdah Selesai
                        #Fungsi Keluar Dari Program
                        pygame.quit()#Fungsi Menghentikan Program Pygame Ui
                        sys.exit()#Fungsi Menghentikan Program Python

#Fungsi Utama Pada Program Puzzle
def main():#Inisialisasi Awal Fungsi Utama
    while True:#Fungsi Yang Berjalan Terus Menerus(Infinite Loop)
        updatePos()#Memanggil Fungsi updatePos() Untuk Mengupdate Isi Array Data Puzzle Sesuai Masukan/Perintah Yang Kita Masukan Pada Keyboard
        comparePos() #Memanggil Fungsi comparePos() Untuk Membandingan Array Data Terbaru Dengan goalState
        if clearedState == False:#Pengkondisian/Percabangan Menentukan Apakah Puzzle Sudah Terpecahkan Untuk Mengetahui Display Yang Akan Ditampilkan
            displayPuzzle()#Ketika Belum Selesai Tampilkan Ui Puzzle
        else:
            winScreen()#Ketika Sudah Selesai Tampilkan Pesan Kemenangan dan Menu Mengulang

        pygame.display.update()#Program Update Display Puzzle

#Menjalankan Fungsi Main Pada Sistem
if __name__ == "__main__":#Fungsi Utama Sistem
    main()#Memanggil Fungsi Main


    #ALGORITMA PROGRAM :

    #Pertama : Kita Diharuskan Memasukan Initial State Untuk Membuat Kondisi Awal Puzzle Dalam Array 2 Dimensi (3x3)
    #Kedua : Kita Diharuskan Mendesain Tampilan Puzzle Dan Text Yang Akan Dimunculkan
    #Ketiga : Kita Membaca Inputan Dari Keyboard
    #Kelima : Memperbarui Data Dalam Array Sesuai Perintah/Inputan Dari Keyboard Yang Ditekan
    #Keempat : Kita Melakukan Sinkronasi Atau Menghubungkan Kondisi Array Data Dengan Tampilan Sehingga Tampilan Sesuai Dengan Array Data
    #Kelima : Kita Membandingkan Array Data Terbaru Dengan goalState Yang Diiginkan 
    #Keenam : Terus Melakukan Update Tampilan Agar Sesuai Dengan Perubahan Yang Terjadi Pada Array Data
    #Ketujuh : Kalo Sudah Terpecahkan Maka Program Berhenti Dengan Pesan Kemenangan Dengan Pilihan Mengulang Atau Tidak (Restart Y/N?)

#Mencoba GIT workflow dengan vscode