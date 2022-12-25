import shutil #для высокоуровневого взаимодействия с объектами системы
import os #для получения информации о файлах

path = r'C:Users/user/Desktop/Хлам'  # папка сортировки
folder_move = r'C:/Users/user/Desktop'  # папка куда будет переноситься

# массив форматов файлов
video_format = ['AVI', 'MP4', 'MOV', 'MKV']
archive_format = ['ZIP', 'GZ', 'TAR']
image_format = ['JPEG', 'PNG', 'JPG', 'SVG']
document_format = ['DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX']
audio_format = ['MP3', 'OGG', 'WAV', 'AMR']


def sort_trach(path):
    files = os.listdir(path) #получить список всех файлов
    for items in files:      #перебираем имена файлов внутри цикла
        extension = items.split(".")# Разделяем строку по точке и записываем в переменную.
        shutil.unpack_archive(items, 'new_folder_for_data')
        # для image
        if len(extension) > 1 and extension[1].lower in image_format:
            file = path + "/" + items
            new_path = folder_move + "/images/" + items
            shutil.move(file, new_path)
        # для video
        elif len(extension) > 1 and extension[1].lower in video_format:
            file = path + "/" + items
            new_path = folder_move + "/video/" + items
            shutil.move(file, new_path)
        # для документов
        elif len(extension) > 1 and extension[1].lower in document_format:
            file = path + "/" + items
            new_path = folder_move + "/documents/" + items
            shutil.move(file, new_path)
        # для аудио
        elif len(extension) > 1 and extension[1].lower in audio_format:
            file = path + "/" + items
            new_path = folder_move + "/audio/" + items
            shutil.move(file, new_path)
        # для архивов
        elif len(extension) > 1 and extension[1].lower in archive_format:
            file = path + "/" + items
            new_path = folder_move + "/archives/" + items
            shutil.move(file, new_path)
        else:
            file = path + "/" + items
            new_path = folder_move + "/unknown/" + items
            shutil.move(file, new_path)

# удаляем пустые папки
def remove_empty_folders(path):
    subfolder_paths = get_subfolder_paths(path)
    for p in subfolder_paths:
        if not os.listdir(p):
            print('Deleting empty folder:', p.split('\\')[-1], '\n')
            os.rmdir(p)