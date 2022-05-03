import os
import shutil
from pick import pick
import configparser

while True:
    config = configparser.ConfigParser()
    config.read('config.ini')
    
    if config['DEFAULT']['user'] == 'None':
        d = os.listdir('C:\\Users\\')
        d.remove('desktop.ini')
        d.remove('All Users')
        d.remove('Default')
        d.remove('Default User')
        d.remove('Public')
        d.remove('Все пользователи')
        titleUser = f'Выберите пользователя: '
        optionsUser = d
        optionUser, indexUser = pick(optionsUser, titleUser, indicator='=>', default_index=0)
        config['DEFAULT']['user'] = optionUser
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
    
    user = config['DEFAULT']['user']
    files_ = os.listdir()
    files_.remove('YandexCLW.py')
    files_.remove('config.ini')
    files_.append('Сменить пользователя')
    files_.append('Выход')
    title = f'Текущий пользователь: {user}\nВыберите файл: '
    options = files_
    option, index = pick(options, title, indicator='=>', default_index=0)
    
    if option == 'Сменить пользователя':
        d = os.listdir('C:\\Users\\')
        d.remove('desktop.ini')
        d.remove('All Users')
        d.remove('Default')
        d.remove('Default User')
        d.remove('Public')
        d.remove('Все пользователи')
        titleUser = f'Выберите пользователя: '
        optionsUser = d
        optionUser, indexUser = pick(optionsUser, titleUser, indicator='=>', default_index=0)
        config['DEFAULT']['user'] = optionUser
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
        continue

    elif option == 'Выход':
        os._exit(0)
    
    else:
        break
    

user = config['DEFAULT']['user']
directory = os.getcwd() + "\\"
os.chdir(f'C:\\Users\\{user}\\AppData\\Local\\Yandex\\YandexBrowser\\User Data\\Default\\Wallpapers\\store\\')
files = os.listdir()

for file in files:
    if 'video-h264-2560' in file:
        file1 = f'C:\\Users\\{user}\\AppData\\Local\\Yandex\\YandexBrowser\\User Data\\Default\\Wallpapers\\store\\'+file
    elif 'video-vp8-1280' in file:
        file2 = f'C:\\Users\\{user}\\AppData\\Local\\Yandex\\YandexBrowser\\User Data\\Default\\Wallpapers\\store\\'+file

os.chdir(directory)
shutil.copyfile(option, file1)
shutil.copyfile(option, file2)