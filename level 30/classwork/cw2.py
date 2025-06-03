# შექმენით ფუნქცია manual_count, 
# რომელსაც არგუმენტად გადაეცემა რიცხვბის სია,
#  და ერთი რიცხვი, რომლის რაოდენობაც უნდა ვიპოვოთ ამ სიაში. დააბრუნეთ მიღებული რაოდენობა

def manual_count(numbers , number):
    count = 0
    for i in numbers:
        if i == number:
            count += 1
    return count


print(manual_count([1, 2, 3, 2, 4, 2, 5], 2)) 
print(manual_count([10, 20, 30, 40], 25)) 


