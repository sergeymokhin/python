def fib(n):
    # put your code here
    l = []
    l.insert(0, 0)
    l.insert(1, 1)
    for i in range(2, n):
        l.append(l[i-1] + l[i-2])
    return l



def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()