def main():
    number = int(input("정수 입력>"))

    # if number % 2:
    #     print("홀수 입니다")
    # elif nuber %2 == 1:
    #     print("짝수 입니다.")

    print("홀수" if number %2 else "짝수", "입니다.")

if __name__ == "__main__":
    main()
