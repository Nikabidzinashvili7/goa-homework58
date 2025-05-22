 #  შექმენით ფუნქცია, რომელსაც გადაეცემა რიცხვების სია.
 #  გადაუარეთ ამ სიას for ციკლით და ჩაამატეთ მხოლოდ ლუწი რიცხვები ახალ სიაში. საბოლოოდ დააბრუნეთ ეს სია

def get_even_numbers(nums):
    even_numbers = []
    
    for num in nums:
        if num % 2 == 0:
            even_numbers.append(num)
    
    return even_numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = get_even_numbers(numbers)
print(even_numbers) 
