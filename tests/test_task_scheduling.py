from scheduling import TaskScheduling
from task import Task

def test_add_job_offset_0():
    task = Task(0, 3, 5, 5)
    task_scheduling = TaskScheduling(task)
    assert not task_scheduling.jobs
    task_scheduling.add_job(0)
    assert task_scheduling.jobs
    #test if job created is well initialized
    assert task_scheduling.jobs[-1].release_time == 0
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
    assert task_scheduling.jobs[-1].release_time == 2
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
    assert task_scheduling.jobs[-1].release_time == 2
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


def test_run_task():
    task = Task(0, 3, 5, 5)
    task_scheduling=TaskScheduling(task)
    is_same_task_index = True
    instant = 0
    task_scheduling.add_job(0)
    task_has_been_run =task_scheduling.run_task(instant, is_same_task_index)
    assert task_has_been_run
    assert task_scheduling.jobs[-1].job_executions
    assert task_scheduling.jobs[-1].cpu_units==1
    assert task_scheduling.jobs[-1].job_executions[-1].cpu_units==1

    task_has_been_run = task_scheduling.run_task(1,True)
    assert task_has_been_run
    assert len(task_scheduling.jobs[-1].job_executions)==1
    assert task_scheduling.jobs[-1].cpu_units==2
    assert task_scheduling.jobs[-1].job_executions[-1].cpu_units==2

def test_run_task_impossible():
    """Test if when a job is finished and we are before the period, the run is not done
    """
    task = Task(0, 1, 5, 5)
    task_scheduling=TaskScheduling(task)
    is_same_task_index = True
    instant = 0
    task_scheduling.add_job(0)
    task_has_been_run =task_scheduling.run_task(instant, is_same_task_index)
    assert task_has_been_run
    assert task_scheduling.jobs[-1].job_executions
    assert task_scheduling.jobs[-1].cpu_units==1
    assert task_scheduling.jobs[-1].job_executions[-1].cpu_units==1

    task_has_been_run = task_scheduling.run_task(1,True)
    assert not task_has_been_run
    assert len(task_scheduling.jobs[-1].job_executions)==1
    assert task_scheduling.jobs[-1].cpu_units==1
    assert task_scheduling.jobs[-1].job_executions[-1].cpu_units==1

def test_run_task_possible_after_period():
    
    task = Task(0, 1, 2, 2)
    task_scheduling=TaskScheduling(task)
    is_same_task_index = True
    instant = 0
    task_scheduling.add_job(0)
    task_has_been_run =task_scheduling.run_task(instant, is_same_task_index)
    """
    assert task_has_been_run
    assert task_scheduling.jobs[-1].job_executions
    assert task_scheduling.jobs[-1].cpu_units==1
    assert task_scheduling.jobs[-1].job_executions[-1].cpu_units==1
    """
    
    
    task_has_been_run = task_scheduling.run_task(1,True)
    
    assert not task_has_been_run
    """
    assert len(task_scheduling.jobs[-1].job_executions)==1
    assert task_scheduling.jobs[-1].cpu_units==1
    assert task_scheduling.jobs[-1].job_executions[-1].cpu_units==1
    """
    task_scheduling.add_job(2)
    task_has_been_run = task_scheduling.run_task(2,True)
    assert task_has_been_run
    assert task_scheduling.jobs[-1].cpu_units==1
    assert task_scheduling.jobs[-1].job_executions[-1].cpu_units==1


def test_run_task_possible_after_period():
    
    task = Task(0, 2, 2, 2)
    task_scheduling=TaskScheduling(task)
    is_same_task_index = True
    instant = 0
    task_scheduling.add_job(0)
    task_has_been_run =task_scheduling.run_task(instant, is_same_task_index)
   
    task_has_been_run = task_scheduling.run_task(1, False)
    assert task_has_been_run
    assert len(task_scheduling.jobs[-1].job_executions)==2













def generate_task_course_example():
    t1 = Task(0, 3, 5, 5)
    t2 = Task(0, 2, 10, 10)
    t3 = Task(0, 4, 20, 20)

    return [t1, t2, t3]

def generate_task_course_example():
    t1 = Task(2, 3 , 5 , 5)