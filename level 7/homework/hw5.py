#მომხმარებელს შემოატანინე მთელი რიცხვი. იმ შემთხვევაში, თუ ეს რიცხვი არის ლუწი და ამავდროულად არის 10-ზე მეტი, დაბეჭდე True. ყველა სხვა შემთხვევაში False. 
num = int(input("enter number: "))

if num > 10 and num % 2 == 0:
    print("True")
else:
    print("false")


