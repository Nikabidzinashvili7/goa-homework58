# შექმენით პროგრამა, რომელიც მომხარებელს შემოატანინებს წელს და დაპრინტავს რომელი საუკუნეა ის


year = int(input("შეიყვანეთ წელი: "))

if year <= 0:
        print("გთხოვთ შეიყვანოთ დადებითი წელი.")
else:
     
        century = (year + 99) // 100
        print(century)