def reverse_text(text):
    """
    Reverses the input text string.
    
    Parameters:
        text (str): The string to reverse.
    
    Returns:
        str: The reversed string.
    
    Raises:
        TypeError: If input is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")
    return text[::-1]


def add_numbers(a, b):
    """
    Returns the sum of two numbers.
    
    Parameters:
        a (int or float): The first number.
        b (int or float): The second number.
    
    Returns:
        int or float: The sum of the numbers.
    
    Raises:
        TypeError: If inputs are not int or float.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Inputs must be int or float.")
    return a + b
