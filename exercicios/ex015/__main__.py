from classes import *

def main():
    c1 = Carteira(100)
    c2 = Carteira(200)

    c1 += 550
    c2 -= 43

    print(c1, c2)

if __name__ == "__main__":
    main()