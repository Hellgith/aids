from typing import List, Tuple

def optimal_bst(keys: List[int], freq: List[int], n: int) -> Tuple[List[List[int]], List[List[int]]]:
    cost = [[0] * n for _ in range(n)]
    root = [[0] * n for _ in range(n)]

    for i in range(n):
        cost[i][i] = freq[i]
        root[i][i] = i

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            cost[i][j] = float('inf')

            for r in range(i, j + 1):
                c = (cost[i][r - 1] if r > i else 0) + (cost[r + 1][j] if r < j else 0) + sum(freq[i:j + 1])
                if c < cost[i][j]:
                    cost[i][j] = c
                    root[i][j] = r

    return cost, root

def print_optimal_bst(root: List[List[int]], i: int, j: int, keys: List[int]):
    if i > j:
        return
    r = root[i][j]
    print(f"Root: {keys[r]}")
    print(f"Left subtree of {keys[r]}:")
    print_optimal_bst(root, i, r - 1, keys)
    print(f"Right subtree of {keys[r]}:")
    print_optimal_bst(root, r + 1, j, keys)

def get_user_input() -> Tuple[List[int], List[int], int]:
    n = int(input("Enter the number of keys: "))
    keys = [int(input(f"Key {i + 1}: ")) for i in range(n)]
    freq = [int(input(f"Frequency of key {keys[i]}: ")) for i in range(n)]
    return keys, freq, n

if __name__ == "__main__":
    keys, freq, n = get_user_input()
    cost, root = optimal_bst(keys, freq, n)

    print("\nOptimal Binary Search Tree:")
    print_optimal_bst(root, 0, n - 1, keys)

    print(f"\nMinimum search cost: {cost[0][n - 1]}")
