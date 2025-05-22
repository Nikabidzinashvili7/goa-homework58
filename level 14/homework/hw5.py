#  შექმენით ორი ცარიელი სია, for loop-ის გამოყენებით მომხარებელს 5-ჯერ შემოატანინეთ ნებისმიერი სიტყვა.
#  თუ შემოტანილი სიტყვის სიგრძე არ აღემატება 5-ს ჩაამატეთ პირველ სიაში, სხვა შემთხვევაში მეორეში. საბოლოოდ დაბეჭდეთ ორივე სია

short_word = []
long_word = []

for i in range(5):
    word = input("enter word: ")
    if len(word) > 5:
        long_word.append(word)
    else:
       short_word.append(word)

    print("short word",short_word)
    print("long word",long_word)
    
