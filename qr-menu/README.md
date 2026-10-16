# QR Menü

Tek sayfa: kategoriye dokununca açılır, her ürünün solunda küçük resmi var, resme dokununca büyür.
Worker kodu yok, Cloudflare sayfayı ve resimleri statik dosya olarak sunar: istekler ücretsiz ve sınırsızdır.

## Menüyü düzenleme

`public/index.html` içinde:

- Restoran adı: `<h1>` satırı.
- Kategori: bir `<details class="kat">` bloğu, başlığı `<summary>`.
  Sayfa açılınca açık gelmesini istediğin kategoriye `open` yaz: `<details class="kat" open>`.
- Ürün: bir `<li>` satırı:

  ```html
  <li><img src="resimler/menemen.webp" alt="" loading="lazy"><span class="ad">Menemen</span><span class="fiyat">220 ₺</span></li>
  ```

  Resmi olmayan üründe `<img …>` kısmını sil.

## Resimler

`public/resimler/` klasörüne koy, `<img src="resimler/dosya-adi.webp">` ile göster.
Şimdiki resimler yer tutucu çizimler; aynı adla gerçek fotoğrafları koyman yeterli.

- Kare kırp (listede 56 px kare görünür, büyütünce tam genişlik).
- 600×600 px, `.webp` ya da `.jpg`, tanesi 50 KB altında olsun: müşteri mobil veriyle açıyor.
- Dosya adında Türkçe karakter ve boşluk kullanma: `izgara-kofte.webp`.

## Yayınlama

```sh
cd qr-menu
npx wrangler login     # ilk seferde
npx wrangler deploy
```

Çıkan `https://qr-menu.<hesabın>.workers.dev` adresini QR koda çevir.
Menüyü değiştirince tekrar `npx wrangler deploy` yeterli, QR kod aynı kalır.
