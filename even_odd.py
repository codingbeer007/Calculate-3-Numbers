a=int(input("Set 01 -> "))
b=int(input("Set 02 -> "))
c=int(input("Set 03 -> "))

keet_int=[a,b,c]
count = 0
total = 0

while count < 3:

    if keet_int[count]%2==0:
        print(keet_int[count], "เป็นเลขคู่") 
    elif keet_int[count]%2!=0:
        print(keet_int[count], "เป็นเลขคี่")
    else:
        print("Error")
        
    count=count+1
