name = input('Enter name?. ')
name = name.title()
print('Hello, ' + name + '. Enter year of study below.')
while True:
    year_of_study = input('Enter year of study.')
    if year_of_study.isdigit():
        year_of_study = int(year_of_study)
        if year_of_study in [2, 3]:
            break
        else:
            print('Application is only for Year 2 and 3')
    else:
        print('Enter a valid number.')

if year_of_study == 2:
    print('Enter your admission number.')
    while True:
        number = input('Admission number. ')
        if number.isdigit():
            number = int(number)
            break
        else:
            print('Admission should be numeric. ')

    department = input('Enter department name. ')
    faculty = input('Faculty name. ')
    while True:
        unit_code = input('Unit code.')
        if unit_code.isdigit() and len(unit_code) == 4:
            unit_code = int(unit_code)
            break
        else:
            print('Enter Four digit code!!!!')



elif year_of_study == 4:
    print('Upload your fee statement.')
else:
    print('Check with the COD.')
print("Thank you, for providing your information")