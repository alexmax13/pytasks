# Write a script that creates a new output file called myfile.txt
# writes the string "Hello file world!" in it.
# Then write another script that opens myfile.txt, and reads and prints its contents.
# Run your two scripts from the system command line

with open('myfile.txt', 'w') as hello:
    hello.write('Hello file world!\n')

with open('myfile.txt') as hello:
    f = hello.read()
print(f)
