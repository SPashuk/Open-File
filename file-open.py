path_dir = 'files/'
file_dir = '1.txt'
file_path = path_dir+file_dir
print(file_path)
import osfor root. dir,files in os.walk(path_dir
                                        )
with open(file_path, "r", encoding='utf-8') as file:
    a = True
    count = 0
    while a:
        file_line = file.readline()
        #print('Длина строки\n', len(file_line))
        count +=1
        if not file_line:
            pass #print("End Of File")
            a = False
# with open('out/all_file.txt', 'w', encoding='utf-8') as file_out:
#     file_o = 
print('\n количесткво строк в файле ', count)
dict_file = {'name_file': file_dir, 'count': count}
print(dict_file)