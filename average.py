# maryam keshtegar's average program
name=str(input("please enter student's name': "))
family=str(input("please enter student's family "))
i1=float(input("please enter first lesson's score"))
i2=float(input("please enter second lesson's score "))
i3=float(input("please enter third lesson's score "))
if i1<=20>=0 and i2<=20>=0  and i3<=20>=0:
    average=(i1+i2+i3)/3
    if average>=17:
        print("Greate")
    if average<17>=12:
        print("Normal")
    if average<12:
        print("Fail")
else:
    print("نمرات در محدوده نیستند")