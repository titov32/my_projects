from rustfib import fib
from time import time
def fib_py(num):
	if num==0:
		return 0
	elif num==1:
		return 1
	else:
		return fib_py(num - 1) + fib_py(num - 2)



if __name__ == '__main__':
	
	num = 40

	print(f'тест функции фиббоначи python на {num}')
	time1 = time()
	rezult=fib_py(num)
	print(f'число фиббоначи {num} = {rezult}')
	time2 = time()
	delta_time_python = time2 - time1
	print(f'время выполенения {delta_time_python} секунд')

	print(f'тест функции фиббоначи rust на {num}')
	time1 = time()
	rezult=fib(num)
	print(f'число фиббоначи {num} = {rezult}')
	time2 = time()
	delta_time_rust = time2 - time1
	print(f'время выполенения {delta_time_rust} секунд')
		
	delta_lang= delta_time_python/delta_time_rust

	print(f'Функция на rust быстрее в {delta_lang}')

