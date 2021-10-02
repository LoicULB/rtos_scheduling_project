from task import Task
from scheduling import SystemScheduling
from exceptions import DeadlineMissedException
def is_task_lowest_priority_viable(task_index : int, tasks : List[Task] ):
    """Checks if the tasks of the pointed by the task index in the tasks list is lower priority viable

    Args:
        task_index (int): the task index to check
        tasks (List[Task]): the tasks set (the set is supposed to be soft tasks)
    Return:
        boolean : true if the task is lowest priority viable
    """
    new_tasks_set= tasks.copy()
    #assign the lowest priority to the task
    task =new_tasks_set.pop(task_index)
    task.is_hard=True
    new_tasks_set.append(task)

    #it justs works
    sys_sched= SystemScheduling(new_tasks_set)
    try :
        sys_sched.execute_FTP_schedule()
        return True
    except DeadlineMissedException:
        return False

def make_all_tasks_soft(tasks):
    for task in tasks:
        task.is_hard=False
def audlsey(tasks: List[Task], leftover_tasks : List[Task]):
    """Find a FTP schedulable priority assignement for task set "tasks".

    Args:
        tasks (List[Task]): tasks set of which we will assign a FTP schedulable priority ordering.
        This list will be sorted at the end of the algorithm.
    """
    if(tasks):
        for i, task in enumerate(tasks):
            if is_task_lowest_priority_viable(i,tasks):
                audlsey(tasks, tasks.copy().remove(i))
                tasks.pop(i)
                tasks.append(task)
                 
                
                #break
        return False
    return False   

