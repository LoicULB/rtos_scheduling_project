from test_functions.task_sets import *
from model.scheduling import SystemScheduling


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


def test_scheduling_course_exemple():
    scheduling = get_scheduling_course_first_exemple()
    # scheduling = get_scheduling_course_second_exemple()
    print(str(scheduling))
    print(scheduling.get_nb_deadline_misses())

# get_scheduling_course_exemple()

# test_scheduling_course_exemple()
