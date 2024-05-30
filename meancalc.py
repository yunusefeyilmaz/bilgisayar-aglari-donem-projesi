import os
import re

# Klasör adları için regex deseni
folder_pattern = re.compile(r'run(\d+)')

# Fonksiyon tanımla
def process_experiment(experiment_folder):
    # Toplam paket sayılarını ve gecikmeyi saklamak için değişkenler
    total_tx_packets = 0
    total_rx_packets = 0
    total_mean_delay = 0
    flow_count = 0

    # Mevcut dizindeki klasörleri kontrol et
    for folder_name in os.listdir(experiment_folder):
        folder_path = os.path.join(experiment_folder, folder_name)
        if os.path.isdir(folder_path):  # Sadece klasörleri al
            match = folder_pattern.match(folder_name)
            if match:  # Klasör adı uygunsa
                log_file_path = os.path.join(folder_path, 'log.txt')
                if os.path.exists(log_file_path):  # log.txt mevcutsa
                    with open(log_file_path, 'r') as log_file:
                        log_content = log_file.read()
                        # Paket sayılarını ve gecikmeyi bul
                        tx_packets = sum(map(int, re.findall(r'Tx Packets: (\d+)', log_content)))
                        rx_packets = sum(map(int, re.findall(r'Rx Packets: (\d+)', log_content)))
                        mean_delay_match = re.search(r' Mean flow delay:\s+([\d.]+)', log_content)
                        if mean_delay_match:
                            mean_delay = float(mean_delay_match.group(1))
                            # Toplam değerlere ekle
                            total_tx_packets += tx_packets
                            total_rx_packets += rx_packets
                            total_mean_delay += mean_delay * (rx_packets / tx_packets)  # Gecikme değeri, ulaşılan paket sayısına göre ağırlıklı olarak eklenir
                            flow_count += 1

    # Ortalamaları hesapla
    if flow_count > 0:
        avg_tx_packets = total_tx_packets / flow_count
        avg_rx_packets = total_rx_packets / flow_count
        avg_mean_delay = total_mean_delay / flow_count
        print(f"Deney: {experiment_folder}")
        print(f"Ortalama Tx Paket Sayısı: {avg_tx_packets}")
        print(f"Ortalama Rx Paket Sayısı: {avg_rx_packets}")
        print(f"Ortalama Gecikme: {avg_mean_delay} ms")
        
        # Ulaşılan miktarı bul
        reached_amount = total_rx_packets / total_tx_packets
        print(f"Ulaşılan Miktar: {reached_amount}")
        
    else:
        print(f"Deney: {experiment_folder}")
        print("Hiç geçerli log dosyası bulunamadı.")

# Deney dosyalarını işle
experiment_folders = ['/Test_20_2/', '/Test_20_5/', '/Test_60_5/','/Test_20_10/']
for experiment_folder in experiment_folders:
    process_experiment('./experiments' + experiment_folder)
