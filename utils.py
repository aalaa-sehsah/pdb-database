from time import time


class LoadingBar:
    def __init__(self, total: int, interval: float = 0.1):
        self.total: int = total
        self.ti: float = time()
        self.t0: float = self.ti
        self.td: float = interval

    def update(self, i: int):
        tc = time()
        if tc - self.t0 > 0.1:
            self.t0 = tc
            percentage = f"{i / self.total * 100:6.2f}"
            print(f"[WAIT] {percentage}% ({i}\\{self.total})", end="\r")

    def finish(self):
        time_taken = f"in {time()-self.ti:.2f} sec"
        print(f"[DONE] 100.00% ({self.total}\\{self.total}) {time_taken}")
