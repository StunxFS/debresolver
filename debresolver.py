import os, sys

def main(deb):
    print("DebResolver by Stunx")
    print("¡Descarga un paquete deb con todas sus dependencias en la carpeta actual para instalar sin internet!")
    cmd = """PACKAGES=<package>
apt-get download $(apt-cache depends --recurse --no-recommends --no-suggests \
   --no-conflicts --no-breaks --no-replaces --no-enhances \
   --no-pre-depends ${PACKAGES} | grep "^\w")"""
    if deb != "noarg":
        os.system(cmd.replace("<package>", deb[0]))
        #print(cmd.replace("<package>", deb[0]))
    else: print("¡Debes dar el nombre del paquete como argumento del programa!")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1:])
    else: main("noarg")
