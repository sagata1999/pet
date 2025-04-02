# crazy one by LEGEND!
ll = [[1,3], [100, 200], [1, 4]]
ololo = [
    [
        min(result), max(result)
    ] for result in set(
        frozenset(z) for z in [
            ls[x] for ls in [
                [set(range(l[0], l[1]+1)) for l in ll]
            ] for x in range(len(ls))
            for y in range(len(ls)) if (x != y and ls[x] & ls[y] and ls[x].update(ls[y]) is None and ls[y].update(ls[x]) is None) or True
        ]
    )
]
print(ololo)

# normal one
def merge_intervals(intervals):
    # Сортируем отрезки по их началу
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        # Если список merged пуст или текущий отрезок не пересекается с последним в merged,
        # добавляем его как новый отрезок.
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            # Иначе объединяем отрезки, обновляя правую границу.
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged

print(merge_intervals(ll))
