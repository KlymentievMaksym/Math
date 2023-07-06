from RAE import RAE


def LinEq(a, b, n):
    gcd = RAE(a, n, is_Secret=False)
    if gcd['b'][-1] == 1:
        x = (gcd['u1'][-1] * b) % n
        return f'\ngcd(a,n) == 1\nx = ({gcd["u1"][-1]} * {b}) % {n} = {x}'
    elif b % gcd['b'][-1] == 0:
        a0 = int(a / gcd['b'][-1])
        b0 = int(b / gcd['b'][-1])
        n0 = int(n / gcd['b'][-1])
        print(f"\na0*x === b0 (mod n0) | {a0}*x === {b0} (mod {n0}), gcd(a0, n0) == 1\nx0 = a0^-1 * b0 (mod n0)")
        gcd_small = RAE(a0, n0, is_Secret=False)
        x0 = (gcd_small['u1'][-1] * b0) % n0
        print(f"\nx0 = {gcd_small['u1'][-1]} * {b0} (mod {n0}) | x0 = {x0}")
        x = [str(x0)]
        x0_start = x0
        i = 1
        while x0 <= n:
            x0 += n0
            if x0 > n:
                break
            print(f'x0 + {i}*n0 = x{i} | {x0_start} + {i * n0} = {x0}')
            i += 1
            x += [str(x0)]
        return x
    else:
        print(f"\n{b} % {gcd['b'][-1]} == {b % gcd['b'][-1]} != 0")
        return "None of X was found"


while True:
    a = int(input('a: '))
    b = int(input("b: "))
    n = int(input("n: "))
    result = LinEq(a, b, n)
    if type(result) == list:
        print("x =", ", ".join(result))
    else:
        print(result)