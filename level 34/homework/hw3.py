# შექმენით ფუნქცია, რომელიც არგუმენტად იღებს რიცხვების სიას და აბრუნებს მას კლებადობის მიხედვით დასორტირებულს

def sort_descending(numbers):
    
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] < numbers[j]:  
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers


print(sort_descending([5, 1, 9, 3]))   
print(sort_descending([10, -2, 7, 7])) 
