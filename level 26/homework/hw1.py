 #  შექმენით ფუნქცია, რომელიც მიიღებს წინადადებას, 
 # ფუნქციამ ამ წინადადების თითოეული სიტყვა უნდა შეინახოს სიაში, როგორც ცალკე ელემენტი.
 #  საბოლოოდ გადააქციეთ სია ისევ წინადადებად, სადაც სიტყვებს შორის არის მძიმე და ერთი დაშორება(", ")


def sentence_to_comma(sentence):
    words = sentence.split()
    new_sentence = ", ".join(words)
    return new_sentence

print(sentence_to_comma("Hello my name is Nika"))

