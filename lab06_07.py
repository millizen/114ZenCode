x = int(input("Enter an 8-bit number: "))
numbits = bin(x)[2:].count("1")
print("The number %d has %d non-zero bits" % (x, numbits))
