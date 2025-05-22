# შექმენით სია შემდგარი სახელებისგან. მომხარებელს შემოატანინეთ მისი სახელი, თუ მისი სახელი იქნება 5 სიმბოლოს ტოლი ან მეტი. 
# ჩაამატეთ სიაში, სხვა შემთხვევაში დაუბეჭდეთ "Name is too short"
names = ["andria","aleqsandre","giorgi","lasha"] # vqmnit  list saxelbit 

user_name = input("Enter your name:") # aq vtxovt momxmarebels shemoitanos tavisi saxeli 

if len(user_name) >= 5:# aq if is daxmarebit vayalibebt pirobas tu sityvashi asos sigrdze metia xutze daprintos 
    names.append(user_name) # aq vadzlevt brdzanebas ro chamatos
    print(f"the list of names after add your name is :{names} ") # aq tu ra daprintos 
else: # sxva shemtxvevashi ki
    print("your name is too short")   # daprintos es 