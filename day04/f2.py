file1 = open("file2.txt",'w')

content = '''
This is a Python Programming class
Trainer: Bhimashakar 
DOT: 22-12-2024
'''

str1 = input("Enter the string")
# file1.write('''
# This is a Python Programming class
# Trainer: Bhimashakar T
# DOT: 22-12-2024
# ''')
file1.write(str1)
file1.close()
