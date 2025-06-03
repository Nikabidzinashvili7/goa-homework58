#  შექმენით ფუნქცია, რომელსაც გადაეცემა წინადადება.
#  თქვენი დავალებაა ამ წინადადების სიტყვები შეაბრუნოთ და დააბრუნოთ(სიტყვების სიმბოლოები არ უნდა იყოს შებრუნებული)

  # მაგალითად: "Hello World!" >>> "World! Hello"

def reverse_words(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    return " " .join(reversed_words)


print(reverse_words("Hello World!"))


