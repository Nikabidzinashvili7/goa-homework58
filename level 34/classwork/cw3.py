# შექმენით manual_count ფუნქცია, რომელსაც გადაეცემა სთრინგი ან სია და ელემენტი
#  რომლის რაოდენობაც უნდა გაიგოთ. დააბრუნეთ მიღებული შედეგი.


def manual_count(data, target):
    count = 0
    for item in data:
        if item == target:
            count += 1
    return count


print(manual_count("banana", "a"))        
print(manual_count([1, 2, 3, 2, 2, 4], 2)) 
print(manual_count(["a", "b", "a"], "a"))  
