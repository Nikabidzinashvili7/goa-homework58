# შექმენით სია სადაც გექნებათ რიცხვები. for loop-ის გამოყენებით იპოვეთ ამ სიაში ყველაზე პატარა რიცხვი

numbers = [3,4,5,6,7,8,9,77,]

lower_number = numbers[0]

for number in numbers:
    if number < lower_number:
        lower_number = number


print(lower_number)