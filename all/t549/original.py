#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 15:48:20 2023

@author: bas
"""

import numpy as np
from xpsi.global_imports import  _keV, _k_B
k_B_over_keV = _k_B / _keV

def get_T_in_log10_Kelvin(T_keV):
  """
  Converts temperature from keV to log10(K) for a given input (scalar or tuple).

  Args:
      T_keV: The temperature in keV, can be a scalar or a tuple.

  Returns:
      A scalar or tuple containing the temperature in log10(K) for each input element.

  Raises:
      ValueError: If the input is not a scalar or a tuple.
  """

  if isinstance(T_keV, (int, float)):
    # Handle scalar case
    T_log10_Kelvin = np.log10(T_keV / k_B_over_keV)
    return T_log10_Kelvin
  elif isinstance(T_keV, tuple):
    # Handle tuple case
    T_log10_Kelvin_values = []
    for t in T_keV:
      T_log10_Kelvin_values.append(np.log10(t / k_B_over_keV))
    return tuple(T_log10_Kelvin_values)
  else:
    raise ValueError("Input must be a scalar or a tuple.")