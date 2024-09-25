
def detrend_dataarray(data_array, dim, order=4, return_trend=False):
    """
    Generated with ChatGPT4
    Detrends an xarray DataArray using a polynomial of specified order.

    :param data_array: xarray DataArray with time series data.
    :param dim: Name of the dimension along which to detrend (e.g., 'time').
    :param order: Order of the polynomial to be used for detrending. Default is 4.
    :return: xarray DataArray of detrended data.
    """
    if not isinstance(data_array, xr.DataArray):
        raise ValueError("Input must be an xarray DataArray.")

    # Extracting the dimension values (e.g., time)
    dim_values = data_array[dim].values

    # Reshaping for polynomial fitting
    X = np.array(dim_values).reshape(-1, 1)

    # Create polynomial features
    poly = PolynomialFeatures(degree=order)
    X_poly = poly.fit_transform(X)

    # Fit the model
    model = LinearRegression()
    model.fit(X_poly, data_array.values)

    # Predict the trend
    trend = model.predict(X_poly)

    # Detrend the data
    detrended = data_array - trend

    if return_trend:
        return trend, detrended
    else:
        return detrended