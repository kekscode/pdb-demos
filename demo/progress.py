class ProgressBar():
    def __init__(self, width=50):
        self.pointer = 0
        self.width = width

    def __call__(self,x):
         # x in percent
         self.pointer = int(self.width*(x/100.0))
         return "|" + "#"*self.pointer + "-"*(self.width-self.pointer)+\
                "|\n %d percent done" % int(x)

if __name__ == '__main__':
    pb = ProgressBar(100)
    for step in [25, 50, 75, 100]:
        # Set two breakpoints to check value:
        # break 18, step == 25
        # break 18, step == 25*3
        print(pb(step))
        import time; time.sleep(1)
        print(chr(27) + "[2J")
