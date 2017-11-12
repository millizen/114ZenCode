sent = input("")

fullsent = len(sent)
NumDot = sent.count('.')
NumComma = sent.count(',')
checkletter = sent.replace(",", "")
checkalp = checkletter.replace(".", "")
allletter = checkalp.isdigit()
sentletter = sent.isdigit()
i = 1

if allletter == True or sentletter == True :
  i = 2

if allletter == False or sentletter == False :
  ans = False

if NumDot == 1  and NumComma == 0 and i != 1:  #check such as : 123.1231 123.04
  typedata = "dot"
  sent2 = sent.rfind(".")
  long1 = len(sent[sent2:])
  if float(sent) % 1 != 0 :
    if long1 == 3 :
      ans = True
    if long1 != 3 :
      ans = False
  if float(sent) % 1 == 0 :
    ans = True
  if sent[-1] == "." :
    ans = True

if NumDot == 0  and NumComma == 0 and i != 1 :  #check such as : 123
  ans = True
  typedata = "full"

if NumDot == 0  and NumComma >= 1 and i != 1 :  #check such as : 123,123 1111,223
  long1 = len(sent)
  stop = (long1 // 4)
  ans = False
  typedata = "comma"
  i = 1
  while long1 >= 5 :
    if i <= stop :
      if sent[-4*i] == "," :
        i = i + 1
        ans = True
      else :
        ans = False
        i = i +1
        break
      if i > stop :
        break

if NumDot == 1  and NumComma >= 1 and i != 1 :  #check such as : 123,123.36 111,223.3241
  typedata = "dotcomma"
  checkdot = sent.replace(",", "")
  sent2 = checkdot.rfind(".")
  long1 = len(checkdot[sent2:])
  checkcomma = sent[0:-3]
  if checkdot[-1] == "." :
    ans = True

  if float(checkdot) % 1 != 0 :
    if long1 == 3 :
        ans = True
    if long1 != 3 :
        ans = False
  if ans == True :
    long2 = len(checkcomma)
    stop = (long2 // 4)
    i = 1
    while long2 >= 5:
      if i <= stop :
        if checkcomma[-4*i] == "," :
          i = i + 1
          ans = True
        else :
          ans = False
          i = i +1
          break
        if i > stop :
          break

if ans == True :
  if typedata == "full" :
    show = int(sent)
    show = show + 1
    print (show)
  if typedata == "dot" :
    if sent[-1] == "." :
      show2 = float(sent)
      show9 = show2 + 1
      print ("%.0f." % show9)
    else :
      show2 = float(sent)
      show9 = show2 + 1
      print ("%.2f" % show9)
  if typedata == "comma" :
    returncommaout = sent.replace(",", "")
    show3 = int(returncommaout)
    show = show3 + 1
    print (show)
  if typedata == "dotcomma" :
    returncommaout = sent.replace(",", "")
    if sent[-1] == "." :
      show4 = float(returncommaout)
      show10 = show4 + 1
      print ("%.0f." % show10)
    else :
      show4 = float(returncommaout)
      show10 = show4 + 1
      print ("%.2f" % show10)
if ans == False :
  print ("ERROR")
