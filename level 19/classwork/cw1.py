# შექმენით რიცხვების სია, შემდგარი მინიმუმ 10 ელემენტისგან. გადაუარეთ ამ საის while loop-ის გამოყენებით. 
# გაიგეთ ცალკე ლუწი და კენტი რიცხვების ჯამი,
# საბოლოოდ შეადარეთ ისინი ერთმანეთს და დაპრინტეთ უდიდესი


numbers = [1,2,3,4,5,6,7,8,9,10]
sum_even = 0
sum_odd = 0
i = 0

while i < len(numbers):
   if numbers[i] % 2 == 0:
      sum_even += numbers[i]
   else:
      sum_odd += numbers[i]
   i += 1
if sum_even > sum_odd:
   print(sum_even)
else:
   print(sum_odd)
   