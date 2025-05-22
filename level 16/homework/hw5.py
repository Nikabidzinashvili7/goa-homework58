# შექმენით რიცხვების სია სადაც გექნებათ დადებითი და უარყოფითი რიცხვები,
# შემდეგ შექმენით ახალი სია სადაც გექნებათ მხოლოდ უარყოფითი რიცხვები და დაბეჭდეთ ის(გამოიყენეთ while).


numbers = [3,-4,8,-3,-9,6,28] 

negative_numbers = []

index = 0

while index < len(numbers):
    if numbers[index] < 0:
        negative_numbers.append(numbers[index])
    index += 1
print(negative_numbers)

# es igive kodi for loop is gamoyenebit
#numbers = [8,3,-7,-3,7,5,9,-44]
#negative_numbers = []



#for num in numbers:
 #   if num < 0:
 #       negative_numbers.append(num)
#print(negative_numbers)




        

