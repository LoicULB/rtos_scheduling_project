from scheduling import JobExecution

def test_default_constructor():
    job_exe = JobExecution()
    assert job_exe.start == 0
    assert job_exe.cpu_units==1

