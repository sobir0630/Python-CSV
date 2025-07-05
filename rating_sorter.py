
import csv

with open('students.csv') as f:
    reader = csv.DictReader(f)
    students = list(reader)

sorted_students = sorted(students, key=lambda x: int(x['Score']), reverse=True)

with open('rating.csv', 'w', newline='') as f2:
    fieldnames = ['Name', 'Score']
    writer = csv.DictWriter(f2, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(sorted_students)
