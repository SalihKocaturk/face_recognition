# Bölüm 1:  Yüz İfadelerinden Duygu Analizi(Veri Toplama) - README

## Özet
Projemizin ilk aşamasında, veri toplama ve veri artırma işlemlerine odaklandık.

## I. Giriş
Bu çalışmada, yüz ifadelerinden duygu analizi yapacak bir uygulama geliştirmek amacıyla veri toplama ve veri artırma işlemleri gerçekleştirilmiştir. Veri artırımı yöntemleri, verilerin çeşitliliğini ve miktarını artırarak sınıflandırma doğruluğunun artmasına katkı sağlamıştır. 

## II. Kullanılan Teknolojiler ve Yöntemler
Projenin ilk aşamasında, insan yüzlerinden duygu analizi üzerine yapılmış mevcut araştırmaları inceledik. Bu araştırmalar sayesinde konuyu daha derinlemesine anlamış olduk. Özellikle Pillow resmi sitesi, blog yazıları ve YouTube videoları bize bu yolda yardımcı olmuştur.

Araştırmaların ardından, proje süreci hakkında bilgi paylaşımı yapmak ve kararlar almak amacıyla çevrimiçi bir toplantı düzenledik. Bu toplantıda analiz edilecek duygular tartışılmış ve 10 farklı duygu kategorisi belirlenmiştir. Yapılan değerlendirmeler sonucu, veri toplama ve analiz işlemleri için uygun olan 5 duygu seçilmiştir.

Veri artırımı için döndürme, rastgele şekil ekleme gibi tekniklerden yararlanılmıştır. Bu yöntemler, model eğitimi için gerekli olan veri setinin çeşitliliğini artırmaya yardımcı olmuştur. Son olarak, proje kodları tamamlanarak GitHub üzerinden paylaşılabilir hale getirilmiş ve projenin ilk aşaması başarıyla tamamlanmıştır.

## III. Veri Toplama
Projenin başında, hocamızın önerisi doğrultusunda, şirketlerin toplantı yapmak için kullandığı Zoom, Microsoft Teams gibi platformlar üzerinden veri toplamaya başladık. Bu platformlarda yapılan toplantılardan anlamlı veriler elde etmeye çalıştık. YouTube üzerinde birçok toplantı videosunu inceledik, ancak şirketlerden doğrudan veri temin edemediğimiz için bu kaynaklarımız sınırlı kaldı. Bu süreç uzun zaman almasına rağmen yeterli veri artışını sağlayamadı.

Daha sonra, tepki videoları üzerinden veri toplamayı denedik, ancak beklenen verimliliği sağlayamadık. Nötr ve mutlu duygular için yeterli kaynak bulunmasına rağmen diğer duygular için uygun veri kaynaklarına ulaşmada zorluk yaşadık.

Son olarak, stok fotoğraf sitelerinden yararlanmaya başladık. Shutterstock, iStock, Pexels ve Pixabay gibi platformlardan fotoğraflar temin ettik. Shutterstock üzerinde uygun filtreleri kullanarak, diğer duygu sınıfları için yeterli veri sağlamayı başardık. Bu süreç, projemizin ilerleyen aşamaları için önemli bir adım olmuştur.

## IV. Veri Artırımı
Veri setini yeterli seviyeye çıkarmak için veri artırımı yöntemlerinden faydalandık. Veri artırımı, mevcut verilerin çeşitli dönüşümlerle zenginleştirilmesiyle modelin daha geniş bir veri kümesiyle eğitilmesine imkan tanır. Biz de projemizde bu işleme ihtiyaç duyduk.

Kullandığımız veri artırımı teknikleri arasında döndürme, parlaklık ve kontrast değişiklikleri, bulanıklık uygulama ve rastgele şekil çizme gibi işlemler yer almaktadır. Bu işlemler, her bir görüntüye özgün özellikler katmakta ve modelin farklı durumlarla karşılaşmasını sağlamaktadır.

Veri artırımı işlemlerini Python dili ile gerçekleştirerek Pillow (Python Imaging Library) kütüphanesinden yararlandık. Bu süreçte, veri artırımı tekniklerini öğrenmek ve geliştirmek amacıyla Pillow’un resmi kaynaklarını, Medium’daki blogları ve YouTube videolarını kaynak olarak kullandık.

---
# Bölüm 2:  Yüz İfadelerinden Duygu Analizi(Makine Öğrenimi) - README
# Yüz İfadelerinden His Analizi Projesi

## Proje Açıklaması
Bu proje, yüz ifadelerinden bireylerin hislerini belirlemek için çeşitli transformer tabanlı modellerin performansını değerlendirmeyi amaçlamaktadır. Modellerin eğitimi, doğrulaması ve test edilmesi için Python ve PyTorch kullanılmıştır. 5 farklı sınıf içeren veri seti üzerinde yapılan çalışmalar, modellerin performansını karşılaştırmak ve sonuçları analiz etmek için ROC eğrileri, loss eğrileri ve doğruluk (accuracy) metrikleriyle değerlendirilmiştir.

---

## Kullanılan Modeller ve Performans Sonuçları

| Model     | Accuracy (%) | Epoch |  
|-----------|--------------|-------|  
| **ViT**   | 76.83        | 5     |  
| **CaiT**  | 78.91        | 5     |  
| **DeiT**  | 73.00        | 10    |  
| **PiT**   | 87.40        | 8     |  
| **TinyViT** | 78.00       | 10    |  

---

## Kullanılan Teknolojiler

### Programlama Dili ve Framework
- **Python**

### Kütüphaneler ve Araçlar
- **PyTorch**: Model oluşturma, eğitim ve test işlemleri için.
- **Torchvision**: Görüntü ön işleme ve veri yükleme için.
- **Timm**: Transformer tabanlı modelleri kullanmak için.
- **Matplotlib**: Grafik çizimi (loss ve accuracy eğrileri, ROC eğrileri).
- **Scikit-learn**: Confusion Matrix ve ROC-AUC hesaplamaları.

### Veri Seti
- **Sınıflar**:  
  - **Mutlu**  
  - **Üzgün**  
  - **Kızgın**  
  - **Durgun**  
  - **Şaşkın**
- **Yapı**:  
  - **`train/`**: Eğitim verileri.  
  - **`val/`**: Doğrulama verileri.  
  - **`test/`**: Test verileri.

---

## Loss ve Accuracy Eğrileri
Eğitim ve doğrulama sırasında oluşan loss ve accuracy değerleri grafiklerle görselleştirilmiştir.

### Loss Eğrileri
#### ViT 
![Loss Eğrisi]![image](https://github.com/user-attachments/assets/c48cff8d-37e2-4acf-bcf2-6a3d55a9ebaa)

#### Cait
![Loss Eğrisi]()
#### Deit
![Loss Eğrisi]()
#### Pit
![Loss Eğrisi]()
#### TinyVit
![Loss Eğrisi]()

### Örnek Accuracy Eğrisi
![Accuracy Eğrisi](path/to/accuracy_curve.png)

---

## ROC Eğrileri
Her model için ROC eğrisi çizilerek modellerin sınıflar arasındaki ayrım başarısı gösterilmiştir.

### Örnek ROC Eğrisi
![ROC Eğrisi](path/to/roc_curve.png)

---

## Kullanım

### Gerekli Bağımlılıkların Yüklenmesi
```bash
pip install torch torchvision timm matplotlib scikit-learn

Bu README dosyası, projemizin veri toplama ve artırma aşamaları ile kullanılan yöntemler hakkında bilgi vermektedir. 

