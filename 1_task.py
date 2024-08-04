from io import StringIO


def n_print(n: int) -> str:

    n_str = StringIO()

    for index in range(1, n+1):

        n_str.write(str(index) * index)

    return print(n_str.getvalue())


while True:

    answer = input('input int, please: ')

    n_print(int(answer))
