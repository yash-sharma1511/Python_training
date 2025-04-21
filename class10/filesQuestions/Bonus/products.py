import csv

def sort_products_by_price():
    with open('products.csv', 'r') as infile:
        reader = csv.reader(infile)
        header = next(reader)  
        rows = list(reader)
        rows.sort(key=lambda x: float(x[2]))

    with open('products_sorted.csv', 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(header)
        writer.writerows(rows)

    print("Sorted data written to products_sorted.csv")