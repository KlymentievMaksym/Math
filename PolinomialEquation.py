# from KTO import KTO
# from Oiler import OTA
from sympy import diff, symbols

from RAE import RAE

while True:
    # Inputs
    max_degree_of_polinom = int(input("Enter max degree of polinom: "))  # 3
    line_of_coef = input(f"Write coef-s from x^{max_degree_of_polinom} to x^{0} (There must be {max_degree_of_polinom+1}): ") # '1 2 0 0'
    list_of_coef = []
    for coef in line_of_coef.split():
        coef = int(coef)
        list_of_coef += [coef]

    module = int(input("p^a: "))  # 81

    # Enter welcome words
    welcome_word = ''
    for x_s in range(len(list_of_coef), 0, -1):
        welcome_word += [f"{[f'{list_of_coef[-x_s]}' + ['*', ''][x_s-1 == 0], ''][list_of_coef[-x_s] == 0 or (list_of_coef[-x_s] == 1 and x_s-1 != 0)]}"+[f"x{[f'^{x_s-1}', ''][x_s-1 == 1]}", ""][x_s-1 == 0 or list_of_coef[-x_s] == 0], ''][list_of_coef[-x_s] == '0'] + [[' + ', ''][list_of_coef[-x_s+1] == 0], f' = 0 (mod {module})'][x_s-1 == 0]
    print(welcome_word)

    # Find prime number
    prime_number = 2
    while module % prime_number != 0:
        prime_number += 1


    # Find mod coef by module
    def find_mod_coef_by_module(p, list_of_coef):
        for coef in list_of_coef:
            list_of_coef[list_of_coef.index(coef)] = int(coef) % p
        return list_of_coef

    # Find polynom
    def find_polynom_for_x(x, prime_number, list_of_coef_mod, by_Module=True):
        polynom = 0
        degree = len(list_of_coef_mod)-1
        for coef in list_of_coef_mod:
            # print()
            # print(f"x: {x}")
            # print(f"Degree: {degree}, coef: {int(coef)}")
            if by_Module:
                polynom += int(coef)*x**(degree) % prime_number
            else:
                polynom += int(coef) * x ** (degree)
            degree -= 1
            # print(f"polynom: {polynom}")
        return polynom

    # Find x0
    list_of_coef_mod = find_mod_coef_by_module(prime_number, list_of_coef.copy())
    # print(list_of_coef_mod)

    list_of_suitable_x0 = []
    list_of_suitable_polynom0 = []
    list_of_suitable_polynom = []

    print()

    for number in range(0, prime_number):
        polynom = find_polynom_for_x(number, prime_number, list_of_coef, by_Module=False)
        if polynom % prime_number == 0:
            list_of_suitable_polynom += [[polynom, number]]

    for number in range(0, prime_number):
        polynom = find_polynom_for_x(number, prime_number, list_of_coef_mod)
        print(f"P({number}): {polynom}" + [" != 0", " == 0"][polynom % prime_number == 0] + f" (mod {prime_number})")
        if polynom % prime_number == 0:
            list_of_suitable_x0 += [number]
            list_of_suitable_polynom0 += [[polynom, number]]
    print(f"Suitable x-s: ", end="")
    print(*list_of_suitable_x0, sep=", ")
    print()

    # Find diff of P()

    list_for_diff_coef = []
    x = symbols('x')

    for degree in range(0, len(list_of_coef)):
        different = diff(x**degree)
        # print(f"degree: {degree}")
        # print(f"Diff coef: {different}")
        # print(f"{list_of_coef[-degree - 1]} (coef) * {int(str(different).split('*')[0])} (diff coef)")
        if different != 0:
            list_for_diff_coef += [list_of_coef[-degree - 1] * int(str(different).split("*")[0])]

    list_for_diff_coef.reverse()
    # print(f"Diff coefs: {list_for_diff_coef}")

    # Enter diff words
    diff_word = ''
    for x_s in range(len(list_for_diff_coef), 0, -1):
        diff_word += [f"{[f'{list_for_diff_coef[-x_s]}' + ['*', ''][x_s-1 == 0], ''][list_for_diff_coef[-x_s] == 0 or (list_for_diff_coef[-x_s] == 1 and x_s-1 != 0)]}"+[f"x{[f'^{x_s-1}', ''][x_s-1 == 1]}", ""][x_s-1 == 0 or list_for_diff_coef[-x_s] == 0], ''][list_for_diff_coef[-x_s] == '0'] + [[' + ', ''][list_for_diff_coef[-x_s+1] == 0], f' = 0 (mod {module})'][x_s-1 == 0]
    print(diff_word)

    # Find diff polynoms for suitable x-s

    # print(list_of_suitable_x0)

    list_of_suitable_polynom1 = [[]]*len(list_of_suitable_x0)
    # print(list_of_suitable_polynom1)

    for x0 in list_of_suitable_x0:
        polynom = find_polynom_for_x(x0, prime_number, list_for_diff_coef, by_Module=False)
        print(f"P'({x0}): {polynom}" + [" != 0", " == 0"][polynom % prime_number == 0] + f" (mod {prime_number})")
        if polynom % prime_number != 0:
            # print(list_of_suitable_x0.index(x0))
            print(f"For {x0} there is only One")
            list_of_suitable_polynom1[list_of_suitable_x0.index(x0)] = [polynom, x0, "One"]
        else:
            # print(list_of_suitable_x0.index(x0))
            print(f"For {x0} there is Many or None")
            list_of_suitable_polynom1[list_of_suitable_x0.index(x0)] = [polynom, x0, 'Many or None']

    print()
    print(f"PxTi: {list_of_suitable_polynom1}")


    # lists of solutions
    lists_of_solutions = [[]]*len(list_of_suitable_polynom1)
    # print(lists_of_solutions)

    k_max = 0

    modul = module

    while modul != 1:
        modul = int(modul/prime_number)
        k_max += 1

    def find_polynom_for_x0(x, list_of_suitable_polynom, prime_number, list_of_coef, is_Double=False):
        for polynom in list_of_suitable_polynom:
            if polynom[1] == x:
                return polynom[0]
        return find_polynom_for_x(x, prime_number, list_of_coef, by_Module=False)

    def many_or_none():
        print()
        # print(list_of_PxT[1], list_of_suitable_polynom, list_of_suitable_polynom1[list_of_suitable_polynom1.index(list_of_PxT)])
        # print(lists_of_solutions[list_of_suitable_polynom1.index(list_of_PxT)][k-1])
        polynomk = find_polynom_for_x0(lists_of_solutions[list_of_suitable_polynom1.index(list_of_PxT)][k - 1],
                                       list_of_suitable_polynom, prime_number, list_of_coef.copy())
        # print(polynomk)
        p_k = prime_number ** k
        # print(f"polynomk % p_k * prime_number != 0")
        # print(p_k)
        # print(f"{polynomk} % {p_k * prime_number} != 0")
        # print(polynomk % p_k*prime_number != 0)
        if polynomk % (p_k * prime_number) != 0:
            print(f"{polynomk} % {p_k * prime_number} != 0")
            print("None of x")
        elif polynomk % (p_k * prime_number) == 0:
            print(f"{polynomk} % {p_k * prime_number} == 0")
            print(f"Exists {prime_number} solutions")
            for t in range(prime_number):
                # print(t)
                x_next = lists_of_solutions[list_of_suitable_polynom1.index(list_of_PxT)][k - 1] + p_k * t
                # (x_next)
                lists_of_solutions[list_of_suitable_polynom1.index(list_of_PxT)] += [int(x_next)]
                # print("________________")
                # print()
                print(
                    f'x{k + 1} = {lists_of_solutions[list_of_suitable_polynom1.index(list_of_PxT)][k - 1]} + {p_k}*{int(t)} = {int(x_next)}')

    def check_above_level(p_k, prime_number, item, list_of_suitable_polynom, list_of_coef, k):
        list_of_result = []
        print()
        for t in range(prime_number):
            print(f"x{k+1} = {item} + {p_k}*{t} = {item + p_k*t}")
            list_of_result += [item + p_k*t]
        # polynom = find_polynom_for_x0(item, list_of_suitable_polynom, prime_number, list_of_coef)
        # if polynom % p_k*prime_number == 0:
        # print(list_of_result)
        return list_of_result

    for list_of_PxT in list_of_suitable_polynom1:
        if list_of_PxT[2] == 'One':
            print()
            print('For only One')
            print(f"x1 = x0 = {list_of_PxT[1]}")
            lists_of_solutions[list_of_suitable_polynom1.index(list_of_PxT)] = [list_of_PxT[1]]
            for k in range(1, k_max):
                # print(list_of_PxT[1], list_of_suitable_polynom, list_of_suitable_polynom1[list_of_suitable_polynom1.index(list_of_PxT)])
                # print(lists_of_solutions[list_of_suitable_polynom1.index(list_of_PxT)][k-1])
                polynomk = find_polynom_for_x0(lists_of_solutions[list_of_suitable_polynom1.index(list_of_PxT)][k-1], list_of_suitable_polynom, prime_number, list_of_coef.copy())
                # print(polynomk)
                polynomk_diff = find_polynom_for_x0(lists_of_solutions[list_of_suitable_polynom1.index(list_of_PxT)][k-1], list_of_suitable_polynom1, prime_number, list_for_diff_coef, is_Double=True)
                # print(polynomk_diff)
                p_k = prime_number ** k
                # print(p_k)
                print()
                print(f'x{k+1} = x{k} + {p_k}t')
                print(f't = -({polynomk}/{p_k})*{polynomk_diff}^-1 (mod {prime_number})')
                polynomk_diff_m1 = RAE(polynomk_diff, prime_number, needs_lcm=False, needs_view=True, is_Secret=False)['u1'][-1]
                # print(polynomk_diff_m1)
                t = (-(polynomk/p_k)*polynomk_diff_m1) % prime_number
                # print(t)
                x_next = lists_of_solutions[list_of_suitable_polynom1.index(list_of_PxT)][k-1] + p_k*t
                # (x_next)
                lists_of_solutions[list_of_suitable_polynom1.index(list_of_PxT)] += [int(x_next)]
                # print("________________")

                print(f't = -({polynomk}/{p_k})*{polynomk_diff_m1} (mod {prime_number})')
                print(f't = (-{int(polynomk/p_k)})*{polynomk_diff_m1} (mod {prime_number})')
                print(f't = {-int(polynomk / p_k)*polynomk_diff_m1} (mod {prime_number}) = {int(t)}')
                print(f'x{k+1} = {lists_of_solutions[list_of_suitable_polynom1.index(list_of_PxT)][k - 1]} + {p_k}*{int(t)} = {int(x_next)}')
        elif list_of_PxT[2] == 'Many or None':
            print()
            print('For Many or None')
            print(f"x1 = x0 = {list_of_PxT[1]}")
            lists_of_solutions[list_of_suitable_polynom1.index(list_of_PxT)] = [list_of_PxT[1]]
            list_to_check = [list_of_PxT[1]]
            for k in range(1, k_max):
                p_k = prime_number**k
                list_of_items_above_level = []
                # print(f"list to check: {list_to_check}")
                for item in list_to_check:
                    # print(k)
                    list_of_items_above_level += check_above_level(p_k, prime_number, item, list_of_suitable_polynom, list_of_coef, k)
                    # print(item)
                    # print(list_of_items_above_level)
                for item_next in list_of_items_above_level:
                    polynom = find_polynom_for_x(item_next, prime_number, list_of_coef, by_Module=False)
                    # print(item_next, "|", polynom)
                    checker = p_k * prime_number**2
                    # print(checker, polynom % checker == 0)
                    print(f"P({item_next}): {polynom} {['!=', '=='][polynom % checker == 0]} 0 (mod {checker})")
                    if polynom % checker == 0 and checker <= module:
                        list_to_check += [item_next]
                        lists_of_solutions[list_of_suitable_polynom1.index(list_of_PxT)] += [item_next]
                    elif checker == module * prime_number:
                        lists_of_solutions[list_of_suitable_polynom1.index(list_of_PxT)] += [item_next]
                list_to_check.pop(0)
        # lists_of_solutions[list_of_suitable_polynom1.index(list_of_PxT)] = set(lists_of_solutions[list_of_suitable_polynom1.index(list_of_PxT)])
        # lists_of_solutions[list_of_suitable_polynom1.index(list_of_PxT)] = sorted(list(lists_of_solutions[list_of_suitable_polynom1.index(list_of_PxT)]))
        lists_of_solutions[list_of_suitable_polynom1.index(list_of_PxT)] += [["Only last is correct", "Except first all is correct"][list_of_PxT[2]!="One"]]
        lists_of_solutions[list_of_suitable_polynom1.index(list_of_PxT)] += [f"For {list_of_PxT[1]}"]
    print(lists_of_solutions)