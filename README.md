# 💡 Tapo L530 Kontrol Uygulaması

TP-Link Tapo akıllı ampulünüzü PC'nizden kolayca kontrol edin!

## 🚀 Hoş Geldiniz

Bu uygulama, TP-Link Tapo L530 akıllı ampulünüzü bilgisayarınızdan kontrol etmenizi sağlar. Parlaklığı ayarlayın, renkleri değiştirin - hepsi modern bir GUI arayüzüyle.

## ✨ Özellikler

- 💡 **Ampulu AC/KAPAT** - Anında kontrol
- 🔆 **Parlaklık Ayarı** - %1-100 aralığında
- 🎨 **Renk Yönetimi** - 5 hazır renk + custom renk (0-360 Hue)
- 🔒 **Şifrelenmiş Veri** - AES-256 ile güvenli
- ⚡ **Hafif** - Sadece 21 MB
- 🌐 **Türkçe Arayüz** - Kullanımı kolay

## 📋 Sistem Gereksinimleri

- Windows 7 veya üstü
- TP-Link Tapo L530 akıllı ampul
- Tapo hesabı (email ve şifre)
- Ampulün IP adresi

---

## 📥 Kurulum - 3 Seçenek

### ⭐ **Seçenek 1: EXE İndir (ÖNERİLEN)**

En kolay yöntem! Python kurmanıza gerek yok.

1. GitHub sayfasındaki **Releases** bölümüne gidin
2. `tapocontrol.exe` dosyasını indirin (21 MB) https://github.com/mergenaltay/TapoController/releases/download/Releases/tapocontrol.exe
3. Dosyaya **çift tıklayarak** uygulamayı çalıştırın
4. Tapo hesap bilgilerinizi girin
5. **Başlamaya hazırsınız! 🎉**

**Avantajları:**
- ✅ Python kurulumu gerekmez
- ✅ Hızlı indirme ve çalıştırma
- ✅ Tüm bağımlılıklar dahil
- ✅ Taşınabilir (USB'de taşıyabilirsiniz)

---

### 📦 **Seçenek 2: Git Clone + Batch (ORTA)**

Python yüklü olması gerekir!

#### 1️⃣ Python Yükleyin (Henüz yoksa)

- https://www.python.org/downloads/ adresinden indirin
- **Kurulum sırasında "Add Python to PATH" kutusunu işaretleyin!**

#### 2️⃣ Repo Klonlayın

Komut Satırı (PowerShell veya CMD) aç ve şunu yaz:

git clone https://github.com/senusername/tapo-controller.git
cd tapo-controller


#### 3️⃣ Batch Dosyasını Çalıştırın

- Windows Explorer'da klasörü aç
- `kurulum.bat` dosyasını **çift tıkla**
- Otomatik olarak kütüphaneler kurulacak ve app başlayacak

**Avantajları:**
- ✅ Kaynak kodu görebilirsiniz
- ✅ Batch dosyası tüm işleri otomatik yapar
- ✅ Güncellemeleri kolayca alabilirsiniz

---

### 🔧 **Seçenek 3: Advanced - Terminal (İLERİ)**

Geliştiriciler için! Terminal ile manuel kurulum.

#### 1️⃣ Ön Koşullar

- Python 3.8 veya üstü yüklü olmalı
- Git yüklü olmalı

#### 2️⃣ PowerShell'i Yönetici Olarak Aç

Windows'da PowerShell'i sağ tıkla → "Yönetici olarak çalıştır"

#### 3️⃣ Repo Klonlayın

git clone https://github.com/senusername/tapo-controller.git
cd tapo-controller

#### 4️⃣ Kütüphaneleri Yükleyin
pip install -r requirements.txt

#### 5️⃣ Uygulamayı Çalıştırın
python tapocontrol.py

**Avantajları:**
- ✅ Tam kontrol ve esneklik
- ✅ Kodu değiştirebilirsiniz
- ✅ Debugging ve geliştirme için ideal

---

## 📊 Yöntem Karşılaştırması

| Özellik | EXE | Batch | Terminal |
|---------|-----|-------|----------|
| **Python gerekli** | ❌ Hayır | ✅ Evet | ✅ Evet |
| **Zorluk** | ⭐ Çok kolay | ⭐⭐ Orta | ⭐⭐⭐ İleri |
| **Kurulum süresi** | 30 sn | 1 dk | 2 dk |
| **Dosya boyutu** | 21 MB | 50+ MB | 50+ MB |
| **Taşınabilir** | ✅ Evet | ❌ Hayır | ❌ Hayır |

---

## 🔧 Sorun Giderme

### ❓ Python yüklü değil diyorsa

- Python'u indirin: https://www.python.org/downloads/
- **Kurulum sırasında "Add Python to PATH" kutusunu işaretleyin!**
- PowerShell'i yeniden aç

### ❓ Ampul bağlantısı başarısız

Kontrol edilecekler:
- Tapo hesap bilgileriniz doğru mu?
- Ampulün IP adresi doğru mu? (Tapo app'tan kontrol edin)
- Ampul aynı WiFi ağında mı?
- İnternet bağlantısı stabil mi?

### ❓ Renk ayarı çalışmıyor

- Tapo uygulamasında ampulün renk kontrol özelliği etkinleştirilmiş olduğundan emin olun

### ❓ Git bulunamıyor diyorsa

- Git'i indirin: https://git-scm.com/download/win
- PowerShell'i yeniden aç

---

## 📞 Destek & Geri Bildirim

- 🐛 **Hata mı buldunuz?** → Issues bölümüne yazın
- 💡 **Fikriniz mi var?** → Discussions açın
- 🤝 **Katkı sağlamak mı istiyorsunuz?** → Pull Request gönderin

---

## 📦 İçerikler

tapo-controller/
├── tapocontrol.py # Ana Python dosyası
├── requirements.txt # Kütüphane listesi
├── kurulum.bat # Windows batch dosyası
├── README.md # Bu dosya
└── .gitignore # Git ignore kuralları


---

## 🔒 Güvenlik

- ✅ Tüm giriş bilgileri **AES-256** ile şifrelenir
- ✅ Şifreli veriler `AppData` klasöründe saklanır
- ✅ Kaynak kodu açık, inceleyebilirsiniz
- ✅ Şifre sıfırlama linki doğrudan TP-Link'e yönlendirir

---

## 📄 Lisans

MIT Lisansı

---

## 🙏 Teşekkürler

- TP-Link Tapo API
- Python topluluğu
- Siz! (Bu projeyi kullanan herkes)

---

**🔐 Tüm veriler AES-256 ile şifrelenmiş olarak saklanır**


