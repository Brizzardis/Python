# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

for i in range(1,10):
    os.mkdir(f'dir_{i}',dir_fd=None)

for i in range(1,10):
    os.remove(f'dir_{i}',dir_fd=None)


