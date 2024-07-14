import sqlite3
import random
import time

class SolarDataCollector:
    def __init__(self, db_name='solar_data.db'):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS solar_data (
                                id INTEGER PRIMARY KEY,
                                panel_power REAL,
                                panel_temperature REAL,
                                panel_inclination REAL,
                                sunlight_intensity REAL,
                                panel_efficiency REAL,
                                battery_charge REAL,
                                battery_discharge_rate REAL,
                                battery_temperature REAL,
                                battery_voltage REAL,
                                battery_capacity REAL,
                                inverter_output_power REAL,
                                inverter_efficiency REAL,
                                inverter_input_voltage REAL,
                                inverter_output_voltage REAL,
                                inverter_temperature REAL,
                                inverter_mode TEXT,
                                ambient_temperature REAL,
                                ambient_humidity REAL,
                                wind_speed REAL,
                                atmospheric_pressure REAL,
                                ambient_light_intensity REAL,
                                gateway_data_flow REAL,
                                internet_connection TEXT,
                                remote_control_status TEXT,
                                system_errors TEXT,
                                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                              )''')
        self.conn.commit()

    def generate_data(self):
        while True:
            # Güneş panelleri verileri
            panel_power = random.uniform(0, 100)
            panel_temperature = random.uniform(-10, 60)
            panel_inclination = random.uniform(0, 90)
            sunlight_intensity = random.uniform(0, 1000)
            panel_efficiency = random.uniform(0, 100)

            # Piller verileri
            battery_charge = random.uniform(0, 100)
            battery_discharge_rate = random.uniform(0, 10)
            battery_temperature = random.uniform(-10, 60)
            battery_voltage = random.uniform(10, 30)
            battery_capacity = random.uniform(10, 100)

            # Invertörler verileri
            inverter_output_power = random.uniform(0, 50)
            inverter_efficiency = random.uniform(0, 100)
            inverter_input_voltage = random.uniform(100, 500)
            inverter_output_voltage = random.uniform(100, 500)
            inverter_temperature = random.uniform(-10, 60)
            inverter_mode = random.choice(["şebeke bağlantısı", "off-grid"])

            # Sensörler verileri
            ambient_temperature = random.uniform(-10, 40)
            ambient_humidity = random.uniform(0, 100)
            wind_speed = random.uniform(0, 20)
            atmospheric_pressure = random.uniform(900, 1100)
            ambient_light_intensity = random.uniform(0, 1000)

            # Diğer bileşenler verileri
            gateway_data_flow = random.uniform(0, 100)
            internet_connection = random.choice(["bağlı", "değil"])
            remote_control_status = random.choice(["açık", "kapalı"])
            system_errors = "No errors"  

            # Verileri veritabanına kaydet
            self.cursor.execute('''INSERT INTO solar_data (
                            panel_power, panel_temperature, panel_inclination, sunlight_intensity, panel_efficiency,
                            battery_charge, battery_discharge_rate, battery_temperature, battery_voltage, battery_capacity,
                            inverter_output_power, inverter_efficiency, inverter_input_voltage, inverter_output_voltage, inverter_temperature, inverter_mode,
                            ambient_temperature, ambient_humidity, wind_speed, atmospheric_pressure, ambient_light_intensity,
                            gateway_data_flow, internet_connection, remote_control_status, system_errors
                          ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                        (panel_power, panel_temperature, panel_inclination, sunlight_intensity, panel_efficiency,
                        battery_charge, battery_discharge_rate, battery_temperature, battery_voltage, battery_capacity,
                        inverter_output_power, inverter_efficiency, inverter_input_voltage, inverter_output_voltage, inverter_temperature, inverter_mode,
                        ambient_temperature, ambient_humidity, wind_speed, atmospheric_pressure, ambient_light_intensity,
                        gateway_data_flow, internet_connection, remote_control_status, system_errors))

            self.conn.commit()

            print("Veri Kaydedildi")
            print("Güneş Paneli Güç Üretimi:", panel_power, "W")
            print("Pil Şarj Seviyesi:", battery_charge, "%")
            print("Invertör Çıkış Gücü:", inverter_output_power, "W")
            print("Ortam Sıcaklığı:", ambient_temperature, "°C")
            print("Rüzgar Hızı:", wind_speed, "m/s")
            print("Internet Bağlantısı Durumu:", internet_connection)
            print("Uzaktan Kontrol Durumu:", remote_control_status)
            print("Sistem Hata Durumu:", system_errors)


            time.sleep(5)  

    def close_connection(self):
        self.conn.close()

if __name__ == "__main__":
    data_collector = SolarDataCollector()
    data_collector.generate_data()

