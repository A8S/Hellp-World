hrs = input("Enter Hours:")
h = float(hrs)
r=input("rate:")
basic_rate = float(r)

if h <=40:
   pay = h * basic_rate
elif h > 40:
   pay = 40* basic_rate + (h-40)*1.5*basic_rate
else:
   print ('wrong parameter')


print (pay)
