from model.exceptions import DeadlineMissedException
from model.scheduling import SystemScheduling


def is_task_lowest_priority_viable(task_index, tasks):
    """Checks if the task pointed by the task index in the tasks list is lower priority viable

    Args:
        task_index (int): the task index to check
        tasks (List[Task]): the tasks set (the set is supposed to be soft tasks)
    Return:
        boolean : true if the task is lowest priority viable
    """
    new_tasks_set = tasks.copy()
    make_all_tasks_soft(new_tasks_set)
    # Assign the lowest priority to the task
    task = new_tasks_set.pop(task_index)
    new_tasks_set.append(task)

    # The lowest priority task must be hard real-time
    task.is_hard = True

    sys_schedule = SystemScheduling(new_tasks_set)
    try:
        sys_schedule.execute_FTP_schedule()
        return True
    except DeadlineMissedException:
        return False


def make_all_tasks_soft(tasks):
    """
    Make all tasks from the task set soft
    :param tasks: the task set
    :return: none
    """
    for task in tasks:
        task.is_hard = False


def make_all_tasks_hard(tasks):
    """
    Make all tasks from the task set hard (used only for tests)
    :param tasks: the task
    :return: nothing
    """
    for task in tasks:
        task.is_hard = True


def audsley(tasks):
    sys_schedules = SystemScheduling(tasks)

    # We don't use Audsley if the given assignent is already schedulable
    try:
        sys_schedules.execute_FTP_schedule()
        return True
    except DeadlineMissedException:
        return audsley_recur(tasks, tasks.copy())


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
