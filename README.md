<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tapo L530 Kontrol Uygulaması</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        
        .container {
            max-width: 1000px;
            margin: 0 auto;
            background: white;
            border-radius: 12px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            overflow: hidden;
        }
        
        header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 40px 20px;
            text-align: center;
        }
        
        header h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 15px;
        }
        
        header p {
            font-size: 1.1em;
            opacity: 0.9;
        }
        
        .content {
            padding: 40px;
        }
        
        .intro {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 40px;
            border-left: 4px solid #667eea;
        }
        
        .intro h2 {
            color: #667eea;
            margin-bottom: 10px;
        }
        
        .features {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin: 30px 0;
        }
        
        .feature-card {
            background: linear-gradient(135deg, #667eea15 0%, #764ba215 100%);
            padding: 20px;
            border-radius: 8px;
            border: 1px solid #667eea30;
        }
        
        .feature-card h3 {
            color: #667eea;
            margin-bottom: 10px;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        
        .section {
            margin: 40px 0;
        }
        
        .section h2 {
            color: #333;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 2px solid #667eea;
        }
        
        .option {
            background: #f8f9fa;
            padding: 25px;
            margin: 20px 0;
            border-radius: 8px;
            border-left: 4px solid #667eea;
        }
        
        .option.recommended {
            border-left-color: #10b981;
            background: linear-gradient(to right, #10b98115 0%, transparent 100%);
        }
        
        .option h3 {
            color: #333;
            margin-bottom: 10px;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .badge {
            display: inline-block;
            background: #10b981;
            color: white;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.85em;
            font-weight: bold;
        }
        
        .badge.advanced {
            background: #f59e0b;
        }
        
        .badge.intermediate {
            background: #3b82f6;
        }
        
        .steps {
            list-style: none;
            counter-reset: step-counter;
            margin: 15px 0;
        }
        
        .steps li {
            counter-increment: step-counter;
            margin: 12px 0;
            padding-left: 30px;
            position: relative;
        }
        
        .steps li:before {
            content: counter(step-counter);
            position: absolute;
            left: 0;
            top: 0;
            background: #667eea;
            color: white;
            width: 24px;
            height: 24px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.9em;
            font-weight: bold;
        }
        
        code {
            background: #1f2937;
            color: #10b981;
            padding: 12px 16px;
            border-radius: 6px;
            display: block;
            margin: 10px 0;
            font-family: 'Courier New', monospace;
            font-size: 0.95em;
            overflow-x: auto;
        }
        
        code.inline {
            background: #f3f4f6;
            color: #667eea;
            padding: 2px 6px;
            display: inline;
            margin: 0 4px;
            border-radius: 3px;
        }
        
        .warning {
            background: #fef3c7;
            border-left: 4px solid #f59e0b;
            padding: 15px;
            border-radius: 6px;
            margin: 20px 0;
        }
        
        .warning h4 {
            color: #d97706;
            margin-bottom: 5px;
        }
        
        .success {
            background: #d1fae5;
            border-left: 4px solid #10b981;
            padding: 15px;
            border-radius: 6px;
            margin: 20px 0;
        }
        
        .success h4 {
            color: #047857;
            margin-bottom: 5px;
        }
        
        .requirements {
            background: #ede9fe;
            padding: 20px;
            border-radius: 8px;
            margin: 20px 0;
            border-left: 4px solid #667eea;
        }
        
        .requirements h3 {
            color: #667eea;
            margin-bottom: 10px;
        }
        
        .requirements ul {
            margin-left: 20px;
        }
        
        .requirements li {
            margin: 8px 0;
        }
        
        footer {
            background: #f8f9fa;
            padding: 20px;
            text-align: center;
            color: #666;
            border-top: 1px solid #e5e7eb;
        }
        
        .comparison-table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            background: white;
            border-radius: 8px;
            overflow: hidden;
        }
        
        .comparison-table thead {
            background: #667eea;
            color: white;
        }
        
        .comparison-table th,
        .comparison-table td {
            padding: 12px 15px;
            text-align: left;
        }
        
        .comparison-table tbody tr:nth-child(odd) {
            background: #f8f9fa;
        }
        
        .comparison-table tbody tr:hover {
            background: #f3f4f6;
        }
        
        .emoji {
            font-size: 1.3em;
        }
        
        @media (max-width: 768px) {
            header h1 {
                font-size: 1.8em;
            }
            
            .content {
                padding: 20px;
            }
            
            .features {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>
                <span class="emoji">💡</span>
                Tapo L530 Kontrol Uygulaması
            </h1>
            <p>TP-Link Tapo akıllı ampulünüzü PC'nizden kontrol edin</p>
        </header>
        
        <div class="content">
            <!-- Intro -->
            <div class="intro">
                <h2>🚀 Hoş Geldiniz</h2>
                <p>Bu uygulama, TP-Link Tapo L530 akıllı ampulünüzü bilgisayarınızdan kolayca kontrol etmenizi sağlar. Parlaklığı ayarlayın, renkleri değiştirin - hepsi modern bir GUI arayüzüyle.</p>
            </div>
            
            <!-- Features -->
            <div class="features">
                <div class="feature-card">
                    <h3>⚡ Hızlı Kontrol</h3>
                    <p>AC/KAPAT butonları ile anında kontrolü sağlayın</p>
                </div>
                <div class="feature-card">
                    <h3>🎨 Renk Yönetimi</h3>
                    <p>5 farklı renk + custom renk seçeneği (0-360 Hue)</p>
                </div>
                <div class="feature-card">
                    <h3>🔒 Şifrelenmiş Veri</h3>
                    <p>Tüm giriş bilgileri AES-256 ile şifreleniyor</p>
                </div>
                <div class="feature-card">
                    <h3>📦 Taşınabilir</h3>
                    <p>Tek exe dosyası - hiçbir kurulum gerekmiyor</p>
                </div>
            </div>
            
            <!-- Sistem Gereksinimleri -->
            <div class="section">
                <h2>📋 Sistem Gereksinimleri</h2>
                <div class="requirements">
                    <h3>Tüm Yöntemler İçin:</h3>
                    <ul>
                        <li>Windows 7 veya üstü</li>
                        <li>TP-Link Tapo L530 akıllı ampul</li>
                        <li>Tapo hesabı (email ve şifre)</li>
                        <li>Ampulün IP adresi</li>
                    </ul>
                </div>
            </div>
            
            <!-- Kurulum Seçenekleri -->
            <div class="section">
                <h2>📥 Kurulum Seçenekleri</h2>
                
                <!-- Seçenek 1: EXE İndirme (Önerilen) -->
                <div class="option recommended">
                    <h3>
                        <span class="emoji">⭐</span>
                        Seçenek 1: EXE İndir (Önerilen)
                        <span class="badge">KOLAY</span>
                    </h3>
                    <p><strong>Bu yöntem önerilir!</strong> Python kurmanıza gerek yok, direkt çalıştırabilirsiniz.</p>
                    
                    <ul class="steps">
                        <li>
                            GitHub sayfasındaki <strong>Releases</strong> bölümüne gidin
                            <code>https://github.com/senusername/tapo-controller/releases</code>
                        </li>
                        <li><code class="inline">tapocontrol.exe</code> dosyasını indirin (21 MB)</li>
                        <li>Dosyaya çift tıklayarak uygulamayı çalıştırın</li>
                        <li>Tapo hesap bilgilerinizi ve ampulün IP adresini girin</li>
                        <li>Başlamaya hazırsınız! 🎉</li>
                    </ul>
                    
                    <div class="success">
                        <h4>✅ Avantajları:</h4>
                        <ul>
                            <li>Python kurulumu gerekmez</li>
                            <li>Hızlı indirme ve çalıştırma</li>
                            <li>Tüm bağımlılıklar dahil</li>
                            <li>Kolay bir tıkla başlayın</li>
                        </ul>
                    </div>
                </div>
                
                <!-- Seçenek 2: Batch Dosyası (Orta Seviye) -->
                <div class="option">
                    <h3>
                        <span class="emoji">📦</span>
                        Seçenek 2: Git Clone + Batch
                        <span class="badge intermediate">ORTA</span>
                    </h3>
                    <p><strong>Python yüklü olması gerekir!</strong> Kaynak kodundan çalıştırın, batch dosyası ile otomatik kurulum.</p>
                    
                    <div class="warning">
                        <h4>⚠️ Ön Koşul:</h4>
                        <p>Python 3.8 veya üstünün yüklü olduğundan emin olun. <a href="https://www.python.org/downloads/" target="_blank">İndir</a></p>
                    </div>
                    
                    <ul class="steps">
                        <li>
                            PowerShell'i açın ve klonu yapın:
                            <code>git clone https://github.com/senusername/tapo-controller.git
cd tapo-controller</code>
                        </li>
                        <li>
                            Klasörü açıp <code class="inline">kurulum.bat</code> dosyasına çift tıklayın
                        </li>
                        <li>Otomatik olarak kütüphaneler kurulacak ve app başlayacak</li>
                        <li>Tapo bilgilerinizi girin ve başlayın</li>
                    </ul>
                    
                    <div class="success">
                        <h4>✅ Avantajları:</h4>
                        <ul>
                            <li>Kaynak kodu görebilirsiniz</li>
                            <li>Batch dosyası tüm işleri otomatik yapar</li>
                            <li>Güncellemeleri kolayca alabilirsiniz</li>
                        </ul>
                    </div>
                </div>
                
                <!-- Seçenek 3: Advanced (Terminal) -->
                <div class="option">
                    <h3>
                        <span class="emoji">🔧</span>
                        Seçenek 3: Advanced (Terminal)
                        <span class="badge advanced">İLERİ</span>
                    </h3>
                    <p><strong>Geliştiriciler için!</strong> Terminali manuel olarak kullanarak çalıştırın.</p>
                    
                    <div class="warning">
                        <h4>⚠️ Ön Koşul:</h4>
                        <p>Python 3.8 veya üstü ve Git kurulu olması gerekir.</p>
                    </div>
                    
                    <ul class="steps">
                        <li>
                            PowerShell'i yönetici olarak açın ve repo klonlayın:
                            <code>git clone https://github.com/senusername/tapo-controller.git
cd tapo-controller</code>
                        </li>
                        <li>
                            Kütüphaneleri yükleyin:
                            <code>pip install -r requirements.txt</code>
                        </li>
                        <li>
                            Uygulamayı çalıştırın:
                            <code>python tapocontrol.py</code>
                        </li>
                        <li>Giriş ekranında bilgilerinizi girin ve çalıştırın</li>
                    </ul>
                    
                    <div class="success">
                        <h4>✅ Avantajları:</h4>
                        <ul>
                            <li>Tam kontrol ve esneklik</li>
                            <li>Kodu değiştirebilirsiniz</li>
                            <li>Debugging ve geliştirme için ideal</li>
                        </ul>
                    </div>
                </div>
            </div>
            
            <!-- Karşılaştırma Tablosu -->
            <div class="section">
                <h2>📊 Yöntem Karşılaştırması</h2>
                <table class="comparison-table">
                    <thead>
                        <tr>
                            <th>Özellik</th>
                            <th>EXE (Seçenek 1)</th>
                            <th>Batch (Seçenek 2)</th>
                            <th>Terminal (Seçenek 3)</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Python gerekli</td>
                            <td>❌ Hayır</td>
                            <td>✅ Evet</td>
                            <td>✅ Evet</td>
                        </tr>
                        <tr>
                            <td>Zorluk seviyesi</td>
                            <td>⭐ Çok kolay</td>
                            <td>⭐⭐ Orta</td>
                            <td>⭐⭐⭐ İleri</td>
                        </tr>
                        <tr>
                            <td>Kurulum süresi</td>
                            <td>30 saniye</td>
                            <td>1 dakika</td>
                            <td>2 dakika</td>
                        </tr>
                        <tr>
                            <td>Dosya boyutu</td>
                            <td>21 MB</td>
                            <td>50 MB+ (kurulum sonra)</td>
                            <td>50 MB+ (kurulum sonra)</td>
                        </tr>
                        <tr>
                            <td>Taşınabilir</td>
                            <td>✅ Evet</td>
                            <td>❌ Hayır</td>
                            <td>❌ Hayır</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            
            <!-- Sorun Giderme -->
            <div class="section">
                <h2>🔧 Sorun Giderme</h2>
                
                <div class="option">
                    <h3>❓ Python yüklü değil diyorsa (Seçenek 2-3 için)</h3>
                    <p>Python'u indirin ve yükleyin: <a href="https://www.python.org/downloads/" target="_blank">python.org</a></p>
                    <p><strong>Kurulum sırasında "Add Python to PATH" kutusunu işaretleyin!</strong></p>
                </div>
                
                <div class="option">
                    <h3>❓ Ampul bağlantısı başarısız</h3>
                    <p>Kontrol edilecekler:</p>
                    <ul style="margin-left: 20px; margin-top: 10px;">
                        <li>Tapo hesap bilgileriniz doğru mu?</li>
                        <li>Ampulün IP adresi doğru mu? (Tapo app'tan kontrol edin)</li>
                        <li>Ampul aynı WiFi ağında mı?</li>
                        <li>İnternet bağlantısı stabil mi?</li>
                    </ul>
                </div>
                
                <div class="option">
                    <h3>❓ Renk ayarı çalışmıyor</h3>
                    <p>Tapo uygulamasında ampulün renk kontrol özelliği etkinleştirilmiş olduğundan emin olun.</p>
                </div>
            </div>
            
            <!-- Özellikleri -->
            <div class="section">
                <h2>✨ Uygulama Özellikleri</h2>
                <ul style="margin-left: 20px; line-height: 2;">
                    <li>💡 Ampulu AC/KAPAT kontrolü</li>
                    <li>🔆 Parlaklık ayarı (%1-100)</li>
                    <li>🎨 5 hazır renk + custom renk seçeneği</li>
                    <li>🔒 Şifrelenmiş veri depolaması (AppData'da)</li>
                    <li>🌐 Multilingual (Türkçe ara yüz)</li>
                    <li>⚡ Hızlı ve hafif (21 MB)</li>
                    <li>🔌 Tapo Cloud API entegrasyonu</li>
                </ul>
            </div>
            
            <!-- İletişim -->
            <div class="section">
                <h2>📞 Destek & Geri Bildirim</h2>
                <p>Sorun mu yaşıyorsunuz? Öneriniz mi var?</p>
                <ul style="margin-left: 20px; margin-top: 10px; line-height: 2;">
                    <li>GitHub Issues: <a href="https://github.com/senusername/tapo-controller/issues" target="_blank">Sorunu bildirin</a></li>
                    <li>Pull Requests: <a href="https://github.com/senusername/tapo-controller" target="_blank">Katkı sağlayın</a></li>
                </ul>
            </div>
        </div>
        
        <footer>
            <p>🔐 Tüm veriler AES-256 ile şifrelenmiş olarak saklanır | © 2026 Tapo Kontrol Uygulaması</p>
        </footer>
    </div>
</body>
</html>
