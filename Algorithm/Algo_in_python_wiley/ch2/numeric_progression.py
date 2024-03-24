'''
NumericProgression class design 

Fields:
    start - Proivded by user, default is 0

Behaviors/Methods:
    advance()
    next()
    iter()
    print_progression()
'''

class Num_Progress:
    def __init__(self,start=0):
        self._curr = start

    def advance(self):
        '''
        Update the Self.current to the next value

        This will be overridden by other progression classes to use geo, loc or fib progressions
        '''
        self._curr += 1

    def next(self):
        '''
        Prints the next value
        '''

        if self._curr is None:
            raise StopIteration
        else:
            val = self._curr
            self.advance()
            return val

    def __iter__(self):
        return self

    def print_progression(self,n):
        """Print next n values of the Progression"""
        # print(' '.join(str(next(self)) for j in range(n)))
        for _ in  (n):
            print(self.next())


class Geom_Progres(Num_Progress):
    def __init__(self,start=0,fac=1):
        super().__init__(start)
        self._fac = fac

    def advance(self):
        self._curr = self._curr * self._fac
        return self._curr


g1 = Geom_Progres(2,2)
g1.print_progression(10)