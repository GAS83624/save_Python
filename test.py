import random
x = random.randint(1, 500)
print("========")
print("เฉลย =",x)
print("========")
while True:
    num = int(input("ใส่เลข: "))
    if num == x:
        break
    elif num>=x:
        print("มากไป")
    elif num<=x:
        print("น้อยไป")
    else:
        print("ลองใหม่")
print("ถูกต้อง")