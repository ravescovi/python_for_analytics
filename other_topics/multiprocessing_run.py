import multiprocessing
import time

def square(x):
	return x**2

# python doens't have a main() that is executed automatically
# like some other languages, when a python script is executed from the shell
# it sets some variables, in this case the __name__ which is the name of the current
# module if we are running are module as the main program, for instance "python run.py"
#  __name__ get's  assigned __main__
# simply, we use this if the file is to be executed as a script
# decent rule of thumb, if we intend our code/classes/function from a script to be
# imported, we can forgo this piece of the code
if __name__ == '__main__':
	
	start = time.time()

	vect = list(range(100000000))

	# Runtime: 104 seconds
	#a = []
	#for i in vect:
	#	a.append(square(i))


	# Runtime Square: 30 seconds
	#vect = [square(i) for i in vect]

	# Runtime Square: 32 seconds
	#vect = list(map(square, vect))

	# Runtime Square: 18 seconds
	pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
	results = pool.map(square, vect)

	end = time.time()
	print("Seconds:{}".format(end - start))

