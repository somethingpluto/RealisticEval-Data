# Description:
#  Jax implementation of hash encoding for accelerated implicit neural representation for 1D-4D scenes.
#  Our implementation is based on the paper:
#    Müller, Thomas, et al. "Instant neural graphics primitives with a multiresolution hash encoding." ACM transactions
#     on graphics (TOG) 41.4 (2022): 1-15.
#  with a lot of references from this pytorch implementation:
#    https://github.com/yashbhalgat/HashNeRF-pytorch/blob/main/utils.py
#
# Written by Ruiming Cao on November 23, 2022
# Contact: rcao@berkeley.edu
# Website: https://rmcao.github.io

from typing import Tuple, Union
from functools import partial

import numpy as np
import jax.numpy as jnp
import jax
from flax import linen as nn
from flax.struct import dataclass

import calcil as cc


BOX_OFFSETS_4D = jnp.asarray([[[i,j,k, l] for i in [0, 1] for j in [0, 1] for k in [0, 1] for l in [0, 1]]])
BOX_OFFSETS_3D = jnp.asarray([[[i,j,k] for i in [0, 1] for j in [0, 1] for k in [0, 1]]])
BOX_OFFSETS_2D = jnp.asarray([[[i,j] for i in [0, 1] for j in [0, 1]]])
BOX_OFFSETS_1D = jnp.asarray([[[i] for i in [0, 1]]])


def precision_to_dtype(precision):
    if precision == 'float32':
        return jnp.float32
    elif precision == 'float16':
        return jnp.bfloat16
    else:
        raise NotImplementedError(f'precision = {precision} not implemented.')
