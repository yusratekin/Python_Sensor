# Sales and Traffic Reports

import json


def generate_sales_traffic_report(filename):
    # Burada, gerçek veriler kullanılması gerekmektedir
    sales_data = {
        "date": "2024-04-18",
        "visitors": 1000,
        "sales": 50,
        "conversion_rate": 5.0  # Dönüşüm oranı (%)
    }

    # JSON dosyasına yazma
    with open(filename, 'w') as json_file:
        json.dump(sales_data, json_file, indent=4)

    print(f"Sales and traffic report has been generated and saved to {filename}")


# Örnek bir dosya adı
filename = "sales_traffic_report.json"
generate_sales_traffic_report(filename)
