from tabulate import tabulate

table = [["Sun",696000,1989100000],["Earth",6371,5973.6],["Moon",1737,73.5],["Mars",3390,641.85]]

# Manually define heADERS
print (tabulate(table, headers=["Planet","R (km)", "mass (x 10^29 kg)"]))

# When the headers are keys
print (tabulate({"Name": ["Alice", "Bob"],"Age": [24, 19]}, headers="keys"))