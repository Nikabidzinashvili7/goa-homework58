# შექმენით ფუნქცია, რომელსაც არგუმენტად გადაეცემა სია. 
# ფუნქციამ უნდა დაბეჭდოს ეს სია შებრუნებულად(არ გამოიყენოთ slicing-ი)

def reversed(numbers):
    i = len(numbers) - 1  

    while i >= 0:
        print(numbers[i])
        i = i - 1 

reversed([1, 2, 3, 4, 5, 6, 7, 8, 9])


