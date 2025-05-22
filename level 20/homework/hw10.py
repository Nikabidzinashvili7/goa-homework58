#  შექმენით ფუნქცია, რომელსაც გადაეცემა სახელების სია. შექმენით ახალის სია,
#  სადაც ჩაამატებთ გადმოცემული სიიდან მხოლოდ იმ სახელებს, რომლებიც იწყება "N"-ზე`. საბოლოოდ დააბრუნეთ ეს სია

def names_starting_with_n(names):
    n_names = []

    for name in names:
        if len(name) > 0 and name[0] == "N":
            n_names.append(name)

    return n_names



names = ["Nika", "Nia", "gia", "ia"]
result = names_starting_with_n(names)
print(result)  