from model.task import Task


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

def synchronous_arbitrary_task_set():
    t1 = Task(0, 52, 110, 100)
    t2 = Task(0, 52 , 154, 140)
    return [t1,t2]

def asynchronous_implicit_deadline_task_set():
    t1 = Task(0, 7, 10, 10)
    t2 = Task(0, 1, 16, 16)
    t3 = Task(4, 3, 15, 15)
    return [t1, t2, t3]
def asynchronous_implicit_deadline_task_set_unschedulable():
    t1 = Task(0, 7, 10, 10)
    t2 = Task(0, 1, 16, 16)
    t3 = Task(4, 3, 15, 15)
    return [t3, t2, t1]


def AID_V2_unschedulable():
    t1 = Task(10,1,12,12)
    t2 = Task(0,6,12,12)
    t3 = Task(0, 3 , 8 , 8)
    return [t3,t1,t2]

def AID_V2_schedulable():
    t1 = Task(10,1,12,12)
    t2 = Task(0,6,12,12)
    t3 = Task(0, 3 , 8 , 8)
    return [t3,t2,t1]