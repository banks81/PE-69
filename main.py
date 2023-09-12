
"""
Function: phi
Parameters: int n
Returns: int phi

This function calculates the number of coprime numbers of an integer n using the coprime function
"""
def phi(n):
    i = 1
    phi = 0
    while i < n:
        if coprime(n, i) == True:
            phi += 1
        i += 1
    return phi

"""
Function: coprime
Parameters: int n, int i
Returns: boolean T or F

This function determines if two numbers are coprime
"""
def coprime(n1, i):
    j = 2
    while j < n1:
        if n1 % j == 0 and i % j == 0:
            return False
        j += 1
    return True

def main():
    n = 2
    omega = 0
    while n <= 10000:
        phi2 = phi(n)
        if n/phi2 > omega:
            omega = n/phi2
            print(n, omega)
        n += 1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
