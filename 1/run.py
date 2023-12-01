# file = "sample.txt"
file = "input.txt"

if __name__ == "__main__":

    total = 0

    #one two three four five six seven eight nine ten

    with open(file) as input:
        first=last=0
        for line in input:
            for char in line:
                if char.isdecimal():
                    first = last = char
                    break
            for char in line:
                if char.isdecimal():
                    last = char
            subtotal = int(first+last)
            print(subtotal)
            total += subtotal
    print(total)
