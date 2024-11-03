

sandwich_orders=['Beef','Pork','Vegetable']
finished_sandwiches=[]

#注意[]虽然也为False，但是不等同于None
while sandwich_orders:
    
    finished_sandwiches.append(sandwich_orders.pop())
    print(f'I made your {finished_sandwiches[len(finished_sandwiches)-1]} sandwich')

print(sandwich_orders)
print(finished_sandwiches)
    