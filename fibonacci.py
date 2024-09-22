def fibonacci(n, prev=0, curr=1):
    print(curr)
    if n == 0:
        return prev
    return fibonacci(n - 1, curr, prev + curr)

if __name__ == '__main__':
    n = 100
    print(f"fibonacci({n}) = {fibonacci(n)}")
