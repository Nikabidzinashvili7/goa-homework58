# მომხმარებელს შემოატანინეთ რიცხვი 1-დან 100-ის ჩათვლით(ეს იქნება მისი ქულა). 
# თუ მაგალითად 90-დან 100-ის ჩათვლით ექნება ქულა გამოუტანეთ "Your grade is A", თუ 80-დან 90-მდე, გამოუტანეთ "Your grade is B",
# თუ 70-დან 80-მდე გამოუტანეთ "Your grade is C", სხვა შემთხვევაში გამოუტანეთ "Your grade is D"


score = int(input("Enter your score: ")) # momxmarebels shemoaqvs ricxvi 

if score >= 90 and score <= 100:# aq vayalibebt logikas tu es ricxvi metia an tolia  90 tze da naklebia 100 ze  daweros sheni nishania 
    # A da igivenairad qveda xazebshi 
    print("Your grade is A")
elif score >= 80 and score < 90:
    print("Your garde is B")
elif score >= 70 and score < 80:
    print("Your grade is C")
else:
    print("Your grade is D")