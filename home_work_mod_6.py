import shutil
import os #для получения информации о файлах

path = r'C:/user/Desktop/Хлам'  # папка сортировки

# Ключи - названия папок. Значения - расширения файлов для каждой отдельной папки.
extensions = {
    'video': ['mp4', 'mov', 'avi', 'mkv', 'wmv', '3gp', '3g2', 'mpg', 'mpeg', 'm4v',
              'h264', 'flv', 'rm', 'swf', 'vob'],
    'data': ['sql', 'sqlite', 'sqlite3', 'csv', 'dat', 'db', 'log', 'mdb', 'sav',
             'tar', 'xml'],
    'audio': ['mp3', 'wav', 'ogg', 'flac', 'aif', 'mid', 'midi', 'mpa', 'wma', 'wpl',
              'cda'],
    'images': ['jpg', 'png', 'bmp', 'ai', 'psd', 'ico', 'jpeg', 'ps', 'svg', 'tif',
              'tiff'],
    'archives': ['zip', 'rar', '7z', 'z', 'gz', 'rpm', 'arj', 'pkg', 'deb'],
    'documents': ['pdf', 'txt', 'doc', 'docx', 'rtf', 'tex', 'wpd', 'odt'],
    '3d': ['stl', 'obj', 'fbx', 'dae', '3ds', 'iges', 'step'],
    'presentation': ['pptx', 'ppt', 'pps', 'key', 'odp'],
    'spreadsheet': ['xlsx', 'xls', 'xlsm', 'ods'],
    'font': ['otf', 'ttf', 'fon', 'fnt'],
    'gif': ['gif'],
    'exe': ['exe'],
    'bat': ['bat'],
    'apk': ['apk']
}

# Напишем функцию для создания папок из списка названий
def create_folders_from_list(path, extensions):
    for folder in extensions:
        if not os.path.exists(f'{path}\\{folder}'):
            os.mkdir(f'{path}\\{folder}')

# для получения путей подпапок
def get_subfolder_paths(path) -> list:
    subfolder_paths = [f.path for f in os.scandir(path) if f.is_dir()]
    return subfolder_paths

# пути всех файлов в папке
def get_file_paths(path) -> list:
    file_paths = [f.path for f in os.scandir(path) if not f.is_dir()]
    return file_paths

# сортировка файлов
def sort_files(path):
    file_paths = get_file_paths(path)  # пути файлов
    ext_list = list(extensions.items())  # cоздаем переменную со списком метода словаря
    # цикл для каждого пути файла в списке
    for file_path in file_paths:
        extension = file_path.split('.')[-1]
        file_name = file_path.split('\\')[-1]
        shutil.unpack_archive(file_path, 'new_folder_for_data')
        # цикл внутри
        for dict_key_int in range(len(ext_list)):
            if extension in ext_list[dict_key_int][1].lower:
                print(f'Moving {file_name} in {ext_list[dict_key_int][0].lower} folder\n')
                os.rename(file_path, f'{path}\\{ext_list[dict_key_int][0].lower}\\{file_name}')
            else:
                file = path + "/" + items
                n_path = "/unknown/" + items
                shutil.move(file, n_path)

# удаляем пустые папки
def remove_empty_folders(path):
    subfolder_paths = get_subfolder_paths(path)
    for p in subfolder_paths:
        if not os.listdir(p):
            print('Deleting empty folder:', p.split('\\')[-1], '\n')
            os.rmdir(p)


