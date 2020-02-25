"""@@ -1,5 +1,5 @@"""
from typing import Any, Sequence, Optional

import numpy as np

def binary_search(elem: Any, arr: Sequence) -> Optional[int]:
	"""
@@ -9,5 +9,37 @@ def binary_search(elem: Any, arr: Sequence) -> Optional[int]:
	:param arr: array where element is to be found
	:return: Index of element if it's presented in the arr, None otherwise
	"""
	arr = sorted(arr)
	print(elem, arr)
	return None
	left = 0
	right = len(arr) - 1
	if elem in arr:
		while True:
			if right - left == 1:
				if elem == arr[right]:
					return right
				elif elem == arr[left]:
					return left
				else:
					return None
			middle = (left + right) // 2
			if elem == arr[middle]:
				return middle
			else:
				if elem < arr[middle]:
					right = middle - 1
				elif elem > arr[middle]:
					left = middle + 1

	else:
		return None




if __name__ == "__main__":
	n = 1000
	array = np.arange(n)
	some_elem = np.random.choice(array)
	np.random.shuffle(array)
	print(binary_search(some_elem, array))