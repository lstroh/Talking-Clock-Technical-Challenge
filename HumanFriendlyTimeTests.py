import unittest
import HumanFriendlyTime


class MyTestCase(unittest.TestCase):
    def test_get_hours_string(self):
        obj = HumanFriendlyTime.HumanFriendlyTime()
        sen = {-1: "", 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven',
               8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'noon', 13: 'one', 14: 'two',
               15: 'three', 16: 'four', 17: 'five', 18: 'six', 19: 'seven', 20: 'eight', 21: 'nine',
               22: 'ten', 23: 'eleven', 24: 'midnight', 0: 'midnight', 25: ""}
        for test_input, expected in sen.items():
            self.assertEqual(expected, obj._get_hours_string(test_input),
                             "test input-" + str(test_input) + " expected-" + expected + ".")  # add assertion here

    def test_get_min_string(self):
        obj = HumanFriendlyTime.HumanFriendlyTime()
        sen = {-1: "", 61: "", 0: "", 60: ""}
        upto_11 = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven',
                   8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven'}
        special_cases = {12: 'twelve', 13: "thirteen", 20: 'twenty', 30: 'half'}
        tennsrfix = "teen"
        for test_input, expected in sen.items():
            self.assertEqual(expected, obj._get_min_string(test_input),
                             "test input-" + str(test_input) + " expected-" + expected + ".")
        for test_input, expected in upto_11.items():
            self.assertEqual(expected, obj._get_min_string(test_input),
                             "test input-" + str(test_input) + " expected-" + expected + ".")
        for test_input, expected in special_cases.items():
            self.assertEqual(expected, obj._get_min_string(test_input),
                             "test input-" + str(test_input) + " expected-" + expected + ".")
        for minutes in range(14, 20):
            expected = upto_11[minutes % 10] + tennsrfix
            test_input = minutes
            self.assertEqual(expected, obj._get_min_string(test_input),
                             "test input-" + str(test_input) + " expected-" + expected + ".")
        for minutes in range(21, 30):
            test_input = minutes
            expected = special_cases[20] + " " + upto_11[minutes % 10]
            self.assertEqual(expected, obj._get_min_string(test_input),
                             "test input-" + str(test_input) + " expected-" + expected + ".")
        for minutes in range(31, 40):
            test_input = minutes
            expected_number = 60 - test_input
            expected = special_cases[20] + " " + upto_11[expected_number % 10]
            self.assertEqual(expected, obj._get_min_string(test_input),
                             "test input-" + str(test_input) + " expected-" + expected + ".")
        for minutes in range(41, 47):
            test_input = minutes
            expected_number = 60 - test_input
            expected = upto_11[expected_number % 10] + tennsrfix
            self.assertEqual(expected, obj._get_min_string(test_input),
                             "test input-" + str(test_input) + " expected-"
                             + expected + " expected_number-" + str(expected_number) + ".")
        for minutes, expected in upto_11.items():
            test_input = 60 - minutes
            self.assertEqual(expected, obj._get_min_string(test_input),
                             "test input-" + str(test_input) + " expected-" + expected + ".")
        for minutes, expected in special_cases.items():
            test_input = 60 - minutes
            self.assertEqual(expected, obj._get_min_string(test_input),
                             "test input-" + str(test_input) + " expected-" + expected + ".")

    def test_check_int_input(self):
        obj = HumanFriendlyTime.HumanFriendlyTime()
        self.assertRaises(TypeError, obj._check_int_input, 1.0, 2)
        self.assertRaises(TypeError, obj._check_int_input, "Hi", 2)
        self.assertRaises(TypeError, obj._check_int_input, [], 2)
        self.assertRaises(TypeError, obj._check_int_input, {}, 2)
        self.assertRaises(TypeError, obj._check_int_input, None, 2)
        self.assertRaises(TypeError, obj._check_int_input, obj, 2)
        self.assertRaises(TypeError, obj._check_int_input, 2, 1.0)
        self.assertRaises(TypeError, obj._check_int_input, 2, "Hi")
        self.assertRaises(TypeError, obj._check_int_input, 2, [])
        self.assertRaises(TypeError, obj._check_int_input, 2, {})
        self.assertRaises(TypeError, obj._check_int_input, 2, None)
        self.assertRaises(TypeError, obj._check_int_input, 2, obj)
        self.assertRaises(TypeError, obj._check_int_input, obj, obj)
        for h in range(-1, 26):
            if 0 <= h <= 24:
                obj._check_int_input(h, 10)
            else:
                self.assertRaises(ValueError, obj._check_int_input, h, 10)
        for m in range(-1, 62):
            if 0 <= m <= 60:
                obj._check_int_input(10, m)
            else:
                self.assertRaises(ValueError, obj._check_int_input, 10, m)

    def test_check_string_input(self):
        obj = HumanFriendlyTime.HumanFriendlyTime()
        self.assertRaises(TypeError, obj._check_string_input, 1)
        self.assertRaises(TypeError, obj._check_string_input, 1.0)
        self.assertRaises(TypeError, obj._check_string_input, [])
        self.assertRaises(TypeError, obj._check_string_input, {})
        self.assertRaises(TypeError, obj._check_string_input, obj)
        self.assertRaises(ValueError, obj._check_string_input, "")
        self.assertRaises(ValueError, obj._check_string_input, "1:1:")
        self.assertRaises(ValueError, obj._check_string_input, "12 pm")
        obj._check_string_input("11:11")

    def test_get_human_friendly_time_int(self):
        obj = HumanFriendlyTime.HumanFriendlyTime()
        for h in range(25):
            for m in range(61):
                if m == 0 or m == 60:
                    expected = obj._get_hours_string(h) + " o'clock"
                elif m <= 30:
                    expected = obj._get_min_string(m) + " past " + obj._get_hours_string(h)
                else:
                    expected = obj._get_min_string(m) + " to " + obj._get_hours_string(h)
                test_input = "h -" + str(h) + " m-" + str(m)
                self.assertEqual(expected.capitalize(), obj.get_human_friendly_time_int(h, m),
                                 "test input-" + str(test_input) + " expected-"
                                 + expected.capitalize() + ".")

    def test_get_human_friendly_time_string(self):
        obj = HumanFriendlyTime.HumanFriendlyTime()
        self.assertRaises(ValueError, obj.get_human_friendly_time_string, "kk:1")
        self.assertRaises(ValueError, obj.get_human_friendly_time_string, "1:kk")
        for h in range(25):
            for m in range(61):
                string_time = str(h) + ":" + str(m)
                self.assertEqual(obj.get_human_friendly_time_int(h, m),
                                 obj.get_human_friendly_time_string(string_time),
                                 "string_time-" + str(string_time) + " expected-"
                                 + obj.get_human_friendly_time_int(h, m) + ".")
                if h < 10:
                    string_time = "0" + str(h) + ":" + str(m)
                    self.assertEqual(obj.get_human_friendly_time_int(h, m),
                                     obj.get_human_friendly_time_string(string_time),
                                     "string_time-" + str(string_time) + " expected-"
                                     + obj.get_human_friendly_time_int(h, m) + ".")
                if m < 10:
                    string_time = str(h) + ":0" + str(m)
                    self.assertEqual(obj.get_human_friendly_time_int(h, m),
                                     obj.get_human_friendly_time_string(string_time),
                                     "string_time-" + str(string_time) + " expected-"
                                     + obj.get_human_friendly_time_int(h, m) + ".")


if __name__ == '__main__':
    unittest.main()
