import cmath

if __name__ == "__main__":
    a = int(input())
    A = complex(0, a)
    b = int(input())
    B = complex(b, 0)
    M = (A+B)/2
    phi = cmath.phase(M)
    phi = round(phi*180/cmath.pi)
    print(f"{phi}\N{DEGREE SIGN}")