sub = input()
sub = int(sub)

tip = sub*(.2)
tax = sub*.07

total = sub + tip + tax
print("tip: ", tip, " Tax: ", tax, " Total: ", total)