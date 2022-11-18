import os

class Clear:
    
    def cls(self):

        input()
        return os.system('cls' if os.name=='nt' else 'clear')
