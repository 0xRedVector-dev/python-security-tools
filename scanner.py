import socket

target = "google.com"
print(f"--- ROZPOCZYNAM SKANOWANIE: {target} ---")


for port in range(79, 82):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    s.settimeout(0.5)

    result = s.connect_ex((target, port))

    if result == 0:
        print(f"[+] PORT {port}: OTWARTY! (Sukces)")
        
        if port == 80:
            print("znaleziono stronę WWW!")
        
else:
    print(f"[-] Port {port}: Zamknięty")
              
s.close()