# შექმენით ორი ცვლადი, პირველში შეინახეთ 1-დან 20-ის ჩათვლით ყველა ლუწი რიცხვის ჯამი,
# მეორეში კი ყველა კენტის. აიყვანეთ ორივე მე-5 ხარისხში და დაპრინტეთ ის, რომელიც არის მეტი
sum_even = 0
sum_odd = 0



for i in range(1,21):
   if i % 2 == 0:
        sum_even += i
   else:
        sum_odd += i

odd_power=sum_odd ** 5
even_power=sum_even ** 5

if odd_power > even_power:
   print("more is odd power:",odd_power)
else:
   print("more is even power:",even_power)





