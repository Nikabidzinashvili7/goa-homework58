#  შექმენით ცლვადი სადაც შეინახავთ string-ს,
#  შემდეგ შექმენით ახალი ცვლადი სადაც შეინახავთ ამ სტრინგს შემოტრიალებულად და დაბეჭდეთ ის


text = "nika"
reversed_text = ""

# vipovot stringis sigrdze
length = len(text)

# aq ki davdivart stringis indexze ukugma
for i in range(length - 1, -1, -1):
    reversed_text += text[i]

print(reversed_text)
