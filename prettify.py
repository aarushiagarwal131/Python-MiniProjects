# The function will perform three tasks:
#
# First, it will check all the files present in the folder whose paths are given as an input argument. Then it will
# capitalize the first letter of each file. If the file's name is present in a dictionary file, then it will not
# capitalize the first letter. It will only capitalize the first letter of the files, which are not present in the
# dictionary file. The function renames the file names to numbers in the range of 1 to100 whose format is the same as
# mentioned in the input parameter like 1.jpg.
import os


def prettify(path, file, format):
    os.chdir(path)
    list1 = os.listdir(path)
    count = 1
    # with open(file) as f:
    f = open(file, "r")
    content = f.read().split("\n")
    f.close()
    for file2 in list1:

        if os.path.splitext(file2) == format:
            os.rename(file2, str(count))
            count = count + 1
        elif file2 in content:
            continue
        else:
            os.rename(file2, file2.capitalize())


# path = input("Enter the path of directory :: ")
# file_name = input("Enter the dictionary file name with extension :: ")
# file_format = input("Enter the file format :: ")
prettify(r"C:\Users\HP\PycharmProjects\pythonProject",
         r"C:\Users\HP\PycharmProjects\pythonProject\content", ".png")

