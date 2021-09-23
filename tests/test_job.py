from scheduling import Job

def test_default_constructor():
    job = Job()
    assert job.job_executions==[]
    assert job.start == 0
    assert job.deadline == 0
    assert job.cpu_units == 0
    assert job.cpu_need == 0

def test_start_new_job_execution():
    pass
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


