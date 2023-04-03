
print("ALERT!!!\nGive data in given range for highly precise and accurate result\nProgram will not respomsible for your smartness")
print("--------*******--------********-------------**********------------*******---------")
# n = int(input(print("Enter the number of different layers\e.g coal or metal or sandstone or shale :")))
rmr =[]
i=0
while i<2:

    lt = float(input("Enter your LAYER THICKNESS(in CM)[0-100]:  "))
    if lt < 0:
        ltr = 0
        print("Lenght cant be negative\nRating is 0")
    elif lt >= 0 and lt < 0.4:
        ltr = 0
        print("Layer thickness Rating is ", ltr)
    elif lt >= 0.4 and lt < 0.8:
        ltr = 1
        print("Layer thickness Rating is ", ltr)
    elif lt >= 0.8 and lt < 1.2:
        ltr = 3
        print("Layer thickness Rating is ", ltr)
    elif lt >= 1.2 and lt < 1.6:
        ltr = 4
        print("Layer thickness Rating is ", ltr)
    elif lt >= 1.6 and lt < 2.0:
        ltr = 4
        print("Layer thickness Rating is ", ltr)
    elif lt >= 2 and lt < 2.5:
        ltr = 5
        print("Layer thickness Rating is ", ltr)
    elif lt >= 2.5 and lt < 3.3:
        ltr = 6
        print("Layer thickness Rating is ", ltr)
    elif lt >= 3.3 and lt < 3.7:
        ltr = 7
        print("Layer thickness Rating is ", ltr)
    elif lt >= 3.7 and lt < 4.3:
        ltr = 8
        print("Layer thickness Rating is ", ltr)
    elif lt >= 4.3 and lt < 5.0:
        ltr = 9
        print("Layer thickness Rating is ", ltr)
    elif lt >= 5.0 and lt < 5.6:
        ltr = 10
        print("Layer thickness Rating is ", ltr)
    elif lt >= 5.6 and lt < 6.2:
        ltr = 11
        print("Layer thickness Rating is ", ltr)
    elif lt >= 6.2 and lt < 6.5:
        ltr = 12
        print("Layer thickness Rating is ", ltr)
    elif lt >= 6.5 and lt < 7.5:
        ltr = 13
        print("Layer thickness Rating is ", ltr)
    elif lt >= 7.5 and lt < 9.0:
        ltr = 14
        print("Layer thickness Rating is ", ltr)
    elif lt >= 9 and lt < 10.5:
        ltr = 15
        print("Layer thickness Rating is ", ltr)
    elif lt >= 10.5 and lt < 12:
        ltr = 16
        print("Layer thickness Rating is ", ltr)
    elif lt >= 12 and lt < 13.6:
        ltr = 17
        print("Layer thickness Rating is ", ltr)
    elif lt >= 13.6 and lt < 15.3:
        ltr = 18
        print("Layer thickness Rating is ", ltr)
    elif lt >= 15.3 and lt < 17:
        ltr = 19
        print("Layer thickness Rating is ", ltr)
    elif lt >= 17 and lt < 19:
        ltr = 20
        print("Layer thickness Rating is ", ltr)
    elif lt >= 19 and lt < 22:
        ltr = 21
        print("Layer thickness Rating is ", ltr)
    elif lt >= 22 and lt < 25:
        ltr = 22
        print("Layer thickness Rating is ", ltr)
    elif lt >= 25 and lt < 30:
        ltr = 23
        print("Layer thickness Rating is ", ltr)
    elif lt >= 30 and lt < 35:
        ltr = 24
        print("Layer thickness Rating is ", ltr)
    elif lt >= 35 and lt < 40:
        ltr = 25
        print("Layer thickness Rating is ", ltr)
    elif lt >= 40 and lt < 45:
        ltr = 26
        print("Layer thickness Rating is ", ltr)
    elif lt >= 45 and lt < 50:
        ltr = 27
        print("Layer thickness Rating is ", ltr)
    elif lt >= 50 and lt < 60:
        ltr = 28
        print("Layer thickness Rating is ", ltr)
    elif lt >= 60 and lt < 75:
        ltr = 29
        print("Layer thickness Rating is ", ltr)
    elif lt >= 75 and lt < 100:
        ltr = 30
        print("Layer thickness Rating is ", ltr)
    else:
        print("you Entered the value greater than 100 \nRating automatically fix to 30")
    print("--------*******--------********-------------**********------------*******---------")
    sti = float(input("Enter your STRUCTRAL Indices[0-16]:  "))
    if sti > 16:
        str = 0
        print("Your Structural RAting is ", str)
    elif sti == 16:
        str = 1
        print("Your Structural RAting is ", str)
    elif sti == 15:
        str = 3
        print("Your Structural RAting is ", str)
    elif sti == 14:
        str = 5
        print("Your Structural RAting is ", str)
    elif sti == 13:
        str = 7
        print("Your Structural RAting is ", str)
    elif sti == 12:
        str = 8
        print("Your Structural RAting is ", str)
    elif sti == 11:
        str = 9
        print("Your Structural RAting is ", str)
    elif sti == 10:
        str = 11
        print("Your Structural RAting is ", str)
    elif sti == 9:
        str = 12
        print("Your Structural RAting is ", str)
    elif sti == 8:
        str = 13
        print("Your Structural RAting is ", str)
    elif sti == 7:
        str = 14
        print("Your Structural RAting is ", str)
    elif sti == 6:
        str = 16
        print("Your Structural RAting is ", str)
    elif sti == 5:
        str = 17
        print("Your Structural RAting is ", str)
    elif sti == 4:
        str = 19
        print("Your Structural RAting is ", str)
    elif sti == 3:
        str = 21
        print("Your Structural RAting is ", str)
    elif sti == 2:
        str = 23
        print("Your Structural RAting is ", str)
    elif sti == 1:
        str = 24
        print("Your Structural RAting is ", str)
    elif sti == 0:
        str = 25
        print("Your Structural RAting is ", str)
    else:
        print("please enter the correcrt data\nYour styctural rating is set to 0")
    print("--------*******--------********-------------**********------------*******---------")
    sld = float(input("Enter your SLAKE DURABILITY(I) index % [0-100]:  "))
    if sld >= 0 and sld < 30:
        sdr = 0
        print("Your Slake Durability rating for {} % is {} ".format(sld, sdr))
    elif sld >= 30 and sld < 40:
        sdr = 1
        print("Your Slake Durability rating for {} % is {} ".format(sld, sdr))
    elif sld >= 40 and sld < 50:
        sdr = 2
        print("Your Slake Durability rating for {} % is {} ".format(sld, sdr))
    elif sld >= 50 and sld < 60:
        sdr = 3
        print("Your Slake Durability rating for {} % is {} ".format(sld, sdr))
    elif sld >= 60 and sld < 65:
        sdr = 4
        print("Your Slake Durability rating for {} % is {} ".format(sld, sdr))
    elif sld >= 65 and sld < 70:
        sdr = 5
        print("Your Slake Durability rating for {} % is {} ".format(sld, sdr))
    elif sld >= 70 and sld < 75:
        sdr = 6
        print("Your Slake Durability rating for {} % is {} ".format(sld, sdr))
    elif sld >= 75 and sld < 80:
        sdr = 7
        print("Your Slake Durability rating for {} % is {} ".format(sld, sdr))
    elif sld >= 80 and sld < 85:
        sdr = 8
        print("Your Slake Durability rating for {} % is {} ".format(sld, sdr))
    elif sld >= 85 and sld < 87.4:
        sdr = 9
        print("Your Slake Durability rating for {} % is {} ".format(sld, sdr))
    elif sld >= 87.4 and sld < 89:
        sdr = 10
        print("Your Slake Durability rating for {} % is {} ".format(sld, sdr))
    elif sld >= 89 and sld < 92.2:
        sdr = 11
        print("Your Slake Durability rating for {} % is {} ".format(sld, sdr))
    elif sld >= 92.2 and sld < 94.6:
        sdr = 12
        print("Your Slake Durability rating for {} % is {} ".format(sld, sdr))
    elif sld >= 94.6 and sld < 97:
        sdr = 13
        print("Your Slake Durability rating for {} % is {} ".format(sld, sdr))
    elif sld >= 97 and sld < 97.5:
        sdr = 14
        print("Your Slake Durability rating for {} % is {} ".format(sld, sdr))
    elif sld >= 97.5 and sld < 98:
        sdr = 15
        print("Your Slake Durability rating for {} % is {} ".format(sld, sdr))
    elif sld >= 98 and sld < 98.5:
        sdr = 16
        print("Your Slake Durability rating for {} % is {} ".format(sld, sdr))
    elif sld >= 98.5 and sld < 99:
        sdr = 17
        print("Your Slake Durability rating for {} % is {} ".format(sld, sdr))
    elif sld >= 99.3 and sld < 99.3:
        sdr = 18
        print("Your Slake Durability rating for {} % is {} ".format(sld, sdr))
    elif sld >= 99.3 and sld < 99.6:
        sdr = 19
        print("Your Slake Durability rating for {} % is {} ".format(sld, sdr))
    else:
        sdr = 20
        print("Your Slake Durability rating for {} % is {} ".format(sld, sdr))
    print("--------*******--------********-------------**********------------*******---------")
    rst = float(input("enter your ROCK STRENGTH (kg/cm²):  "))
    if rst < 30:
        rsr = 0
        print("Rock Strength RAting at {} kg/cm² is {}".format(rst, rsr))
    elif rst >= 30 and rst < 65:
        rsr = 1
        print("Rock Strength RAting at {} kg/cm² is {}".format(rst, rsr))
    elif rst >= 65 and rst < 100:
        rsr = 2
        print("Rock Strength RAting at {} kg/cm² is {}".format(rst, rsr))
    elif rst >= 100 and rst < 150:
        rsr = 3
        print("Rock Strength RAting at {} kg/cm² is {}".format(rst, rsr))
    elif rst >= 150 and rst < 200:
        rsr = 4
        print("Rock Strength RAting at {} kg/cm² is {}".format(rst, rsr))
    elif rst >= 200 and rst < 250:
        rsr = 5
        print("Rock Strength RAting at {} kg/cm² is {}".format(rst, rsr))
    elif rst >= 250 and rst < 300:
        rsr = 6
        print("Rock Strength RAting at {} kg/cm² is {}".format(rst, rsr))
    elif rst >= 300 and rst < 375:
        rsr = 7
        print("Rock Strength RAting at {} kg/cm² is {}".format(rst, rsr))
    elif rst >= 375 and rst < 450:
        rsr = 8
        print("Rock Strength RAting at {} kg/cm² is {}".format(rst, rsr))
    elif rst >= 450 and rst < 525:
        rsr = 9
        print("Rock Strength RAting at {} kg/cm² is {}".format(rst, rsr))
    elif rst >= 525 and rst < 600:
        rsr = 10
        print("Rock Strength RAting at {} kg/cm² is {}".format(rst, rsr))
    elif rst >= 600 and rst < 700:
        rsr = 11
        print("Rock Strength RAting at {} kg/cm² is {}".format(rst, rsr))
    elif rst >= 700 and rst < 800:
        rsr = 12
        print("Rock Strength RAting at {} kg/cm² is {}".format(rst, rsr))
    elif rst >= 800 and rst < 900:
        rsr = 13
        print("Rock Strength RAting at {} kg/cm² is {}".format(rst, rsr))
    elif rst >= 900 and rst < 1500:
        rsr = 14
        print("Rock Strength RAting at {} kg/cm² is {}".format(rst, rsr))
    elif rst >= 1500:
        rsr = 15
        print("Rock Strength RAting at {} kg/cm² is {}".format(rst, rsr))
    print("--------*******--------********-------------**********------------*******---------")
    print("press 0 for dry ground surface")
    grs = float(input("enter your GROUND SEEPAGE (ml/min):  "))

    if grs > 5000:
        gsr = 0
        print("Ground Seepage Rating for {}ml/min is {}".format(grs, gsr))
    elif grs > 2000 and grs <= 5000:
        gsr = 1
        print("Ground Seepage Rating for {}ml/min is {}".format(grs, gsr))
    elif grs > 800 and grs <= 2000:
        gsr = 2
        print("Ground Seepage Rating for {}ml/min is {}".format(grs, gsr))
    elif grs > 300 and grs <= 800:
        gsr = 3
        print("Ground Seepage Rating for {}ml/min is {}".format(grs, gsr))
    elif grs > 200 and grs <= 300:
        gsr = 4
        print("Ground Seepage Rating for {}ml/min is {}".format(grs, gsr))
    elif grs > 140 and grs <= 200:
        gsr = 5
        print("Ground Seepage Rating for {}ml/min is {}".format(grs, gsr))
    elif grs > 80 and grs <= 140:
        gsr = 6
        print("Ground Seepage Rating for {}ml/min is {}".format(grs, gsr))
    elif grs > 20 and grs <= 80:
        gsr = 7
        print("Ground Seepage Rating for {}ml/min is {}".format(grs, gsr))
    elif grs > 10 and grs <= 20:
        gsr = 8
        print("Ground Seepage Rating for {}ml/min is {}".format(grs, gsr))
    elif grs > 0 and grs <= 10:
        gsr = 9
        print("Ground Seepage Rating for {}ml/min is {}".format(grs, gsr))
    else:
        gsr = 10
        print("wohooo dry ground seepage\ngreat")
        print("Ground Seepage Rating for {}ml/min is {}".format(grs, gsr))
    rmr.append(ltr + str + sdr + rsr + gsr)
    # print("RMRi is", rmrr)
    i += 1
    # print("--------*******--------********-------------**********------------*******---------")

# rmr =
print("RMR of Coal is",rmr[0])
print("Rmr of Shale/Sandstone is",rmr[1])
print("--------*******--------********-------------**********------------*******---------")
print("we have to find the combined rmr ")
t1= float(input("Enter the overlying strata of Coal or Metal mine(m): "))
t2 = float(input("Enter the intermediate roof strata of shale/sandstone/else: "))
t3 =float(input("Enter the gallery Span Width (m): "))
crmr = ((rmr[0]*t1)+(rmr[1]*(t3-t1)))/t3
print("Combined RMr is ",crmr)


print("--------*******--------********-------------**********------------*******---------")
print("Now we have to Calculate Adjusted RMR")
depth = float(input("Enter the depth(in m)"))
if depth <250:
    armr = crmr*1
elif depth >= 250 and depth <400:
    armr = crmr*0.9
elif depth >= 400 and depth <600:
    armr = crmr*0.8
else :
    armr = crmr*0.7
print("ARMR AFTER DEPTH calculation is ",armr)
print("--------*******--------********-------------**********------------*******---------")

print("CONDITIONS FOR LATERAL STRESS!!!!")
print("press 1 for SMALL STRESS\npress 2 for MEDIUM STRESS\npress 3 for HIGH STRESS ")
lateral_stress = float(input("PRESS 1 OR 2 OR 3 according to your data"))
if  lateral_stress == 1:
    armr = armr*0.9
elif lateral_stress ==2:
    armr =armr*0.8
elif lateral_stress ==3:
    armr = armr*0.7
else :
    print("please enter 1 or 2 or 3")
print("ARMR after including lateral stress is",armr)
print("--------*******--------********-------------**********------------*******---------")
print("CONDITION FOR INDUCED STRESS!!!")
print("press 1 for NO ADJACENT WORKING IN THE SEAM\npress 2 for EXTRACTION AREA WITHIN 20-40 m IN THE SAME SEAM\n"
      "press 3 for EXTRACTION AREA WITHIN 10-20m in the same seam\npress 4 for working with 10-20m parting\n"
      "press 5 for working within 3 - 10m parting\npress 6 if you dont have this data")
induced_stress = float(input("PRESS THE INDUCED STRESS CONDITION CAREFULLY"))
if induced_stress==1:
    armr = armr*1
elif induced_stress ==2:
    armr = armr*0.9
elif induced_stress==3:
    armr = armr*0.75
elif induced_stress==4:
    armr=armr*0.9
elif induced_stress==5:
    armr = armr*0.75
else:
    print("either you dont know")
    print("please press the respective key ")
print("ARMR after including INDUCED STRESS is",armr)
print("--------*******--------********-------------**********------------*******---------")
print("CONDITIONS FOR METHOD OF WORKING")
print("press 1 for MECHANISED WORKING OR CONTINUOUS MINER\npress 2 for UNDERCUT AND BLASTING\n"
      "press 3 for BLASTING OFF THESOILD\n press another key if u dont have data  ")
method_excavation = float(input("PRESS THE RESPECTIVE KEY CAREFULLY"))
if method_excavation==1:
    armr=armr*1.1
elif method_excavation==2:
    armr = armr*1
elif method_excavation==3:
    armr = armr*0.9
else:
    print("PROGRAM GOT TO KNOW THAT YOU DONT HAVE THIS DATA")
print("ARMR after including METHOD OF EXCAVATION is",armr)

print("--------*******--------********-------------**********------------*******---------")
gallery_span = float(input("Enter the GAllery span(in m)\nGAllery span is varies betwwen 0-6m"))
if gallery_span <4.8:
    armr = armr*1
elif gallery_span >=4.8 and gallery_span<=6:
    armr = armr*0.85
else:
    print("ok value will calculated without gallery_span data")
print("ARMR after including gallery calculation is ",armr)
print("--------*******--------********-------------**********------------*******---------")

if armr> 90 and armr <= 100.0:
    print("your rmr is",armr)
    print("EXCELLENT ROCK")
elif armr >= 80 and armr <= 90:
    print("Your rmr is ",armr)
    print("VERY GOOD STRATA")
elif armr >60 and armr <80:
    print("Your rmr is ", armr)
    print("GOOD STRATA")
elif armr >40 and armr <= 60:
    print("Your rmr is ", armr)
    print("FAIR STRATA")
elif armr >20 and armr <= 40:
    print("Your rmr is ", armr)
    print("POOR STRATA")
elif armr >0 and armr <= 20 :
    print("Your rmr is less than 20")
    print("VERY POOR STRATA")
else :
    print("armr",armr)
    print("VALUE ABSURD")
    print("RMR CAN'T BE GREATER THAN 100")
    print("MEASURE RMR INDICICES AGAIN")
print("--------*******--------********-------------**********------------*******---------")
print("CALCULATING ROCK LOAD\npress 1 for COAL MINE\npress 2 for METAL MINE\npressing other than that key doesnt make sense")
rock_l = float(input("press the respective key for getting rock load"))
mean_density = float(input("enter the mean density(t/m^3)"))
if rock_l == 1:
    print("You selected coal mine")
    print("your gallery span is",gallery_span)
    r_load_height = gallery_span*(1.7-(0.037*armr)+(0.0002*(armr**2)))
    print("ROCK LOAD HEIGHT is",r_load_height)
    rock_load_c=mean_density*r_load_height
    print("ROck load based upon indian rmr")
    print("rock load in m", rock_load_c )
    print("good luck")
elif rock_l==2 :
    print("You selected the METAL MINE")
    print("unal formula applies")
    rock_load_m = ((100-armr)/armr)*gallery_span*mean_density
    print("Rock load in m ",rock_load_m)
    print("all the best")
else:
    print("wrong key selection")



