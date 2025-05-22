 # დაწერეთ პროგრამა, რომელიც მომხარებელს შემოატანინებს წელს და გაიგებს არის თუ არა ის ნაკიანი(წელი როდესაც თებერვალში 29 დღე გვაქვს)
#ნაკიანი არის წელი თუ ის იყოფა 4-ზე და არ იყოფა 100-ზე ან იყოფა 400-ზე.
# (გამოიყენეთ and და or ოპერატორები)

# 1) shmemovananine weli 
# 2) vayalibebt logikas tu momxmareblis shemotanili ricvxi iyofa 4 ze unashtod da ar iyofa 100 ze unashtod.

user_year = int(input("Enter year: "))

if user_year % 4 == 0 and user_year % 100 != 0:
    print("es weli aris nakiani")
elif user_year % 400 == 0:
    print("es weli aris nakiani")
else:
    print("es weli ar aris nakiani")