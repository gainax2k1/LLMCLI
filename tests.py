from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.overwrite_file import overwrite_file
from functions.run_python import run_python_file

# fourth tests
print(run_python_file("calculator", "main.py"))
print(run_python_file("calculator", "tests.py"))
print(run_python_file("calculator", "../main.py")) # should return error
print(run_python_file("calculator", "empty.py")) # should return error


""" third tests
print(overwrite_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
print(overwrite_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
print(overwrite_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
"""


""" second tests
print(get_file_content("calculator", "main.py"))
print(get_file_content("calculator", "pkg/calculator.py"))
print(get_file_content("calculator", "/bin/cat"))
"""


# print(get_file_content("calculator", "lorem.txt"))


""" initial tests
print(get_files_info("calculator", "."))

print(get_files_info("calculator", "pkg"))

print(get_files_info("calculator", "/bin"))

print(get_files_info("calculator", "../"))
"""