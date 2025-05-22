password = "goa1234" # aq  vayenebt parols
user_pass = " " # aq momxmarebelistvis vtovebT adgils sadac chaiwereba misis shemotanili paroli
tries = 3 # aq ramdeni cda eqneba magas vwert
while tries > 0 and user_pass != password: # aq vwert tu sanamde unda gaesvas kodi sanam cda eqneba 0 lze meti da sanam momxmarblis 
   # paroli ar dametxveva chvens shemnils
    user_pass = input("Enter your password (you have " + str(tries) + "tries left): ") #aq  veubnebit ro sheiyvanos parlo da aseve
    # veubnebit tu ramdeni cda darcha 
    tries = tries - 1 # aq while shi vashenebt eset dvalebas rom yovel cdaze cdis raodenobas erti daakldes 

    if user_pass == password: # aq tu  momxmareblis paroli danmtxveva  chven sheqmnil rom qveda xazi gamoutanos 
        print("access granted")# ai es rac weria brwkalebshu
    elif tries == 0:# aq tu cdebi nuls gautoldeba ro meti cdis sashvaleba ar misces 
        print("you've reached maximum number of tries. access denied") # da es gamoutanos 
    else:# sxva shemtxvevashi ki 
        print("access denied, try again") # es dauweros 
