# Number of Ways to Make Change using Dynamic Programming


def count_ways(denominations, target):
    if target < 0:
        raise ValueError("The target amount cannot be negative.")
    if any(coin <= 0 for coin in denominations):
        raise ValueError("Coin denominations must be positive integers.")

    ways = [0] * (target + 1)
    ways[0] = 1

    for coin in sorted(set(denominations)):
        for amount in range(coin, target + 1):
            ways[amount] += ways[amount - coin]

    return ways[target]


def main():
    try:
        coin_input = input(
            "Enter coin denominations separated by spaces or commas: "
        ).replace(",", " ")
        denominations = [int(coin) for coin in coin_input.split()]
        target = int(input("Enter the target amount: "))

        if not denominations:
            raise ValueError("Enter at least one coin denomination.")

        total_ways = count_ways(denominations, target)
        print(f"Total possible combinations: {total_ways}")
    except ValueError as error:
        print(f"Invalid input: {error}")


if __name__ == "__main__":
    main()
