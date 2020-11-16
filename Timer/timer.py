from statistics import mean, median
from time import perf_counter


class Timer:

    """Context manager to time a code block."""

    def __init__(self, func=None):
        self.func = func
        self.runs = []

    def __call__(self, *args, **kwargs):
        with self:
            return self.func(*args, **kwargs)

    def __enter__(self):
        self.start = perf_counter()
        return self

    def __exit__(self, *args):
        self.end = perf_counter()
        self.elapsed = self.end - self.start
        self.runs.append(self.elapsed)
        self.mean = mean(self.runs)
        self.median = median(self.runs)
        self.min = min(self.runs)
        self.max = max(self.runs)
