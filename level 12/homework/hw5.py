# მომხარებელს შემოატანინეთ რიცხვი და გაიგეთ არის თუ არა ის მარტივი, თუ მარტივია დაპრინტეთ "Number is prime",
# სხვა შემთხვევაში "Number is not prime"(მარტივია რიცხვი, რომელიც იყოფა მარტო თავის თავზე და ერთზე)

num=int(input("Enter number: ")) 

if num > 1: 
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
            
    
    if  is_prime == True:
        print("Number is prime")
    else:
        print("Number is not prime")

