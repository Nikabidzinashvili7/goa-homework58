#  შექმენით ფუნქიცა, manual_find, რომელსაც გადაეცემა არგუმენტად სთრინგი და ერთი სიმბოლო,
#  რომელიც უნდა ვიპოვოთ ამ სთრინგში.
#  თუ სიმბოლო მოიძებნა დააბრუნეთ მისი ინდექსი, სხვა შემთხვევაში დააბრუნეთ -1
def manual_find(text, symbol):
    for i in range(len(text)):
        if text[i] == symbol:
            return i
    return -1


print(manual_find("hello", "e"))  
print(manual_find("world", "z"))  
