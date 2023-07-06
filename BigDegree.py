from Oiler import fi
from RAE import RAE

def BigDegree(a, d, n):
    gcd = RAE(a, n, is_Secret=False)['b'][-1]
    if gcd == 1:
        print(f"\ngcd(a,n) == 1")
        d_start = d
        d = d % (fi(n, is_Secret=False))
        print(f"\nd = {d_start} % {fi(n)} = {d}")
        print(f"{a}^{d} % {n}")
        return (a**d) % n
    return f"gcd != 1, (Calculated by computer without doing something: ) {a}^{d} === {(a**d)%n} (mod {n})"


while True:
    print(f'Result is {BigDegree(int(input("a: ")), int(input("degree: ")), int(input("n: ")))}')
