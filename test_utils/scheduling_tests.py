from model.scheduling import SystemScheduling
from test_utils.task_sets import *


def get_scheduling_course_first_exemple():
    tasks = get_first_course_example_schedule()
    scheduling = SystemScheduling(tasks)
    scheduling.execute_FTP_schedule()
    return scheduling


def get_scheduling_course_second_exemple():
    tasks = get_second_example_schedule()
    scheduling = SystemScheduling(tasks)
    scheduling.execute_FTP_schedule()
    return scheduling


def get_scheduling_deadline_missed():
    tasks = get_deadline_missed_example()
    scheduling = SystemScheduling(tasks)
    scheduling.execute_FTP_schedule()
    return scheduling