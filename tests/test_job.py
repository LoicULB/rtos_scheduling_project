from scheduling import Job

def test_default_constructor():
    job = Job()
    assert job.job_executions==[]

    assert job.absolute_deadline == 0
    assert job.cpu_units == 0
    assert job.cpu_need == 0

def test_start_new_job_execution():
    job = Job()
    assert not job.job_executions
    job.start_new_job_execution(3)
    assert job.release_time != 3
    assert len(job.job_executions)==1
    assert job.cpu_units==1
    assert job.job_executions[0].cpu_units==1
    assert job.job_executions[0].start == 3

def test_start_2_new_job_execution():
    job = Job()
    
    job.start_new_job_execution(3)
    job.start_new_job_execution(5)
   
    assert len(job.job_executions)==2
    assert job.cpu_units==2
    assert job.job_executions[-1].cpu_units==1
    assert job.job_executions[-1].start == 5

    

def test_add_default_cpu_unit():
    job = Job()
    job.start_new_job_execution(start=0)
    job.add_cpu_unit()
    assert job.cpu_units == 2
    assert job.job_executions[-1].cpu_units == 2

def test_add_given_cpu_unit():
    job = Job()
    job.start_new_job_execution(start=0)
    job.add_cpu_unit(5)
    assert job.cpu_units == 6
    assert job.job_executions[-1].cpu_units == 6


def test_is_finished():
    job = Job(cpu_need=10)
    assert job.is_finished() == False
    job.cpu_units = 10
    assert job.is_finished()

"""
def test_get_end_of_job_with_one_exe():
    job = Job(cpu_need=2)
    job.start_new_job_execution(start=0)
    job.add_cpu_unit()
    assert job.get_end_of_job()==2
"""    
"""
def test_get_end_of_job_with_two_exe():
    job = Job(cpu_need=2)
    job.start_new_job_execution(start=0)
    job.add_cpu_unit()
    assert job.get_end_of_job()==2
    job.start_new_job_execution(start=2)
    job.add_cpu_unit()
    assert job.get_end_of_job()==4
"""

# TODO checks deadline with refactor
def test_is_deadline_missed():
    job = Job(release_time=0, absolute_deadline = 5, cpu_units = 0,cpu_need = 3)
    assert not job.is_deadline_missed(0)
    assert job.is_deadline_missed(6)
    assert not job.is_deadline_missed(4)
    assert job.is_deadline_missed(7)    