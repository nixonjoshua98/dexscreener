import time
import threading
import collections


class RateLimiter:
    def __init__(self, max_calls, period):
        self.calls = collections.deque()

        self.period = period
        self.max_calls = max_calls
        self.lock = threading.Lock()

    def __enter__(self):
        with self.lock:
            if len(self.calls) >= self.max_calls:
                until = time.time() + self.period - self._timespan
                sleeptime = until - time.time()
                if sleeptime > 0:
                    time.sleep(sleeptime)
            return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with self.lock:
            self.calls.append(time.time())

            while self._timespan >= self.period:
                self.calls.popleft()

    @property
    def _timespan(self):
        return self.calls[-1] - self.calls[0]