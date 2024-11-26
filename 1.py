# Daily Steps Tracker Program
steps_input = input("Enter the number of steps taken each day, separated by spaces: ")

steps = list(map(int, steps_input.split()))

highest_steps = max(steps)

lowest_steps = min(steps)

average_steps = sum(steps) / len(steps)

sorted_steps = sorted(steps, reverse=True)

print("\nDaily Steps Tracker Results:")
print(f"Highest Step Count: {highest_steps}")
print(f"Lowest Step Count: {lowest_steps}")
print(f"Average Daily Steps: {average_steps:.2f}")
print("Step Counts (Descending Order):", sorted_steps)