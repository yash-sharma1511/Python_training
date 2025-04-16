import csv
with open('sales.csv', 'r') as infile:
    reader = csv.reader(infile)
    header = next(reader)  
    high_sales = []
    for row in reader:
        amount = float(row[1])
        if amount > 10000:
            high_sales.append(row)
print("Sales above ₹10,000:")
for sale in high_sales:
    print(sale)
with open('high_sales.csv', 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(header)        
    writer.writerows(high_sales)   
print("High sales saved to 'high_sales.csv'.")
