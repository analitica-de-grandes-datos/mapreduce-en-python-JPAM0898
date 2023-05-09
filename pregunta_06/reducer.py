#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == '__main__':
    c_value = None
    maximo = 0
    minimo = 0
    for line in sys.stdin:
        key, val = line.split(",")
        val = float(val)
        if key == c_value:
            if val > maximo:
                maximo = val
            if val < minimo:
                minimo = val
        else:
            if c_value is not None:
                sys.stdout.write("{}\t{}\t{}\n".format(c_value, maximo, minimo))
            c_value = key
            maximo = val
            minimo = val
    sys.stdout.write("{}\t{}\t{}\n".format(c_value, maximo, minimo))