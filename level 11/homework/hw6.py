#  დაწერეთ პროგრამა, რომელიც მომხარებელს შემოატანინებს რიცხვს და დაბეჭდავს ეს რიცხვი დადებითია, უარყოფითია თუ 0-ია

num = int(input("Enter number: "))

if num > 0:
    print("number is positive")
elif num == 0:
    print("number is 0")
else:
    print("number is negative")
