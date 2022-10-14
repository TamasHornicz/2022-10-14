veg=int(input("Meddig szeretnéd összeszorozni a számokat: "))

fakt=1
for i in range(1, veg+1,1):
    fakt = fakt*i
    print("Számok fakt.-ja: ",fakt)