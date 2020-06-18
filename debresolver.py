import os, sys

def main(deb):
    print("DebResolver by Stunx")
    print("¡Descarga un paquete deb con todas sus dependencias en la carpeta actual para instalar sin internet!")
    print("Créditos a: Ubunlog.com por un artículo de donde saqué la idea")
    cmd = "for i in $(apt-cache depends <package> | grep -E 'Depends|Recommends|Suggests' | cut -d ':' -f 2,3 | sed -e s/''/''/); do sudo apt-get download $i 2>>errors.txt; done"
    if deb != "noarg":
        os.system(cmd.replace("<package>", deb[0]))
        #print(cmd.replace("<package>", deb[0]))
    else: print("¡Debes dar el nombre del paquete como argumento del programa!")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1:])
    else: main("noarg")
