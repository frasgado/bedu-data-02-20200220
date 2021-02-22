import csv

FILENAME = 'employees.csv'

with open(FILENAME) as csv_file:
    csv_reader = csv.reader(csv_file)
    print(csv_reader)
    for row in csv_reader:
        print(type(row))
        print(row[2])


with open(FILENAME) as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        # print(type(row))
        # print(row['Name'])
        # para obtener de manera segura es por el nombre de la llave
        salary = row.get('Salary')
        #salary = row.get('Salary', 10000.00)
        print(salary)
        if salary:
            salary_with_taxes = float(salary) * 1.35
            print(salary_with_taxes)
 
# considerar que el dataset viene con datos erroneos, es necesario validarlos


'''
import csv

FILENAME = 'employees.csv'

with open (FILENAME) as csv_file:
    csv_reader = csv.reader(csv_file)
    # print(csv_reader)
    for row in csv_reader:
        # print(type(row))
        # print(row)
        print(row[2])

'''