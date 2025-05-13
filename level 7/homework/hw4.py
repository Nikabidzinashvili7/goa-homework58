#მომხმარებელს შემოატანინე მისი შემაფასებელი ქულა (0-დან 100-ის ჩათვლით).

#• იმ შემთხვევაში თუ შემოტანილი ქულა მეტია ან ტოლია 90-ის, ტერმინალში გამოიტანე "Grade A".
#• თუ მისი ქულა მეტია ან ტოლია 70-ზე გამოიტანე "Grade B". 
#• თუ მომხმარებლის ქულა მეტია ან ტოლია 50-ზე ტერმინალში დაბეჭდე "Grade C"
#• ყველა დანარჩენ შემთხვევაში გამოიტანე  "Grade F"




num = int(input("enter your point 0-100: "))

if  100 < num > 0:
    print("The score cannot be greater than 100, enter a number from 0-100.")
if  100 > num >= 90:
    print("Grade A")
if  90 > num >= 70:
    print("grade B")
if  70 > num >= 50:
    print("grade C")
if  50 > num > 0:
    print("grade F")
else:
    print


