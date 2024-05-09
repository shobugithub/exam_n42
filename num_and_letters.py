# 4 print_numbers va print_leters nomli funksiyalar yarating. prit_numbers funksiyasi (1,5) gacha bo’lgan
# sonlarni , print_letters esa  ‘’ABCDE” belgilarni loop da bitta dan time sleep(1) qo’yib ,parallel 2ta
# thread yarating.Ekranga parallel ravishda itemlar chiqsin.



import threading
import time


def print_numbers():
    for i in range(1, 5 + 1):
        print(f'Number => {i}')
        time.sleep(1)


#
def print_letters():
    for i in 'ABCDE':
        print(f'Character => {i}')
        time.sleep(1)


thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

start_time = time.time()
thread1.start()

thread2.start()

thread1.join()
thread2.join()
end_time = time.time()
print(f'Total time => {end_time - start_time}')
print('Process finished')