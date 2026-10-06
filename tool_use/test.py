import math
import unittest
from main import calculate_pi


class TestPiCalculation(unittest.TestCase):
    """Test cases for the calculate_pi function"""
    
    def test_pi_to_5_digits(self):
        """Test that pi is calculated accurately to 5 decimal places"""
        calculated_pi = calculate_pi(5)
        actual_pi = math.pi
        
        # Check if the result is accurate to 5 decimal places
        self.assertAlmostEqual(calculated_pi, actual_pi, places=5,
                               msg=f"Expected {actual_pi:.5f}, got {calculated_pi:.5f}")
    
    def test_pi_value_range(self):
        """Test that the calculated pi is in the expected range"""
        calculated_pi = calculate_pi(5)
        
        # Pi should be between 3.14159 and 3.14160
        self.assertGreater(calculated_pi, 3.14159,
                          msg=f"Pi value {calculated_pi} is too low")
        self.assertLess(calculated_pi, 3.14160,
                       msg=f"Pi value {calculated_pi} is too high")
    
    def test_pi_first_5_decimals(self):
        """Test that the first 5 decimal digits match the actual value of pi"""
        calculated_pi = calculate_pi(5)
        
        # Format to 5 decimal places
        calculated_str = f"{calculated_pi:.5f}"
        expected_str = f"{math.pi:.5f}"
        
        self.assertEqual(calculated_str, expected_str,
                        msg=f"Expected {expected_str}, got {calculated_str}")
    
    def test_pi_is_positive(self):
        """Test that the result is a positive number"""
        calculated_pi = calculate_pi(5)
        self.assertGreater(calculated_pi, 0,
                          msg="Pi should be positive")
    
    def test_pi_type(self):
        """Test that the function returns a float"""
        calculated_pi = calculate_pi(5)
        self.assertIsInstance(calculated_pi, (float, int),
                            msg="Result should be a numeric type")
    
    def test_pi_manual_verification(self):
        """Manual verification that pi starts with 3.14159"""
        calculated_pi = calculate_pi(5)
        
        # Extract the first 5 decimal digits
        pi_rounded = round(calculated_pi, 5)
        
        # The actual value of pi to 5 decimal places is 3.14159
        self.assertEqual(pi_rounded, 3.14159,
                        msg=f"Expected 3.14159, got {pi_rounded}")


def run_tests():
    """Run all tests and display results"""
    print("=" * 60)
    print("Testing Pi Calculation Function")
    print("=" * 60)
    
    # Run the unittest suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPiCalculation)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print("\n" + "=" * 60)
    print("Summary")
    print("=" * 60)
    print(f"Tests run: {result.testsRun}")
    print(f"Successes: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    
    # Display the actual calculated value
    print("\n" + "=" * 60)
    print("Calculated Values")
    print("=" * 60)
    pi_value = calculate_pi(5)
    print(f"Calculated Pi: {pi_value}")
    print(f"Actual Pi:     {math.pi}")
    print(f"Difference:    {abs(pi_value - math.pi)}")
    print(f"Pi to 5 decimals: {pi_value:.5f}")
    print("=" * 60)
    
    return result.wasSuccessful()


if __name__ == "__main__":
    run_tests()
