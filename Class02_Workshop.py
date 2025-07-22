#Workshop

x=int(input("กรอกระยะทาง : "))
if x <5:
    print(x,"เดินเองเถอะ")
elif x <=50 :
    print(x,"ราคา 10 บาท ")
elif x <=100 :
    print(x, "ราคา 15 บาท")
elif x <=300 :
    print(x, "ราคา 25 บาท")
elif x <=500 :
    print(x, "ราคา 35 บาท")
else :
    print("ราคา 45 บาท")

