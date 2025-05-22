# თქვენი დავალებაა შექმნათ მარტივი ჩატ-ბოტი, რომელიც კოდის გაშვებისთანავე მიესალმება მომხარებელს და ჰკითხავს "How are your?",
#  თუ მომხარებელი შეიყვანს, "Normal" დაბეჭდეთ "Bot:I hope you will get better", სხვა შემთხვევაში თუ შემოიყვანს "Great",
#  დაუბეჭდეთ "Bot:Good! Have a nice day", ხოლო თუ შემოიყვანა "Sad" ან "Super Sad" დაუბეჭდეთ "Bot:It's sad".
#  საბოლოოდ დაბეჭდეთ "Good bye!" და გათიშეთ while ციკლი. ამისათვის მას გადაეცით სწორი პირობა
# (მინიშნება: შექმენით ცვლადი რომლის მნიშვნელობა თავიდან იქნება False, while ციკლს პირობად გაუწერეთ ეს ცვლადი, 
# თუ მომხარებელმა სწორი ინფორმაცია შემოიყვანა მისი ნიშვნელობა გახდება True და როცა ყველა პირობა შესრულდება while ციკლი გაითიშება).
# თუ მომხარებელი შემოიყვანს ისეთ ინფორმაციას რაზეც თქვენი ბოტი არ არის დაპროგრამირებული, დაბეჭდეთ "Bot: Sorry, I didn't understand, repeat."
# (ამ შემთხვევაში while ციკლისთვის შექმნილი ცვლადის მნიშვნელობა არ იცვლება და ციკლი არ წყვეტს მუშაობას)
# დაგჭირდებათ: while loop; input; if/else; and or.
# თქვენი სურვილით დაამატეთ სხვა ფუნქციები და გააუმჯობესეთ ჩატ-ბოტი



while True:
   print("how are you?")
   user_input = input("").lower()


   if user_input == "normal":
        print("I hope you will get better")
   elif user_input in ["great", "good"]:
        print("good! Have a nice day")
   elif user_input in ["sad","super sad"]:
       print("it's sad")
   elif user_input in ["exit", "good bye"]:
        print("good bye")
        break
   else:
       print("I can't answer your questions")

