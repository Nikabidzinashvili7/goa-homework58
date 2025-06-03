#  შექმენით ფუნქცია manual_pop, რომელსაც გადაეცემა ორი არგუმენტი, სია და ინდექსი.
#  წაშალეთ სიიდან, გადმოცემულ ინდექსზე მყოფი ელემენტი. საბოლოოდ კი დააბრუნეთ ეს სია(არ გამოიყენოთ .pop ფუნქცია)

def manual_pop(my_list, index):
    new_list = []
    for i in range(len(my_list)):
        if i != index:
            new_list.append(my_list[i])
    return new_list


my_list = [10, 20, 30, 40, 50]
result = manual_pop(my_list, 2)
print(result)  

