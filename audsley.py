from exceptions import DeadlineMissedException
from scheduling import SystemScheduling
from task import Task


def is_task_lowest_priority_viable(task_index, tasks):
    """Checks if the tasks of the pointed by the task index in the tasks list is lower priority viable

    Args:
        task_index (int): the task index to check
        tasks (List[Task]): the tasks set (the set is supposed to be soft tasks)
    Return:
        boolean : true if the task is lowest priority viable
    """
    new_tasks_set = tasks.copy()
    # assign the lowest priority to the task
    task = new_tasks_set.pop(task_index)
    task.is_hard = True
    new_tasks_set.append(task)

    # it justs works
    sys_sched = SystemScheduling(new_tasks_set)
    try:
        sys_sched.execute_FTP_schedule()
        task.is_hard = False
        return True
    except DeadlineMissedException:
        task.is_hard = False
        return False


def make_all_tasks_soft(tasks):
    """
    Make all tasks from the task set soft
    :param tasks: the task set
    :return: none
    """
    for task in tasks:
        task.is_hard = False


def audsley_recur(tasks, leftover_tasks):
    """Find a FTP schedulable priority assignement for task set "tasks".

    Args:
        tasks (List[Task]): tasks set of which we will assign a FTP schedulable priority ordering.
        This list will be sorted at the end of the algorithm.
    """
    if (leftover_tasks):
        for i, task in enumerate(leftover_tasks):
            if is_task_lowest_priority_viable(i, leftover_tasks):
                tasks.pop(i)
                tasks.insert(len(leftover_tasks) - 1, task)
                leftover_tasks.pop(i)
                return audsley_recur(tasks, leftover_tasks)
        return False
    return True