#  შექმენით ფუნქცია, რომელიც იღებს წინადადებას, და მასში space-ების მაგივრად სიტყვებს შორის ჩასვამს ტირეს("-"). საბოლოოდ კი აბრუნებს მას


def replace_spaces_with_dash(sentence):
    result = ''
    in_space = False
    first_word = True

    for char in sentence:
        if char != ' ':
            if in_space and not first_word:
                result += '-'
            result += char
            in_space = False
            first_word = False
        else:
            in_space = True 

    return result
