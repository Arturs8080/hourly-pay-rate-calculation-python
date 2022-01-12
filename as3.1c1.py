ahrs = input("Enter Hours:")
arat = input("Enter Rate:")
fhrs = float(ahrs)
frat = float(arat)
# print(fhrs, frat)
if fhrs > 40:
    # print('Overtime')
    mult = fhrs * frat
    min = (fhrs - 40) * (frat * 0.5)
    # print(mult, min)
    count = mult + min
elif:
    # print('Regular')
    count = fhrs * frat
print(count)
