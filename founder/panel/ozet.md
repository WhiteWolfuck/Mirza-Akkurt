# Akkurtone tüketici paneli: özet

100 simüle klinik sahibi (seed 7), `founder/pitch.md` metnini gördü. Ayrıntı: `results.md`, `trial.md`, `pricing/*.md`.

**Bunlar simüle alıcılar, gerçek müşteri değil.** İtirazları ve zayıf noktaları bulmak için iyiler; dönüşüm oranını tahmin etmek için değil. Dil modelleri olumluya kayar, oranları üst sınır olarak okuyun. Panel cevapları müşteri yorumu olarak kullanılamaz.

## Sonuç

- **Deneme başlatan: 52/100. Ücretli devam eden: 11/100.** Deneme → ücretli dönüşüm %21.
- Ücretli devam eden 11 kişinin **hepsi** iki davranış grubundan: "kaçan hastadan şikâyetçi" (6/10) ve "teknolojiye meraklı" (5/10). Diğer beş gruptan (80 kişi) kimse ödemiyor.
- Segmentte en iyi: fizik tedavi (3/10). Poliklinik (0/15) ve estetik (0/15) sıfır.
- Ciro arttıkça alma oranı düşüyor (%18 → %9 → %6): engel fiyat değil, geçiş zahmeti.

## Neden almıyorlar (reason_code, 89 kişi)

| neden | kişi |
| --- | ---: |
| alışkanlık / mevcut düzen (habit) | 45 |
| güven: veri, firma, yapay zekâ (trust) | 33 |
| fiyat (price) | 9 |
| kolaylık (convenience) | 2 |

## Tekrar eden itirazlar (yaklaşık, anahtar kelime sayımı)

Bazıları kartlarda verdiğimiz itiraz ve alışkanlıklardan geliyor (sekreter, KVKK, kredi, taksit), o yüzden sayılar değil **içerik** önemli.

- Mevcut programdan veri taşıma ve iki sistemi yan yana yürütme korkusu. "Kim taşıyacak?" sorusunun cevabı metinde yok.
- Sekreter ve hekimlerin yeni sistemi öğrenmeyeceği; 7 günde düzen değişmez, deneme yarım kalır.
- Verinin nerede tutulduğu, kimin eriştiği, yapay zekânın hasta mesajlarını yurt dışına gönderip göndermediği. "KVKK araçları" ifadesi güvence sayılmıyor.
- Yapay zekânın hastaya yanlış fiyat ya da tıbbi bilgi vermesi; sorumluluğun hekimde kalması. Özellikle estetik klinikler.
- Hiç referans yok; "bir meslektaşım kullanıp memnunsa" denebilecek bir kanıt yok.

## Metinden doğan, kartlarda olmayan bulgular

- **Deneme Standart paketle (5 hekim)**: 6-15 hekimli poliklinikler kliniğin tamamıyla deneyemiyor (16 kişi bunu söyledi).
- **Cevapsız çağrı otomasyonu yalnızca Standart'ta**: tek hekimliler en çok istediği özellik için 5 hekimlik paketi almak zorunda (8 kişi).
- **"Mevcut programımın yanında eklenti olsun"** isteği (yaklaşık 17 kişi): yalnızca hatırlatma ve cevapsız çağrı modülü, veri taşımadan.
- **Ücretsiz veri taşıma ve yerinde kurulum/eğitim** (yaklaşık 26 kişi) en sık "fikrimi değiştirir" cevabı.

## Fiyat (Van Westendorp, pakete göre)

| paket | fiyat | kabul edilebilir aralık | kelepir/pahalı dengesi (IPP) | cevap |
| --- | ---: | ---: | ---: | ---: |
| Başlangıç | ₺1.500 | ₺496 – ₺2.508 | ₺1.005 | 30 |
| Standart | ₺3.500 | ₺1.008 – ₺5.011 | ₺2.498 | 55 |
| Büyüme | ₺9.000 | ₺2.995 – ₺11.986 | ₺5.043 | 15 |

Üç fiyat da aralığın içinde, ama hepsi IPP'nin üstünde. Fiyat ana engel değil (89 kişiden 9'u fiyat dedi).

## Para harcamadan önce değiştirilecek tek şey

Geçiş zahmetini ve güven açığını kapatmak: ücretsiz veri taşıma + yerinde/uzaktan kurulum, verinin Türkiye'de tutulduğunu ve yapay zekânın neyi cevaplayabileceğini yazılı gösteren bir sayfa ve veri işleyen sözleşmesi, ilk referans klinikler. Bunu teklif olarak kurgulamak için `/founder-offer`, mesaja dökmek için `/founder-marketing`.
