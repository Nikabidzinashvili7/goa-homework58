 # შექმენით რიცხვების სია და დაბეჭდეს სიის თითოეული რიცხვის ფაქტორიალი


#numbers = [9,2,4,3,5,6,7,8]


#for i in range(len(numbers)):
  #  my_list = numbers[i]
  #  count = 1
  #  for j in range(2, my_list + 1):
  #      count = count * j
  #  print(count)

numbers = [2,3,4,6,9,5]

for number in numbers:
    product = 1

    for i in range(1, number + 1):
        product = product * i

    print(product)


    # orive varianti sheidzleba 