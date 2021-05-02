def slices(series, length):
    series_len = len(series)

    if series_len < length or length <= 0 or not series:
        raise ValueError('Invalid errors for slice and length')

    if series_len == length:
        return [series]

    step = series_len - length
    return [series[i:length+i] for i in range(step+1)]
