from scheduling import SystemScheduling, get_first_course_example_schedule
from task import Task
def test_get_max_periods_of_tasks():
    tasks = get_first_course_example_schedule()
    sys_sched = SystemScheduling(tasks)
    assert sys_sched.get_maximum_offset() == 0

def test_get_max_periods_of_tasks_different():
    t1 = Task(0, 3, 5, 5)
    t2 = Task(5, 2, 10, 10)
    t3 = Task(88, 4, 20, 20)
    tasks = [t1,t2,t3]
    sys_sched = SystemScheduling(tasks)
    assert sys_sched.get_maximum_offset() == 88

# TODO test get feasibility_interval

# TODO test init System Schedules

# TODO test execute FTP Schedule
