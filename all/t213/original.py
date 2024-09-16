def im2col(x, k, b):
    """ TODO: implement `im2col`"""
    # Source for im2col: https://leonardoaraujosantos.gitbook.io/artificial-inteligence/machine_learning/deep_learning/convolution_layer/making_faster
    #Co-coded with ChatGPT and copilot 
    # Calculate output dimensions
    output_shape_0 = x.shape[0] - k.shape[0] + 1
    output_shape_1 = x.shape[1] - k.shape[1] + 1

    # Create im2col matrix
    im2col_matrix = []
    for row in range(output_shape_0):
        for col in range(output_shape_1):
            window = x[row: row + k.shape[0], col: col + k.shape[1]]
            im2col_matrix.append(window.flatten())
    im2col_matrix = torch.stack(im2col_matrix).transpose(0, 1)

    # Perform matrix multiplication and add the bias
    result = torch.matmul(k.flatten(), im2col_matrix) + b
    return result.view(output_shape_0, output_shape_1)