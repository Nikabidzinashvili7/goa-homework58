# დაწერეთ პროგრამა, რომელიც მომხამრებელს შემოატანინებს რიცხვს და აბრუნებს სიას,
# სადაც იქნება გამდოცემული რიცხვის ყველა გამყოფი

number = int(input("enter your number: "))


divisors = []

for i in range(1,number + 1):
    if number % i == 0:    
        divisors.append(i)


print(divisors)
