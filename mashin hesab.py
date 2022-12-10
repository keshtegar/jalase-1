#maryam keshtegar's calculatre

import math
i=int(input("which operations?? 2 variables or 1 variable? "))
if i==1:
    a=float(input("please enter a number: "))
    c=math.radians(a)
    print("operations are sin, cos , tan, cot ,factorial")
    op=input("please enter operation")
    if op=="sin":
        result=math.sin(c)
        print(result)
        
    if op=="cos":
        result=math.cos(c)
        print(result)
        
    if op=="tan":
        result=math.tan(c)
        print(result)
        
    if op=="cot":
        rsult=1/(c)
        print(result)
        
    if op=="sqrt":
        if a>=0:
            result=math.sqrt(a)
            print(result)
        else:
            print("لطفا مقداری مثبت وارد کنید")
            
    if op=="factorial":
        result=math.factorial(a)
        print(result)
if i==2:
    
    b=float(input("please enter first number: "))
    d=float(input("please enter second number: "))
    print("operations is + , - ,* ,/ , %,")
    op=input("please enter operation")




     

    if op=="+":
        result=b+d
        print(result)

    if op=="-":
        result=b-d
        print(result)
        
    if op=="*":
        result=b*d
        print(result)

    if op=="/":
        if d!=0:
            result=b/d
            print(result)
            
        else:
            print("لطفا مقدار غیر صفر را برای  متغیر دوم وارد  کنید ")
    if op=="%":
        if d!=0:
            result=b/d
            print(result)
        
        else:
            print("لطفا مقدار غیر صفر را برای  متغیر دوم وارد  کنید ")
    

    
        





        
        

