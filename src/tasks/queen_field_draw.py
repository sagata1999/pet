t = "c4"
char_2_num = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
}
v1 = char_2_num[t[0]]
v2 = int(t[1])
for i in reversed(range(1, 9)):
    res_str = ""
    for j in range(1, 9):
        if j == v1 and i == v2:
            res_str += "Q "
        elif (j == v1 or i == v2) or (abs(j-v1) == abs(i-v2)):
            res_str += "* "
        else:
            res_str += ". "
    print(res_str)