from dataclasses import dataclass


@dataclass
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
    offset: int = 0
    wcet: int = 0
    deadline: int = 0
    period: int = 0
    is_hard: bool = True

    def __str__(self):
        return f"{self.offset} {self.wcet} {self.deadline} {self.period}"
