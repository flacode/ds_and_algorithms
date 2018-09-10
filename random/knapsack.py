import unittest


def sort_weight_values(weight, value):
	zipped = zip(weight, value)
	sortL = sorted(zipped, key=lambda item: item[1]/item[0], reverse=True)
	weightS, valueS = map(list, zip(*sortL))
	return (weightS, valueS)

def knapsack(W, weight, values):
	V = 0
	# print(weight, values)
	weight, values = sort_weight_values(weight, values)
	# print(weight, values)
	for i in range(len(weight)):
		if W == 0:
			return V
		a = min(W, weight[i])
		V = V + a * (values[i]/weight[i])
		W = W - a
	return V

class TestSort(unittest.TestCase):
	def test_sorting(self):
		value = [20,18,14]
		weight = [4, 3, 2]
		self.assertEqual(sort_weight_values(weight, value), ([2,3,4], [14, 18, 20] ))
 
	def test_knapsack(self):
		weight = [4,3,2]
		value = [20, 18, 14]
		W = 7
		self.assertEqual(knapsack(W, weight, value), 42) 
if __name__ == '__main__':
    unittest.main()

