from threading import Condition
class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.current = 1
        self.condition = Condition()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
    	while self.current <= self.n:
            self.condition.acquire()

            if self.current > self.n:
                self.condition.release()
                return

            if self.current % 3 == 0 and self.current % 5 != 0:
                printFizz()
                self.current += 1
                self.condition.notify_all()
            
            self.condition.release()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
    	while self.current <= self.n:
            self.condition.acquire()

            if self.current > self.n:
                self.condition.release()
                return

            if self.current % 3 != 0 and self.current % 5 == 0:
                printBuzz()
                self.current += 1
                self.condition.notify_all()
            
            self.condition.release()


    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while self.current <= self.n:
            self.condition.acquire()

            if self.current > self.n:
                self.condition.release()
                return

            if self.current % 3 == 0 and self.current % 5 == 0:
                printFizzBuzz()
                self.current += 1
                self.condition.notify_all()
            
            self.condition.release()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        while self.current <= self.n:
            self.condition.acquire()

            if self.current > self.n:
                self.condition.release()
                return
                
            if self.current % 3 != 0 and self.current % 5 != 0:
                printNumber(self.current)
                self.current += 1
                self.condition.notify_all()

            self.condition.release()
        