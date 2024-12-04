#!env python3

import sys
import re

def main():

    progName = "Day3"
    total = 0

    for line in sys.stdin:
        line.strip()
        new_line = re.findall(r'mul\(\d+,\d+\)',line)
        line = re.sub(r'mul\((\d+),(\d+)\)',r'\1,\2',str(new_line))
        new_line = line.replace('[','')
        line = new_line.replace(']','')
        new_line = line.replace('\'','')
        for pair in new_line.split(', '):
            fields = pair.split(',')
            total += int(fields[0]) * int(fields[1])


    print("Total:")
    print(total)

    return

if __name__ == '__main__':
    main()
