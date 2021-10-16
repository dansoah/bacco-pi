import math

def percentile_to_bars(percentile):
    bar_length = 10
    checked_bars = math.ceil(percentile * bar_length / 100)
    filled_bars = ["#"] * checked_bars
    blank_bars = [" "] * (bar_length - checked_bars)
    return "".join(filled_bars + blank_bars)