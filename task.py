
class Task:
    """
    A class used to represent a Task

    ...

    Attributes
    ----------

    offset : int
        the time after which the jobs will be launched
    wcet : int
        the worst case computation time of the task
    deadline : int
        the time after which the jobs of the given task has to end
    period : int
        the period after which a new job of the task can be re released
    """
    def __init__(self, offset=0, wcet=0, deadline=0 , period=0 ):
        self.offset=offset
        self.wcet = wcet
        self.deadline = deadline
        self.period = period

    def __str__(self):
        return f"{self.offset} {self.wcet} {self.deadline} {self.period}"
        
