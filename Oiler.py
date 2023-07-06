def fi(number, is_Secret=True):
    list_of_fi = []
    dict_of_used_simple = OTA(number, is_Secret)
    for simple_number in dict_of_used_simple:
        fi = dict_of_used_simple[simple_number] - int(dict_of_used_simple[simple_number] / simple_number)
        if not is_Secret:
            print()
            print(f'simple_number: {simple_number}')
            print(f'{dict_of_used_simple[simple_number]} - {int(dict_of_used_simple[simple_number]/simple_number)} == {fi}')
        list_of_fi += [int(fi)]

    result = 1

    for ready_fi in list_of_fi:
        result = result * ready_fi

    return result


def OTA(number, is_Secret):
    dict_of_used_simple = {}
    simple_number = 2
    while number > 1:
        while number % simple_number == 0:
            if not is_Secret:
                print(number, "|", simple_number)
            try:
                dict_of_used_simple[simple_number] = dict_of_used_simple[simple_number] * simple_number
            except KeyError:
                dict_of_used_simple[simple_number] = simple_number
            number = int(number / simple_number)

        simple_number += 1
    return dict_of_used_simple

def repeat():
    while True:
        print(f'Result is: {fi(int(input("Fi(n), n: ")), is_Secret=False)}')
        print()


if __name__ == "__main__":
    repeat()