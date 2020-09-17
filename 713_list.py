squad_713 = [
    'Alice',
    'Alpha',
    'Anthony',
    'Barent',
    'Branden',
    'Channee',
    'Cristina',
    'Cabassa',
    'Elaine',
    'Han',
    'Irene',
    'Joshua',
    'Levin',
    'Lizz',
    'Margaret',
    'Nicholas',
    'Philip',
    'Rohun',
    'Sameh',
    'Shane',
    'Steven',
    'Subrata',
    'Tanner',
    'Yoel',
    'Adam',
    'Pete',
    'Rome',
    'Taylor'
]



ga_file = open('generall_assembly.txt', 'w')
ga_file.writelines(squad_713)
ga_file.close()

#using readlines()
ga_file = open('generall_assembly.txt', 'r')
Lines = ga_file.readlines()

count = 0
#strips the newline chracter
for line in Lines:
    print("Line{}: {}\n".format(count, line.strip()))

ga_file = open('general_assembly.txt', 'w')

for i in range(len(squad_713)):
    person = squad_713[i]

    ga_file.write('{}\n'.format(person))

ga_file.close()

read_ga_file = open('general_assembly.txt')
list_of_people = read_ga_file.readline()
print(list_of_people)