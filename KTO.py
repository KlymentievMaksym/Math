from RAE import RAE


def KTO(bi, ni):
    N = 1
    Ni = []
    Ni_1 = []
    Mi = []
    x0 = 0
    for n in ni:
        N = N * int(n)
    for n in ni:
        Ni += [int(N/int(n))]
    for i in range(len(Ni)):
        Ni_1 += [RAE(Ni[i], int(ni[i]), needs_lcm=False, is_Secret=False)["u1"][-1]]
    for i in range(len(Ni_1)):
        Mi += [Ni_1[i] % int(ni[i])]
    for i in range(len(bi)):
        print(f"{int(bi[i])} * {Ni[i]} * {Mi[i]}")
        x0 += int(bi[i]) * Ni[i] * Mi[i]
    x0 = x0 % N
    for i in range(len(bi)):
        result = int(bi[i])
        is_True = result % int(ni[i]) == x0 % int(ni[i])
        print(f"{x0} === {result} (mod {ni[i]}), {is_True}")

    print(N, Ni, Ni_1, Mi, x0)


if __name__ == "__main__":
    bi = input("bi: ").split()
    ni = input("ni: ").split()
    if len(bi) == len(ni):
        while True:
            KTO(bi, ni)
            bi = input("bi: ").split()
            ni = input("ni: ").split()
    else:
        print("Something is missing")