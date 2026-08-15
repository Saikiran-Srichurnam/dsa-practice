from threading import Lock

class DiningPhilosophers:

    def __init__(self):
        self.forks = [Lock() for _ in range(5)]

    # call the functions directly to execute, for example, eat()
    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        
        left = philosopher
        right = (philosopher + 1) % 5

        first = min(left, right)
        second = max(left, right)

        self.forks[first].acquire()
        self.forks[second].acquire()

        pickLeftFork()
        pickRightFork()

        eat()
        
        putLeftFork()
        putRightFork()

        self.forks[first].release()
        self.forks[second].release()
        