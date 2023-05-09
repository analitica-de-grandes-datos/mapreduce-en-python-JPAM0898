# 
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    for line in sys.stdin:
        clave, letras = line.strip().split("\t")
        for letra in letras.split(','):
            sys.stdout.write("{} {}\n".format(clave, letra))