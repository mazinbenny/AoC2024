#!env python3

import sys

def main():

    progName = "Day2"
    total = 0

    for line in sys.stdin:
        line.strip()
        #fields = line.split()
        fields_pre = line.split()
        fields = [int(i) for i in fields_pre]
        sorted_fields = sorted(fields)
        reverse_sorted_fields = sorted(fields, reverse = True)
        good = True
        if (fields == sorted_fields) or (fields == reverse_sorted_fields):
            for diff in range(len(fields) - 1):
                if (abs(fields[diff] - fields[diff + 1]) > 3) or (abs(fields[diff] - fields[diff + 1]) == 0):
                    good = False
            if good:
                total += 1

    print("Total:")
    print(total)

    return

if __name__ == '__main__':
    main()
