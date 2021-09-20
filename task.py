class Task:
    def __init__(self, offset=0, wcet=0, deadline=0 , period=0 ):
        self.offset=offset
        self.wcet = wcet
        self.deadline = deadline
        self.period = period

    def __str__(self):
        return f"{self.offset} {self.wcet} {self.deadline} {self.period}"
        
