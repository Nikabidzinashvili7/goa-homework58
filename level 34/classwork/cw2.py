# შექმენით manual_join ფუნქცია, რომელსაც გადაეცემა სთინგების სია და ერთი სთრინგი.
#  ამ ფუნქციამ უნდა შეართოს ეს სია და თითოეულ ელემენტს შორის ჩასვას გადმოცემული სთრინგი
# არ გამოიყენოთ .join() ფუნქცია

def manual_join(string_list, separator):
    result = ""
    for i in range(len(string_list)):
        result += string_list[i]
        if i < len(string_list) - 1:
            result += separator
    return result

words = ["apple", "banana", "cherry"]
sep = " - "
print(manual_join(words, sep))
