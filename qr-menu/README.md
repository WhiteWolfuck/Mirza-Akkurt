# QR Menü

Tek sayfa, kategoriye tıklayınca açılan liste. JavaScript yok, Worker kodu yok:
Cloudflare bunu statik dosya olarak sunar, istekler ücretsiz ve sınırsızdır.

## Menüyü düzenleme

`public/index.html` içinde:

- Restoran adı: `<h1>` satırı.
- Kategori: bir `<details>` bloğu, başlığı `<summary>`.
- Ürün: bir `<li>` satırı. Açıklama istemezsen `aciklama` kısmını sil.
- Sayfa açılınca açık gelmesini istediğin kategoriye `open` yaz: `<details open>`.

## Yayınlama

```sh
cd qr-menu
npx wrangler login     # ilk seferde
npx wrangler deploy
```

Çıkan `https://qr-menu.<hesabın>.workers.dev` adresini QR koda çevir.
Menüyü değiştirince tekrar `npx wrangler deploy` yeterli, QR kod aynı kalır.
