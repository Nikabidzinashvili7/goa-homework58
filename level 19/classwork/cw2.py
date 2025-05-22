# შექმენით სიმბოლოების სია, გადაუარეთ მას for loop-ით და სიიდან ყველა სიმბოლოს შორის მოახდინეთ კონკადინაცია.
# ციკლის გარეთ დაგჭირდებათ ცვლადი სადაც შაამატებთ ამ სთრინგებს

symbols_list=["lasha ", "giorgi ", "nika ", "andria "]
full_names=""
for i in range(len(symbols_list)):
        full_names+=symbols_list[i] 
print(full_names)