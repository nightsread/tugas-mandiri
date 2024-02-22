# Fungsi untuk menghitung berat badan ideal
def hitung_bb_ideal(tinggi, jk):
    if jk.lower() == 'pria':
        bb_ideal = (tinggi - 100) - ((tinggi - 100) * 10 / 100)
    elif jk.lower() == 'wanita':
        bb_ideal = (tinggi - 100) - ((tinggi - 100) * 15 / 100)
    else:
        bb_ideal = None
    return bb_ideal

# Input tinggi dan jenis kelamin dari pengguna
tinggi = float(input("Masukkan tinggi (dalam cm): "))
jk = input("Masukkan jenis kelamin (pria/wanita): ")

# Memanggil fungsi hitung_bb_ideal
bb_ideal = hitung_bb_ideal(tinggi, jk)

# Menampilkan hasil
if bb_ideal is not None:
    print(f"Berat badan ideal Anda adalah {bb_ideal:.2f} kg")
else:
    print("Data yang Anda masukkan tidak valid.")
