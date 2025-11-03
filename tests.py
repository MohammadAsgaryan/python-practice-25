import unittest
from main import safe_divide, convert_to_int

class TestErrorHandling(unittest.TestCase):

    # ✅ تست تقسیم درست
    def test_normal_division(self):
        self.assertEqual(safe_divide(10, 2), 5)

    # ✅ تست خطای تقسیم بر صفر
    def test_divide_by_zero(self):
        self.assertEqual(safe_divide(10, 0), "Error: Cannot divide by zero.")

    # ✅ تست تایپ اشتباه
    def test_divide_invalid_type(self):
        self.assertEqual(safe_divide("a", 2), "Error: Inputs must be numbers.")

    # ✅ تبدیل موفق رشته به عدد
    def test_convert_valid_number(self):
        self.assertEqual(convert_to_int("123"), 123)

    # ✅ تبدیل نامعتبر
    def test_convert_invalid_string(self):
        self.assertIsNone(convert_to_int("abc"))

    # ✅ تبدیل تایپ اشتباه
    def test_convert_none(self):
        self.assertIsNone(convert_to_int(None))


if __name__ == "__main__":
    unittest.main()
