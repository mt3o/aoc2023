from dataclasses import dataclass


@dataclass
class Card():
    score: int
    copies: int


def main(filename):
    """
    >>> main('sample.txt')
    30
    """
    with open(filename) as f:
        data = (line.strip() for line in f.readlines())  # read all lines
        data = (line.split("|") for line in data)  # split left and right blocks
        data = ((winning.split(":")[1], scrached) for winning, scrached in data)  # remove the "card X:" prefix
        data = ((  # convert both sections into set[int]
            set([int(_) for _ in winning.strip().split(" ") if _ != ""]),
            set([int(_) for _ in scrached.strip().split(" ") if _ != ""])
        ) for winning, scrached in data)
        data = [Card(len(w.intersection(s)), 1) for w, s in data]

    def generator(ptr, data):
        while ptr < len(data):
            card = data[ptr]
            ptr += 1
            copied_cards = data[ptr:ptr + card.score]
            for _ in range(card.copies):
                for c in copied_cards:
                    c.copies += 1
        return sum((c.copies for c in data))

    return generator(0, data)


if __name__ == "__main__":
    print(main("input.txt"))
# 8467762 OK
