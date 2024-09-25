def conv_backward_naive(dout, cache):
    """
    A naive implementation of the backward pass for a convolutional layer.

    Inputs:
    - dout: Upstream derivatives.
    - cache: A tuple of (x, w, b, conv_param) as in conv_forward_naive

    Returns a tuple of:
    - dx: Gradient with respect to x
    - dw: Gradient with respect to w
    - db: Gradient with respect to b
    """
    dx, dw, db = None, None, None
    ###########################################################################
    # TODO: Implement the convolutional backward pass.                        #
    ###########################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    # Generated with GPT-3

    x, w, b, conv_param = cache
    stride = conv_param['stride']
    pad = conv_param['pad']

    N, C, H, W = x.shape
    F, _, HH, WW = w.shape
    _, _, out_H, out_W = dout.shape

    dx = np.zeros_like(x)
    dw = np.zeros_like(w)
    db = np.zeros_like(b)

    x_pad = np.pad(x, ((0, 0), (0, 0), (pad, pad), (pad, pad)), mode='constant')

    dx_pad = np.pad(dx, ((0, 0), (0, 0), (pad, pad), (pad, pad)), mode='constant')

    for n in range(N):
        for f in range(F):
            for h_out in range(out_H):
                for w_out in range(out_W):
                    h_start = h_out * stride
                    h_end = h_start + HH
                    w_start = w_out * stride
                    w_end = w_start + WW

                    dx_pad[n, :, h_start:h_end, w_start:w_end] += w[f] * dout[n, f, h_out, w_out]
                    dw[f] += x_pad[n, :, h_start:h_end, w_start:w_end] * dout[n, f, h_out, w_out]
                    db[f] += dout[n, f, h_out, w_out]

    dx = dx_pad[:, :, pad:-pad, pad:-pad]
      
    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    ###########################################################################
    #                             END OF YOUR CODE                            #
    ###########################################################################
    return dx, dw, db