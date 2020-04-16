
def dynamic_programming(items, taken, capacity):
    best = [[0] * len(items)]
    for c in range(1, capacity + 1):
        for i in range(len(items)):
            if i == 0:
                best.append([0])
            elif (items[i].weight <= c) and (best[c - items[i].weight][i-1] + items[i].value > best[c][i-1]):
                best[c].append(best[c - items[i].weight][i-1] + items[i].value)
            else:
                best[c].append(best[c][i-1])

    tmp_capacity = capacity
    tmp_idx = 0
    for i in range(len(items)):
        if best[capacity][i] > best[capacity][tmp_idx]:
            tmp_idx = i


    value = 0
    weight = 0

    while tmp_capacity > 0 and tmp_idx >= 0:
        if best[tmp_capacity][tmp_idx] == best[tmp_capacity][tmp_idx-1]:
            taken[tmp_idx] = 0
        else:
            taken[tmp_idx] = 1
            value += items[tmp_idx].value
            weight += items[tmp_idx].weight
            tmp_capacity -= items[tmp_idx].weight
        tmp_idx -= 1

    return value, weight, 1