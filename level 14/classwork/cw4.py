# შექმენით სია სადაც გექნებათ 10 რიცვი, შემდეგ შექმენით ახალი სია, 
# სადაც ჩაამატებთ პირველი სიიდან ყველა ლუწ რიცხვს და გაიგებთ მათ საშუალო არითმეტიკულს.(ახალ სიაზე გამოიყენეთ len() ფუნქცია)

numbers = [1,2,3,4,5,6,7,8,9,10]

even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(numbers)


if len(even_numbers) > 0:
    avarage = sum(even_numbers) / len(even_numbers)
    print("avarage of numbers are: ",avarage)

    