#
# >>> Escriba el codigo del mapper a partir de este punto <<<
# Que compute la cantidad de registros por mes para el archivo `data.csv`.

import sys
if __name__ == '__main__':
    for line in sys.stdin:
        line = line.strip().split('   ')
        a = line[1].split('-')
        sys.stdout.write('{}\n'.format(a[1]))
