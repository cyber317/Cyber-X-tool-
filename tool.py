import os
import socket
import subprocess
import platform
import sys
import urllib.request

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def banner():
    print(r"""
CYBER X 

def get_public_ip():
    try:
        ip = urllib.request.urlopen('https://api.ipify.org').read().decode()
        print(f"Public IP: {ip}")
    except:
        print("Public IP alınamadı.")

def get_ip():
    site = input("Site veya domain girin: ")
    try:
        ip = socket.gethostbyname(site)
        print(f"{site} IP adresi: {ip}")
    except:
        print("IP adresi bulunamadı.")

def ping_site():
    site = input("Ping atılacak site/domain: ")
    param = '-c' if os.name == 'posix' else '-n'
    subprocess.call(['ping', param, '4', site])

def traceroute():
    site = input("Traceroute yapılacak site/domain: ")
    if os.name == 'posix':
        subprocess.call(['traceroute', site])
    else:
        subprocess.call(['tracert', site])

def dns_lookup():
    site = input("DNS sorgusu yapılacak domain: ")
    subprocess.call(['nslookup', site])

def whois_lookup():
    site = input("Whois sorgusu yapılacak domain/IP: ")
    subprocess.call(['whois', site])

def port_scan():
    site = input("Port taraması yapılacak IP/domain: ")
    start_port = int(input("Başlangıç portu: "))
    end_port = int(input("Bitiş portu: "))
    print(f"{site} üzerinde port taraması yapılıyor...")
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((site, port))
        if result == 0:
            print(f"Port {port} açık")
        sock.close()

def show_network_interfaces():
    if os.name == 'posix':
        subprocess.call(['ip', 'addr'])
    else:
        subprocess.call(['ipconfig'])

def show_system_info():
    print(f"Sistem: {platform.system()}")
    print(f"Sürüm: {platform.version()}")
    print(f"Mimari: {platform.machine()}")
    print(f"İşlemci: {platform.processor()}")

def list_files():
    path = input("Listelemek istediğiniz dizin (boş bırakılırsa mevcut dizin): ")
    if path == '':
        path = '.'
    try:
        files = os.listdir(path)
        for f in files:
            print(f)
    except Exception as e:
        print("Dizin okunamadı:", e)

def current_directory():
    print("Mevcut dizin:", os.getcwd())

def disk_usage():
    if os.name == 'posix':
        subprocess.call(['df', '-h'])
    else:
        subprocess.call(['wmic', 'logicaldisk', 'get', 'size,freespace,caption'])

def cpu_usage():
    if os.name == 'posix':
        subprocess.call(['top', '-b', '-n', '1'])
    else:
        subprocess.call(['wmic', 'cpu', 'get', 'loadpercentage'])

def memory_usage():
    if os.name == 'posix':
        subprocess.call(['free', '-h'])
    else:
        subprocess.call(['wmic', 'OS', 'get', 'FreePhysicalMemory,TotalVisibleMemorySize', '/Value'])

def netstat_info():
    if os.name == 'posix':
        subprocess.call(['netstat', '-tulnp'])
    else:
        subprocess.call(['netstat', '-an'])

def arp_table():
    if os.name == 'posix':
        subprocess.call(['arp', '-a'])
    else:
        subprocess.call(['arp', '-a'])

def open_ports():
    site = input("Açık portları kontrol edilecek IP/domain: ")
    subprocess.call(['nmap', '-sT', site])

def reverse_dns():
    ip = input("Reverse DNS sorgusu yapılacak IP: ")
    try:
        host = socket.gethostbyaddr(ip)
        print(f"Reverse DNS: {host[0]}")
    except:
        print("Reverse DNS bulunamadı.")

def check_website_status():
    site = input("Kontrol edilecek site/domain: ")
    try:
        response = urllib.request.urlopen(f"http://{site}")
        print(f"Site durumu: {response.status}")
    except:
        print("Siteye ulaşılamıyor.")

def download_file():
    url = input("İndirilecek dosyanın URL'si: ")
    filename = input("Kaydedilecek dosya adı: ")
    try:
        urllib.request.urlretrieve(url, filename)
        print(f"{filename} indirildi.")
    except Exception as e:
        print("İndirme başarısız:", e)

def show_date_time():
    subprocess.call(['date'])

def show_uptime():
    if os.name == 'posix':
        subprocess.call(['uptime'])
    else:
        print("Bu özellik Windows'ta desteklenmiyor.")

def show_logged_users():
    if os.name == 'posix':
        subprocess.call(['who'])
    else:
        subprocess.call(['query', 'user'])

def show_env_variables():
    for k, v in os.environ.items():
        print(f"{k}={v}")

def simple_http_server():
    port = input("HTTP server portu (default 8000): ")
    if port == '':
        port = '8000'
    print(f"HTTP server başlatılıyor, port: {port}")
    if sys.version_info[0] == 3:
        subprocess.call(['python3', '-m', 'http.server', port])
    else:
        subprocess.call(['python', '-m', 'SimpleHTTPServer', port])

def exit_program():
    print("Çıkış yapılıyor...")
    exit()

def main():
    while True:
        clear()
        banner()
        print("1. Public IP öğren")
        print("2. Site IP öğren")
        print("3. Siteye ping at")
        print("4. Traceroute yap")
        print("5. DNS sorgusu yap")
        print("6. Whois sorgusu yap")
        print("7. Port taraması yap")
        print("8. Ağ arayüzlerini göster")
        print("9. Sistem bilgisi göster")
        print("10. Dizin dosyalarını listele")
        print("11. Mevcut dizini göster")
        print("12. Disk kullanımını göster")
        print("13. CPU kullanımını göster")
        print("14. Bellek kullanımını göster")
        print("15. Netstat bilgisi göster")
        print("16. ARP tablosunu göster")
        print("17. Açık portları nmap ile tara")
        print("18. Reverse DNS sorgusu yap")
        print("19. Site durumunu kontrol et")
        print("20. Dosya indir")
        print("21. Tarih ve saat göster")
        print("22. Sistem çalışma süresi göster")
        print("23. Giriş yapmış kullanıcıları göster")
        print("24. Ortam değişkenlerini göster")
        print("25. Basit HTTP server başlat")
        print("26. ---")
        print("27. ---")
        print("28. ---")
        print("29. ---")
        print("30. Çıkış")
        choice = input("Seçiminiz (1-30): ")
        if choice == '1':
            get_public_ip()
        elif choice == '2':
            get_ip()
        elif choice == '3':
            ping_site()
        elif choice == '4':
            traceroute()
        elif choice == '5':
            dns_lookup()
        elif choice == '6':
            whois_lookup()
        elif choice == '7':
            port_scan()
        elif choice == '8':
            show_network_interfaces()
        elif choice == '9':
            show_system_info()
        elif choice == 
