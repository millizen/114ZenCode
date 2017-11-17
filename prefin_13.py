def change(num, nn):
    n1 = ["","one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
    n3 = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    s = ''
    if num != nn:
        s = n3[int(nn / 10) - 1] + '-'
        d = num % (nn-10)
        s += n1[d]
        return s
    elif num == nn:
        r = int(nn / 10)
        s = n3[r]
        return s
num = input()
s = ''
n1 = ["zero","one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
n2 = n1 + ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty']
if num.isdigit() and int(num) < 1000 and int(num) >= 0:
    num = int(num)
    if num <= 10: s = n1[num]
    elif num <= 20: s = n2[num]
    elif num <= 30: s = change(num, 30)
    elif num <= 40: s = change(num, 40)
    elif num <= 50: s = change(num, 50)
    elif num <= 60: s = change(num, 60)
    elif num <= 70: s = change(num, 70)
    elif num <= 80: s = change(num, 80)
    elif num <= 90: s = change(num, 90)
    elif num < 100: s = change(num, 100)
    elif num > 100:
        c = num // 100
        div = num % 100
        s = n1[c] + '-hundred' + '-'
        if div <= 10: s += n1[div]
        elif div <= 20: s += n2[div]
        elif div <= 30: s += change(div, 30)
        elif div <= 40: s += change(div, 40)
        elif div <= 50: s += change(div, 50)
        elif div <= 60: s += change(div, 60)
        elif div <= 70: s += change(div, 70)
        elif div <= 80: s += change(div, 80)
        elif div <= 90: s += change(div, 90)
        elif div < 100: s += change(div, 100)
else:
    s = "ERROR"
print(s)
