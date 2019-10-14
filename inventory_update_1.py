#this code helps update an inventory list with two parameters
#more parameter values can be added as per user requirement
#it uses classes and methods to provide the correct output
#it uses pandas module to output the table with the updated inventory list
#Concepts covered: pandas module, While loop, class, method, 


import pandas as pd
items=[]		#create a list of items
quantity=[]		#create a list of item quantity

continue_adding_item='Y'

while(continue_adding_item=='Y'):
	print('Add the item name')
	item_name_1=input()

	print('Add item quantity')
	item_quantity_1=int(input())

	class add_items():

		def __init__(self, item_name, item_quantity):
			self.item_name=item_name
			self.item_quantity=item_quantity


	new_item=add_items(item_name_1,item_quantity_1)

	items.append(new_item.item_name)
	quantity.append(new_item.item_quantity)
	print('Do you want to add more item?	Y/N')
	continue_adding_item=input()

	print_inventory={'Item': items,'Quantity': quantity}
	final_inventory=pd.DataFrame(print_inventory)

	
	if continue_adding_item=='N':
		
		print(final_inventory)
		break
