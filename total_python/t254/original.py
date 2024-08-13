# MOST PLOTS ARE PARTIALLY AI GENERATED VIA CHATGPT

def separate_by_sol_andplot(data, indices):
    transposed_rows = []  # Collect transposed rows in a list

    for i in indices:
        if is_nan_string(i):
            continue  # Skip NaN strings

        i = int(i)
        rowy = data.iloc[i]
        rowy = rowy.T
        transposed_rows.append(rowy)

    # Concatenate all transposed rows into the output DataFrame
    if transposed_rows:
        output = pd.concat(transposed_rows, axis=1)
    else:
        output = pd.DataFrame()  # Empty DataFrame if no valid rows were found

    return output.T