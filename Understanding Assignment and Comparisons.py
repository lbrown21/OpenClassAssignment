# task 1 Value Swapping

def swap(a, b):
  """Swaps the values of two variables.

  Args:
    a: The first variable.
    b: The second variable.
  """

  temp = a
  a = b
  b = temp

  # Compare the values of the two variables to ensure they have been swapped.
  if a != b:
    raise ValueError("The values of the two variables were not swapped.")


# Example usage:

a = 1
b = 2

swap(a, b)

print(a, b)