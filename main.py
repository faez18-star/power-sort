def printPowerSet(input_set, set_size):
    # Calculate the size of the power set (2^n)
    power_set_size = 2**set_size

    # Loop over all possible combinations (from 0 to 2^set_size - 1)
    for outer in range(power_set_size):
        subset = []

        # For each number, check which bits are set (which elements to include)
        for inner in range(set_size):
            # If the bit at position 'inner' is set (1), include the element in the subset
            if outer & (1 << inner):
                subset.append(input_set[inner])

        # Print the subset
        print(subset)

# Example usage
input_set = [6, 4, 8, 5, 7]
set_size = len(input_set)
print("Power set of", input_set, "is:")
printPowerSet(input_set, set_size)