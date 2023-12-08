from functools import cmp_to_key

legit_symbols = '!@#$%^&*()_+-/:;<=>?@x'
digits = '1234567890'


def main(file):
    """
        >>> main('sample.txt')
        467835
    """

    with open(file, 'r') as input_file:
        data = [list(line.strip()) for line in input_file.readlines()]
    found_numbers = []
    max_position_in_line = len(data[0]) - 1
    max_line = len(data) - 1
    for line_number, line in enumerate(data):

        positions_to_check = [
            position_in_line
            for position_in_line, symbol
            in enumerate(line)
            if symbol in legit_symbols
        ]

        for position in positions_to_check:

            # read line above
            if line_number - 1 >= 0:
                buffer = []
                did_read_right = False
                for delta in [-1, 0, 1]:
                    if data[line_number - 1][position + delta] in digits:
                        # read right
                        ptr = delta
                        while position + ptr <= max_position_in_line and (
                        scanned := data[line_number - 1][position + ptr]) in digits:
                            did_read_right = True
                            buffer.append(scanned)
                            ptr += 1
                        # read left
                        ptr = delta - 1
                        while position + ptr >= 0 and (scanned := data[line_number - 1][position + ptr]) in digits:
                            buffer.insert(0, scanned)
                            ptr -= 1
                    if len(buffer) > 0:
                        found_numbers.append((int("".join(buffer)), line_number, position, data[line_number][position]))
                        buffer = []

            # read chars left to the symbol
            if position - 1 >= 0 and data[line_number][position - 1] in digits:
                buffer = []
                ptr = -1
                while position + ptr >= 0 and (scanned := data[line_number][position + ptr]) in digits:
                    buffer.insert(0, scanned)
                    ptr -= 1
                if len(buffer) > 0:
                    found_numbers.append(
                        (int("".join(buffer)), line_number, position, data[line_number][position]))

            # read chars right to the symbol
            if position + 1 <= max_position_in_line and data[line_number][position + 1] in digits:
                buffer = []
                ptr = 1
                while position + ptr < max_position_in_line and (
                scanned := data[line_number][position + ptr]) in digits:
                    buffer.append(scanned)
                    ptr += 1
                if len(buffer) > 0:
                    found_numbers.append((int("".join(buffer)), line_number, position, data[line_number][position]))

            # read line below
            if line_number < max_line:
                buffer = []
                for delta in [-1, 0, 1]:
                    if data[line_number + 1][position + delta] in digits:
                        # read right
                        ptr = delta
                        while position + ptr <= max_position_in_line and (
                                scanned := data[line_number + 1][position + ptr]) in digits:
                            buffer.append(scanned)
                            ptr += 1
                        # read left
                        ptr = delta - 1
                        while position + ptr >= 0 and (scanned := data[line_number + 1][position + ptr]) in digits:
                            buffer.insert(0, scanned)
                            ptr -= 1

                    if len(buffer) > 0:
                        found_numbers.append((int("".join(buffer)), line_number, position, data[line_number][position]))
                        buffer = []

    def comparator(a, b):
        if a[1] < b[1]:
            return -1
        if a[1] > b[1]:
            return 1
        if a[2] < b[2]:
            return -1
        if a[2] > b[2]:
            return 1
        return 0

    found_numbers = sorted(list(set(found_numbers)), key=cmp_to_key(comparator), reverse=False)
    ptr = 0
    gear_ratio = 0
    done = set()
    gears=[]
    while ptr < len(found_numbers):
        element = found_numbers[ptr]
        if element in done:
            ptr += 1
            continue
        matching_symbols = [f for f in found_numbers if f[1] == element[1] and f[2] == element[2]]
        if len(matching_symbols) == 1:
            ptr += 1
            continue
        if len(matching_symbols) == 2:
            done.add(matching_symbols[0])
            done.add(matching_symbols[1])
            gears.append(matching_symbols)
            gear_ratio += matching_symbols[0][0] * matching_symbols[1][0]
            ptr+=2
        else:
            ptr+=1
    return gear_ratio


if __name__ == "__main__":
    print(main("input.txt"))

### 68179580 # too low
# 81296995
