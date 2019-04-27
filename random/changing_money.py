import unittest

def change_money(C, M):
	C = sorted(C, reverse=True)
	print(C)
	V = 0
	for i in range(len(C)):
		if M == 0:
			return V
		V = V + (M//C[i])
		M = M%C[i]
		print("div: ", M//C[i], "M:", M,"V: ", V)
	return V


class TestMoneyChange(unittest.TestCase):
	def test_change_money(self):
		C = [1, 5, 10]
		M = 28
		self.assertEqual(change_money(C, M), 6)
		


if __name__ == '__main__':
    unittest.main()

