def main():
    print( 10 == 100) 
    print( 10 != 100) 
    print( 10 < 100) 
    print( 10 <= 100)
    print(type(True))

    print(not True)
    print(not False)
    print(True and True)
    print(True or False)

    a=int(input("100 보다 큰 숫자를 넣어>"))

    if a > 100:
        print("a는 100 보다 큼.")
    print("시스템 종료")


if __name__ == "__main__":
    main()