from functools import reduce

def main():

    ways_to_win = []
    record_distance = 233101111101487
    time = 40828492
    poss_distances = []
    for i in range(time):
        charge_time = i
        distance = charge_time * (time - charge_time)
        if distance > record_distance:
            poss_distances.append(distance)
    print(poss_distances)
    ways_to_win.append(len(poss_distances))
    print(ways_to_win)
    sum = reduce(lambda x, y: x*y, ways_to_win)
    print(sum)


if __name__ == "__main__":
    main()
