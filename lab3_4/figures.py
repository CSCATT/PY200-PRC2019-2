from abc import abstractmethod

class Figure:
	def __init__ (self, x = 0, y = 0):
		self._x = x
		self._y = y

	@abstractmethod
	def perimeter (self):
		return 0.0

	@abstractmethod
	def square (self):
		return 0.0

	@property
	def width (self):
		return 0.0

	@property
	def height (self):
		return 0.0

	@property
	def x(self):
		return  self._x

	@x.setter
	def x(self, x):
		if not isinstance(x, int):
			raise TypeError
		self._x = x

	@property
	def y(self):
		return self._y

	@y.setter
	def y(self, y):
		if not isinstance(y, int):
			raise TypeError
		self._y = y



class Rectangle(Figure):
	def __init__ (self, x = 0, y = 0, w = 0, h = 0):
		#self.__x = x
		#self.__y = y
		super().__init__(x, y)
		self.width = w
		self.height = h

	@property
	def height(self):
		return self._height

	@height.setter
	def height(self, height):
		if not isinstance(height, int):
			raise TypeError
		self._height = height

	@property
	def width (self):
		return self._width

	@width.setter
	def width (self, width):
		if not isinstance(width, int):
			raise TypeError
		self._width = width

	def perimeter (self):
		return 2 * (self.w + self.h)

	def square (self):
		return self.w * self.h


class Ellipse (Figure):
	def __init__ (self, x = 0, y = 0, w = 0, h = 0):

		super().__init__(x, y)
		self.width = w
		self.height = h

	@property
	def height (self):
		return self._height

	@height.setter
	def height (self, height):
		if not isinstance(height, int):
			raise TypeError
		self._height = height

	@property
	def width (self):
		return self._width

	@width.setter
	def width (self, width):
		if not isinstance(width, int):
			raise TypeError
		self._width = width

	def perimeter (self):
		return 2 * (self.w + self.h)

	def square (self):
		return self.w * self.h


class CloseFigure(Figure):
	def __init__(self, *args):
		self.d = [{"x": x0, "y": y0},
				  {"x": x1, "y": y1}]
