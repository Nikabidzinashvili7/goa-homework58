#  შექმენით ფუნქცია, რომელიც არგუმენტად მიიღებს string-ს.
#  ამ ფუნქციამ უნდა გაიგოს გადმოცემულ string-ში თითოეული სიმბოლოს რაოდენობა 
# და ჩაამატოს ახალ სიაში(ერთი სიმბოლის რაოდენობა მხოლოდ ერთხელ უნდა ჩაამატოთ.
#  მგალითად თუ string-ში 5 "a" გვხვდება, რიცხვი 5 მასივში მხოლოდ ერთხელ უნდა ჩავამატოთ,
#  მაგრამ სხვა სიმბოლოც თუ გვხვდება იგივე რაოდენობით, 
# მას ვამატებთ ჩვეულებრივ). საბოლოდ დაასორტირეთ მიღებული სია ზრდადობით და დააბრუნეთ


def unique_char_counts_sorted(text):
    counts = []  
    for char in text:
        count = 0

        
        for c in text:
            if c == char:
                count += 1

        
        if count not in counts:
            counts.append(count)

    
    for i in range(len(counts)):
        for j in range(i + 1, len(counts)):
            if counts[i] > counts[j]:
                counts[i], counts[j] = counts[j], counts[i]

    return counts
