#ทำตามลำดับ ถ้ามีข้าวเป็น False จะไม่ทำเงื่อนไขต่อไป
hasRice = True
hasSpoon = False
if hasRice:
    print("มีข้าว")
    if hasSpoon:
        print("มีช้อน")
        print("กินข้าวได้")
    else:
        print("กินข้าวไม่ได้เพราะไม่มีช้อน")
else:
    print("กินข้าวไม่ได้ เพราะไม่มีข้าว")

print("=======================")
# โปรแกรมคำนวณผลรวม


while True:
   inp = float(input("input number : "))
   if inp ==7.0:
        break

