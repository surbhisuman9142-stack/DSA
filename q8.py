def hms(total):
    h = total//3600
    m = (total%3600)//60
    s = total%60
    return(h,m,s)
total = 3665
print(hms(total))