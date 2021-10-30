"""
This is the main file used to launch the program from the command line
"""

from os import sys

from model.audsley import audsley
from model.exceptions import DeadlineMissedException
from model.scheduling import SystemScheduling
from view.scheduling_diagram import show_scheduling_diagram
from model.task import Task



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

    with open("outputs/audsley/audsley.txt", 'w') as output_file:
        for task in task_set:
            output_file.write(str(task) + "\n")


if __name__ == "__main__":

    if len(sys.argv) < 3:
        sys.exit("The number of arguments is incorrect. Usage : ./project audsley|scheduler <task_file>")

    if sys.argv[1] == "scheduler":
        task_set = parse_input_file(sys.argv[2])
        scheduling = SystemScheduling(task_set)

        try:
            scheduling.execute_FTP_schedule()
            show_scheduling_diagram(scheduling)
        except DeadlineMissedException as dme:
            show_scheduling_diagram(scheduling, str(dme))


    elif sys.argv[1] == "audsley":
        task_set = parse_input_file(sys.argv[2])
        if audsley(task_set):
            write_output_file(task_set)
        else :
            sys.exit("The given task-set has no feasible FTP assignement !")

    else:
        sys.exit("The second argument must be either 'scheduler' or 'audsley'.")
