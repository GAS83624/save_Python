#หาผลรวมของตัวเลขไม่จำกัดจำนวน
ans = 0
while True:
    number = int(input("ป้อนตัวเลข :"))
    if number<=0:
        break
    ans += number
print("คำตอบคือ :",ans)
