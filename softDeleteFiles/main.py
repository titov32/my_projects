import os
import datetime


def modification_date(filename):
    t = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(t)

deadtime = datetime.datetime(2021, 12, 25)
folder = 'Y:\Public_E\Dokument`s\_ТехОтдел'
tree = os.walk(folder)
for address, _, files in tree:
    for file in files:
        path = address+'\\'+file
        if deadtime>modification_date(path):
            try:
                #os.remove(path)
                print(f'new file {path}')
            except PermissionError as e:
                print(f'Отказано в доступе {path}')
        else:
            print(path)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass


