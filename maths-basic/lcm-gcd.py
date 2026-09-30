a = 5
b = 10

gcd = a
temp = b

while temp != 0:
    gcd,temp = temp, gcd % temp
    
print(gcd)

lcm = (a*b)//gcd

print(lcm)

print([lcm,gcd])