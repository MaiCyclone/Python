'''
a=0;
while(a<8):
    print( "{} , {}".format("hello",a));
    a = a+1;
'''
'''
a=0;
for i in range(0,8):
    
    if(i==6):
        continue;
    elif(i==0):
        continue;
    print(i);
'''
#ChengFaKouJue
for i in range(1,10):
    for j in range(1,i+1):
        print("{}{}{}{}{}".format(i,"*",j,"=",i*j),end = " ");
    print();
    

