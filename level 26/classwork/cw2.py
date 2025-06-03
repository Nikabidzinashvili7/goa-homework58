#  შექმენით ფუნქცია, manual_title, რომელიც იქნება title ფუნქციის კლონი


def manual_title(text):
    result = ""
    words = text.split()  
    for word in words:
        if len(word) > 0:
            result += word[0].upper() + word[1:].lower() + " "
    return result.strip()  


print(manual_title("MY NAME iS NIkOLoz"))





