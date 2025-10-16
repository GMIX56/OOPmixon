import StudentClass as sc

studentid = 1001
name = 'John'
dob = '10/9/2001'
classification = 'junior'

student1 = sc.Student(studentid,name,dob,classification)

student1.calc_age()
student1.registration() 

print(f'age: {student1.return_age()}')
print(f'registraiton: {student1.return_registration()}')

