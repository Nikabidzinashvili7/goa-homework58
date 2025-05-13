# თამაში "რიცხვის გამოცნობა". შექმენით ცვლადი და შეინახეთ რომელიმე რიცხვი 1-დან 20-ის ჩათვლით(ეს იქნება ჩაფიქრებული რიცხვი). გამოიყენეთ while loop-ი და მომხარებელს შემოატანინეთ რიცხვი იქამდე სანამ არ გამოიცნობს მას. თუ მომხარებლის მიერ შემოტანილი რიცხვი მეტია ჩაფიქრებულზე, დაპრინტეთ To high, თუ ნაკლებია Too low, ხოლო იმ შემთხვევაში თუ მომხარებელი გამოიცნობს რიცხვს დაპრინტეთ "You win"

secret_number = 8
user_num = 0

while user_num != secret_number:
    user_num = int(input("guess the number: "))

    if user_num > secret_number:
        print("your number is too hight")
    elif user_num < secret_number:
        print("your number is too low") 
    else: 
        print("you are right, you win")
    