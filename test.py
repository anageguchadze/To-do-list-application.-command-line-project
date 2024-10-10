from tabulate import tabulate

my_list = ["go to doctor", "buy flowers", "fix the bike", "call grandma"]

# Create a list of lists with count and name
data = [[count, name] for count, name in enumerate(my_list, start=1)]

# Print the table without headers
print(tabulate(data, tablefmt="github"))
