"""
This is the main file used to launch the program from the command line
"""

from os import sys

from scheduling import SystemScheduling
from scheduling import get_lcm_tasks_period
from scheduling_diagram import gantt_of_schedule
from audsley import audsley_recur
from audsley import make_all_tasks_soft
from task import Task
from exceptions import DeadlineMissedException


def parse_input_file(file_path):
    """
    Parse the input file given by the user as argument
    :return: the list containing all the Task objects
    """
    with open(file_path) as input_file:
        lines = input_file.readlines()
        task_set = []

        for line in lines:
            task = line.strip().split(" ")
            task = [int(x) for x in task]  # We convert the string values into integers
            task_set.append(Task(*task))

    return task_set

def write_output_file(task_set):
    """
    Create the file audsley.txt which contains the FTP assignment that has been found
    Note: the file will be created at the project root
    """

    with open("audsley.txt", 'w') as output_file:
       for task in task_set:
           output_file.write(f"{task.offset} {task.wcet} {task.deadline} {task.period} \n")


if __name__ == "__main__":

    if len(sys.argv) < 3:
        sys.exit("The number of arguments is incorrect. Usage : ./project audsley|scheduler <task_file>")

    if sys.argv[1] == "scheduler":
        task_set = parse_input_file(sys.argv[2])
        #make_all_tasks_soft(task_set)
        scheduling = SystemScheduling(task_set)
        
        try:
            scheduling.execute_FTP_schedule()
        except DeadlineMissedException:
            pass
        
        gantt_of_schedule(scheduling, get_lcm_tasks_period(task_set))

    elif sys.argv[1] == "audsley":
        task_set = parse_input_file(sys.argv[2])
        audsley_recur(task_set, task_set.copy())
        write_output_file(task_set)

    else:
        sys.exit("The second argument must be either 'scheduler' or 'audsley'.")