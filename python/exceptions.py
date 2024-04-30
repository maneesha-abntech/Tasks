def divide(x, y):
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        print("Error: Division by zero!")
    except TypeError:
        print("Error: Unsupported operand type(s) for division!")
    except Exception as e:
        print("An unexpected error occurred:", e)

# Example usage
try:
    # Test division by zero
    print(divide(10, 0))
    # Test unsupported operand types
    print(divide("10", 2))
    # Test valid division
    print(divide(10, 2))
except Exception as e:
    print("An unexpected error occurred in the main program:", e)



'''
def get_positive_integer():
    try:
        num = int(input("Enter a positive integer: "))
        if num <= 0:
            raise ValueError("Input must be a positive integer")
        return num
    except ValueError as ve:
        print("Error:", ve)
        return None
    except Exception as e:
        print("An unexpected error occurred:", e)
        return None
    finally:
        print("Input validation complete.")

num = get_positive_integer()
    if num is not None:
        print("You entered:", num)
'''