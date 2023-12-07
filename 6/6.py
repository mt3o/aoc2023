# f = "sample.txt"
# f="input.txt"
f="input2.txt"

if __name__ == "__main__":
    with open(f,'r') as input:
        time_row = input.readline().strip()
        distance_row = input.readline().strip()

    pairs = [(int(time), int(distance)) for time, distance in zip(
        filter(lambda i: i != '', time_row.split(" ")[1:]),
        filter(lambda i: i != '', distance_row.split(" ")[1:])
    )]
    result = 1
    for time, distance in pairs:
        valid_options = 0
        for pressing_time in range(1,time):
            # pressing time equals speed, so boat can travel for rest of the time
            time_left = time - pressing_time
            distance_travelled = time_left * pressing_time
            if distance_travelled > distance:
                valid_options += 1
        result *= valid_options
    print(result)
