# System Monitoring and Alerting

import psutil


def check_system_status():
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    network_traffic = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv

    alert = ""
    if cpu_usage > 90:
        alert += "Warning: High CPU usage!\n"
    if memory_usage > 90:
        alert += "Warning: High memory usage!\n"
    if disk_usage > 90:
        alert += "Warning: High disk usage!\n"
    if network_traffic > 10e6:  # Örnek bir eşik değeri (10 MB)
        alert += "Warning: High network traffic!\n"

    if not alert:
        alert = "System is running normally."

    return alert


system_alert = check_system_status()
print(system_alert)
