class A:
	public_class_attr_A = "public_class_attr_A"
	_protected_class_attr_A = "_protected_class_attr_A"
	__private_class_attr_A = "__private_class_attr_A"

	def __init__(self):
		...

	def public_object_method (self):
		print ("public_object_method")
	def _protected_object_method (self):
		print("_protected_object_method")
	def __private_object_method (self):
		print ("__private_object_method")

if __name__ == "__main__":
	a = A()
	#print (a.public_class_attr_A)
	#print(a._protected_class_attr_A)
	#print(a.__private_class_attr_A)

	#a.public_object_method()
	#a._protected_object_method()
	#a.__private_object_method()