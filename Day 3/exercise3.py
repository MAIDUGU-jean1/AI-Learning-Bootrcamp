base_input = input("Enter a number: ")

try:
    base = float(base_input)
except ValueError:
    print("Please enter a valid number.")
    exit(1)

print(f"Times table for {base}:")
for i in range(1, 13):
    result = base * i
    print(f"{base} x {i} = {result}")