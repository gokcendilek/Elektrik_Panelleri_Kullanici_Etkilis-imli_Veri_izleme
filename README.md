# ⚡ Elektrik Panelleri Kullanıcı Etkileşimli Veri İzleme Sistemi

Bu proje, **güneş enerjisi sistemlerine ait farklı bileşenlerden veri üretimi, depolaması ve analizini** içeren bir kullanıcı etkileşimli izleme sistemidir. Panel, pil, invertör ve çevresel sensörlerden gelen veriler belirli aralıklarla simüle edilerek SQL veritabanına kaydedilir. Kullanıcılar, belirli tarih aralıklarına göre verileri grafiksel ve özet formatta görüntüleyebilir.

---
## 📊 Proje Özeti

- ⏱️ 5 saniyede bir rastgele veri üretimi
- 💾 Verilerin SQL veritabanına kaydı
- 👁️ Anlık kaydedilen verilerin terminalde gösterimi
- 📅 Tarih aralığı seçerek veri filtreleme
- 📈 Elektrik üretimi, pil, invertör, sensör ve gateway bileşenleri için grafiksel gösterim
- 📌 Performans özetleri

---

## 🔢 Üretilen Veriler

### ☀️ Güneş Panelleri
- `panel_power`  
- `panel_temperature`  
- `panel_inclination`  
- `sunlight_intensity`  
- `panel_efficiency`

### 🔋 Piller
- `battery_charge`  
- `battery_discharge_rate`  
- `battery_temperature`  
- `battery_voltage`  
- `battery_capacity`

### ⚙️ İnvertörler
- `inverter_output_power`  
- `inverter_efficiency`  
- `inverter_input_voltage`  
- `inverter_output_voltage`  
- `inverter_temperature`  
- `inverter_mode`

### 🌡️ Çevresel Sensörler
- `ambient_temperature`  
- `ambient_humidity`  
- `wind_speed`  
- `atmospheric_pressure`  
- `ambient_light_intensity`

### 🌐 Diğer Bileşenler
- `gateway_data_flow`  
- `internet_connection`  
- `remote_control_status`  
- `system_errors`

---

## 🖥️ Uygulama Özellikleri

- Veriler otomatik olarak **her 5 saniyede bir** üretilip SQL veritabanına kaydedilir.
- Veri kaydı yapılırken, terminalde **rastgele seçilmiş spesifik veriler** gösterilir.
- Kullanıcılar başlangıç ve bitiş tarihlerini girerek o aralığa ait:
  - 🔋 Pil performansı
  - ⚡ Elektrik üretimi
  - ⚙️ İnvertör verimliliği
  - 🌡️ Sensör aktiviteleri
  - 🌐 Gateway veri akışı
  grafiklerini ve özet raporlarını görüntüleyebilir.

---

## 🛠️ Kullanılan Teknolojiler

- Python   
- SQLite  
- Matplotlib / Plotly / Chart.js (Grafikler için)  

## ⚙️ Kurulum

1. Depoyu klonlayın:
   ```bash
   git clone https://github.com/yourusername/Elektrik_Panelleri_Kullanici_Etkilesimli_Veri_izleme.git

