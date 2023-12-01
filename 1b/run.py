# file = "sample.txt"
file = "../1/input.txt"

if __name__ == "__main__":

    total = 0

    digits = ['zero','one','two','three','four','five','six','seven','eight','nine']

    with open(file) as input:
        first=last=0
        for line in input:
            length = len(line)

            # calculate first number
            for start in range(0, length):
                try:
                    if line[start].isdecimal():
                        first=last=line[start]
                        raise Exception("OK")
                    candidates = [
                        line[start:start + 3],
                        line[start:start + 4] if start+4 < length else '!',
                        line[start:start + 5] if start+5 < length else '!',
                    ]
                    for pos,name in enumerate(digits):
                        if name in candidates:
                            first = last = pos
                            raise Exception("OK")
                except Exception:
                    tailpos = start
                    break

            # calculate last digit
            for start in range(tailpos, length):

                if line[start].isdecimal():
                    last=line[start]

                candidates = [
                    line[start:start + 3],
                    line[start:start + 4] if start+4 < length else '!',
                    line[start:start + 5] if start+5 < length else '!',
                ]
                for pos,name in enumerate(digits):
                    if name in candidates:
                        last = pos





            subtotal = int(str(first)+str(last))
            print(subtotal)
            total += subtotal
    print(total)
