import os
import shutil

def turkce_karakterleri_donustur(harf):
    """Türkçe karakterleri uygun karşılıklarına çevirir."""
    ceviri_tablosu = str.maketrans("çğıöşü", "CGIOSU")
    return harf.translate(ceviri_tablosu)

def dosyalari_isime_gore_ayir(dizin):
    """
    Belirtilen dizindeki dosyaları isimlerine göre ayrıştırır ve alt dizinlere taşır.

    Args:
        dizin (str): Dosyaların bulunduğu dizin.
    """
    for dosya_adi in os.listdir(dizin):
        dosya_yolu = os.path.join(dizin, dosya_adi)

        # Sadece normal dosyaları işle (dizinleri ve gizli dosyaları atla)
        if os.path.isfile(dosya_yolu) and not dosya_adi.startswith("."):
            # Dosya adının ilk harfini al ve Türkçe karakterleri düzelt
            ilk_harf = turkce_karakterleri_donustur(dosya_adi[0].upper())

            # Geçerli bir harf olup olmadığını kontrol et
            if not ilk_harf.isalpha():
                ilk_harf = "DIGER"  # Harf olmayan karakterlerle başlayan dosyalar için

            # Alt dizini oluştur
            alt_dizin = os.path.join(dizin, ilk_harf)
            os.makedirs(alt_dizin, exist_ok=True)

            # Dosyayı ilgili alt dizine taşı
            try:
                yeni_dosya_yolu = os.path.join(alt_dizin, dosya_adi)
                shutil.move(dosya_yolu, yeni_dosya_yolu)
                print(f"{dosya_adi} -> {ilk_harf}/")
            except Exception as e:
                print(f"Hata: {dosya_adi} taşınamadı. {e}")

if __name__ == "__main__":
    dizin = r"C:\Users\rasla\Desktop\muhammed_hoca_sunum_materyaller"  # Buraya gerçek dizin yolunu gir
    dosyalari_isime_gore_ayir(dizin)
    print("Dosyalar isimlerine göre ayrıldı.")
