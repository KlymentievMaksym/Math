while True:
    rae = {"a": [], "b": [], "r": [], "q": [], "u0": [], "u1": [], "v0": [], "v1": []}
    small_rae = {"a": [], "b": [], "r": [], "q": [], "u0": [], "u1": [], "v0": [], "v1": []}
    try:
        a = int(input("a: "))
    except ValueError:
        break
    b = int(input("b: "))
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

    def small_era(a, b, r, q, u0, u1, v0, v1):
        small_rae["a"] += [int(a)]
        small_rae["b"] += [int(b)]
        small_rae["r"] += [int(r)]
        small_rae["q"] += [int(q)]
        small_rae["u0"] += [int(u0)]
        small_rae["u1"] += [int(u1)]
        small_rae["v0"] += [int(v0)]
        small_rae["v1"] += [int(v1)]


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

    print("")

    for j in rae.keys():
        print(f"{j}: ", end="")
        print(*rae.get(j))

    print("")

    is_True = rae['a'][0] * rae['u1'][i - 1] + rae['b'][0] * rae['v1'][i - 1] == rae['b'][i - 1]
    print(f"{rae['a'][0]} * ({rae['u1'][i - 1]}) + {rae['b'][0]} * ({rae['v1'][i - 1]}) = {rae['b'][i - 1]}, {is_True}")

    print("")

    print(f"lcm(a,b) = {lcm}")

    print("")
    c = int(input("c: "))
    is_True_mod = c % rae['b'][i - 1] == 0
    print(f"{c}//{rae['b'][i - 1]}, {is_True_mod}")

    a0 = rae['a'][0] / rae['b'][i - 1]
    b0 = rae['b'][0] / rae['b'][i - 1]
    c0 = c / rae['b'][i - 1]

    print(f"\n{int(a0)}*x0 + {int(b0)}*y0 = {int(c0)}")

    q0 = a0 // b0
    r0 = a0 - b0 * q0
    u0 = 1
    u1 = 0
    v0 = 0
    v1 = 1

    k = 0

    if is_True_mod:
        while True:
            if b0 == 0:
                break
            small_era(a0, b0, r0, q0, u0, u1, v0, v1)

            a0 = small_rae["b"][k]
            b0 = small_rae["r"][k]
            u1 = u0 - u1 * q0
            v1 = v0 - v1 * q0
            try:
                q0 = a0 // b0
            except ZeroDivisionError:
                q0 = 0
            r0 = a0 - b0 * q0
            u0 = small_rae["u1"][k]
            v0 = small_rae["v1"][k]

            k += 1

        print("")

        for j in small_rae.keys():
            print(f"{j}: ", end="")
            print(*small_rae.get(j))

        x0 = small_rae['u1'][k-1] * c0
        y0 = small_rae['v1'][k-1] * c0

        print(f"\nGCD({small_rae['a'][0]}, {small_rae['b'][0]}) = {small_rae['b'][-1]}")
        print(f"\nu = {small_rae['u1'][-1]}, v = {small_rae['v1'][-1]}")

        print()
        print(f"x0 = {small_rae['u1'][k-1]} * {int(c0)}")
        print(f"y0 =  {small_rae['v1'][k-1]} * {int(c0)}")

        x = int(x0) + small_rae['b'][0]
        y = int(y0) - small_rae['a'][0]

        print("")

        print(f"x = {int(x0)} + {small_rae['b'][0]}t")
        print(f"y = {int(y0)} - {small_rae['a'][0]}t")

        is_Real = rae['a'][0]*x + rae['b'][0]*y == c
        print(is_Real)
        print("")
    else:
        print("Something wrong")
        print("")