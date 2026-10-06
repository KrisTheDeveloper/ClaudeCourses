def calculate_pi(precision=5):
    """
    Calculate pi to the specified number of decimal digits.
    Uses the Machin formula for faster convergence: pi/4 = 4*arctan(1/5) - arctan(1/239)
    
    Args:
        precision: Number of decimal digits to calculate (default 5)
    
    Returns:
        float: Approximation of pi
    """
    def arctan(x, num_terms):
        """Calculate arctan using Taylor series"""
        result = 0
        x_squared = x * x
        x_power = x
        for n in range(num_terms):
            sign = (-1) ** n
            result += sign * x_power / (2 * n + 1)
            x_power *= x_squared
        return result
    
    # Using Machin's formula: pi/4 = 4*arctan(1/5) - arctan(1/239)
    # Need enough terms for desired precision
    num_terms = 500  # Sufficient for 5+ decimal places
    
    pi_over_4 = 4 * arctan(1/5, num_terms) - arctan(1/239, num_terms)
    pi = 4 * pi_over_4
    
    return pi


def main():
    print("HELLO THIS IS THE MAIN FILE")
    pi_value = calculate_pi(5)
    print(f"Pi calculated to 5 decimal places: {pi_value:.5f}")
    print(f"Full precision: {pi_value}")



if __name__== "__main__": 
    main()