"""
This is the main file used to launch the program from the command line
"""

from os import sys

from scheduling import SystemScheduling
from scheduling_diagram import gantt_of_schedule
from task import Task


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


if __name__ == "__main__":

    if len(sys.argv) < 3:
        sys.exit("The number of arguments is incorrect. Usage : ./project audsley|scheduler <task_file>")

    if sys.argv[1] == "scheduler":
        task_set = parse_input_file(sys.argv[2])
        scheduling = SystemScheduling(task_set)
        scheduling.execute_FTP_schedule()

        array = scheduling.get_array_of_schedules()
        gantt_of_schedule(array, scheduling.get_feasibility_interval())


    elif sys.argv[1] == "audsley":
        pass
