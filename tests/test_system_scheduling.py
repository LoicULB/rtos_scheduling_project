from scheduling import SystemScheduling, get_first_course_example_schedule, get_scheduling_course_second_exemple, get_scheduling_deadline_missed, get_deadline_missed_example
from task import Task
import pytest
from scheduling import DeadlineMissedException
from scheduling import synchronous_arbitrary_task_set
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

def test_no_exception_fc():
    tasks = get_first_course_example_schedule()
    sys_sched = SystemScheduling(tasks)
    sys_sched.execute_FTP_schedule()
"""
def test_no_exception_fc_perm_1():
    t1 = Task(0, 3, 5, 5)
    t2 = Task(0, 2, 10, 10)
    t3 = Task(0, 4, 20, 20)
    tasks = [t2,t3,t1]
    tasks = get_first_course_example_schedule()
    sys_sched = SystemScheduling(tasks)
    sys_sched.execute_FTP_schedule()
"""
def test_raise_deadline_exception():
    with pytest.raises(DeadlineMissedException):
        tasks = get_scheduling_deadline_missed()

def test_raise_deadline_exception_v2():
    with pytest.raises(DeadlineMissedException):
        tasks = get_scheduling_deadline_missed()
        sys_sched = SystemScheduling(tasks)
        sys_sched.execute_FTP_schedule()

def test_raise_deadline_exception_v3():
    t1 = Task(0, 3, 5, 5)
    t2 = Task(0, 2, 10, 10)
    t3 = Task(0, 4, 20, 20)

    tasks_set = [t2, t3, t1]
    with pytest.raises(DeadlineMissedException):
        #tasks = get_scheduling_deadline_missed()
        sys_sched = SystemScheduling(tasks_set)
        sys_sched.execute_FTP_schedule()

def test_raise_deadline_exception_SAD():

    tasks_set = synchronous_arbitrary_task_set()
    with pytest.raises(DeadlineMissedException):
        sys_sched = SystemScheduling(tasks_set)
        sys_sched.execute_FTP_schedule()


# TODO test get feasibility_interval

# TODO test init System Schedules

# TODO test execute FTP Schedule
