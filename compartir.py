#!/usr/bin/python3
import os, sys, socket

def extract_ip():
    st = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:       
        st.connect(('10.255.255.255', 1))
        IP = st.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        st.close()
    return IP
ip = extract_ip()
ruta = os.getcwd()
arcivo = sys.argv[1]
ruta_compar = "http://" + str(ip) + ":4124/" + str(arcivo)
print("para descargar el archivo dirijase a " + ruta_compar)
os.system("qrcode " + ruta_compar)
print
os.system("python3 -m http.server 4124 > /dev/null 2>&1")


