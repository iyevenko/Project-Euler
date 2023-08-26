def num_rectangles(h, w):
    s = 0
    for i in range(1, h+1):
        for j in range(1, w+1):
            s += i*j
    return s


def closest_to_n_rectangles(N):
    i = 1
    while num_rectangles(i, i) < N:
        i += 1
    
    h = w = i
    min_diff = 100000
    best_pair = (h, w)

    while h > 1:
        curr = num_rectangles(h, w)
        if abs(curr-N) < min_diff:
            min_diff = abs(curr-N)
            best_pair = (h, w)

        if curr > N:
            h-=1
        else:
            w+=1

    print(best_pair, num_rectangles(*best_pair))
    return best_pair[0] * best_pair[1]

print(closest_to_n_rectangles(2e6))