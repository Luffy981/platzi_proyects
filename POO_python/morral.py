#!/usr/bin/env python3

def morral(morral_size, weight, values, n):
    if n == 0 or morral_size == 0:
        return 0
    if weight[n - 1] > morral_size:
        return morral(morral_size, weight, values, n - 1)
    return max(values[n - 1] + morral(morral_size - weight[n - 1], weight, values, n - 1), morral(morral_size, weight, values, n - 1))


if __name__ == '__main__':
    values = [60, 100, 120]
    weight = [10, 20, 30]
    morral_size = 50
    n = len(values)
    result = morral(morral_size, weight, values, n)
    print(result)
