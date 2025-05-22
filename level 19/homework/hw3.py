 #  შექმენით რიცხვების სია შემგარი 10 მინიმუმ ელემენტისგან.
 # გაიგეთ ამ სიაში ყველაზე პატარა და დიდი რიცხვი, შემდეგ კი დაბეჭდეთ მათი ჯამი

numbers = [1,2,3,4,5,6,7,8,9,10]

biggest_number = numbers[0]
smalles_number = numbers[0]

for i in numbers:
    if i > biggest_number:
        biggest_number = i
    if i < smalles_number:
        smalles_number = i

print(biggest_number+smalles_number)