# შექმენით სიმბოლოების სია, სადაც იქნება დუბლიკატები. შექმენით ახალი სია სადაც ყველა სიმბოლო მხოლოდ ერთხელ გვხვდება

lst = ['w', '1', 'w', '4', 'm']
new_lst = []

def find(arr, symbol):
    for i in range(len(arr)):
        if arr[i]==symbol:
            return True
    return False

for i in range(len(lst)):
    if not find(new_lst, lst[i]):
        new_lst.append(lst[i])

print(new_lst) 




