def compute_10_minute_intervals(shifts_for_day):
    """
    This function is used to compute the number of shifts that occur in each
    10-minute interval of a day.

    Parameters
    ----------
    shifts_for_day : list

    Returns
    -------
    list
        A list of dictionaries containing the number of shifts that occur in
    """

    # A list to store the counts for each 10-minute interval
    counts = [0] * 144  # 24 hours * 6 intervals per hour

    for shift in shifts_for_day:
        start_idx = (shift.start_shift.hour * 6) + (shift.start_shift.minute // 10)
        end_idx = (shift.end_shift.hour * 6) + (shift.end_shift.minute // 10)

        # Increase the count for each interval that the shift spans
        for idx in range(start_idx, end_idx):
            counts[idx] += 1

    # Convert counts to the desired output format
    intervals = []
    for hour in range(24):
        for minute in range(0, 60, 10):
            time = f"{str(hour).zfill(2)}:{str(minute).zfill(2)}"
            idx = (hour * 6) + (minute // 10)
            intervals.append({"time": time, "count": counts[idx]})

    return intervals
