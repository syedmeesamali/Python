class Total:
    i = 0
    def __init__(self):
        self._amount = None

    
    @classmethod
    #@property
    def amount(self):
        print(f'Ran {self.i}th time')
        self.i += 1
        return self.amount

Total().amount()