# maryam keshtegar's triangle program
a=float(input("please enter first namber: "))

b=float(input("please enter second namber: "))

c=float(input("please enter third namber: "))

if a >0 and b>0 and c>0:
    if( a+b>c and a+c>b and b+c>a):
        print("با این سه عدد می توان یک مثلث رسم کرد")
    else:
        print("با این سه عدد نمیتوان مثلث رسم کرد")
else:
    print("لطفا مقادیر مثبت غیر صفر وارد کنید")

