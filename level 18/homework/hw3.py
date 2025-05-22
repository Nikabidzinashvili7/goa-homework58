#  შექმენით რიცხვების სია, while loop-ის გამოყენებით გაიგეთ ამ სიაში ყველა ლუწი რიცხვის ჯამი და დაპრინტეთ


numbers = [1, 28, 99, 4, 199, 6, 837, 8, 967, 10]


num = 0
sum_even = 0

while num < len(numbers):
    if numbers[num] % 2==0:  
        sum_even = sum_even+numbers[num]
    num=num + 1
print(sum_even)

