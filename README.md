# E-SINIF

## Takım İsmi
Notperest

## Ürün İsmi
E-Sınıf – Anonim ve Yapay Zekâ Destekli Ödev Değerlendirme Sistemi

## Ürün Tanımı

E-Sınıf, öğretmenlerin ödev değerlendirme sürecini daha adil, hızlı ve sistemli hâle getirmek amacıyla geliştirilen, yapay zekâ tabanlı bir dijital araçtır.  
Bu platformda öğrenciler sisteme kimlik bilgileri yerine, her ödev için rastgele üretilen kod adlarıyla giriş yapar. Bu sayede, öğretmenlerin öğrenciyi tanımadan ödevi değerlendirmesi sağlanır. Sistem, değerlendirmede anonimlik ilkesini esas alır.

Yüklenen ödevler, belirlenen ölçütlere göre yapay zekâ tarafından analiz edilir ve puanlanır. Aynı zamanda öğrenciye özel geri bildirimler üretilir. Öğretmen isterse yapay zekânın verdiği notu inceleyip değiştirme hakkına sahiptir.  
E-Sınıf, değerlendirme sürecini öğretmen için kolaylaştırırken, öğrenciler için daha objektif bir ortam sunmayı amaçlar.

## Takım Organizasyonu

İletişim WhatsApp üzerinden sağlandı ve rollere ekip içi görüş birliğiyle karar verildi.
 
- Product Owner: Ali Nebi ER 
- Scrum Master: Hasan SAKAR
- Developer 1: Sıla BULUT
- Developer 2: Zeynep SALĞUN
- Developer 3: Nisanur ÜNAL

Roller, ekip içi değerlendirme ve istek üzerine belirlenmiştir. Her ekip üyesi yazılım geliştirme sürecine aktif olarak katkı sağlamaktadır.

## Hedef Kitle

- Lise ve üniversite öğretmenleri  
- Ödev yoğunluğu yüksek eğitim kurumları  
- Öğrenci gizliliğini esas alan çevrimiçi eğitim platformları  
- Akademik değerlendirmede tarafsızlık arayan tüm eğitimciler

## Temel Özellikler

- Öğrencilere her ödevte özel olarak atanan anonim kullanıcı kodu  
- Yapay zekâ destekli değerlendirme (doğruluk, bütünlük, özgünlük gibi ölçütlere göre)  
- Tanımlı rubriklere göre puanlama ve detaylı geri bildirim  
- Öğretmenin yapay zekâ puanını onaylama ya da değiştirme yetkisi  
- Gelişmeleri kaydeden öğretmen paneli  
- GitHub üzerinden proje sürecinin açık ve belgeli şekilde izlenebilmesi



# SPRINT 1 

Bu sprint için belirlenen puan: ** 150/ 300**

Sprint 1’de odak noktamız proje planlaması, ekip uyumu ve dokümantasyon hazırlıklarıydı. Teknik geliştirmeye temel oluşturacak bu hazırlık süreci aşağıdaki adımlarla tamamlandı:

| İş Kalemi                                                            | Puan | Açıklama                                                                                |
|----------------------------------------------------------------------|------|------------------------------------------------------------------------------------------|
| Takım içi tanışma ve rol paylaşımı                                   | 3    | Görev dağılımı yapıldı, iletişim düzeni kuruldu.                                         |
| Proje fikrinin netleştirilmesi ve isimlendirme                       | 4    | E-Sınıf ismi belirlendi, takım adı olarak Notperest seçildi.                             |
| Ürün açıklaması, hedef kitle ve temel özelliklerin yazılması         | 4    | README dosyasında proje tanımı ve kullanıcı hedefi açıklandı.                            |
| GitHub reposunun oluşturulması ve README dosyasının düzenlenmesi     | 2    | Temel yapılar oluşturuldu, içerikler yerli yerinde yazıldı.                              |
| Product backlog ve kullanıcı hikâyelerinin hazırlanması              | 4    | Kullanıcı odaklı ihtiyaçlar belirlendi ve hikâyeleştirildi.                              |
| Sprint sürecinin yazılı hale getirilmesi (Sprint Notes)              | 4    | Süreç adımları ve tarih aralıkları net şekilde belgelendi.                               |
| Sprint Review ve Retrospective yazımı                                | 5    | Ekip içi değerlendirme ve gözlemler sade biçimde aktarıldı.                              |
| Günlük iletişim şekli/düzeni (Daily Scrum)                           | 2    | WhatsApp üzerinden yapılan iletişim süreci yazıya eklendi.                               |
| Sprint Board ekran görüntüsü paylaşımı                               | 2    | Yapılan işler ve durumlar görselleştirilerek board üzerinden belgelenmiştir.             |

**Toplam Puan:** `30 / 30`

## Sprint Review

Sprint sürecinde ekip içi iletişim sağlıklı şekilde yürütülmüştür. Ürün fikri kısa sürede belirlenmiş ve sprint boyunca dokümantasyon çalışmaları önceliklendirilmiştir.  
Sprint sonunda gelinen noktada:  
- Ürün tanımı, hedef kitle ve temel özellikler yazıya döküldü.  
- Kullanıcı ihtiyaçlarına uygun hikâyeler oluşturulmaya başlandı.  
- Teknik geliştirme için ihtiyaç duyulacak araçlar (ör. Python, OpenAI API) değerlendirmeye alındı.
- Süreç hakkındaki tüm görüntüleri [buradan](https://drive.google.com/drive/folders/1v8xIpiVUeH5tLkQxgVq88m0z8aU4spU3?usp=sharing) ulaşabilirsiniz.
  
## Sprint Process
**İlk Günler (20–26 Haziran)**  
- Takım içi tanışma yapıldı.  
- Proje konusu belirlendi: *E-Sınıf* – yapay zekâ destekli anonim notlandırma sistemi.  
- Temel yapı ve hedef netleştirildi: anonim öğrenci girişi, AI destekli değerlendirme ve öğretmen onayı mekanizması.

**Son Günler (27 Haziran – 6 Temmuz)**  
- GitHub repo oluşturuldu.  
- README ve backlog içerikleri yazıldı.  
- Takım ismi olarak **Notperest** belirlendi.  
## Gözlemler ve Gelişim Alanları

- Anonim kimliğin her ödev sonrası otomatik olarak yenilenmesi konusu teknik düzeyde planlanıyor.  
- AI değerlendirme yapısının detayları ve model seçimi ikinci sprintte netleşecek.  
- Takım içinde iletişim düzenli, içerik üretimi dengeli şekilde yürütülüyor.

## Product Backlog
[Product Backlog URL](https://miro.com/app/board/uXjVIg7ztw4=/)

##  Sprint Retrospektif

Bu sprintte, ekip olarak fikir belirleme ve proje dokümantasyonu üzerine çalıştık. Başlangıç sürecinde ekip üyeleri birbirini tanıdı, iletişim düzeni kuruldu ve iş bölümü yapıldı.

### İyi Giden Noktalar

- Ekip içinde iletişim netti ve kararlar birlikte alındı  
- Herkes görevini zamanında yerine getirdi  
- Belge içerikleri özenli ve anlaşılır şekilde yazıldı  
- Proje fikri hızlıca netleştirildi ve ortak bir zeminde buluşuldu

### Geliştirilebilecek Alanlar

- Belgeler biraz daha erken hazırlanabilirdi  
- Teknik kısımlara geçiş süresi biraz uzadı  
- User story’lerin çeşitliliği artırılabilir

## Genel Değerlendirme

Sprint 1, ekip uyumu ve hazırlık açısından verimli geçti.  
Sorumluluklar netti ve dokümantasyon planlandığı gibi tamamlandı.  
Bir sonraki sprintte teknik uygulamaya geçilecek ve görev dağılımı bu doğrultuda yeniden düzenlenecek.

# SPRINT 2

Bu sprint için belirlenen puan: **30 / 300**

Sprint 2’de odak noktamız, arayüz tasarımı ve veritabanı entegrasyonuyla ürünün temel yapısını oluşturmaktı.

| İş Kalemi                                                  | Puan | Açıklama                                                                 |
|------------------------------------------------------------|------|--------------------------------------------------------------------------|
| Ürün arayüz tasarımının oluşturulması                      | 25   | Arayüz çizimleri yapıldı, kullanıcı dostu tasarım geliştirildi.          |
| Arayüz kodlamasına başlanması                              | 25   | HTML/CSS/JS kullanılarak frontend geliştirme başlatıldı.                 |
| SQLite tabanlı veritabanı tasarımı                         | 20   | Veritabanı yapısı ve tablo ilişkileri oluşturuldu.                       |
| Veritabanının projeye entegre edilmesi                     | 15   | Arayüzle veritabanı arasında temel bağlantılar test edildi.              |
| Tasarımın etkileşimli hale getirilmesi                     | 20   | Butonlar, formlar, giriş alanları gibi unsurlar eklendi.                 |
| Takım içi rol güncellemesi ve Scrum Master değişikliği     | 10   | Rol değişikliği ekip kararıyla yapıldı.                                  |
| Sprint Review ve Retrospektif yazımı                       | 15   | Sprint sonundaki değerlendirmeler yazılı hale getirildi.                 |
| Sprint süreci boyunca iletişim ve iş birliği               | 10   | WhatsApp üzerinden düzenli iletişim sağlandı.                            |
| GitHub'a kodların yüklenmesi (başlatıldıysa)               | 10   | Kodlar GitHub'da yüklendiyse bu madde uygulanır.                         |

**Toplam Puan: 150 / 300**

##  Sprint Process – Zaman Çizelgesi

### İlk Günler (7–13 Temmuz)
- Ürün arayüz tasarımı yapıldı.
- Sayfa yapısı ve kullanıcı bileşenleri belirlendi.
- Veritabanı yapısı planlandı.
- Takım içi rol değişikliği kararlaştırıldı.

### Son Günler (14–20 Temmuz)
- Arayüzün HTML/CSS kodlaması başlatıldı.
- Arayüz etkileşimli hâle getirildi (buton, form vb.).
- SQLite tabanlı veritabanı oluşturuldu ve entegre edildi.
- Sprint Review ve Retrospektif metinleri yazıldı.


## Sprint Review
Sprint sürecinde ekip içi iletişim sağlıklı şekilde yürütülmüştür. Sprint boyunca tasarım noktasına önem verilmiştir. Scrum Masterda değişikliğe gidilmiştir.
Sprint sonunda gelinen noktada:  
- Ürün arayüz tasarımı yapıldı. 
- Ürün arayüzünün kodlanması başlanıldı ve yeterince ilerlendi.
- Veritabanı için tasarım yapıldı.
- Veritabanı SQLite üzerinden oluşturuldu.

##  Sprint Retrospektif

Bu sprintte, ekip olarak arayüz ve veritabanı tasarımı üzerine çalıştık. Tasarımları etkileşimli hale getirdik.
Sprint süresince ortaya çıkan tasarıma ve çalışmaya bu bağlantı üzerinden erişebilirsiniz: [Drive Linki](https://drive.google.com/drive/folders/19sjM13FoTyYWb_7hwULeULt2ZUcQOO49?usp=sharing)

### İyi Giden Noktalar
- Tasarım aşamasında sade ve titiz çalışıldı. 
- Belge içerikleri özenli ve anlaşılır şekilde yazıldı. 

### Geliştirilebilecek Alanlar
- Back-ende bu sprintte başlanılması gerekiyordu.
  
## Genel Değerlendirme
Sprint 2, tasarım ve kodlama açısından verimli geçti.  
Ekip içerisindeki rolleri baştan gözden geçirdik.
