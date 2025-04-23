#หาผลรวมของตัวเลข 5 จำนวน
ans = 0
for n in range(1, 6):
    number = int(input("ลำดับที่ "+str(n) + ":"))
    ans += number
print("ผลรวม :",ans)