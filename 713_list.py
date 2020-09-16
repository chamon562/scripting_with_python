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
    print("Line{}: {}".format(count, line.strip()))
