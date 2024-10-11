import numpy as np


def get_mids_from_edges(edges):
    mids_len = len(edges)-1
    mids = np.empty(mids_len)
    for i in range(mids_len):
        mids[i] = (edges[i]+edges[i+1])/2
    return mids
