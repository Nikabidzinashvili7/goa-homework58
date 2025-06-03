# შექმენით ფუნქცია, manual_capitalize რომელიც იქნება capitalize ფუნქციის კლონი

def manual_capitalize(text):
    if not text:
        return text
    first = text[0].upper()
    rest = text[1:].lower()
    return first + rest

print(manual_capitalize("mY Name IS NIKa"))
