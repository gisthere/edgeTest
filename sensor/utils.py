import time


class debounce:

    def __init__(self, max_calls_per_second):
        self.period = 1/max_calls_per_second
        self.last_call_time = None

    def __call__(self, fn):

        def wrapped_function(*args, **kwargs):
            current = time.time()

            if self.last_call_time is not None:
                timedelta = current - self.last_call_time
                if timedelta <= self.period:
                    time.sleep(self.period - timedelta)

            self.last_call_time = time.time()
            fn(*args, **kwargs)

        return wrapped_function
