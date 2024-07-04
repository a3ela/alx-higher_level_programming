#!/usr/bin/python3
def find_peak(list_of_integers):
  """
  Finds a peak (an element greater than its neighbors) in a list of unsorted integers.

  Args:
      list_of_integers: A list of integers.

  Returns:
      The first peak element found in the list, or None if no peak is found.
  """
  
  # Handle edge cases: empty list or list with one element
  if len(list_of_integers) <= 1:
    return None

  # Recursive binary search to find a peak
  def binary_search(start, end):
    if start == end:
      return list_of_integers[start]  # Single element is considered a peak

    mid = (start + end) // 2

    # Check if middle element is a peak
    if (mid > 0 and list_of_integers[mid] > list_of_integers[mid - 1]) and (mid < len(list_of_integers) - 1 and list_of_integers[mid] > list_of_integers[mid + 1]):
      return list_of_integers[mid]

    # If middle element is not a peak, search for peak in the appropriate half
    elif mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
      return binary_search(start, mid - 1)
    else:
      return binary_search(mid + 1, end)

  # Initiate the binary search on the entire list
  return binary_search(0, len(list_of_integers) - 1)
