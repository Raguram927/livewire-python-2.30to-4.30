# if else
'''a= int(input("enter a number"))
b=int(input("enter a number"))
if a<b:
      print(b)
else:
    print(a)

a= int(input("enter a number"))
b=int(input("enter a number"))
if a>b:
      print(b)
else:
    print(a)


n=int(input("enter a number"))
if n<0:
    print ("abuslute")
else :
    print("not")
   
a= int(input("enter a number"))

if a%2==0:
    print("even")
else:
    print("odd")
a= int(input("enter a number"))
if a%5==0:
    print ("multiple by 5")
else :
    print("not multiple by 5")
a= int(input("enter a number"))
if a%3==0:
    print ("multiple by 3")
else :
    print("not multiple by 3")
# stings
s="livewire"
print (s)
print(s[:])
print(s[:5])
print(s[0:8])
print(s[4:8])
print(s[-1])
print (s[1])
print(s[::-1])
print(s[2])
print (s[::-6])

#reverse string
s="livewire"
t=""
n=len(s)
for i in range (n-1,-1,-1):
    t=t+s[i]
print(t)
s="tenet"
t=""
n=len(s)
for i in range  (n-1,-1,-1):
    t=t+s[i]
if s==t:
    print("palindrome")
else:
    print("not palindrome")
s="tenet"
t=""
n=len(s)
for i in range  (n-1,-1,-1):
    t=t+s[i]
if s==s[::-1]:
    print("palindrome")
else:
    print("not palindrome")
# case changing
s="this Is PYthon"
print (s.lower())
print (s.upper())
print (s.capitalize())
print (s.title())
print (S.sweapcase())
#testing
print ("python".isalpha())
print("12345".isdigit())
print("m1m2m3".isalnum())
print(" ".isspace())
print("python".islower())
print("python".isupper())
print("Python Langage".istitle())'''
n=("\,+,+,=,@,python is the language")
symbols=0
upper=0
lower=0
space=0
number=0
for i in n:
    
    if(i.isupper):
        upper+=1
   
    elif(i.islower):
        lower+=1
    elif(i.isspace):
        space+=1
    elif(i.isnumber):
        number+=1
    elif(i.issymbols):
        symbols+=1
    print("upper Case:",upper)
    print("number:",digits)
    print("lowercase:",lower)
    print("space :",space)
    print("symbols:",symbols)
