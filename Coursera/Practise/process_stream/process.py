# рассотрим работу ассинхроного модуля
# для получения процесса, мы можем использовать
# системные команды os.getpid()
# чтобы чклонировать запрос используем
# os.fork() не работает в windows


import time
import os

pid = os.fork()

if pid == 0:
    print(f"child {os.getpid()}")
    time.sleep(5)

else:
    print(f"parent {os.getpid()}")
    os.wait()