import csv
import sys, getopt

#2
def main(argv):
    target_file = ''
    path = ''
    try:
      opts, args = getopt.getopt(argv,"hi:o:",["tfile=","path="])
    except getopt.GetoptError:
      print('fail')
      sys.exit(2)


#1A
def filereader():
    with open('csv.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                line_count += 1
        print(f'Processed {line_count} lines.')
filereader()
#def filewriter():
#    with open('employee_file.csv', mode='w') as employee_file:
#        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

#        employee_writer.writerow(['John Smith', 'Accounting', 'November'])
#        employee_writer.writerow(['Erica Meyers', 'IT', 'March'])
#filewriter()
#1B
'''def filewriter(*names):
    with open('employee_file.csv', mode='w') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for name in names:
            employee_writer.writerow([name])
filewriter("Jens")'''
#1C
def readcsv():
    with open('csv.txt') as csv_file:
        rowlist = []
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            rowlist.append(row)
        return rowlist
listofthings = readcsv()
print(listofthings)      

