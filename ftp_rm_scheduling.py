
from task_generator import generate_random_tasks
from numpy import lcm
from task import Task
from scheduling import Job
import numpy as np

def ftp_rm_schedule(tasks):
    """Sort the tasks according to their period
    (RM Monotonic assignement)

    Args:
        tasks (list): a list of tasks
    """
    tasks.sort(key=lambda x: x.period)


def get_lcm_tasks_period(tasks):
    """Get the least common multiple of the tasks periods

    Args:
        tasks (list): the list of tasks

    Returns:
        int: the least common multiple of the tasks periods
    """
    periods = []
    for task in tasks:
        periods.append(task.period)
    return (lcm.reduce(periods))
#tasks is already sorted
# TODO add to JOB class
def is_job_ended(job,task):
    """Checks wheter or not the job has consume all of it's computation time

    Args:
        job (Job): the job
        task (Task): the task of the job

    Returns:
        boolean: true if the job has ended
    """
    return job.nb_cpu_units >= task.wcet

# TODO documentation
def is_job_waiting(job, task, instant):

    range_period_start = job.start//task.period
    range_period_instant = instant // task.period
    return  not (range_period_start == range_period_instant)
    #return job.start


def get_ftp_rm_schedule(tasks):
    """Compute the scheduling a the given list of tasks

    Args:
        tasks (list): a priority sorted list of tasks to schedule

    Returns:
        list of list: the scheduling of the tasks input
    """
    lcm_tasks = get_lcm_tasks_period(tasks)
    
    #for i in range(len(tasks)):
    schedules =  []
    for i in range(len(tasks)):
        schedules.append([])
    last_task_index =0
    for i in range(lcm_tasks):
        #print(f"i is {i}")
        for task_index in range(len(tasks)):
            #print(f"task : {task_index} job { str(schedules[task_index][-1]) if schedules[task_index] else 0 }")
            if (not schedules[task_index]):
                schedules[task_index].append(Job(i,1))
                last_task_index = task_index
                break
            job = schedules[task_index][-1]

            bool1 = task_index != last_task_index
            bool2 = is_job_waiting(job,tasks[task_index], i)
            if(bool1 and bool2):

                #if (job.nb_cpu_units < tasks[task_index].wcet):
                if (task_index != last_task_index ):
                    schedules[task_index].append(Job(i, 1))
                elif (job.nb_cpu_units < tasks[task_index].wcet): 
                    job.nb_cpu_units +=1
                last_task_index = task_index
                break
            if(task_index == last_task_index and not is_job_ended(job, tasks[task_index])):
            #the problem we have here is that we do not handle the preemption
            #a preemption can occurs many times
            #if(task_index == last_task_index and not is_job_ended(job, tasks[task_index])):
                job.nb_cpu_units +=1
                last_task_index = task_index
                break
    return schedules

# TODO put to test
def test_lcm_tasks_periods():
    t1 = Task(0, 10 , 80, 80)
    t2 = Task(0, 10 , 10, 10)
    t3 = Task(0, 10 , 3, 3)
    tasks = [t1, t2, t3]
    print(get_lcm_tasks_period(tasks))

# TODO put to tests
def test_ftp_rm_schedule():
    tasks = generate_random_tasks(5)
    for task in tasks:
        print(task)

    print()
    ftp_rm_schedule(tasks)
    for task in tasks:
        print(task)

def get_first_example_ftp_rm_schedule():
    t1 = Task(0, 4, 20, 20)
    t2 = Task(0, 2, 10, 10)
    t3 = Task(0, 3, 5, 5)
    tasks = [t1, t2, t3]
    ftp_rm_schedule(tasks)

    return get_ftp_rm_schedule(tasks)

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