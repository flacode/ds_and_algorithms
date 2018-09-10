# Uses python3
import unittest

def allocate_ad_slots(ads, slots):
	# sort lists
	ads = sorted(ads)
	slots = sorted(slots)
	result = 0
	for i in range(len(ads)):
		result = result + (ads[i]*slots[i])
	return result

class TestAdSlot(unittest.TestCase):
	def test_one_slot_one_add(self):
		ads = [23]
		slots = [39]
		self.assertEqual(allocate_ad_slots(ads, slots), 897)

	def test_multiple_ads_slots(self):
		ads=[56, 87, 64]
		slots = [14, 10, 20]
		self.assertEqual(allocate_ad_slots(ads, slots), 3196)


if __name__ == '__main__':
    unittest.main()
