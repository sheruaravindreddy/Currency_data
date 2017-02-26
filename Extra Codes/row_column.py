import csv
with open('output.csv', 'w', newline='') as csvfile:
    output = ['USA','IND']
    d = csv.writer(csvfile, delimiter=',', quotechar='|', 
    quoting=csv.QUOTE_MINIMAL)  
    d.writerow(output)
    d.writerow(output)
