name =input(("เขียนชื่อ:"))
if name.startswith("นาย"):
    print("สวัสดีครับ", name)
elif name.startswith("นางสาว"):
    print("สวัสดีค่ะ", name)
elif name.startswith("นาง"):
    print("สวัสดีค่ะ", name)
else:
    print("สวัสดี", name)

  
# mouth=input(("เขียนเดือน:"))
# if mouth.endswith("คม"):
#     print("มี 31 วัน")
# elif mouth.endswith("ยน"):
#     print("มี 30 วัน")