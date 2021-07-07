from threading import Event

# wait() until set()

class Foo:
    def __init__(self):
        self.firstEvent = Event()
        self.secondEvent = Event()


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.firstEvent.set()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        self.firstEvent.wait()
        printSecond()
        self.secondEvent.set()


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        self.secondEvent.wait()
        printThird()