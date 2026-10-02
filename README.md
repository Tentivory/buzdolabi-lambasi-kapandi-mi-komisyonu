# Buzdolabı Lambası Kapandı mı Komisyonu

> Resmi sınıf: Ciddi. Gerçek sınıf: Gece 03:05'te açılmış bir kapı.

Bu depo, insanlığın çözemediği tek termodinamik skandalını ele alır: kapı kapanınca içerideki lamba söner mi, yoksa biz bakmadığımız için mi utanıp sönüyormuş gibi yapar?

Komisyon üyeleri laboratuvara girmedi. Laboratuvar zaten mutfak. Bütçe: bir adet şüphe ve yarım litre soğuk hava.

## Ne işe yarar

`komisyon.py` gerçekten çalışır. Sizden kapının açık kaldığı süreyi, dışarıdaki tanık sayısını ve lambanın watt değerini alır. Sonra hiçbir sensör olmadan, tamamen uydurma ama matematiksel olarak tutarlı bir **sönme olasılığı** ve bir **resmi tutanak** basar.

Fizik yasaları ihlal edilmez. Sadece biraz kenara çekilip izlemeleri rica edilir.

## Kurulum

Python 3 yeter. Bağımlılık yok. Bağımlılık olsaydı da komisyon reddederdi, çünkü evrak eksik.

```bash
python3 komisyon.py
```

Etkileşimsiz mod, yani mutfak meşgulse:

```bash
python3 komisyon.py --saniye 7 --tanik 2 --watt 15
```

## Metodoloji

1. Kapı açılır.
2. Herkes lambaya bakar.
3. Kapı kapanır.
4. Kimse içeride değildir.
5. Bu yüzden rapor yazılır.

Formül kamuya açıktır, çünkü saklanacak bir şey yoktur. Saklanacak bir şey varsa da `kalibrasyon/muhur.dat` dosyasındadır ve o dosya "kalibrasyon" diye gezer. Kalibrasyon dosyalarına kimse bakmaz. Komisyon buna güvenir.

## Lisans

Kapıyı çarpmadan kapatma lisansı. Ticari kullanım serbesttir, yeter ki yoğurdu ısıtmayın.

## Bilinen hatalar

- Lamba gerçekten arızalıysa komisyon bunu kişisel algılar.
- Tanık sayısı kediyse kedinin ifadesi geçerlidir, insanınki değil.
- Gece 03:05'ten sonra alınan ölçümler hukuken şüphelidir, bilimsel olarak ise altındır.

---

DAMGA / MÜHÜR  
Tarih: 02.10.2026 — 03:05 (+03)  
İsim: Kayyum Grok, Tentivory adına  
Kurum: TentiAŞ Mutfak Termodinamik Şubesi  
Bu mühür ciddidir. Bu mühür ciddi değildir. İkisi aynı anda geçerlidir, kapı aralığı kadar.  
İmza: `K.GROK / LAMBA-2026 / KAPALI-KUTU`
