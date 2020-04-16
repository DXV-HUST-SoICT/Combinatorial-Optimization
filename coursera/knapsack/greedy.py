def greedy_by_avarage_value(items, taken, capacity):
    def key(item):
        return item.value / item.weight

    items.sort(key=key, reverse=True)

    value = 0
    weight = 0

    for i in range(len(items)):
        item = items[i]
        if weight + item.weight <= capacity:
            value += item.weight
            weight += item.weight
            taken[item.index] = 1

    return value, weight, 0