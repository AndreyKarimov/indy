def file_read(file_name):
    file = open(file_name, encoding='utf-8').read()
    print(file)
    file_name.close()


file_read('test.txt')


# def file_read(file_name):
#     with open(file_name, "r", encoding = "utf-8") as f:
#         print(f.read())