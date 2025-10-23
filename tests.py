# python
from functions.get_files_info import get_files_info

print("Running test #1")
get_files_info("calculator", ".")
print("Running test #2")
get_files_info("calculator", "pkg")
print("Running test #3")
get_files_info("calculator", "/bin")
print("Running test #4")
get_files_info("calculator", "../")

