n = int(input())
dicti=[]

for i in range(n):
    dicti.append(str(input()))
def startingnumcheck(num):
    if num[0]=='4' or num[0]=='5' or num[0]=='6':
        return True
    else:
        return False
def lengthcheck(num):
    if '-' in num:
        if len(num)==19:
            return True
        else:
            return False
    elif len(num)==16:
        return True
    else:
        return False
def digitcheck(num):
    if not num.isdigit():
        for i in num:
            if not (i.isdigit() or i=='-'):
                return False
    return True
def seperationcheck(num):
    if '-' in num:
         for val in num.split("-"):
             if len(val) != 4:
                 return False

    return True

def repcheck(num):
    res = "".join(num.split("-"))
    for i in range(len(res)):
        try:
            if (res[i] == res[i+1]):
                if (res[i+1] == res[i+2]):
                    if (res[i+2] == res[i+3]):
                        return False
        except IndexError:
           pass
    return True
for num in dicti:
    num=str(num)
    result=[startingnumcheck(num),lengthcheck(num),digitcheck(num),seperationcheck(num),repcheck(num)]
    if False in result:
        print('Invalid')
    else:
        print('Valid')
    