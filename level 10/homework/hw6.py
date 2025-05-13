 # მომხარებელს შემოატანინეთ რიცხვი და შეინახეთ ის ცვლადში. შემდეგ დაბეჭდეთ შემოტანილი რიცხვის ჩათვლით ყველა რიცხვის კვადრატის ჯამი

user_num = int(input("Enter num: "))

sum = 0

for num in range(user_num + 1):
    sum = sum + num * num

print(sum)