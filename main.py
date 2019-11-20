#!usr/bin/python
#use-python

true = 'bilangan tersebut adalah Positif'

false = 'bilangan tersebut adalah Negatif'

leng = 'bilangan tersebut Nol'

def cek(num):

	global num
	if num > 0:

		print true

		ing()

	else:

		if num == 0:

			print leng

			ing()

		else:

			print false

			ing()

def ing():

	global num

	num = raw_input('Masukan Bilangan : ')

	cek(num)
