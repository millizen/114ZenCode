m = "medium"
M = "medium"
h = "high"
H = "high"
l = "low"
L = "low"
lp = int(input("Enter level pokemon: "))
if lp >= 0 and lp <= 40:
    lb = input("Enter level pokeball: ")
    if lb == m or lb == M:
        lb = 0.03
    elif lb == h or lb == H:
        lb = 0.01
    elif lb == l or lb == L:
        lb = 0.05
elif lp >= 41 and lp <= 60:
    lb = input("Enter level pokeball: ")
    if lb == m or lb == M:
        lb = 0.05
    elif lb == h or lb == H:
        lb = 0.01
    elif lb == l or lb == L:
        lb = 0.03
elif lp >= 61 and lp <=100:
    lb = input("Enter level pokeball: ")
    if lb == h or lb == H:
        lb = 0.01
    elif lb == m or lb == M:
        lb = 0.08
    elif lb == l or lb == L:
        lb = 0.1

dis = float(input("Enter distance: "))
percent = 100 - (lp * lb * dis)
print("%.2f percent." %percent)
