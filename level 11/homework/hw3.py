#  დაბეჭდეთ 1-დან 100-მდე ყველა ლუწი რიცხვის საშუალო არითმეტიკული.
#  გამოიყენეთ while loop-ი.(დაგჭირდებათ ორი ცვლადის შექმნა, ერთში შეინახავთ ჯამს, მეორეში რაოდენობას)
quantity = 0# aq shemogvaq quality sadac vinaxavt gameorebebs am shemtxvevashi nuli
i = 1 # aq shemogva i radganac i is 1 da 99 mde unda gadavuyvet
sum = 0 # aq ki jami


while i < 100: # aq vayalibebt aset logikas sanam i naklebi iqneba 100 ze es operacia gaakete 
    if i % 2 == 0: # aq i vyoft orze radganac mxolod luzi ricxvebi amoigos 
        sum += i # aq jams unda mivumato i
        quantity += 1  # aq ki raodenobas davumatot erti radganac gavigot sul ricxvebis raodenoba 
    i += 1   # aq ki i is davumatt erti radganac cikli dsruldes rodesac i 99 ts gadacdeba 
    
avarge = int(sum / quantity) #aq jami unda gavyot raodenobaze ro sashvalo davtvalot. da int- svuwert win ro ricxvad gadavaqciot

print("luwi ricvis sashvalo aritmetikuli", avarge)# aq ki es gamoprintos 

