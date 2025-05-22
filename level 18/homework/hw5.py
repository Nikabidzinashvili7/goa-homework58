# შექმენით რიცხვების სია,
# სადაც გექნებათ დუბლიკატები. გადაუარეთ მას for loop-ით და დაბეჭდეთ მხოლოდ ისეთი რცხვების ჯამი, რომლებიც არ მეორდება სიაში


numbers = [1,2,3,44,5,34,5,2,1,]
total = 0

def how_many_elements(arr, num): 
    count = 0
    for i in range(len(arr)):
        if arr[i]==num:
            count += 1
    return count
for i in range(len(numbers)):
    count = how_many_elements(numbers, numbers[i])
    if count == 1:
        total += numbers[i]
        

        