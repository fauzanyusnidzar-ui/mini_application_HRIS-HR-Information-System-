from tabulate import tabulate

accounts = {
    "admin01": {"password": "admin123", "role": "admin", "blocked": False, "fail": 0},
    "spv01": {"password": "spv123", "role": "supervisor", "blocked": False, "fail": 0},
    "user01": {"password": "user123", "role": "user", "blocked": False, "fail": 0},
    "super01": {"password": "super123", "role": "super_admin", "blocked": False, "fail": 0},
}

employees = [
    {
        "nip": "1001",
        "nama": "Alucard Dark Slayer",
        "ttl": "Land of Dawn, 12 Jan 1998",
        "alamat_ktp": "Moniyan Empire",
        "alamat_tinggal": "Castle of Light",
        "hp": "081111001",
        "rumah": "02110001",
        "emergency": "Tigreal",
        "riwayat": "Demon Hunter Squad",
        "pangkat": "Officer",
        "gaji": 12000000,
        "departemen": "Jungler"
    },
    {
        "nip": "1002",
        "nama": "Miya Moonlight Archer",
        "ttl": "Moonlit Forest, 3 Mar 2000",
        "alamat_ktp": "Azrya Woodlands",
        "alamat_tinggal": "Elven Base",
        "hp": "081111002",
        "rumah": "02110002",
        "emergency": "Estes",
        "riwayat": "Moon Elf Guard",
        "pangkat": "Assistant",
        "gaji": 9500000,
        "departemen": "Gold Lane"
    },
    {
        "nip": "1003",
        "nama": "Chou Kungfu Master",
        "ttl": "Cadia Riverlands, 7 Jul 1997",
        "alamat_ktp": "Eastern Region",
        "alamat_tinggal": "Dragon Temple",
        "hp": "081111003",
        "rumah": "02110003",
        "emergency": "Ling",
        "riwayat": "Martial Arts School",
        "pangkat": "Senior Officer",
        "gaji": 13000000,
        "departemen": "Roamer"
    },
    {
        "nip": "1004",
        "nama": "Layla Energy Gunner",
        "ttl": "Eruditio, 1 Mei 2001",
        "alamat_ktp": "Scientific City",
        "alamat_tinggal": "Tech District",
        "hp": "081111004",
        "rumah": "02110004",
        "emergency": "Lolita",
        "riwayat": "Energy Lab",
        "pangkat": "Assistant",
        "gaji": 9000000,
        "departemen": "Gold Lane"
    },
    {
        "nip": "1005",
        "nama": "Gusion Holy Blade",
        "ttl": "Paxley House, 9 Sep 1999",
        "alamat_ktp": "Magic Academy",
        "alamat_tinggal": "Noble District",
        "hp": "081111005",
        "rumah": "02110005",
        "emergency": "Aamon",
        "riwayat": "Magic Assassin Guild",
        "pangkat": "Officer",
        "gaji": 12500000,
        "departemen": "Jungler"
    }
]

resign_employees = [
    {
        "nip": "2001",
        "nama": "Argus Fallen Angel",
        "ttl": "Moniyan Empire, 10 Okt 1996",
        "alamat_ktp": "Dark Abyss",
        "alamat_tinggal": "Shadow Realm",
        "hp": "082222001",
        "rumah": "02120001",
        "emergency": "Rafaela",
        "riwayat": "Dark Forces",
        "pangkat": "Officer",
        "gaji": 11000000,
        "departemen": "EXP Lane"
    },
    {
        "nip": "2002",
        "nama": "Hanzo Akuma Ninja",
        "ttl": "Scarlet Village, 5 Mei 1995",
        "alamat_ktp": "Cadia Riverlands",
        "alamat_tinggal": "Forbidden Temple",
        "hp": "082222002",
        "rumah": "02120002",
        "emergency": "Hanabi",
        "riwayat": "Shadow Sect",
        "pangkat": "Senior Officer",
        "gaji": 11500000,
        "departemen": "Jungler"
    }
]

account_requests = []

def kembali():
    input("\nTekan ENTER untuk kembali...")

def cari_karyawan(nip):
    for emp in employees:
        if emp["nip"] == nip:
            return emp
    return None

def cari_resign(nip):
    for emp in resign_employees:
        if emp["nip"] == nip:
            return emp
    return None

def login():
    while True:
        print("\n===== LOGIN =====")
        user_id = input("User ID : ")
        password = input("Password: ")

        if user_id not in accounts:
            print("User tidak ditemukan")
            continue

        user = accounts[user_id]

        if user["blocked"]:
            print("Account anda terblokir")
            continue

        if password == user["password"]:
            return user_id, user["role"]
        else:
            user["fail"] += 1
            print("Password salah!")

            if user["fail"] == 3:
                user["blocked"] = True
                print("Account anda terblokir")

def lihat_data_karyawan():
    print("DATA KARYAWAN")
    keyword = input("Cari berdasarkan NIP / Nama (kosongkan untuk semua): ").strip().lower()

    if keyword == "":
        data = employees
    else:
        data = []
        for emp in employees:
            if (keyword in emp["nip"].lower()) or (keyword in emp["nama"].lower()):
                data.append(emp)

    if not data:
        print("Data tidak ditemukan")
        kembali()
        return

    rows = []
    for e in data:
        rows.append([
            e["nip"],
            e["nama"],
            e["ttl"],
            e["hp"],
            e["departemen"]
        ])

    print(tabulate(
        rows,
        headers=["NIP", "Nama", "TTL", "HP", "Departemen"],
        tablefmt="simple_grid"
    ))

    kembali()

def lihat_pangkat_gaji():
    nip = input("Masukkan NIP: ")
    emp = cari_karyawan(nip)

    if emp:
        rows = [[
            emp["nip"],
            emp["nama"],
            emp["pangkat"],
            f"Rp {emp['gaji']:,}"
        ]]

        print(tabulate(
            rows,
            headers=["NIP", "Nama", "Pangkat", "Gaji"],
            tablefmt="simple_grid"
        ))
    else:
        print("Data tidak ditemukan")

    kembali()

def tambah_karyawan():
    while True:
        print("TAMBAH KARYAWAN")

        data = {
            "nip": input("NIP: "),
            "nama": input("Nama: "),
            "ttl": input("TTL: "),
            "alamat_ktp": input("Alamat KTP: "),
            "alamat_tinggal": input("Alamat Tinggal: "),
            "hp": input("No HP: "),
            "rumah": input("No Rumah: "),
            "emergency": input("Emergency Contact: "),
            "riwayat": input("Riwayat Kerja: "),
            "pangkat": input("Pangkat: "),
            "gaji": int(input("Gaji: ")),
            "departemen": input("departemen: ") 
        }

        confirm = input("Yakin tambah data? (Y/N): ").upper()
        if confirm == "Y":
            employees.append(data)
            print("Data karyawan berhasil ditambahkan")

        lagi = input("Tambah lagi? (Y/N): ").upper()
        if lagi == "N":
            break

    kembali()

def update_karyawan():
    nip = input("Masukkan NIP: ")
    emp = cari_karyawan(nip)

    if not emp:
        print("Data tidak ditemukan")
        kembali()
        return

    print("UPDATE DATA KARYAWAN")
    print("Kosongkan jika tidak ingin mengubah data.\n")

    new_nip = input(f"NIP ({emp['nip']}): ").strip()
    new_nama = input(f"Nama ({emp['nama']}): ").strip()
    new_ttl = input(f"TTL ({emp['ttl']}): ").strip()
    new_alamat_ktp = input(f"Alamat KTP ({emp['alamat_ktp']}): ").strip()
    new_alamat_tinggal = input(f"Alamat Tinggal ({emp['alamat_tinggal']}): ").strip()
    new_hp = input(f"No HP ({emp['hp']}): ").strip()
    new_rumah = input(f"No Rumah ({emp['rumah']}): ").strip()
    new_emergency = input(f"Emergency ({emp['emergency']}): ").strip()
    new_riwayat = input(f"Riwayat Kerja ({emp['riwayat']}): ").strip()
    new_pangkat = input(f"Pangkat ({emp['pangkat']}): ").strip()
    new_gaji = input(f"Gaji ({emp['gaji']}): ").strip()
    new_departemen = input(f"departemen({emp['departemen']}): ").strip()

    confirm = input("Yakin update data? (Y/N): ").upper()

    if confirm == "Y":
        if new_nip: 
            emp["nip"] = new_nip
        if new_nama: 
            emp["nama"] = new_nama
        if new_ttl: 
            emp["ttl"] = new_ttl
        if new_alamat_ktp: 
            emp["alamat_ktp"] = new_alamat_ktp
        if new_alamat_tinggal: 
            emp["alamat_tinggal"] = new_alamat_tinggal
        if new_hp: 
            emp["hp"] = new_hp
        if new_rumah: 
            emp["rumah"] = new_rumah
        if new_emergency: 
            emp["emergency"] = new_emergency
        if new_riwayat: 
            emp["riwayat"] = new_riwayat
        if new_pangkat: 
            emp["pangkat"] = new_pangkat
        if new_gaji: 
            emp["gaji"] = int(new_gaji)
        if new_departemen: 
            emp["departemen"] = new_departemen

        print("Data karyawan berhasil diupdate")
    else:
        print("Update dibatalkan")

    kembali()

def tambah_resign():
    nip = input("Masukkan NIP resign: ")
    emp = cari_karyawan(nip)

    if not emp:
        print("Data tidak ditemukan")
        kembali()
        return

    confirm = input("Yakin resign-kan? (Y/N): ").upper()

    if confirm == "Y":
        idx = employees.index(emp)       
        removed_emp = employees.pop(idx)  

        resign_employees.append(removed_emp)

        print(f"{removed_emp['nama']} dipindahkan ke daftar resign")

    kembali()


def lihat_resign():
    print("DATA KARYAWAN RESIGN")
    keyword = input("Cari berdasarkan NIP / Nama (kosongkan untuk semua): ").strip().lower()

    if keyword == "":
        data = resign_employees
    else:
        data = []
        for emp in resign_employees:
            if (keyword in emp["nip"].lower()) or (keyword in emp["nama"].lower()):
                data.append(emp)

    if not data:
        print("Data tidak ditemukan")
        kembali()
        return

    rows = []
    for e in data:
        rows.append([
            e["nip"],
            e["nama"],
            e["ttl"],
            e["departemen"],
            e["hp"]
        ])

    print(tabulate(
        rows,
        headers=["NIP", "Nama", "TTL", "Departemen", "HP"],
        tablefmt="simple_grid"
    ))

    kembali()

def request_account(action):
    role = input("Role (user/supervisor/admin): ").strip().lower()
    uid = input("User ID: ").strip()

    req_data = {
        "action": action,
        "role": role,
        "user_id": uid
    }

    if action == "add":
        password = input("Password akun baru: ").strip()
        req_data["password"] = password

    if action == "delete":
        if uid not in accounts:
            print("User tidak ditemukan")
            kembali()
            return

        if accounts[uid]["role"] == "super_admin":
            print("Super Admin tidak boleh dihapus!")
            kembali()
            return

    confirm = input("Kirim request? (Y/N): ").upper()

    if confirm == "Y":
        account_requests.append(req_data)
        print("Request sudah dijalankan")
    if confirm == "N":
        print("Request dibatalkan")
    elif confirm != "N" and confirm !="Y" :
        print("Harus diisi Y/N")

    kembali()

def super_admin_menu():
    while True:
        print("MENU SUPER ADMIN")
        print("1. Konfirmasi Request")
        print("2. Lihat Semua Account")
        print("0. Logout")

        pilih = input("Pilih: ")

        if pilih == "1":
            for req in account_requests:
                print(f"request : {req["action"]}")
                print(f"role : {req["role"]}")
                print(f"user_name : {req["user_id"]}")
                print("Password : *********")
                conf = input("Setujui? (Y/N): ").upper()

                if req["action"] == "add" and conf == "Y":
                    accounts[req["user_id"]] = {
                    "password": req["password"],
                    "role": req["role"],
                    "blocked": False,
                    "fail": 0
                                }
                    print("Account berhasil ditambahkan")


                elif req["action"] == "delete" and conf == "Y":
                    accounts.pop(req["user_id"], None)

            account_requests.clear()

        elif pilih == "2":
            for u, d in accounts.items():
                print(u, "-", d["role"], "- blocked:", d["blocked"])
            kembali()

        elif pilih == "0":
            break

def menu_user():
    while True:
        print("1. Lihat Data Karyawan")
        print("2. Lihat Karyawan Resign")
        print("0. Logout")
        p = input("Pilih: ")

        if p == "1":
            lihat_data_karyawan()
        elif p == "2":
            lihat_resign()
        elif p == "0":
            break

def menu_admin():
    while True:
        print("""
MENU ADMIN
1. Lihat Data Karyawan
2. Lihat Pangkat & Gaji
3. Tambah Karyawan
4. Lihat Resign
5. Tambah Resign
6. Update Data
7. Request Add Account
8. Request Delete Account
0. Logout
""")
        p = input("Pilih: ")

        if p == "1": lihat_data_karyawan()
        elif p == "2": lihat_pangkat_gaji()
        elif p == "3": tambah_karyawan()
        elif p == "4": lihat_resign()
        elif p == "5": tambah_resign()
        elif p == "6": update_karyawan()
        elif p == "7": request_account("add")
        elif p == "8": request_account("delete")
        elif p == "0": break

def menu_supervisor():
    while True:
        print("MENU SUPERVISOR")
        print("1. Lihat Data Karyawan")
        print("2. Lihat Pangkat & Gaji")  
        print("3. Lihat Karyawan Resign")
        print("0. Logout")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            lihat_data_karyawan()

        elif pilih == "2":
            lihat_pangkat_gaji()   

        elif pilih == "3":
            lihat_resign()

        elif pilih == "0":
            break

        else:
            print("Menu tidak tersedia")

def main():
    while True:
        user_id, role = login()

        if role == "admin":
            menu_admin()
        elif role  == "user":
            menu_user()
        elif role == "supervisor" :
            menu_supervisor()
        elif role == "super_admin":
            super_admin_menu()

main()




