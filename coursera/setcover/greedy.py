
def greedy(set_count, item_count, sets):
    covered = set()
    solution = [0] * set_count
    while len(covered) < item_count:
        m = float("inf")
        t = None
        for i in range(set_count):
            if (len(sets[i].items) != 0) and ((sets[i].cost / len(sets[i].items)) < m):
                m = sets[i].cost / len(sets[i].items)
                t = i
        solution[t] = 1
        for i in range(set_count):
            if i != t:
                for item in sets[t].items:
                    sets[i].items.discard(item)
        covered |= sets[t].items
        # print("length of covered set:", len(covered))
        sets[t].items.clear()
    return 0, solution

