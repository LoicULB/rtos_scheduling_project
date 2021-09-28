from scheduling import TaskScheduling
from task import Task

def test_is_last_job_finished_one_job_one_exe():
    task = Task(wcet=2, deadline=2, period=3)
    task_scheduling=TaskScheduling(task)
    assert task_scheduling.is_last_job_finished()
    task_scheduling.add_job(start=0)
    assert not task_scheduling.is_last_job_finished()
    task_scheduling.jobs[-1].add_cpu_unit()
    assert task_scheduling.is_last_job_finished()

def test_is_task_waiting():
    task = Task(wcet=2, deadline=2, period=3)

def generate_task():
    t1 = Task(0, 3, 5, 5)
    t2 = Task(0, 2, 10, 10)
    t3 = Task(0, 4, 20, 20)

    return [t1, t2, t3]