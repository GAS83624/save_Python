#ธนาคาร IF
username = input("Enter username = ")
password = input("Enter password = ")

while True:
    if username =="bank" and password =="123":
    print("Login completed")
    service = input("Select service 1-2 = ")
        if service =="1":
            print("บริการถอนเงิน")
            money = int(input("จำนวนเงิน : "))  # แปลงเป็นตัวเลขเพราะครั้งก่อนผิดพลาด
            if 0 <= money <= 1000:
                print("ขอบคุณที่ใช้บริการ")
                break
            else:
                print("จำนวนเงินผิดพลาด")
        elif service =="2":
            print("บริการฝากเงิน")
            money = int(input("จำนวนเงิน : "))  # แปลงเป็นตัวเลขเพราะครั้งก่อนผิดพลาด
            if 0 <= money <= 1000:
                print("ขอบคุณที่ใช้บริการ")
            else:
                print("จำนวนเงินผิดพลาด")
        else:
            print("ไม่มีบริการดังกล่าว")
    else:
        print("Account not found")