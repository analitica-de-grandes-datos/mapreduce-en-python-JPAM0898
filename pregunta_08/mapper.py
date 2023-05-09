#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == '__main__':
    for line in sys.stdin:
        line = line.strip().split('   ')
        sys.stdout.write('{},{}\n'.format(line[0],line[2]))