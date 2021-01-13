from multiprocessing import Process
from threading import Thread


class TestThread(Thread):

    def __init__(self, count):
        super().__init__()
        self.count = count

    def run(self):
        print('obj is run {count}'.format(count=self.count))


def test_func_process(digit):
    for elem in range(digit):
        print(elem)


if __name__ == "__main__":

    th = TestThread(15)
    th.start()
    th.join()

    print('First thread is end')

    th = Process(target=test_func_process, args=((12,)))
    th.start()
    th.join()


