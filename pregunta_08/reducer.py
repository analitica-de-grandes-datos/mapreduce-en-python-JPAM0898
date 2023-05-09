#
# Reducer que compute la suma y el promedio de la tercera columna por letra del  archivo `data.csv`.
#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys  
if __name__ == '__main__':
    c_item = None
    total = 0
    n = 0
    prom = 0
    for line in sys.stdin:
        key, val = line.split(",")
        val = float(val)
        if key == c_item:
            total += val
            n += 1
            prom = total/n
        else:
            if c_item is not None:
                sys.stdout.write("{}\t{}\t{}\n".format(c_item, total, prom))
            c_item = key
            total = val
            n = 1
            prom = total/n
    sys.stdout.write("{}\t{}\t{}\n".format(c_item, total,prom))
