from shutil import move
import datetime
import hashlib
import logging
import os

logging.basicConfig(filename="backup.log", level=logging.INFO)
is_even_day = (datetime.date.today().day + 1) % 2
src_file = os.listdir(path='Vesy_CH')[0]

dst_folder = 'even_day' if is_even_day else 'uneven_day'

dst_file = dst_folder + '\\' + 'Vesy_CH_backup.backup'
src_file = 'Vesy_CH' + '\\' + src_file

logging.error(f'{datetime.datetime.now().ctime()} delete all file to folder destination')
try:
    list_file = os.listdir(path=dst_folder)
    for i in list_file:
        path = dst_folder + '//' + i
        os.remove(path=path)
except Exception as e:
    logging.error(f'{datetime.datetime.now().ctime()} Error for delete file. Error: {e} call SisAdmin Titov Evgeniy')
else:
    logging.info(f'{datetime.datetime.now().ctime()} folder success clear')

# функция возвращает хэш файла


def md5_hash(filename):
    BUF_SIZE = 65536
    md5 = hashlib.md5()
    sha1 = hashlib.sha1()

    with open(filename, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            md5.update(data)
            sha1.update(data)

    logging.info(filename + ' ' + "MD5: {0}".format(md5.hexdigest()))
    return md5


hash_src, hash_dst = 0, 1
# берем хэш суммы файлов и проверяем их наличие
try:
    hash_src = md5_hash(src_file).hexdigest()
except FileNotFoundError:
    logging.error(f'{datetime.datetime.now().ctime()} source file not found')
    exit()
try:
    hash_dst = md5_hash(dst_file).hexdigest()
except FileNotFoundError:
    logging.error(f'{datetime.datetime.now().ctime()} destination file not found')
    hash_dst = 0
try:
    # проверяем хэши если файла нет то перемещаем файл
    if not hash_src == hash_dst:
        logging.info(f'{datetime.datetime.now().ctime()} move file to even_day')
        move(src_file, dst_file)
    else:
        logging.error(f'{datetime.datetime.now().ctime()} file exist')
except Exception as e:
    logging.error(f'{datetime.datetime.now().ctime()} Error {e} call SisAdmin Titov Evgeniy')
else:
    logging.info(f'{datetime.datetime.now().ctime()} file success move')
