import asyncio
import tkinter as tk
from tkinter import messagebox
import json
import os
from tapo import ApiClient
from cryptography.fernet import Fernet
import webbrowser
from zeroconf import ServiceBrowser, Zeroconf

# ✅ AppData klasörünü kullan
APPDATA = os.path.expanduser("~\\AppData\\Local\\TapoController")
if not os.path.exists(APPDATA):
    os.makedirs(APPDATA)

CONFIG_FILE = os.path.join(APPDATA, "tapo_config.json")
KEY_FILE = os.path.join(APPDATA, "tapo_key.key")

class CryptoManager:
    def __init__(self):
        self.key = self.load_or_create_key()
        self.cipher = Fernet(self.key)

    def load_or_create_key(self):
        if os.path.exists(KEY_FILE):
            with open(KEY_FILE, "rb") as f:
                return f.read()
        else:
            key = Fernet.generate_key()
            with open(KEY_FILE, "wb") as f:
                f.write(key)
            return key

    def encrypt(self, data):
        return self.cipher.encrypt(data.encode()).decode()

    def decrypt(self, encrypted_data):
        return self.cipher.decrypt(encrypted_data.encode()).decode()

crypto = CryptoManager()

class TapoLogin:
    def __init__(self, root, callback):
        self.root = root
        self.callback = callback
        self.root.title("Tapo Giriş")
        self.root.geometry("380x420")
        self.root.configure(bg="#2c3e50")
        self.root.resizable(False, False)

        tk.Label(root, text="🔐 Tapo Giriş",
                font=("Arial", 16, "bold"), bg="#2c3e50", fg="white").pack(pady=10)

        tk.Label(root, text="Email:", font=("Arial", 10), bg="#2c3e50", fg="white").pack()
        self.email_entry = tk.Entry(root, font=("Arial", 10), width=30)
        self.email_entry.pack(pady=3)

        tk.Label(root, text="Şifre:", font=("Arial", 10), bg="#2c3e50", fg="white").pack()
        self.password_entry = tk.Entry(root, font=("Arial", 10), width=30, show="*")
        self.password_entry.pack(pady=3)

        tk.Button(root, text="Şifremi Unuttum", bg="#e67e22", fg="white",
                 font=("Arial", 9, "bold"), command=self.reset_password).pack(pady=3)

        tk.Label(root, text="Ampul IP:", font=("Arial", 10), bg="#2c3e50", fg="white").pack(pady=(10, 3))
        self.ip_entry = tk.Entry(root, font=("Arial", 10), width=30)
        self.ip_entry.pack(pady=3)

        tk.Button(root, text="Nasıl Bulurum?", bg="#3498db", fg="white",
                 font=("Arial", 9, "bold"), command=self.show_help).pack(pady=3)

        self.status_label = tk.Label(root, text="", font=("Arial", 9), bg="#2c3e50", fg="#f39c12")
        self.status_label.pack(pady=5)

        self.login_btn = tk.Button(root, text="GİRİŞ YAP", bg="#27ae60", fg="white",
                                  font=("Arial", 12, "bold"), width=20,
                                  command=self.login)
        self.login_btn.pack(pady=15)

    def reset_password(self):
        """Şifre sıfırla linkine git"""
        webbrowser.open("https://tapo.tplinkcloud.com/tapo_web/#/login/forgotPassword")

    def show_help(self):
        """IP nasıl bulunur göster"""
        help_text = """
📱 Tapo Uygulamasından IP Adresini Bulma:

1. Telefonunuzda Tapo uygulamasını açın
2. Ampulünüzü seçin (sol tarafta listelenen cihazlar)
3. Sağ üst köşedeki ⚙️ (Ayarlar) ikonuna basın
4. "Cihaz Bilgileri" veya "Device Info" seçeneğine basın
5. "IP Adresi" veya "IP Address" kısmında IP'yi göreceksiniz

Örnek IP: 192.168.1.100

✅ Bu IP'yi yukarıdaki kutucuğa girin
        """
        messagebox.showinfo("IP Nasıl Bulurum?", help_text)

    def login(self):
        email = self.email_entry.get().strip()
        password = self.password_entry.get().strip()
        ip = self.ip_entry.get().strip()

        if not email or not password or not ip:
            messagebox.showerror("Hata", "Tüm alanları doldurun!")
            return

        # Verileri şifrele
        encrypted_email = crypto.encrypt(email)
        encrypted_password = crypto.encrypt(password)
        encrypted_ip = crypto.encrypt(ip)

        config = {
            "email": encrypted_email,
            "password": encrypted_password,
            "ip": encrypted_ip
        }

        with open(CONFIG_FILE, "w") as f:
            json.dump(config, f)

        messagebox.showinfo("OK", "Giriş bilgileri şifrelenmiş şekilde kaydedildi!")
        self.callback()

class CustomSlider(tk.Canvas):
    def __init__(self, parent, from_=1, to=100, command=None, width=250):
        super().__init__(parent, width=width, height=40, bg="#34495e", highlightthickness=0)
        self.from_ = from_
        self.to = to
        self.command = command
        self.value = 70

        self.bind("<Button-1>", self.on_click)
        self.bind("<B1-Motion>", self.on_drag)
        self.bind("<Configure>", self.on_configure)

    def on_configure(self, event):
        self.redraw()

    def on_click(self, event):
        self.value = int((event.x / self.winfo_width()) * (self.to - self.from_) + self.from_)
        self.value = max(self.from_, min(self.to, self.value))
        if self.command:
            self.command(self.value)
        self.redraw()

    def on_drag(self, event):
        self.on_click(event)

    def redraw(self):
        self.delete("all")
        width = self.winfo_width()
        height = self.winfo_height()

        if width < 2 or height < 2:
            return

        self.create_line(5, height//2, width-5, height//2, fill="#7f8c8d", width=3)
        filled_width = ((self.value - self.from_) / (self.to - self.from_)) * (width - 10) + 5
        self.create_line(5, height//2, filled_width, height//2, fill="#3498db", width=3)
        self.create_oval(filled_width-8, height//2-8, filled_width+8, height//2+8, fill="#3498db", outline="#2980b9")
        self.create_text(width//2, 8, text=f"{self.value}%", fill="white", font=("Arial", 9, "bold"))

    def set(self, value):
        self.value = value
        self.redraw()

class TapoGUI:
    def __init__(self, root, email, password, ip):
        self.root = root
        self.root.title("Tapo L530")
        self.root.geometry("380x620")
        self.root.configure(bg="#2c3e50")

        self.email = email
        self.password = password
        self.ip = ip
        self.client = ApiClient(email, password)
        self.device = None

        tk.Label(root, text="💡 Tapo Kontrol",
                font=("Arial", 18, "bold"), bg="#2c3e50", fg="white").pack(pady=10)

        btn_frame = tk.Frame(root, bg="#2c3e50")
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="AC ✓", bg="#27ae60", fg="white",
                 font=("Arial", 12, "bold"), width=10,
                 command=self.turn_on).pack(side="left", padx=5)

        tk.Button(btn_frame, text="KAPAT ✗", bg="#e74c3c", fg="white",
                 font=("Arial", 12, "bold"), width=10,
                 command=self.turn_off).pack(side="left", padx=5)

        tk.Label(root, text="Parlaklık", font=("Arial", 10), bg="#2c3e50", fg="white").pack()
        self.brightness_slider = CustomSlider(root, from_=1, to=100,
                                             command=self.set_brightness, width=250)
        self.brightness_slider.pack(pady=5, padx=20)
        self.brightness_slider.set(70)

        tk.Label(root, text="Renk Seç", font=("Arial", 10), bg="#2c3e50", fg="white").pack(pady=(10, 5))

        colors_frame = tk.Frame(root, bg="#2c3e50")
        colors_frame.pack()

        self.colors = {
            "🔴 Kırmızı": 0,
            "🟢 Yeşil": 120,
            "🔵 Mavi": 240,
            "🟡 Sarı": 60,
            "⚪ Beyaz": 0
        }

        for color_name, hue in self.colors.items():
            tk.Button(colors_frame, text=color_name, font=("Arial", 9),
                     width=15, command=lambda h=hue, n=color_name: self.set_color(h, n)).pack(pady=2)

        # Custom Renk Girişi
        tk.Label(root, text="Custom Renk (0-360)", font=("Arial", 9), bg="#2c3e50", fg="#ecf0f1").pack(pady=(10, 3))

        custom_frame = tk.Frame(root, bg="#2c3e50")
        custom_frame.pack()

        tk.Label(custom_frame, text="Hue:", font=("Arial", 9), bg="#2c3e50", fg="white").pack(side="left", padx=5)
        self.custom_hue_entry = tk.Entry(custom_frame, font=("Arial", 10), width=12)
        self.custom_hue_entry.pack(side="left", padx=5)
        self.custom_hue_entry.insert(0, "0")

        tk.Button(custom_frame, text="Uygula", bg="#9b59b6", fg="white",
                 font=("Arial", 9, "bold"), command=self.apply_custom_color).pack(side="left", padx=5)

        # Durum
        self.status_label = tk.Label(root, text="Bağlanıyor...",
                                    font=("Arial", 9), bg="#2c3e50", fg="#f39c12")
        self.status_label.pack(pady=10)

        tk.Button(root, text="ÇIKIŞ YAP", bg="#95a5a6", fg="white",
                 font=("Arial", 11, "bold"), width=20,
                 command=self.logout).pack(pady=10)

        self.root.after(100, self.connect_device)

    async def async_connect(self):
        try:
            self.device = await self.client.l530(self.ip)
            self.status_label.config(text="✓ Bağlandı", fg="#27ae60")
            await self.device.set_brightness(70)
        except Exception as e:
            self.status_label.config(text=f"✗ Bağlantı hatası", fg="#e74c3c")

    def connect_device(self):
        try:
            asyncio.run(self.async_connect())
        except:
            self.root.after(2000, self.connect_device)

    async def async_turn_on(self):
        try:
            await self.device.on()
            self.status_label.config(text="✓ AÇILDI", fg="#27ae60")
        except:
            self.status_label.config(text="✗ Hata", fg="#e74c3c")

    def turn_on(self):
        try:
            asyncio.run(self.async_turn_on())
        except:
            pass

    async def async_turn_off(self):
        try:
            await self.device.off()
            self.status_label.config(text="✓ KAPANDI", fg="#e74c3c")
        except:
            self.status_label.config(text="✗ Hata", fg="#e74c3c")

    def turn_off(self):
        try:
            asyncio.run(self.async_turn_off())
        except:
            pass

    async def async_set_brightness(self, value):
        try:
            if self.device:
                await self.device.set_brightness(int(value))
        except:
            pass

    def set_brightness(self, value):
        try:
            asyncio.run(self.async_set_brightness(value))
        except:
            pass

    async def async_set_color(self, hue, color_name):
        try:
            if self.device:
                if color_name == "⚪ Beyaz":
                    await self.device.set_color_temperature(6500)
                else:
                    await self.device.set_hue_saturation(hue, 100)
                self.status_label.config(text=f"✓ {color_name}", fg="#27ae60")
        except Exception as e:
            self.status_label.config(text=f"✗ Renk hatası", fg="#e74c3c")

    def set_color(self, hue, color_name):
        try:
            asyncio.run(self.async_set_color(hue, color_name))
        except Exception as e:
            pass

    def apply_custom_color(self):
        """Custom renkle hue değerini uygula"""
        try:
            hue_str = self.custom_hue_entry.get().strip()

            if not hue_str:
                messagebox.showerror("Hata", "Hue değeri girin!")
                return

            hue = int(hue_str)

            if not (0 <= hue <= 360):
                messagebox.showerror("Hata", "Hue değeri 0-360 arasında olmalı!")
                return

            asyncio.run(self.async_set_color(hue, f"Custom ({hue}°)"))
        except ValueError:
            messagebox.showerror("Hata", "Lütfen geçerli bir sayı girin!")

    def logout(self):
        if os.path.exists(CONFIG_FILE):
            os.remove(CONFIG_FILE)
        if os.path.exists(KEY_FILE):
            os.remove(KEY_FILE)
        messagebox.showinfo("Çıkış", "Bilgiler silindi!")
        self.root.quit()

def main():
    root = tk.Tk()

    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            config = json.load(f)

        try:
            email = crypto.decrypt(config["email"])
            password = crypto.decrypt(config["password"])
            ip = crypto.decrypt(config["ip"])
            gui = TapoGUI(root, email, password, ip)
        except Exception as e:
            messagebox.showerror("Hata", f"Veri deşifreleme hatası: {str(e)}")
            root.quit()
    else:
        def go_to_gui():
            root.destroy()
            new_root = tk.Tk()
            with open(CONFIG_FILE, "r") as f:
                config = json.load(f)

            try:
                email = crypto.decrypt(config["email"])
                password = crypto.decrypt(config["password"])
                ip = crypto.decrypt(config["ip"])
                gui = TapoGUI(new_root, email, password, ip)
            except Exception as e:
                messagebox.showerror("Hata", f"Veri deşifreleme hatası: {str(e)}")
                new_root.quit()

        login = TapoLogin(root, go_to_gui)

    root.mainloop()

if __name__ == "__main__":
    main()
