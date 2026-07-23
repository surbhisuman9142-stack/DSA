def celsius_fahrenheit_pairs(start,stop,step):
    return[(c,c*9/5+32)for c in range(start,stop+1,step)]
print(celsius_fahrenheit_pairs(0,100,20))