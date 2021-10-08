import pytest

from model.exceptions import DeadlineMissedException
from test_utils.scheduling_tests import *


def test_get_max_periods_of_tasks():
    tasks = get_first_course_example_schedule()
    sys_sched = SystemScheduling(tasks)
    assert sys_sched.get_maximum_offset() == 0


def test_get_max_periods_of_tasks_different():
    t1 = Task(0, 3, 5, 5)
    t2 = Task(5, 2, 10, 10)
    t3 = Task(88, 4, 20, 20)
    tasks = [t1, t2, t3]
    sys_sched = SystemScheduling(tasks)
    assert sys_sched.get_maximum_offset() == 88


def test_no_exception_fc():
    tasks = get_first_course_example_schedule()
    sys_sched = SystemScheduling(tasks)
    sys_sched.execute_FTP_schedule()


def test_raise_deadline_exception():
    with pytest.raises(DeadlineMissedException):
        get_scheduling_deadline_missed()


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
        sys_sched = SystemScheduling(tasks_set)
        sys_sched.execute_FTP_schedule()


def test_raise_deadline_exception_SAD():
    tasks_set = synchronous_arbitrary_task_set()
    with pytest.raises(DeadlineMissedException):
        sys_sched = SystemScheduling(tasks_set)
        sys_sched.execute_FTP_schedule()

def test_no_raise_deadline_exception_SAD_inverted():
    tasks_set = synchronous_arbitrary_task_set()
    task = tasks_set.pop(0)
    tasks_set.append(task)
    sys_sched = SystemScheduling(tasks_set)
    sys_sched.execute_FTP_schedule()

# TODO test get feasibility_interval
