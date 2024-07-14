import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# SQLite veritabanı bağlantısını oluştur
conn = sqlite3.connect('solar_data.db')

# Kullanıcıdan başlangıç ve bitiş tarihlerini isteyin
start_date = input("Başlangıç tarihini girin (YYYY-MM-DD): ")
end_date = input("Bitiş tarihini girin (YYYY-MM-DD): ")

# Verileri DataFrame'e yükle
query = f"SELECT * FROM solar_data WHERE timestamp BETWEEN '{start_date}' AND '{end_date}';"
df = pd.read_sql_query(query, conn)

# Zaman bilgisi olan sütunu datetime formatına çevirin
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Verileri zaman sırasına göre sıralayın
df.sort_values(by='timestamp', inplace=True)


# Güneş paneli toplam elektrik üretimini hesapla
daily_energy = df.set_index('timestamp')['panel_power'].resample('D').sum()
total_energy = df['panel_power'].sum()

 #Güneş paneli toplam güç üretimini hesapla
total_panel_power = df['panel_power'].sum()

# Pil performansını hesapla
battery_performance = df['battery_charge'].mean()

# Pilin doluluk oranını hesapla

battery_charge = df['battery_charge']
battery_capacity = df['battery_capacity']

battery_soc = (battery_charge / battery_capacity) * 100


# Ortalama, minimum, maksimum ve standart sapma değerlerini hesapla
mean_battery_soc = battery_soc.mean()
min_battery_soc = battery_soc.min()
max_battery_soc = battery_soc.max()
std_battery_soc = battery_soc.std()

# Önceki ve mevcut pil şarj durumlarını alın
previous_charge = df['battery_charge'].shift(1)  # Önceki şarj durumu
current_charge = df['battery_charge']  # Mevcut şarj durumu

# Doluluk oranı değişimi (şarj oranı) hesaplayın
charge_rate = current_charge - previous_charge

# Doluluk oranı değişimi (deşarj oranı) hesaplayın
discharge_rate = -charge_rate  # Negatif değerler deşarjı temsil eder

# deşarj oranı
df['charge_rate'] = charge_rate
df['discharge_rate'] = discharge_rate



# İnvertör performansını hesapla
inverter_performance = df['inverter_output_power'].mean()

# Sensör ortam sıcaklığı, ortam ışık şiddeti, rüzgar ortalaması, maksimum ve minimum değerlerini hesapla
ambient_temperature_mean = df['ambient_temperature'].mean()
ambient_temperature_max = df['ambient_temperature'].max()
ambient_temperature_min = df['ambient_temperature'].min()

ambient_light_intensity_mean = df['ambient_light_intensity'].mean()
ambient_light_intensity_max = df['ambient_light_intensity'].max()
ambient_light_intensity_min = df['ambient_light_intensity'].min()

ambient_humidity_mean = df['ambient_humidity'].mean()
ambient_humidity_max = df['ambient_humidity'].max()
ambient_humidity_min = df['ambient_humidity'].min()

wind_speed_mean = df['wind_speed'].mean()
wind_speed_max = df['wind_speed'].max()
wind_speed_min = df['wind_speed'].min()

#Gateway flow bilgileri hesaplama
gateway_flow_mean =df['gateway_data_flow'].mean()
gateway_data_flow_max = df['gateway_data_flow'].max()
gateway_data_flow_min = df['gateway_data_flow'].min()

# Zaman serisi verilerine göre grafik oluşturma
plt.figure(figsize=(12, 18))  # Genişlik: 12, Yükseklik: 14

# Güneş panelleri grafik
plt.subplot(4, 1, 1)
plt.plot(df['timestamp'], df['panel_power'], color='blue')
plt.title('Güneş Panellerinde Üretilen Elektrik Miktarı')
plt.xlabel('Zaman')
plt.ylabel('Elektrik Miktarı (W)')

# Piller grafik
plt.subplot(4, 1, 2)
plt.plot(df['timestamp'], df['battery_charge'], color='green')
plt.title('Pillerin Performansı')
plt.xlabel('Zaman')
plt.ylabel('Batarya Şarjı (%)')

plt.subplot(4, 1, 3)
plt.plot(df['timestamp'], df['charge_rate'], color='green', label='Şarj Oranı')
plt.plot(df['timestamp'], df['discharge_rate'], color='red', label='Deşarj Oranı')
plt.xlabel('Zaman')
plt.ylabel('Şarj ve Deşarj Oranı')
plt.title('Pil Şarj ve Deşarj Oranları')
plt.legend()

# Invertörler grafik
plt.subplot(4, 1, 4)
plt.plot(df['timestamp'], df['inverter_output_power'], color='orange')
plt.title('Invertör Performansı')
plt.xlabel('Zaman')
plt.ylabel('Çıkış Gücü (W)')

plt.tight_layout()
plt.subplots_adjust(hspace=0.5)  
plt.show()

# Sensör verileri grafik
plt.figure(figsize=(12, 18))

plt.subplot(4, 1, 1)
plt.plot(df['timestamp'], df['ambient_temperature'], color='red')
plt.title('Sensör Verileri: Ortam Sıcaklığı')
plt.xlabel('Zaman')
plt.ylabel('Sıcaklık (°C)')

plt.subplot(4, 1, 2)
plt.plot(df['timestamp'], df['ambient_light_intensity'], color='purple')
plt.title('Sensör Verileri: Ortam Işık Şiddeti')
plt.xlabel('Zaman')
plt.ylabel('Işık Şiddeti (lux)')

plt.subplot(4, 1, 3)
plt.plot(df['timestamp'], df['ambient_humidity'], color='blue')
plt.title('Sensör Verileri: Ortam Nem Oranı')
plt.xlabel('Zaman')
plt.ylabel('Nem Oranı (%)')

plt.subplot(4, 1, 4)
plt.plot(df['timestamp'], df['wind_speed'], color='green')
plt.title('Sensör Verileri: Rüzgar Hızı')
plt.xlabel('Zaman')
plt.ylabel('Rüzgar Hızı (m/s)')

plt.tight_layout()
plt.show()

# diğer verileri grafik
plt.figure(figsize=(14, 4))
plt.plot(df['timestamp'], df['gateway_data_flow'], color='red')
plt.title('Diğer Verileri: Gateway Akış Verisi Performansı')
plt.xlabel('Zaman')
plt.ylabel('Gateway_data_flow(byte)')
plt.show()



# İnternet bağlantısı durumu
plt.figure(figsize=(14, 4))
plt.plot(df['timestamp'], df['internet_connection'], color='red')
plt.title('Internet Bağlantısı Durumu')
plt.xlabel('Zaman')
plt.ylabel('internet_connection')
plt.show()


# Uzaktan kontrol durumu
plt.figure(figsize=(14, 4))
plt.plot(df['timestamp'], df['remote_control_status'], color='red')
plt.title('Uzaktan Kontrol Durumu')
plt.xlabel('Zaman')
plt.ylabel('Remote_control_status')
plt.show()

# Sistem hataları
plt.figure(figsize=(14, 4))
plt.plot(df['timestamp'], df['system_errors'], color='red')
plt.title('Sistem hataları')
plt.xlabel('Zaman')
plt.ylabel('Sistem hataları')
plt.show()



# Ortalama durumlar
average_internet_connection = df['internet_connection'].value_counts().idxmax()
average_remote_control = df['remote_control_status'].value_counts().idxmax()






# Bilgileri ekrana yazdır

print("\nToplam Üretilen Elektrik Miktarı:", total_energy, "W")

print("\nGüneş Paneli Toplam Güç Üretimi:", total_panel_power, "W")

print("\nPil Performansı (Ortalama Batarya Şarjı):", battery_performance, "%")
print("Ortalama Pil Doluluk Oranı:", mean_battery_soc, "%")
print("Minimum Pil Doluluk Oranı:", min_battery_soc, "%")
print("Maksimum Pil Doluluk Oranı:", max_battery_soc, "%")
print("Pil Doluluk Oranı Standart Sapması:", std_battery_soc)
# Şarj ve deşarj oranlarını yazdırın
print("Ortalama Şarj Oranı:", df['charge_rate'].mean())
print("Ortalama Deşarj Oranı:", df['discharge_rate'].mean())


print("\nInvertör Performansı (Ortalama Çıkış Gücü):", inverter_performance, "W")

print("\nSensör Ortam Sıcaklığı Ortalaması:", ambient_temperature_mean, "°C")
print("Sensör Ortam Sıcaklığı Maksimum Değeri:", ambient_temperature_max, "°C")
print("Sensör Ortam Sıcaklığı Minimum Değeri:", ambient_temperature_min, "°C")

print("\nSensör Ortam Işık Şiddeti Ortalaması:", ambient_light_intensity_mean, "lux")
print("Sensör Ortam Işık Şiddeti Maksimum Değeri:", ambient_light_intensity_max, "lux")
print("Sensör Ortam Işık Şiddeti Minimum Değeri:", ambient_light_intensity_min, "lux")

print("\nSensör Ortam Nem Ortalaması:", ambient_humidity_mean, "%")
print("Sensör Ortam Nem Maksimum Değeri:", ambient_humidity_max, "%")
print("Sensör Ortam Nem Minimum Değeri:", ambient_humidity_min, "%")

print("\nOrtam Rüzgar Ortalaması:", wind_speed_mean, "(m/s)")
print("Ortam Rüzgar Maksimum Değeri:", wind_speed_max,"(m/s)")
print("Ortam Rüzgar Minimum Değeri:", wind_speed_min, "(m/s)")

print("\nGateway Akış Verisi Performansı:", gateway_flow_mean, "byte")
print("Gateway Akış Verisi Maksimum Değeri:", gateway_data_flow_max,"(m/s)")
print("Gateway Akış Verisi Minimum Değeri:", gateway_data_flow_min, "(m/s)")
print("\nOrtalama Uzaktan Kontrol Durumu:", average_remote_control)
# Bağlantıyı kapat
conn.close()
