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
        maybe = 0
        good = True
        if (fields == sorted_fields) or (fields == reverse_sorted_fields):
            for diff in range(len(fields) - 1):
                if (abs(fields[diff] - fields[diff + 1]) > 3) or (abs(fields[diff] - fields[diff + 1]) == 0):
                    maybe += 1
                    if maybe > 1:
                        good = False
        else:
            #list is unsorted, less than 1 element?
            #walk through each element, remove, check if then matches sorted or reverse sorted?
            good = False
            for element in range(len(fields)):
                fields_post = fields.copy();
                fields_post.pop(element)
                sorted_fields = sorted(fields_post)
                reverse_sorted_fields = sorted(fields_post, reverse = True)
                if (fields_post == sorted_fields) or (fields_post == reverse_sorted_fields):
                    good = True
                    for diff in range(len(fields_post) - 1):
                        if (abs(fields_post[diff] - fields_post[diff + 1]) > 3) or (abs(fields_post[diff] - fields_post[diff + 1]) == 0):
                            maybe += 1
                            if maybe > 1:
                                good = False
                                break
                    break

        if good:
            total += 1

    print("Total:")
    print(total)

    return

if __name__ == '__main__':
    main()
