# @TODO: Import libraries
import csv
import sys
from pathlib import Path

# @TODO: Set file paths for menu_data.csv and sales_data.csv
menu_filepath = Path("menu_data.csv")
sales_filepath = Path("sales_data.csv")

# @TODO: Initialize list objects to hold our menu and sales data
menu = []
sales = []

# @TODO: Read in the menu data into the menu list
with open(menu_filepath, newline='') as l:
    menu_iter = iter(csv.reader(l))
    next(menu_iter)
    for r in menu_iter:
        menu.append(r)
        

# @TODO: Read in the sales data into the sales list

with open(sales_filepath, newline='') as l:
    sales_iter = iter(csv.reader(l))
    next(sales_iter)
    for r in sales_iter:
        sales.append(r)
            

# @TODO: Initialize dict object to hold our key-value pairs of items and metrics
report = {}

# Initialize a row counter variable


# @TODO: Loop over every row in the sales list object

for i in menu:
    quantity = 0
    for j in sales:
        if j[4]==i[0]:
            quantity = quantity + int(j[3])
            if i[0] not in report: 
                
                report.update({i[0] : {"01-count": quantity, "02-revenue": quantity * float(i[3]), "03-cogs": float(i[4]) * quantity, 
                      "04-profit": (float(i[3])-float(i[4])) * quantity}})
            else:
                report[i[0]]["01-count"] = quantity
                report[i[0]]["02-revenue"] = quantity * float(i[3])
                report[i[0]]["03-cogs"] = float(i[4]) * quantity
                report[i[0]]["04-profit"] = (float(i[3])-float(i[4])) * quantity       
                      
        else: 
            print(f"{j[4]} does not equal {i[0]}! NO MATCH!")
    
    
        
sys.stdout = open("readme.txt", "w")

print(report)

sys.stdout.close()
            
   



    # Line_Item_ID,Date,Credit_Card_Number,Quantity,Menu_Item
    # @TODO: Initialize sales data variables


    # @TODO:
    # If the item value not in the report, add it as a new entry with initialized metrics
    # Naming convention allows the keys to be ordered in logical fashion, count, revenue, cost, profit








    # @TODO: For every row in our sales data, loop over the menu records to determine a match


        # Item,Category,Description,Price,Cost
        # @TODO: Initialize menu data variables




        # @TODO: Calculate profit of each item in the menu data


        # @TODO: If the item value in our sales data is equal to the any of the items in the menu, then begin tracking metrics for that item


            # @TODO: Print out matching menu data






            # @TODO: Cumulatively add up the metrics for each item key





        # @TODO: Else, the sales item does not equal any fo the item in the menu data, therefore no match



    # @TODO: Increment the row counter by 1


# @TODO: Print total number of records in sales data




# @TODO: Write out report to a text file (won't appear on the command line output)
