#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == '__main__':
    c_item = None
    max_value = 0
    for line in sys.stdin:
        key, val = line.split("\t")
        val = int(val)
        if key == c_item:
            if val > max_value:
                max_value = val
        else:
            if c_item is not None:
                sys.stdout.write("{}\t{}\n".format(c_item, max_value))
            c_item = key
            max_value = val
    sys.stdout.write("{}\t{}\n".format(c_item, max_value))

