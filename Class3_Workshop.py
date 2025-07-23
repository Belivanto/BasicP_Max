#starburst stream
zombie = "เลือด 20"
Sword = "พลังโจมตี 10"
Staff = "พลังโจมตี 5"
Bow = "พลังโจมตี 5"

while True:
    num = int(input("เลือก 1 ถ้าสู้กับมอนเตอร์ เลือก 2 หนี :"))
    if num ==2:
        print("หนี")
        break
    elif num==1:
        print("คุณเลือกจะสู้")
        round = int(input("จะเลือกตีกี่รอบ : "))
        for i in range (round):
            weapon = int(input("อาวุธ 1.Sword 2.Staff 3.Bow : "))
            print(weapon)
        