#  შექმენით სია სადაც გექნებათ რიცხვები. for loop-ის გამოყენებით იპოვეთ ამ სიაში ყველაზე დიდი რიცხვი


my_list = [23, 34, 43, 60, 1]
max = my_list[0]

for i in range(1,len(my_list)):
    if max < my_list[i]:
      max = my_list[i]
        
print(max)






