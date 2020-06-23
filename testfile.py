s=input()
import cmath as cm
s=s.replace('j','')
if '+' in s:
    x=s.split('+')
else:
    x=s.split()
print(x)


#a=cm.phase(complex(int(x[0]),int(x[1])))
#b=abs(complex(int(x[0]),int(x[1])))
#print("{:.3f}".format(a))
#print("{:.3f}".format(b))





