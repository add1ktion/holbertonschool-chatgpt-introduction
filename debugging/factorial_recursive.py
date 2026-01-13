#!/usr/bin/python3
"""
Recursive Factorial Calculator - Holberton School
Usage: ./factorial_recursive.py <non-negative integer>
Calculates n! (factorial) using recursive algorithm with full error handling.
"""

import sys

def factorial(n):
    """
    Computes factorial of non-negative integer using recursion.
    
    Args:
        n (int): Non-negative integer >= 0 to compute factorial for
        
    Returns:
        int: Factorial of n (n!)
        
    Raises:
        ValueError: If n < 0
        RecursionError: For very large n (Python recursion limit)
    """
    if n < 0:
        raise ValueError("Factorial undefined for negative numbers")
    if n == 0:
        return 1
    return n * factorial(n - 1)

def main():
    """
    Main execution entry point.
    Validates command line arguments and computes factorial.
    
    Args:
        sys.argv[1] (str): Single command line argument - non-negative integer
        
    Returns:
        int: Exit code (0 success, 1 error)
    """
    if len(sys.argv) != 2:
        print("Usage: factorial_recursive.py <non-negative integer>")
        print("Example: ./factorial_recursive.py 5")
        return 1
    
    try:
        n = int(sys.argv[1])
        result = factorial(n)
        print(result)
        return 0
    except ValueError as e:
        if "negative" in str(e):
            print("Error: Input must be non-negative integer")
        else:
            print("Error: Invalid input. Enter integer only.")
        return 1

if __name__ == "__main__":
    """
    Program execution guard.
    Calls main() and handles exit gracefully.
    """
    sys.exit(main())
