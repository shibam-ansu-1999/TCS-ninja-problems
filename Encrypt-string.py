st = input("Enter your simple string:")
key = int(input("Enter your key:"));
rs = []
if key < 0 :
    print("INVALID INPUT")
else:
    for i in st:
        if i != " ":
            ascii = ord(i)
            ch = ascii + key
            if ch in range(97,123):
                rs.append(chr(ch))
            elif ch in range(65,91):
                rs.append(chr(ch))
            elif ch > 91 and ch < 97:
                r = ch % 91
                chn = 65 + r
                rs.append(chr(chn))
            elif ch > 122:
                r = ch % 122
                chn = 97 + r
                rs.append(chr(chn))
                
        else:
            rs.append(i)
    print("Your encrypt code is:",end = " ")
    for j in rs:
        print(j,end = "")
