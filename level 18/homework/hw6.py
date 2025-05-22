# შექმენით პროგრამა, რომელიც მომხარებელს შემოატანინებს რიცხვს და დაბეჭდავს 1-დან შემოტანილ რიცხვამდე ყველა მარტივ რიცხვს
lst = [1,23,4,2,1,2,4,4,5]
total = 0

def how_many_elements(arr, num): 
    count = 0
    for i in range(len(arr)):
        if arr[i]==num:
            count += 1
    return count
for i in range(len(lst)):
    count = how_many_elements(lst, lst[i])
    if count == 1:
        total += lst[i]
    print(total)


for i in range(len(lst)):
    count = 0
    for j in range(len(lst)):
        if lst[i]==lst[j]:
            count += 1
    if count==1:
        total+=lst[i]