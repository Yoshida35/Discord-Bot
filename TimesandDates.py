import datetime

#https://www.w3schools.com/python/python_datetime.asp

#datenow = datetime.datetime.now()

#print("This year is:")
#print(datenow.strftime(%Y))

#print("This month is:")
#print(datenow.strftime(%B))

#print("Today is:")
#print(datenow.strftime(%A))


#print(datenow.strftime(%d), "/", datenow.strftime(%m), "/", datenow.strftime(%Y))
#print("The time is", datenow.strftime(%X), "according to", datenow.strftime(%Z), "Timezone.")




#https://docs.python.org/3/library/datetime.html

datenow = datetime.datetime.now()

print("This year is:")
print(datenow.year)

print("This month is:")
print(datenow.month)

print("Today is:")
print(datenow.day)

print("")

print(datenow.day, "/", datenow.month, "/", datenow.year)
print("The time is", datenow.hour, ":", datenow.minute)#, "according to", datenow.tzinfo, "Timezone.")

#tzinfo I couldn't get to work automatically.
