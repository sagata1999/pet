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

ll = [[1, 3], [100, 200], [1, 4]]

print(merge_intervals(ll))
