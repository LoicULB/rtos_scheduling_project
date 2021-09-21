
from task_generator import generate_random_tasks
from numpy import lcm
from task import Task
from scheduling import Job
import numpy as np
def ftp_rm_schedule(tasks):
    tasks.sort(key=lambda x: x.period)

def get_lcm_tasks_period(tasks):
    periods = []
    for task in tasks:
        periods.append(task.period)
    return (lcm.reduce(periods))
#tasks is already sorted
def is_job_ended(job,task):
    return job.nb_cpu_units >= task.wcet
def is_job_waiting(job, task, instant):

    range_period_start = job.start/task.period
    range_period_instant = instant / task.period
    return  not (range_period_instant == range_period_instant)
    #return job.start 
def get_ftp_rm_schedule(tasks):
    lcm_tasks = get_lcm_tasks_period(tasks)
    
    #for i in range(len(tasks)):
    schedules =  []
    for i in range(len(tasks)):
        schedules.append([])
    last_task_index =0
    for i in range(lcm_tasks):
        print(f"i is {i}")
        for task_index in range(len(tasks)):
            if (not schedules[task_index]):
                schedules[task_index].append(Job(i,1))
                last_task_index = task_index
                break
            job = schedules[task_index][-1]
            if(task_index != last_task_index and is_job_waiting(job,tasks[task_index], i)):

                if (job.nb_cpu_units < tasks[task_index].wcet):
                    if (task_index != last_task_index):
                        schedules[task_index].append(Job(i, 1))
                    else: 
                        job.nb_cpu_units +=1
                    last_task_index = task_index
                    break
            if(task_index == last_task_index and not is_job_ended(job, tasks[task_index])):
                job.nb_cpu_units +=1
                last_task_index = task_index
                break
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

def test_ftp_rm_schedule_full():
    t1 = Task(0, 4 , 20, 20)
    t2 = Task(0, 2 , 10, 10)
    t3 = Task(0, 3 , 5, 5)
    tasks = [t1, t2, t3]
    ftp_rm_schedule(tasks)
    for task in tasks:
        print(task)
    schedules = get_ftp_rm_schedule(tasks)
    for index, schedule in enumerate(schedules):
        print("Task : "+str(index))
        for job in schedule:
            print(str(job))
        #print(str(schedule))
#test_lcm_tasks_periods()
test_ftp_rm_schedule_full()