# შექმენით სია, 
# სადაც გექნებათ 5 ელემენტი.
#  წაშალეთ სიის მე-3 ელემენტი და დაამატეთ ახალი მე-0 ინდექსზე. საბოლოოდ დააბრუნეთ ეს სია


def modify_list():
   
    my_list = [1, 2, 3, 4, 5]

    new_list = []
    for i in range(len(my_list)):
        if i != 2:  
            new_list.append(my_list[i])
    
    final_list = [3]  
    for item in new_list:
        final_list.append(item)  
    return final_list


print(modify_list())



