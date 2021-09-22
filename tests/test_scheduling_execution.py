from ftp_rm_scheduling import get_ftp_rm_schedule
from task import Task
from scheduling import Job

def test_execution_of_single_task():
    t = Task(0, 3, 5, 5)
    tasks = [t]
    schedules = get_ftp_rm_schedule(tasks)
    print(schedules[0])
    
    assert (len(schedules)) == 1
    assert len(schedules[0])==1
    job = schedules[0][0]
    assert job.start == 0
    assert job.nb_cpu_units == 3

def test_execution_of_two_tasks_with_same_periods():
    t1 = Task(0, 3, 5, 5)
    t2 = Task(0, 2, 5, 5)
    tasks = [t1, t2]
    schedules = get_ftp_rm_schedule(tasks)
    assert(len(schedules)==2)
    assert(len(schedules[0])==1)
    assert(len(schedules[1])==1)
    job_t1 = schedules[0][0]
    job_t2 = schedules[1][0]
    assert job_t1.start == 0
    assert job_t1.nb_cpu_units == 3
    assert job_t2.start == 3
    assert job_t2.nb_cpu_units == 2

def test_execution_of_two_tasks():
    t1 = Task(0, 3, 5, 5)
    t2 = Task(0, 2, 10, 10)
    tasks = [t1, t2]
    schedules = get_ftp_rm_schedule(tasks)
    assert(len(schedules)==2)
    assert(len(schedules[0])==2)
    assert(len(schedules[1])==1)
    job1_t1 = schedules[0][0]
    job1_t2 = schedules[1][0]
    assert job1_t1.start == 0
    assert job1_t1.nb_cpu_units == 3
    assert job1_t2.start == 3
    assert job1_t2.nb_cpu_units == 2
    #job 2
    job2_t1 = schedules[0][1]
    
    assert job2_t1.start == 5
    assert job2_t1.nb_cpu_units == 3

def test_execution_of_three_tasks_with_same_periods():
    t1 = Task(0, 3, 5, 5)
    t2 = Task(0, 1, 5, 5)
    t3 = Task(0, 1, 5, 5)
    tasks = [t1, t2, t3]
    schedules = get_ftp_rm_schedule(tasks)
    assert(len(schedules)==3)
    assert(len(schedules[0])==1)
    assert(len(schedules[1])==1)
    assert(len(schedules[2])==1)
    job_t1 = schedules[0][0]
    job_t2 = schedules[1][0]
    job_t3 = schedules[2][0]
    assert job_t1.start == 0
    assert job_t1.nb_cpu_units == 3
    assert job_t2.start == 3
    assert job_t2.nb_cpu_units == 1
    assert job_t3.start == 4
    assert job_t3.nb_cpu_units == 1  

def test_execution_of_first_course_exemple():
    t1 = Task(0, 3, 5, 5)
    t2 = Task(0, 2, 10, 10)
    t3 = Task(0, 4, 20, 20)
    tasks = [t1, t2, t3]
    schedules = get_ftp_rm_schedule(tasks)
    assert(len(schedules)==3)
    assert(len(schedules[0])==4)
    assert(len(schedules[1])==2)
    assert(len(schedules[2])==2)

    schedule_t1 = [Job(0,3), Job(5,3), Job(10,3), Job(15,3)]
    schedule_t2 = [Job(3,2), Job(13,2)]
    schedule_t3 = [Job(8,2), Job(18,2)]
    assert schedules[0] == schedule_t1
    assert schedules[1] == schedule_t2
    assert schedules[2] == schedule_t3
      
    
