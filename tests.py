# python
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

# print("Running tests for get_files_info...")
# print("Test #1 (get_files_info)")
# get_files_info("calculator", ".")
# print("Test #2 (get_files_info)")
# get_files_info("calculator", "pkg")
# print("Test #3 (get_files_info)")
# get_files_info("calculator", "/bin")
# print("Test #4 (get_files_info)")
# get_files_info("calculator", "../")

# print("\nRunning tests for get_file_content...")
# content = get_file_content("calculator", "main.py")
# print(content)

# content = get_file_content("calculator", "pkg/calculator.py")
# print(content)

# content = get_file_content("calculator", "/bin/cat")
# print(content)

# content = get_file_content("calculator", "pkg/does_not_exist.py")
# print(content)

# print("---------------------------------")
# print("\nRunning tests for write_file...")
# print("---------------------------------")
# status = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
# print(status)

# status = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
# print(status)

# status = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
# print(status)

print("---------------------------------")
print("\nRunning tests for run_python_file...")
print("---------------------------------")
# Test 1 should return should print the calculator's usage instructions
# Test 2 should run the calculator... which gives a kinda nasty rendered result)
# Tests 3,4,5 should return an error
test_cases_rpf = [ ('calculator', 'main.py', ''), 
                   ('calculator', 'main.py', ["3 + 5"]),
                   ('calculator', 'tests.py', ''),
                   ('calculator', '../main.py', ''),
                   ('calculator', 'nonexistent.py', ''),
                   ('calculator', 'lorem.txt', '') ] 

for test in test_cases_rpf:
    status = run_python_file(*test)
    print(status)
    print('-------------')

# working_directory = ['calculator','calculator','calculator','calculator','calculator','calculator']
# file_path = ['main.py','main.py','tests.py','../main.py','nonexistent.py','lorem.txt']
# myargs = [[], ["3 + 5"], '', '', '', '']
# for i in range(0,len(working_directory)):
#     status = run_python_file(working_directory[i], file_path[i], myargs[i]) # should print the calculator's usage instructions
#     print(status)

# status = run_python_file("calculator", "main.py", ["3 + 5"]) 
# status = run_python_file("calculator", "tests.py")
# status = run_python_file("calculator", "../main.py") 
# status = run_python_file("calculator", "nonexistent.py") # this should return an error
# status = run_python_file("calculator", "lorem.txt") # this should return an error