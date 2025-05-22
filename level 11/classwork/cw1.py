# პაროლის ვალიდაციის პროგრამა:

#შექმენით ცვლადი სადაც შეინახავთ პაროლს(მაგალითად: goa1234)

#სანამ მომხარებელი არ შემოიყვანს სწორ პაროლს მანამდე შემოატანინეთ ხელახლა. მომხარებელს ექნება 3 ცდა. თუ შემოიყვანა სწორი პაროლი დაუპრინტეთ "წვდომა მიღებულია", სხვა შემთხვევაში "სცადეთ ხელახლა", დაპრინტეთ რამდენი მცდელობა დარჩა და გამოაკელით ცდას ერთი. როდესაც მცდელობები ამოიწურება გათიშეთ while loop-ი
# ჩემი კომენტარები
# 1 შევქმნათ ცვლადი სადაც შემოიტანს პაროლს ექნება სულ სამი ცდა
# 2 whili -ის დამხარებით სანამ არ სჰემოიტანს სწორ პასხს მანამდე ახლიდან შემოტანა ვთხოვო
# 3 თუ სწორი პაროლი დაწერა დავუპრინტავ პაროლი სწორია თუ აარა 
password = "goa1234"
user_pass = " "
tries = 3
while tries > 0 and user_pass != password:
    user_pass = input("Enter your password (you have " + str(tries) + "tries left): ")
    tries = tries - 1

    if user_pass == password:
        print("access granted")
    elif tries == 0:
        print("you've reached maximum number of tries. access denied")
    else:
        print("access denied, try again")



    


