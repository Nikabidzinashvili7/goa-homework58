# მომხარებელს შემოატანინეთ ორი რიცხვი, აიყვანეთ ისინი მე-3 ხარისხში და გაიგეთ მათი ჯამი,
#  თუ ჯამი ლუწია დაპრინტეთ "Result is Even", სხვა შემთვევაში "Result is Odd"
# აღწერეთ თითოეული მოქმედება კომენტარებით
num1 = int(input("Enter first number: ")) #momxmarebels shemoaqvs ricvxi 
num2 = int(input("Enter second number: ")) # momxmarebels shemoaqvs meore ricvxi 


cube1 = (num1 ** 3) # aq vigebt ramdeni iqneba kubshi pirveli 
cube2 = (num2 ** 3) # aq igive meore 

result=cube1 + cube2 # aq kubebis shedegebs vamatebt da varqmevt result-s 

if result % 2 == 0: # aq vwer logikas tu orze iyofa es resulti 
    print("Result is Even")# aris luwi 
else: # svx shemtxvevashi 
    print("Result is odd") # aris kenti

