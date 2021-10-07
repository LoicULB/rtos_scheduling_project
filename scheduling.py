from dataclasses import dataclass, field
from numpy import lcm
from typing import List
from exceptions import DeadlineMissedException
from task import Task
from task_sets import *
from job import *


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




@dataclass
class TaskScheduling:
    task: Task = Task()
    jobs: List[Job] = field(default_factory=list)

    """
    def get_deadline_of_next_job(self, start):
        range_period_start = (start-self.task.offset)//self.task.period
        next_deadline =(range_period_start+1)*self.task.deadline + self.task.offset
        return next_deadline
    """

    def is_release_time(self, instant: int):
        """Checks whether or not a new job is ready to be released

        Args:
            instant (int): instant where we will check whether or not a new job is ready to be released

        Returns:
            [type]: [description]
        """
        return (instant - (self.task.offset)) % self.task.period == 0

    def add_job(self, instant):
        """Add a job to the TaskScheduling

        Args:
            start (int): the time at which the job will start
        """
        # job_exe = [JobExecution(start=inst)]
        job = Job(release_time=instant, cpu_need=self.task.wcet, absolute_deadline=instant + self.task.deadline)
        self.jobs.append(job)

    def is_last_job_finished(self):
        if not self.jobs: return True
        return self.jobs[-1].is_finished()

    """
    def is_last_job_interrupted(self, instant):
        if not self.jobs:
            return False
        last_job = self.jobs[-1]
        last_job[-1]
        if self.is_last_job_finished() a
    """

    def run_task(self, instant, is_same_task_index):
        if not self.jobs:
            return False
        if not self.is_last_job_finished() and not self.is_deadline_missed(instant):
            if is_same_task_index:
                # TODO make a def 
                if not self.jobs[-1].job_executions :
                    # TODO make a func
                    self.jobs[-1].start_new_job_execution(instant)
                else: 

                    self.jobs[-1].add_cpu_unit()
            else:
                self.jobs[-1].start_new_job_execution(instant)

            return True
        return False

    def get_scheduling_array(self):
        arr = []
        for job in self.jobs:
            job_arr_tuple = job.get_as_array_of_jobs_exe()
            arr += job_arr_tuple
        return arr

    def is_deadline_missed(self, instant: int):
        if not self.jobs:
            return False
        return self.jobs[-1].is_deadline_missed(instant)

    # TODO write is deadline missed


class SystemScheduling:
    """
    Class representing a a bounded scheduling of a set of tasks
    """

    def __init__(self, tasks):
        sched = []
        self.tasks = tasks
        for task in tasks:
            sched.append(TaskScheduling(task))
        self.schedules = sched
        self.feasibility_interval = self.get_feasibility_interval()

    def get_maximum_offset(self):
        return max(self.tasks, key=lambda task: task.offset).offset

    def get_feasibility_interval(self):
        return self.get_maximum_offset() + (2 * get_lcm_tasks_period(self.tasks))

    def execute_FTP_schedule(self):
        # TODO change the time limit to the instructions
        
        #for i in range(len(tasks)):
        """
        schedules =  []
        for task in self.tasks:
            schedules.append(TaskScheduling(task))
        """
        schedules = self.schedules
        last_task_index = 0
        for i in range(self.feasibility_interval):
            is_task_run = False
            for task_index in range(len(self.tasks)):
                task_scheduling = schedules[task_index]

                if (task_scheduling.task.is_hard):
                    if (task_scheduling.is_deadline_missed(i)):
                        raise DeadlineMissedException(
                            f"A deadline has been missed at instant {i} for task {task_index} ")

                if (task_scheduling.is_release_time(i)):
                    task_scheduling.add_job(i)
                if not is_task_run:
                    is_task_run = task_scheduling.run_task(i, task_index == last_task_index)
                    if (is_task_run):
                        # print("index tâche : ", task_index)
                        last_task_index = task_index

        self.schedules = schedules
        return schedules

    def get_array_of_schedules(self):
        arr = []
        for schedule in self.schedules:
            arr.append(schedule.get_scheduling_array())
        return arr

    def get_nb_deadline_misses(self):
        cpt = 0
        for schedule in self.schedules:
            for job in schedule.jobs:
                if job.is_deadline_missed(50):
                    cpt += 1
        return cpt

    def __str__(self) -> str:
        string = ""
        arr = self.get_array_of_schedules()
        for schedule in arr:
            string += str(schedule)
            string += "\n"
        return string

    # def print_schedules_in_line(self):





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

#test_scheduling_course_exemple()
