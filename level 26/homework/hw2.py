# შექმენით ფუნქცია, რომელიც მიიღებს წინადადებას და დაბეჭდავს მის თითოეულ სიტყვაში სიმბოლოების რაოდენობას(ცალ-ცალკე)

def sentance(text):
    words = text.split()
    for word in words:
        print(f"word: '{word}' - Number of characters: {len(word)}")


sentance("my name is nika")

