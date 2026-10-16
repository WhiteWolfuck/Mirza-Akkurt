#!/usr/bin/env python3
"""Türkçe ve SaaS'a uyarlanmış founder-consumer paneli.

Kart dağıtma, kontrol, kaydetme ve sayım işi skill'in kendi panel.py'sinde kalır.
Bu dosya yalnızca tüm alıcılar için aynı olan şeyleri değiştirir:

- Türkçe isimler,
- Türkçe brief: gelir yerine kliniğin aylık cirosu (₺), "satın alır mı" yerine
  "denemeden sonra ücretli aboneliğe geçer mi", ek olarak starts_trial ve fit_plan,
  fiyat soruları uygun paketin aylık TL fiyatı için,
- sonuçlardaki gelir bantlarında $ yerine ₺,
- `extra` komutu: deneme/ücretli sayımları ve paket başına fiyat CSV'leri
  (founder-pricing'in van_westendorp.py'si bunları okur).

    python3 founder/panel_tr.py init --customer founder/customer.json --pitch founder/pitch.md --n 100 --seed 7
    python3 founder/panel_tr.py prompts | check | save P003 | tally | status
    python3 founder/panel_tr.py extra
"""

import csv
import importlib.util
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL = os.path.join(HERE, "..", ".claude", "skills", "founder-consumer", "panel.py")
_spec = importlib.util.spec_from_file_location("panel", SKILL)
panel = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(panel)

panel.FIRST_NAMES = [
    "Ahmet", "Mehmet", "Ayşe", "Fatma", "Elif", "Zeynep", "Mustafa", "Emre", "Burak", "Can", "Deniz", "Selin",
    "Ece", "Merve", "Büşra", "Gizem", "Kerem", "Mert", "Onur", "Serkan", "Hakan", "Murat", "Kemal", "Levent",
    "Tolga", "Volkan", "Cem", "Barış", "Ozan", "Umut", "Yasemin", "Esra", "Derya", "Pınar", "Seda", "Gamze",
    "Tuğba", "Hande", "Aslı", "Burcu", "Ceren", "Dilek", "Ebru", "Filiz", "Gül", "Hülya", "İpek", "Leyla",
    "Melis", "Nazlı", "Özge", "Sibel", "Tülay", "Zehra", "Arda", "Berk", "Cenk", "Doğan", "Erdem", "Fırat",
    "Gökhan", "Hasan", "İlker", "Kaan", "Koray", "Mahmut", "Necati", "Okan", "Rıza", "Selim", "Sinan", "Taner",
    "Uğur", "Yavuz", "Yusuf", "Zafer", "Ali", "Ömer", "Halil", "İbrahim", "Hüseyin", "Osman", "Sevgi", "Nur",
    "Şule", "Banu", "Canan", "Didem", "Eda", "Feride", "Gonca", "Hilal", "İrem", "Kübra", "Meltem", "Nilay",
    "Oya", "Rabia", "Sena", "Tuba", "Yeliz", "Zerrin", "Alper", "Bora", "Çağlar", "Egemen", "Ferhat", "Görkem",
    "Harun", "İsmail", "Kadir", "Metin", "Nihat", "Orhan", "Sarp", "Tayfun", "Yiğit", "Aylin", "Bahar", "Duygu",
]

panel.BRIEF = """Bir tüketici panelinde simüle edilmiş bir alıcısın. Bir girişimci, para harcamadan önce senin gibi gerçek klinik sahiplerinin bu ürünü alıp almayacağını öğrenmek istiyor. Cevabın ancak dürüstse işe yarar: çoğu klinik, karşısına çıkan yazılımların çoğunu almaz ve kibar bir "evet", net bir "hayır"dan daha kötüdür.

=== SEN KİMSİN ===
{name}, {age} yaşında. {segment}. Kliniğinin aylık cirosu yaklaşık ₺{income}.
Nasıl satın alırsın: {behaviour}. {behaviour_how}
{habit_line}Böyle bir teklif duyduğunda aklına ilk gelen: "{objection}"
Şu kitleden birisin: {target}.
=== SON ===

=== SUNULAN ÜRÜN (ilk kez görüyorsun; web sitesine ya da bir reklama denk gelen biri gibi) ===
{pitch}
=== SON ===

Bu kişi olarak karar ver: kendi paran, kliniğin, alışkanlıkların ve şüphelerinle, sıradan bir hafta. Kibar olmaya çalışma. Ürün hakkında yukarıda yazanların dışında bilgi uydurma.

"buys" denemeyi başlatmak değil, ödeme yapmaktır: 7 günlük ücretsiz deneme bittikten sonra ücretli aboneliğe geçer misin?

{out} dosyasını dosya yazma aracınla oluştur (cevabı sadece mesajında yazdırma). Dosyada YALNIZCA aşağıdaki JSON olsun; markdown çiti yok, başka hiçbir şey yok. Metin alanlarını Türkçe, kendi ağzından yaz:
{{
  "id": "{id}",
  "starts_trial": true ya da false (7 günlük ücretsiz denemeyi başlatır mısın),
  "buys": true ya da false (deneme bittikten sonra ücretli aboneliğe geçer misin),
  "fit_plan": kliniğinin büyüklüğüne uyan paket, şunlardan biri: "baslangic" / "standart" / "buyume",
  "purchases_first_month": ücretli devam edersen 1, etmezsen 0,
  "reason_code": şunlardan biri, İngilizce ve aynen: {reasons},
  "reason": "neden, bir iki cümleyle, kendi ağzından",
  "objection": "seni en çok düşündüren şüphe, kendi kelimelerinle",
  "would_change_my_mind": "kararını tersine çevirecek tek şey, yoksa boş",
  "price_too_cheap": fit_plan paketi için iyi olamayacak kadar ucuz geleceği aylık fiyat (TL, KDV hariç, yalnızca sayı),
  "price_cheap": aynı paket için kelepir geleceği aylık fiyat (TL, sayı),
  "price_expensive": pahalı gelmeye başladığı ama yine de alabileceğin aylık fiyat (TL, sayı),
  "price_too_expensive": hiç almayacağın aylık fiyat (TL, sayı)
}}
"""

_write_briefs = panel.write_briefs


def write_briefs(d, wave=panel.WAVE):
    """panel.write_briefs, with the income written the Turkish way (₺1.250.000)."""
    state, cards = panel.load_state(d)
    target = state["customer"]["target"]
    todo = []
    for c in cards:
        out = panel._path(d, "answers", c["id"] + ".json")
        if panel._answer_ok(out, c["id"]) is None:
            continue
        card = dict(c, income="{:,}".format(c["income"]).replace(",", "."))
        brief = panel.BRIEF.format(pitch=state["pitch"], target=target, out=os.path.abspath(out),
                                   habit_line=("Ayrıca: %s.\n" % c["habit"]) if c.get("habit") else "",
                                   reasons=" / ".join(panel.REASONS), **card)
        bp = panel._path(d, "briefs", c["id"] + ".md")
        with open(bp, "w", encoding="utf-8") as fh:
            fh.write(brief)
        todo.append((c["id"], os.path.abspath(bp)))
    return [todo[i:i + wave] for i in range(0, len(todo), wave)]


panel.write_briefs = write_briefs

PLANS = {"baslangic": 1500, "standart": 3500, "buyume": 9000}


def extra(d):
    """Trial vs paid counts, by plan, and one price CSV per plan for van_westendorp.py."""
    _, cards = panel.load_state(d)
    seg = {c["id"]: c["segment"] for c in cards}
    rows = []
    for c in cards:
        p = panel._path(d, "answers", c["id"] + ".json")
        if panel._answer_ok(p, c["id"]) is None:
            rows.append(panel._read_json(p))
    n = len(rows)
    trial = sum(1 for r in rows if r.get("starts_trial") is True)
    paid = sum(1 for r in rows if r.get("buys") is True)
    L = ["# Deneme ve ücretli abonelik", "",
         "%d geçerli cevap. Denemeyi başlatan: **%d** (%%%d). Ücretli devam eden: **%d** (%%%d). "
         "Deneme başlatanların ücretliye dönüşü: %%%d." % (
             n, trial, round(100 * trial / n), paid, round(100 * paid / n), round(100 * paid / trial) if trial else 0),
         "", "| grup | cevap | deneme | ücretli |", "| --- | ---: | ---: | ---: |"]
    for key, label in (("fit_plan", "paket"), ("segment", "segment")):
        groups = {}
        for r in rows:
            g = r.get("fit_plan", "?") if key == "fit_plan" else seg[r["id"]]
            groups.setdefault(g, []).append(r)
        for g, rs in sorted(groups.items(), key=lambda kv: -len(kv[1])):
            L.append("| %s: %s | %d | %d | %d |" % (label, g, len(rs), sum(1 for r in rs if r.get("starts_trial") is True),
                                                   sum(1 for r in rs if r.get("buys") is True)))
    os.makedirs(panel._path(d, "pricing"), exist_ok=True)
    L += ["", "Paket başına fiyat cevapları: `%s/pricing/<paket>.csv` (van_westendorp.py ile okunur)." % d]
    for plan in PLANS:
        rs = [r for r in rows if r.get("fit_plan") == plan]
        with open(panel._path(d, "pricing", plan + ".csv"), "w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh)
            w.writerow(["too_cheap", "cheap", "expensive", "too_expensive"])
            for r in rs:
                vals = [panel._num(r.get(k)) for k in ("price_too_cheap", "price_cheap", "price_expensive", "price_too_expensive")]
                if all(v is not None for v in vals):
                    w.writerow(vals)
    out = panel._path(d, "trial.md")
    with open(out, "w", encoding="utf-8") as fh:
        fh.write("\n".join(L) + "\n")
    print("\n".join(L))


def _lira(d):
    """The skill's tally writes income bands in dollars; this panel's income is TL."""
    for name in ("results.md", "results.json"):
        p = panel._path(d, name)
        if os.path.exists(p):
            with open(p, encoding="utf-8") as fh:
                t = fh.read()
            with open(p, "w", encoding="utf-8") as fh:
                fh.write(re.sub(r"\$(?=\d)", "₺", t))


if __name__ == "__main__":
    argv = sys.argv[1:]
    d = os.path.join("founder", "panel")
    if "--dir" in argv:
        d = argv[argv.index("--dir") + 1]
    if argv[:1] == ["extra"]:
        extra(d)
        sys.exit(0)
    rc = panel.main(argv)
    if argv[:1] == ["tally"]:
        _lira(d)
    sys.exit(rc)
