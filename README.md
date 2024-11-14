# Yüz İfadelerinden Duygu Analizi - README

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

Bu README dosyası, projemizin veri toplama ve artırma aşamaları ile kullanılan yöntemler hakkında bilgi vermektedir. 

