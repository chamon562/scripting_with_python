# open the file
# channee_file = open('channee.txt')
# read and write to it needs open(channee.txt, r+)
# a means append r = read r+ means read and write w means write
channee_file = open('channee.txt', 'a')

numbers = [1,2,3]
for i in range(len(numbers)):
    num = numbers[i]
    channee_file.write("{}\n".format(num))

#write to the file
# open a file then append to it sup tho and close
# channee_file.write('\nSup tho\n')
# close a file
channee_file.close()

# read a file  
# print(channee_file.read())


#if file is not found.k one will be create for you
bob_file = open('bob.txt', 'w')
bob_file.write('Bob')
bob_file.close()

# look up how to read lines from a file in python 

L = ["player\n", "cats\n", "bear\n"]
# writing the file
file1 = open('myfile.txt', 'w')
file1.writelines(L)
file1.close()

#using readlines()
file1 = open('myfile.txt', 'r')
Lines = file1.readlines()

count = 0
#strips the newline chracter
for line in Lines:
    print("Line{}: {}".format(count, line.strip()))


new_file = open('new_file.txt')
file_items = new_file.readline()

for i in range(len(file_items)):
    each_item = file_items[i]
    print('Before: {}'.format(each_item))
    print(each_item[0:-1])
    file_items[i] = each_item[0:-1]
    print(file_items)
# print(file_items)

new_file.close()

