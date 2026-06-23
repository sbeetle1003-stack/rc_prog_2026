import datetime

from a01_hello import main as hello_main

def main():
    hello_main()
    now = datetime.datetime.now()

    if 9 < now.hour < 12:
        print(f"현재 시각은 {now.hour}로 오전입니다.")
    elif now.hour < 9:
        print(f"현재 시각은 {now.hour}로 새벽입니다.")
    else:
        print(f"현재 시각은 {now.hour}로 오후입니다.")

    if 11 < now.month < 4:
        print(f"현재 계절은 {now.month}로 겨울입니다.")
    elif 3 < now.month < 6:
        print(f"현재 계절은 {now.month}로 봄입니다.")
    elif 5 < now.month < 9:
        print(f"현재 계절은 {now.month}로 여름입니다.")
    else:
        print(f"현재 계절은 {now.month}로 가을입니다.")

    print(now.month, type(now.month))
    # 봄, 여름, 가을, 겨울 출력
    # 12, 1, 2, 3->겨울
    # 4, 5->봄
    # 6, 7, 8->여름
    # 9, 10, 11->가을

if __name__ == "__main__":
    main()