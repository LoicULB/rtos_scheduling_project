from scheduling import TaskScheduling
from task import Task

def test_is_last_job_finished_one_job_one_exe():
    task = Task(wcet=2, deadline=2, period=3)
    task_scheduling=TaskScheduling(task)
    assert task_scheduling.is_last_job_finished()
    task_scheduling.add_job(instant=0)
    assert not task_scheduling.is_last_job_finished()
    task_scheduling.jobs[-1].start_new_job_execution(0)
    task_scheduling.jobs[-1].add_cpu_unit()
    assert task_scheduling.is_last_job_finished()

def test_is_task_waiting_offset_0():
    task = Task(0, 3, 5, 5)
    task_scheduling=TaskScheduling(task)
    assert task_scheduling.is_task_waiting(0)
    assert task_scheduling.is_task_waiting(1)
    task_scheduling.add_job(0)
    assert not task_scheduling.is_task_waiting(0)
    assert task_scheduling.is_task_waiting(5)
    assert task_scheduling.is_task_waiting(6)
    assert task_scheduling.is_task_waiting(10)
    assert task_scheduling.is_task_waiting(11)

def test_is_waiting_offset_2():
    task = Task(2, 3, 5, 5)
    task_scheduling=TaskScheduling(task)
    assert not task_scheduling.is_task_waiting(0)
    assert not task_scheduling.is_task_waiting(1)
    assert task_scheduling.is_task_waiting(2)
    for i in range(2, 8):
        assert task_scheduling.is_task_waiting(i)

    task_scheduling.add_job(2)
    assert not task_scheduling.is_task_waiting(2)
    assert task_scheduling.is_task_waiting(7)
    assert task_scheduling.is_task_waiting(12)
    assert task_scheduling.is_task_waiting(17)




def generate_task_course_example():
    t1 = Task(0, 3, 5, 5)
    t2 = Task(0, 2, 10, 10)
    t3 = Task(0, 4, 20, 20)

    return [t1, t2, t3]

def generate_task_course_example():
    t1 = Task(2, 3 , 5 , 5)