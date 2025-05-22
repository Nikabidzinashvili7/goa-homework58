# შექმენით სია სადაც გექნებათ 10 რიცხვი,
# თქვენი დავალებაა გაიგოთ ამ სიაში ყველა ლუწი და კენტი რიცხვიოს ჯამი და დაბეჭდოთ

numbers = [1,2,3,4,5,6,7,8,9,10,]

sum_even = 0
sum_odd = 0



for num in numbers:
    if num % 2 == 0:
        sum_even += num
    else:
        sum_odd += num

print("sum of even numbers are: ",sum_even)
print("sum of odd numbers are: ",sum_odd)