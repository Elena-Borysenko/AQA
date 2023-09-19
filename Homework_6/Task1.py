import csv

usd_to_uah_rate = 36.9343

with open('test_file.csv', 'r') as usd_salary_file, open('salaries_uah.csv', 'w', newline='') as uah_salary_file:
    usd_reader = csv.reader(usd_salary_file)
    uah_writer = csv.writer(uah_salary_file)

    header = next(usd_reader)
    header.append('Total_Salary_UAH')
    uah_writer.writerow(header)

    for row in usd_reader:
          employee_name = row[0]
          usd_salaries = list(map(float, row[1:]))
          uah_salaries = [usd_salary * usd_to_uah_rate for usd_salary in usd_salaries]
          total_uah_salary = sum(uah_salaries)
          uah_writer.writerow([employee_name] + uah_salaries + [total_uah_salary])









