def maximo(a, b):
	if (a >= b):
		return a
	else: 
		return b

def test_1():
	assert (maximo(10,5) == 10)

def test_2():
	assert (maximo(20,55) == 55)

def test_3():
	assert (maximo(0,0) == 2)