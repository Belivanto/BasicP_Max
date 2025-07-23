#Workshop

distance=int(input("กรอกระยะทาง : "))
if distance <5:
    print(distance,"km","เดินเองเถอะ")
elif distance <=50 :
    print(distance,"km","ราคา 10 บาท ")
elif distance <=100 :
    print(distance,"km", "ราคา 15 บาท")
elif distance <=300 :
    print(distance,"km", "ราคา 25 บาท")
elif distance <=500 :
    print(distance,"km", "ราคา 35 บาท")
else :
    print(distance,"km","ราคา 45 บาท")

