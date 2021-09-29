from scheduling import TaskScheduling
from task import Task

def test_add_job_offset_0():
    task = Task(0, 3, 5, 5)
    task_scheduling = TaskScheduling(task)
    assert not task_scheduling.jobs
    task_scheduling.add_job(0)
    assert task_scheduling.jobs
    #test if job created is well initialized
    assert task_scheduling.jobs[-1].offset == 0
    assert task_scheduling.jobs[-1].cpu_need == 3
    assert task_scheduling.jobs[-1].absolute_deadline == 5
    assert task_scheduling.jobs[-1].cpu_units == 0
    assert not task_scheduling.jobs[-1].job_executions

def test_add_job_offset_2():
    task = Task(2, 3, 5, 5)
    task_scheduling = TaskScheduling(task)
    assert not task_scheduling.jobs
    task_scheduling.add_job(2)
    assert task_scheduling.jobs
    #test if job created is well initialized
    assert task_scheduling.jobs[-1].offset == 2
    assert task_scheduling.jobs[-1].cpu_need == 3
    assert task_scheduling.jobs[-1].absolute_deadline == 7
    assert task_scheduling.jobs[-1].cpu_units == 0
    assert not task_scheduling.jobs[-1].job_executions

def test_add_job_deadline_not_same_as_period():
    task = Task(2, 3, 10, 5)
    task_scheduling = TaskScheduling(task)
    assert not task_scheduling.jobs
    task_scheduling.add_job(2)
    assert task_scheduling.jobs
    #test if job created is well initialized
    assert task_scheduling.jobs[-1].offset == 2
    assert task_scheduling.jobs[-1].cpu_need == 3
    assert task_scheduling.jobs[-1].absolute_deadline == 12
    assert task_scheduling.jobs[-1].cpu_units == 0
    assert not task_scheduling.jobs[-1].job_executions


def test_is_last_job_finished_one_job_one_exe():
    task = Task(wcet=2, deadline=2, period=3)
    task_scheduling=TaskScheduling(task)
    assert task_scheduling.is_last_job_finished()
    task_scheduling.add_job(instant=0)
    assert not task_scheduling.is_last_job_finished()
    task_scheduling.jobs[-1].start_new_job_execution(0)
    task_scheduling.jobs[-1].add_cpu_unit()
    assert task_scheduling.is_last_job_finished()

def test_is_last_job_finished_one_job_two_exe():
    task = Task(wcet=2, deadline=2, period=3)
    task_scheduling=TaskScheduling(task)

    assert task_scheduling.is_last_job_finished()
    task_scheduling.add_job(instant=0)
    assert not task_scheduling.is_last_job_finished()

    task_scheduling.jobs[-1].start_new_job_execution(0)
    assert not task_scheduling.is_last_job_finished()
    
    #preemption
    task_scheduling.jobs[-1].start_new_job_execution(2)
    assert task_scheduling.is_last_job_finished()
    # TODO divide in two tests
    task_scheduling.add_job(5)
    assert not task_scheduling.is_last_job_finished()
    task_scheduling.jobs[-1].start_new_job_execution(5)
    task_scheduling.jobs[-1].add_cpu_unit(1)
    assert task_scheduling.is_last_job_finished()





def test_is_release_time_offset_0():
    task = Task(0, 3, 5, 5)
    task_scheduling=TaskScheduling(task)
    assert task_scheduling.is_release_time(0)
    assert not task_scheduling.is_release_time(1)
    task_scheduling.add_job(0)
    assert task_scheduling.is_release_time(0)
    assert task_scheduling.is_release_time(5)
    assert not task_scheduling.is_release_time(6)
    assert task_scheduling.is_release_time(10)
    assert not task_scheduling.is_release_time(11)

def test_is_release_time_offset_2():
    task = Task(2, 3, 5, 5)
    task_scheduling=TaskScheduling(task)
    assert not task_scheduling.is_release_time(0)
    assert not task_scheduling.is_release_time(1)
    assert task_scheduling.is_release_time(2)
    for i in range(3, 7):
        assert not task_scheduling.is_release_time(i)
    assert task_scheduling.is_release_time(7)

    task_scheduling.add_job(2)
    assert task_scheduling.is_release_time(2)
    assert task_scheduling.is_release_time(7)
    assert task_scheduling.is_release_time(12)
    assert task_scheduling.is_release_time(17)






def generate_task_course_example():
    t1 = Task(0, 3, 5, 5)
    t2 = Task(0, 2, 10, 10)
    t3 = Task(0, 4, 20, 20)

    return [t1, t2, t3]

def generate_task_course_example():
    t1 = Task(2, 3 , 5 , 5)