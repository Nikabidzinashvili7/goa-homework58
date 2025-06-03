# შექმენით manual_range ფუნქცია, რომელიც იქნება range ფუნქციის კოლნი, 
# ამ ფუნქციას უნდა ჰქონდეს 3 არგუმენტი, მაგრამ თუ გამოძახებისას გადაეცა მხოლოდ 
# 1 არგუმენტი default-ად start-ის მნიშვნელობა იქნება 0 და step-ის 1. ხოლო 2 არგუმენტის შემთხვევაში მხოლოდ step-ი იქნება 1.
#გაიხსენეთ, რომ range ფუნქციას გადაეცემა 3 პარამეტრი start, end, step


def manual_range(*args):
    result = []

    
    if len(args) == 1:
        start = 0
        end = args[0]
        step = 1

    
    elif len(args) == 2:
        start = args[0]
        end = args[1]
        step = 1

 
    elif len(args) == 3:
        start = args[0]
        end = args[1]
        step = args[2]

    else:
        raise TypeError("manual_range expected 1 to 3 arguments, got {}".format(len(args)))

    
    if step == 0:
        raise ValueError("step cannot be zero")

    if step > 0:
        while start < end:
            result.append(start)
            start += step
    else:
        while start > end:
            result.append(start)
            start += step  

    return result

print(manual_range(5))          
print(manual_range(2, 6))     
print(manual_range(10, 2, -2))  
