#  შექმენით სახელების სია, გადაუარეთ მას for loop-ით და დაბეჭდეთ ამ სიიდან მხოლოდ ის სახელები, რომლებიც იწყებიან "A"-ზე
names = ["ana", "Nika","gio", "Dato", "andria",  "Lasha"]

def starts_with_a(word):
    if len(word) == 0:
        return False
    return word[0] == "a"


for name in names:
    if starts_with_a(name):
        print(name)
