def are_sets_equal(set1, set2, rtol=1e-5, atol=1e-6):
  """
  Compares two sets of floats for equality within a relative and absolute tolerance.

  Args:
      set1: The first set of floats.
      set2: The second set of floats.
      rtol: The relative tolerance (default: 1e-5).
      atol: The absolute tolerance (default: 1e-8).

  Returns:
      True if the sets are equal within the specified tolerances, False otherwise.
  """
  if len(set1) != len(set2):
    return False  # Sets must have the same length
  for x, y in zip(set1, set2):
    if not np.isclose(x, y, rtol=rtol, atol=atol):
      return False
  return True