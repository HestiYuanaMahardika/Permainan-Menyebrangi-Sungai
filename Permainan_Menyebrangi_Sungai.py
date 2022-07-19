from time import sleep
from os import system
import platform

class perahu:

	def __init__(self, kordinat, isi_perahu):
		self.kordinat = kordinat
		self.isi_perahu = isi_perahu

class karakter:
	def __init__(self, nama, posisi, predator, makanan):
		self.nama = nama
		self.posisi = posisi
		self.predator = predator
		self.makanan = makanan

	def naik_perahu(self, lokasi_skg, perahu):
		lokasi_skg.remove(self)
		perahu.isi_perahu.append(self)

	def turun_perahu(self, lokasi_skg, perahu):
		lokasi_skg.append(self)
		perahu.isi_perahu.remove(self)

def clear_screen():
	if platform.system() == "Windows":
		system('cls')
	else:
		system('clear')
	sleep(0.4)

def start_game(ayam, gabah, harimau, petani, lokasiA):
	clear_screen()

	print("\t\tSelamat Datang di Game Tantangan Menyebrangi Sungai")
	print("\n\nBeberapa aturan yang harus dipatuhi di game ini adalah : ")
	print("1. Jangan tinggalkan harimau hanya dengan ayam.")
	print("2. Jangan tinggalkan ayam hanya dengan gabah.")
	print("3. Semua karakter harus sampai dengan selamat di sisi B.")
	print("4. Hanya ada 1 perahu yang muatan maksimalnya 2 karakter.")
	print("5. Untuk dapat berjalan, perahu harus ada penumpangnya.")

	print("\n\n\nSudah siap bermain??")
	input('enter to continue')

	lokasiA.append(ayam)
	lokasiA.append(gabah)
	lokasiA.append(harimau)
	lokasiA.append(petani)

def print_status(list_keberadaan):

	print("dengan jumlah karakter di sana:", len(list_keberadaan))
	if list_keberadaan:
		print("yaitu: ")
		urutan = 1
		for i in list_keberadaan:
			print(str(urutan) + ".", i.nama)
			urutan += 1

def status(perahu, lokasi_skg, lokasi_lain):
	clear_screen()

	print("\t\tSTATUS PERMAINAN")

	print("\n\nStatus Perahu:")
	print("berada di lokasi", "B" if perahu.kordinat else "A")
	print_status(perahu.isi_perahu)

	print("\n\nStatus Lokasi", "B" if perahu.kordinat else "A")
	print_status(lokasi_skg)

	print("\n\nStatus Lokasi", "A" if perahu.kordinat else "B")
	print_status(lokasi_lain)

	input("\n\nEnter to continue....")

def proses_naik_turun_perahu(perahu, lokasi_skg, lokasi_lain):
	while True:
		clear_screen()
	
		print("Silahkan masukan menu yang tersedia (huruf saja)")
		print("A. Pilih karakter untuk turun perahu")
		print("B. Pilih karakter untuk naik ke perahu")
		print("C. Menyebrangi sungai dengan karakter yang ada di atas perahu")
		print("D. Tampilkan status permainan")
		print("X. Untuk keluar dari permainan")
		pilih = input("pilihan: ").lower()

		if pilih == "a":
			if perahu.isi_perahu:
				print("Silahkan pilih karakter di atas perahu yang akan diturunkan ke lokasi")
				print("Pilihan: ")
				urutan = 1
				for i in perahu.isi_perahu:
					print(str(urutan) + ".", i.nama)

				try:
					urutan = input("Masukkan pilihan (angka saja):")
					urutan = int(urutan)
					print(perahu.isi_perahu[urutan].nama, "sudah turun perahu.")
					perahu.isi_perahu[urutan],turun_perahu(lokasi_skg, perahu)
				except:
					print("INPUT SALAH!\n")
					sleep(3)
					continue
				finally:
					print("Di lokasi", "B" if perahu.kordinat else "A")
					urutan = 1
					for i in lokasi_skg:
						print(str(urutan) + ".", i.nama)
					input("enter untuk lanjut")

			elif not perahu.isi_perahu:
				print("Perahu kosong, tidak ada yang bisa turun.")
				input("enter untuk kembali")

			else:
				print("Perahu sudah kosong")
				input("enter untuk kembali")

			if cek_menang(perahu, lokasi_skg):
				return True
			else:
				pass

		elif pilih == "b":
			if lokasi_skg and len(perahu.isi_perahu) < 2:
				print("Silahkan pilih karakter yang akan naik ke perahu")
				print("Pilihan : ")
				urutan = 1
				for i in lokasi_skg:
					print(str(urutan) + ".", i.nama)

				try:
					urutan = input("Masukkan pilihan (angka saja):")
					urutan = int(urutan)
					print(lokasi_skg[urutan].nama, "sudah naik perahu.")
					lokasi_skg[urutan],naik_perahu(lokasi_skg, perahu)
				except:
					print("INPUT SALAH!")
					print("enter untuk lanjut")
					continue

				finally:
					print("Di perahu sudah terdapat karakter: ")
					urutan = 1
					for i in perahu.isi_perahu:
						print(str(urutan) + ".", i.nama)
						urutan += 1
					input("enter untuk lanjut")

			elif not lokasi_skg:
				print("Tidak ada lagi yang bisa naik ke perahu")
				input("enter untuk kembali")
			elif len(perahu.isi_perahu) == 2:
				print("Perahu sudah penuh")
				input("enter untuk kembali")

		elif pilih == "c":
			if perahu.isi_perahu:
				clear_screen()

				print("Perahu akan segera berangkat")
				sleep(2)
				print("Perahu sedang dalam perjalanan")
				sleep(3)
				perahu.kordinat = not perahu.kordinat
				print("perahu sudah sampai ke lokasi")
				sleep(1)

				input("enter untuk lanjut")
				clear_screen()

				x = test_peraturan(perahu, lokasi_skg)
				break
			else:
				print("Perahu masih kosong, tidak bisa berangkat")
				input("enter untuk kembali")

		elif pilih == "d":
			status(perahu, lokasi_skg, lokasi_lain)

		elif pilih == "x":
			print("\n\npermainan berakhir...")
			sleep(1)
			clear_screen()
			quit()

		else:
			print("INPUT SALAH!!!")

	return x

def menyebrang(perahu, lokasiA, lokasiB):
	if perahu.kordinat:
		return proses_naik_turun_perahu(perahu, lokasiB, lokasiA)

	elif not perahu.kordinat and lokasiA:
		return proses_naik_turun_perahu(perahu, lokasiA, lokasiB)

def turun_perahu(perahu, lokasiA, lokasiB):
	status(perahu, lokasiA, lokasiB)

	if perahu.kordinat:
		print("\n\nPerahu sudah sampai di lokasi B")
		proses_naik_turun_perahu(perahu, lokasiA, lokasiB)

	else:
		print("Perahu sudah sampai di lokasi A")
		proses_naik_turun_perahu(perahu, lokasiA, lokasiB)

def cek_menang(perahu, lokasi_skg):
	if perahu.kordinat and len(lokasi_skg) == 4:
		clear_screen()
		sleep(2)
		print("Sudah sampai dengan selamat ke lokasi B")
		print("\n\n\nANDA ADALAH JUARANYAAA...")
		input("\n\n\nenter untuk lanjut...")
		clear_screen()
		print("game akan direset setelah 3 detik...")
		sleep(3)
		return True
	else:
		return False

def test_peraturan(perahu, lokasi_skg):
	clear_screen()
	if len(lokasi_skg) == 2:
		try:
			if (lokasi_skg[0].nama == lokasi_skg[1],makanan):
				clear_screen()
				print("Melakukan Test Peraturan....")
				sleep(3)
				print("Terdapat Pelanggaran di lokasi")
				print(lokasi_skg[0].nama, "tidak boleh bersama dengan", lokasi_skg[1].nama)
				sleep(1)
				print("\n\n.....GAME OVER.....")
				input("\n\nenter untuk lanjut...")
				clear_screen()
				print("\n\ngame akan direset dalam 2 detik...")
				sleep(3)

				return True
		except:
			pass

	else:
		return False

ayam = karakter("Ayam", False, "Harimau", "Gabah")
gabah = karakter("Gabah", False, "Ayam", None)
harimau = karakter("Harimau", False, None, "Ayam")
petani = karakter("Petani", False, None, None)
perahu = perahu(False, [])
x = True

while  True:
	if x:
		lokasiB = []
		lokasiA = []
		perahu.isi_perahu = []
		perahu.kordinat = False

		start_game(ayam, gabah, harimau, petani, lokasiA)

	x = menyebrang(perahu, lokasiA, lokasiB)