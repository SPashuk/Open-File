from pprint import pprint
import os

path_dir = "D:/CODE/FILE-OPEN/files/"
file_in_dir = os.listdir(path_dir)

file_list = []

for file_i in file_in_dir:
    file_full_path = path_dir + file_i
    #print(file_full_path)
    with open(file_full_path, 'rt', encoding = 'utf-8') as file:
        file_list.append(file.readlines())
#pprint(file_list)#собираем список из файлов
#print('\n************************************\n')
i = 0
# формируем структуру имя файла, кол-во строк, строки из файла
for list in file_list:
    list.insert(0, len(list))
    list.insert(0, file_in_dir[i])
    #print(len(list))
    #print(file_in_dir[i], '\n***************************')
    i += 1
#pprint(list)
#сортируем
sorted_file = file_list.sort(key=lambda x:len(x))
#pprint(file_list)#,'\n************выводим в файл ************************\n'
with open ('/CODE/FILE-OPEN/out/all_file.txt', 'w', encoding = 'utf-8') as file_all:
        file_all.write(file_list[0][0] + '\n' + str(file_list[0][1]) + '\n' + ''.join(file_list[0][2:]) + '\n')
        file_all.write(file_list[1][0] + '\n' + str(file_list[1][1]) + '\n' + ''.join(file_list[1][2:]) + '\n')
        file_all.write(file_list[2][0] + '\n' + str(file_list[2][1]) + '\n' + ''.join(file_list[2][2:]) + '\n')
with open('/CODE/FILE-OPEN/out/all_file.txt', "rt", encoding='utf-8') as file:
    fine = file.read()
    print(fine)
