from utils.hello_random import greet


def main():
    count = input("How many greetings would you like? ")
    if not count or not count.isdigit() or int(count) < 1:
        count = 1

    greet(int(count))



if __name__ == '__main__':
    main()
