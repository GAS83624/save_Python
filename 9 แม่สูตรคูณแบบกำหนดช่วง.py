#แม่สูตรคูณแบบกำหนดช่วง
start=int(input("ตั้งแต่:"))
end=int(input("จนถึง:"))
for i in range(start,  end+1):
    print("================")
    print("สูตรคูณแม่:", i)
    print("================")
    for o in range(1, 13):
        print(i, "x", o,"=", i*o)