from pprint import pprint
import os

#*****************************
path_dir = "D:/CODE/FILE-OPEN/files/"
file_in_dir = os.listdir(path_dir)

# def op_file_count (path_dir, file_in_dir):# вариант 1 функция подсчет
#     file_path = path_dir+file_in_dir
#     print(file_path)
#     with open(file_path, "r", encoding='utf-8') as file:
#         a = True
#         count = 0
#         while a:
#             file_line = file.readline()
#             #print('Длина строки\n', len(file_line))
#             count +=1
#             if not file_line:
#                 pass #print("End Of File")
#                 a = False
#     print('\n количесткво строк в файле ', count)
#     dict_file = {'name_file': file_in_dir, 'count': count}
#     return dict_file
#print(file_in_dir)
file_list = []

for file_i in file_in_dir:
    file_full_path = path_dir + file_i
    #print(file_full_path)
    with open(file_full_path, encoding = 'utf-8') as file:
        file_list.append(file.readlines())
#pprint(file_list)#
#print('\n************************************\n')
i = 0
for list in file_list:
    list.insert(0, len(list))
    list.insert(0, file_in_dir[i])
    #print(len(list))
    #print(file_in_dir[i], '\n***************************')
    i += 1
#pprint(list)
#print(len(list))
sorted_file = file_list.sort(key=lambda x:len(x))
#pprint(file_list)#,'\n************************************\n'
with open ('/CODE/FILE-OPEN/out/all_file.txt', 'w', encoding = 'utf-8') as file_all:
        file_all.write(file_list[0][0] + '\n' + str(file_list[0][1]) + '\n' + ''.join(file_list[0][2:]) + '\n')
        file_all.write(file_list[1][0] + '\n' + str(file_list[1][1]) + '\n' + ''.join(file_list[1][2:]) + '\n')
        file_all.write(file_list[2][0] + '\n' + str(file_list[2][1]) + '\n' + ''.join(file_list[2][2:]) + '\n')
with open('/CODE/FILE-OPEN/out/all_file.txt', "rt", encoding='utf-8') as file:
    fine = file.read()
    print(fine)