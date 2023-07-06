def RAE(a, b, needs_lcm=True, needs_view=True, is_Secret=True):
    rae = {"a": [], "b": [], "r": [], "q": [], "u0": [], "u1": [], "v0": [], "v1": []}
    if a == 0:
        return "error"
    if b == 0:
        return a
    q = a // b
    r = a - b * q
    u0 = 1
    u1 = 0
    v0 = 0
    v1 = 1

    i = 0

    def era(a, b, r, q, u0, u1, v0, v1):
        rae["a"] += [a]
        rae["b"] += [b]
        rae["r"] += [r]
        rae["q"] += [q]
        rae["u0"] += [u0]
        rae["u1"] += [u1]
        rae["v0"] += [v0]
        rae["v1"] += [v1]

    while True:
        if b == 0:
            break
        era(a, b, r, q, u0, u1, v0, v1)

        a = rae["b"][i]
        b = rae["r"][i]
        u1 = u0 - u1 * q
        v1 = v0 - v1 * q
        try:
            q = a // b
        except ZeroDivisionError:
            q = 0
        r = a - b * q
        u0 = rae["u1"][i]
        v0 = rae["v1"][i]

        i += 1

    lcm = (rae['a'][0] * rae['b'][0]) / rae['b'][i - 1]

    # print(rae)
    if not is_Secret:
        print("")

        for j in rae.keys():
            print(f"{j}: ", end="")
            print(*rae.get(j))

        print("")

    is_True = rae['a'][0] * rae['u1'][i - 1] + rae['b'][0] * rae['v1'][i - 1] == rae['b'][i - 1]
    if needs_view:
        print(f"{rae['a'][0]} * ({rae['u1'][i - 1]}) + {rae['b'][0]} * ({rae['v1'][i - 1]}) = {rae['b'][i - 1]}, {is_True}")

        print("")

    if not is_Secret and needs_lcm:
        print(f"lcm(a,b) = {lcm}")
    return rae


def repeat():
    while True:
        RAE(int(input('a: ')), int(input('b: ')), is_Secret=False)


if __name__ == "__main__":
    repeat()