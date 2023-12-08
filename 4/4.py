from math import floor


def main(filename):
    """
    >>> main('sample.txt')
    13
    """
    with open(filename) as f:
        data = (line.strip() for line in f.readlines()) #read all lines
        data = (line.split("|") for line in data) #split left and right blocks
        data = ((winning.split(":")[1], scrached) for winning,scrached in data) #remove the "card X:" prefix
        data = ((  #convert both sections into set[int]
            set([int(_) for _ in winning.strip().split(" ") if _!=""]),
            set([int(_)for _ in scrached.strip().split(" ") if _!=""])
        ) for winning,scrached in data)
        data = [_ for _ in data]

    return sum([
        floor(2**(len(w.intersection(s))-1))
        for w,s in data
    ])


if __name__ == "__main__":
    print(main("input.txt"))
# 26346 OK
