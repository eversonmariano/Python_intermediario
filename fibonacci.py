from typing import Dict
memo:Dict[int, int] = {0: 0, 1: 1}

def fib(n: int) -> int:
    if n not in memo:
        return fib(n - 1) + fib(n - 2)
    return memo[n]
if __name__ == "__main__":
    print(fib(5))
    print(fib(10))
    print(fib(20))
    print(fib(30))
    print(fib(40))
    print(fib(45))
    print(fib(50))