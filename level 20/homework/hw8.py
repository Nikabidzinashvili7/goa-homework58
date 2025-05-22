 #  შექმენით ფუნქცია, რომელსაც გადაეცემა რიცხვების სია.
 #  გადაუარეთ ამ სიას while ციკლით და ჩაამატეთ გაორმაგებული რიცხვები ახალ სიაში. საბოლოოდ დააბრუნეთ ეს სია

nums = [1,-5, 2, 3, 4, 5]

def double_numbers(nums):
    result = []
    i = 0

    while i < len(nums):
        doubled = nums[i] * 2
        result.append(doubled)
        i += 1

    return result

doubled_list = double_numbers(nums)
print(doubled_list) 
