text = {}
count = 0
#*****************************
path_dir = 'files/'
file_dir = '1.txt'

def op_file_count (path_dir, file_dir):
    file_path = path_dir+file_dir
    print(file_path)
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
    print('\n количесткво строк в файле ', count)
    dict_file = {'name_file': file_dir, 'count': count}
    return dict_file
#*****************************
# with open('files/2.txt', "r", encoding='utf-8') as file:
#     #while True
#     text = file.read()
#     count = len(text)
# print(count, text)

