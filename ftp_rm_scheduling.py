
from task_generator import generate_random_tasks
from numpy import lcm
from task import Task
from scheduling import Job
def ftp_rm_schedule(tasks):
    tasks.sort(key=lambda x: x.period)

def get_lcm_tasks_period(tasks):
    periods = []
    for task in tasks:
        periods.append(task.period)
    return (lcm.reduce(periods))
#tasks is already sorted
def is_job_ended(job,task):
    return job.nb_cpu_unit >= task.wcet
def is_job_waiting(job, task, instant, jobs_of_same_task):
    nb_job = len(jobs_of_same_task)
    v = instant / nb_job
    w = nb
    return job.start 
def get_ftp_rm_schedule(tasks):
    lcm_tasks = get_lcm_tasks_period(tasks)
    
    #for i in range(len(tasks)):
    schedules =  []
    last_task_index =0
    for i in range(lcm_tasks):

        for task_index in range(len(tasks)):
            if (schedules[task_index]["nb_cpu_units"] < tasks[task_index].wcet):
                if (task_index != last_task_index):
                    schedules[task_index].append({"start" : i, "nb_cpu_units" : 1})
                else: 
                    schedules[task_index][-1]["nb_cpu_units"] +=1

    
    return schedules


def test_lcm_tasks_periods():
    t1 = Task(0, 10 , 80, 80)
    t2 = Task(0, 10 , 10, 10)
    t3 = Task(0, 10 , 3, 3)
    tasks = [t1, t2, t3]
    print(get_lcm_tasks_period(tasks))


def test_ftp_rm_schedule():
    tasks = generate_random_tasks(5)
    for task in tasks:
        print(task)

    print()
    ftp_rm_schedule(tasks)
    for task in tasks:
        print(task)

test_lcm_tasks_periods()