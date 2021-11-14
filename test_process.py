import time


def main():
    result = 0
    with open('test_process.py', 'r') as f:
        print(f.read())
        for _ in range(2**27):
            result += 1
    print(result)

    time.sleep(1)

    for _ in range(2 ** 27):
        result += 1
    print(result)


if __name__ == '__main__':
    main()
