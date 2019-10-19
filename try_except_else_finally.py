try:
	f = open('my_module.py')
	#if f.name == 'my_module.py':
		#raise Exception
except Exception:
	print('Error!')
else:
	print(f.read())	
	f.close()
finally:
	print('Executing finally...')	