#!env python3

import sys

def main():

    progName = "Day1"
    total = 0
    list0 = []
    list1 = []

    for line in sys.stdin:
        line.strip()
        fields=line.split()
        list0.append(fields[0])
        list1.append(fields[1])

    #list0.sort()
    #list1.sort()

    for diff in range(len(list0)):
        #total += abs(int(list0[diff]) - int(list1[diff]))
        total += int(list0[diff]) * list1.count(list0[diff])

    print("Total:")
    print(total)

    return

if __name__ == '__main__':
    main()
