
def main(filename):
    """
    >>> main('sample.txt')
    "sample_result"
    """
    with open(filename) as f:
        data = [line.strip() for line in f.readlines()]
    return data

if __name__ == "__main__":
    print(main("input.txt"))
