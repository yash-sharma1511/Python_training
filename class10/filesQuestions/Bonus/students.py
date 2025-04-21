import csv
import json
def convert_txt_to_json():
    with open('students.txt', 'r') as infile:
        reader = csv.DictReader(infile)
        students = [row for row in reader]
    with open('students.json', 'w') as outfile:
        json.dump(students, outfile,indent=4)
    print("Data has been successfully written to students.json")
convert_txt_to_json()
