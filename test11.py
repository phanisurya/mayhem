n=int(input()) #read input number of number
ls=[]  #intialise the empty list

for i in range (0,n) :
        x=int(input())
        y=bin(x)  #convert each number to binary form
        y2=str.replace(str(y),'0','#') #replace 0 with #
        y3=str.replace(y2,'1','*')    #replace 1 with *
        y4=str.replace(y3,'#b','')      #since y=bin(x) prints a number say '1' in 0b001 liewise replace 0b whic is now #b
        ls.append(y4)
for x in ls:
    print(x)