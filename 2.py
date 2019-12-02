prices = {"banana":[4,3], "apple":[2,8],"orange":[1.5,2],"pear":[3,7]}
total = 0
for i,j in prices.items():
    print(i)
    print("price: "+str(j[0]))
    print("stock: "+str(j[1]))

for k in prices.values():
    total = total + k[0]*k[1]

print(total)