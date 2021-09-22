from task import Task
# TODO complete this class
class Scheduling:
    """
    Class representing a a bounded scheduling of a set of tasks
    """
    def __init__(self, array=[]):
        self.scheduling=array

def get_first_course_example_schedule():
    t1 = Task(0, 3, 5, 5)
    t2 = Task(0, 2, 10, 10)
    t3 = Task(0, 4, 20, 20)
    return [t1, t2, t3]



class Job:
    """
    Class representing a job

    A job is defined by a start (offset) and the number of cpu units it has received yet
    """
    def __init__(self, start=0, nb_cpu_units=0):
        self.start = start
        self.nb_cpu_units = nb_cpu_units

    def __str__(self):
        return f"{self.start} {self.nb_cpu_units}"
