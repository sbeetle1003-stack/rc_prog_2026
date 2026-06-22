def main():
    string = "abc"
    string2 = "this is format test: {}".format(10)
    print(string)
    print(string2)

    string3="this is format test: {2}, {1}, {0}".format(10, 20, 30)
    print(string3)
    string4="this is format test: {2:d} {1:5d} {0:05d}".format(-10, -20, -30)
    print(string4)

    string5="this is format test: {2:+2.f} {1:+5.f} {0:+05.2d}".format(10.1263, -20.4213, -38)
    print(string5)

if __name__ == "__main__":
    main()