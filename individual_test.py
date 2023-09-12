
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
    n = 30030
    phi2 = phi(n)
    omega = n/phi2
    print(n, omega)

if __name__ == '__main__':
    main()