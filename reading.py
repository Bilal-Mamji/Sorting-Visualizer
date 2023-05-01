my_file = open(r"C:\Users\Dell\Desktop\File1.txt")
# file2=open(r"C:\Users\Dell\Desktop\Input_File-2.txt")

data = my_file.read()
# data2=file2.read()

data_into_list = data.replace('\n', ' ').split(",")
# data_into_list_2 = data2.replace('\n', ' ').split(",")


File1 = [eval(i) for i in data_into_list]
print(File1)
# File2 = [float(i) for i in data_into_list_2]
# print(File2)

my_file.close()
# file2.close()