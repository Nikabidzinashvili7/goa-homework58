#შექმენთ ფუნქცია, რომელიც არგუმენტად იღებს სიმბოლოების სიას.
#  დაასორტირეთ ეს სია ანბანის მიხედვით, გადააქციეთ string-ად და დააბრუნეთ


def sort_and_join(chars):
    
    for i in range(len(chars)):
        for j in range(i + 1, len(chars)):
            if chars[i] > chars[j]:
                chars[i], chars[j] = chars[j], chars[i]

   
    result = ""
    for char in chars:
        result += char

    return result
