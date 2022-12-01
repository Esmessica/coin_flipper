from  random import randint

class Decider:
    """Logic of decision making"""
    def heads_or_tails(self):
        _x = randint(1,2)
        if _x == 1:
            return 1 

        else:
            return 0 

