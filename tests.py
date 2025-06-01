from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.overwrite_file import overwrite_file



print(overwrite_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
print(overwrite_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
print(overwrite_file("calculator", "/tmp/temp.txt", "this should not be allowed"))



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