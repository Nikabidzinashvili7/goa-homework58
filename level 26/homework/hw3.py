#  შექმენით ფუნქცია,
#  რომელიც იღებს წინადადებას, სადაც ყოველი სიტყვის შორის ერთზე მეტი დაშორებაა(space). თქვენი დავალებაა ჩამოაშოროთ 
# გადმოცემულ წინადადებას ზედმეტი space-ები(სიტყვებს შორის მხოლოდ ერთი უნდა იყოს). საბოლოოდ დააბრუნეთ ეს წინადადება


def normalize_spaces_low_level(sentence):
    result = ''
    in_space = False

    for char in sentence:
        if char != ' ':
            result += char
            in_space = False
        else:
            if not in_space:
                result += ' '
                in_space = True

    return result.strip()
sentence = "hello   my  name   is        nikoloz"
print(normalize_spaces_low_level(sentence))
