n = int(input("Enter the number of country stamp Rupal has :- "))

stamps = set()

for i in range(n):
     stamp = input(f"Enter the country name {i+1} ")
     stamps.add(stamp)

print(" the total number of distinct country stamps are ",len(stamps))     