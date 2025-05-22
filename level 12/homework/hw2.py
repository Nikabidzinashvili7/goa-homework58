#  შექმენით რიცხვების დიაპაზონი 1-დან 100-მდე, შეამოწმეთ თუ რიცხვი იყოფა 3-ზე დაბეჭდეთ "Fizz" და გვერდზე მიუწერეთ რიცხვი.
# თუ რიცხვი იყოფა 5-ზე დაბეჭდეთ "Buzz" და გვერდზე მიუწერეთ რიცხვი,
# ხოლო თუ იყოფა 3-ზეც და 5-ზეც დაბეჭდეთ "FizzBuzz" და გვერდზე მიუწერეთ რიცხვი.

for i in range(1,100): # for loop is daxmarebit gadavuyvebit 1 da 100 amde 
   if i % 3 == 0 and i % 5 == 0: # tu i iyofa 3 ze da iyofa 5 ze dabechdos "Fizzbuzz"
    print("Fizzbuzz-", i) # rogor aq weia da miuweros ricxvi
   elif i % 3 == 0: # aq samze gayofisas da ase shemdeg
     print("Fizz-", i)
   elif i % 5 == 0:
     print("Buzz-",i)
   

