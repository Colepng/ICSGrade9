hours = float(input("Input amount of hours in between 0-24 "))
minu = float(input("Input amount of minutes in between 0-59 "))
sec = float(input("Input amount of seconds in between 0-59 "))
minu_sec = minu + (sec/60)
hours_minu = hours + (minu_sec/60)
print(hours,"hours,", minu,"minutes", sec,"seconds", "is", round(hours_minu,2))


