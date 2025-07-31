import numbers as n
import math


class result:
    def __init__(s, tn, on):  # type: ignore
        s.Total_Marks = tn
        s.Obtained_Marks = on

    def Credentials(s):  # type: ignore
        print('')
        print('RESULT'.center(20, '='))
        print(
            'Total marks'.ljust(16, '.') + str(s.Total_Marks).rjust(4)
        )
        print(
            'Obtained Marks'.ljust(16, '.') + str(s.Obtained_Marks).rjust(4)
        )

    def percentage(s):  # type: ignore
        age = (int(s.Obtained_Marks) / int(s.Total_Marks)) * 100
        print(
            'Percentage'.ljust(16, '.') + str(age).rjust(4)
        )


if __name__ == "__main__":

    print(
        "Please input..."
    )

    a = input('Total Marks\n')
    b = input('Obtained Marks\n')

    if not type(a) or type(b) is int:
        raise ('Only Numbers are accepted.')  # type: ignore

    else:
        alpha = result(a, b)
        alpha.Credentials()
        alpha.percentage()


xyz = math.factorial(3)
print(xyz)










































