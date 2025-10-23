# python
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

# print("Running tests for get_files_info...")
# print("Test #1 (get_files_info)")
# get_files_info("calculator", ".")
# print("Test #2 (get_files_info)")
# get_files_info("calculator", "pkg")
# print("Test #3 (get_files_info)")
# get_files_info("calculator", "/bin")
# print("Test #4 (get_files_info)")
# get_files_info("calculator", "../")

print("\nRunning tests for get_file_content...")

content = get_file_content("calculator", "main.py")
print(content)

content = get_file_content("calculator", "pkg/calculator.py")
print(content)

content = get_file_content("calculator", "/bin/cat")
print(content)

content = get_file_content("calculator", "pkg/does_not_exist.py")
print(content)