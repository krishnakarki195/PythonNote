'''
crated by Krishna Karki decorator example

'''

class decorator_class(object):
	def __init__(self,original_function):
		self.original_function = original_function

	def __call__(self, *args, **kwargs):
		print("Call method executed before {}".format(self.original_function.__name__))
		return self.original_function(*args,**kwargs)


@decorator_class
def display_info(name, age):
	print("Display info ran with the argument {} {}").format(name,age)
	

display_info("John", 20)

