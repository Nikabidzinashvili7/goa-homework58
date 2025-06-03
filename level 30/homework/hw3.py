#  შექმენით ფუნქცია manual_len, რომელსაც გადაეცემა სთრინგი ან სია,
#  ხოლო ფუნქციამ უნდა დააბრუნოს გადმოცემული სთრინგის/სიის სიგრძე(არ გამოიყენოთ len-ი)


def manual_len(data):
    count = 0
    for _ in data:
        count += 1
    return count


print(manual_len("hello"))   
print(manual_len([1, 2, 3, 4]))  
