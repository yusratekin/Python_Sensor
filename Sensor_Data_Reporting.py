# Sensor Data Reporting

import json


def generate_sensor_data_report(filename):
    # Burada, gerçek sensör verileri kullanılmalıdır
    sensor_data = {
        "date": "2024-04-18",
        "temperature": 25.5,
        "humidity": 60,
        "light_intensity": 500,
        "motion_detected": True
    }

    # JSON dosyasına yazma
    with open(filename, 'w') as json_file:
        json.dump(sensor_data, json_file, indent=4)

    print(f"Sensor data report has been generated and saved to {filename}")


# Örnek bir dosya adı
filename = "sensor_data_report.json"
generate_sensor_data_report(filename)
