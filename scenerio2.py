# 0/1 Knapsack Problem using Dynamic Programming


def knapsack_max_value(weights, values, capacity):
    if len(weights) != len(values):
        raise ValueError("The number of weights and values must be the same.")
    if capacity < 0:
        raise ValueError("Bag capacity cannot be negative.")
    if any(weight < 0 for weight in weights):
        raise ValueError("Item weights cannot be negative.")

    best_values = [0] * (capacity + 1)

    for weight, value in zip(weights, values):
        for current_capacity in range(capacity, weight - 1, -1):
            best_values[current_capacity] = max(
                best_values[current_capacity],
                best_values[current_capacity - weight] + value,
            )

    return best_values[capacity]


def read_integer_list(prompt):
    entries = input(prompt).replace(",", " ").split()
    return [int(entry) for entry in entries]


def main():
    try:
        weights = read_integer_list(
            "Enter item weights separated by spaces or commas: "
        )
        values = read_integer_list(
            "Enter item values in the same order: "
        )
        capacity = int(input("Enter the bag capacity: "))

        maximum_value = knapsack_max_value(weights, values, capacity)
        print(f"Maximum obtainable value: {maximum_value}")
    except ValueError as error:
        print(f"Invalid input: {error}")


if __name__ == "__main__":
    main()
