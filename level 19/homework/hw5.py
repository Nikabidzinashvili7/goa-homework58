# შექმენით რიცხვების სია,
# გადაუარეთ მას for loop-ით, გაიგეთ რამდენი ლუწი და რამდენი კენტი რიცხვი გვაქვს სიაში და დაბეჭდეთ მათი რაოდენობ

numbers = [1,2,3,4,5,6,7,8,9,10]
even_num = []
odd_num = []
for num in numbers:
    if num % 2 == 0:
        even_num.append(num)
    else:
        odd_num.append(num)

print("even numbers are:", len(even_num))
print("odd numbers are:", len(odd_num))

