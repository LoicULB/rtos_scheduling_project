from task import Task

def get_first_course_example_schedule():
    t1 = Task(0, 3, 5, 5)
    t2 = Task(0, 2, 10, 10)
    t3 = Task(0, 4, 20, 20)
    return [t1, t2, t3]


def get_second_example_schedule():
    t1 = Task(0, 2, 4, 5)
    t2 = Task(0, 2, 4, 4)
    return [t1, t2]

def get_deadline_missed_example():
    t1 = Task(0, 3, 5, 5)
    t2 = Task(0, 2, 10, 10)
    t3 = Task(0, 4, 10, 20)
    return [t1, t2, t3]