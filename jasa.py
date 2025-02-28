def hitung_biaya_pengiriman(berat, jarak, express=False, member=False):
    """
    Menghitung total biaya pengiriman berdasarkan faktor berat, jarak, jenis pengiriman, dan status keanggotaan.
    
    Parameter:
    berat (float): Berat paket dalam kg.
    jarak (float): Jarak pengiriman dalam km.
    express (bool): True jika memilih layanan express, False jika biasa.
    member (bool): True jika pelanggan adalah member, False jika non-member.
    
    Returns:
    int: Total biaya pengiriman dalam Rupiah.
    """
    # Biaya dasar
    biaya = 10000
    
    # Tambahan biaya untuk berat lebih dari 5 kg
    if berat > 5:
        biaya += 5000
    
    # Tambahan biaya untuk jarak lebih dari 10 km
    if jarak > 10:
        biaya += 8000
    
    # Tambahan biaya untuk layanan express
    if express:
        biaya += 20000
    
    # Diskon 10% untuk member
    if member:
        biaya *= 0.9
    
    return int(biaya)  # Mengembalikan hasil sebagai bilangan bulat

# Contoh penggunaan
if __name__ == "__main__":
    berat_paket = float(input("Masukkan berat paket (kg): "))
    jarak_pengiriman = float(input("Masukkan jarak pengiriman (km): "))
    express_option = input("Apakah menggunakan layanan express? (ya/tidak): ").strip().lower() == "ya"
    member_status = input("Apakah pelanggan adalah member? (ya/tidak): ").strip().lower() == "ya"
    
    biaya_total = hitung_biaya_pengiriman(berat_paket, jarak_pengiriman, express=express_option, member=member_status)
    print(f"Total biaya pengiriman: Rp {biaya_total}")
