from typing import List

from numpy import lcm

from model.exceptions import DeadlineMissedException
from model.job import *
from test_utils.task_sets import *


def ftp_rm_schedule(tasks):
    """Sort the tasks according to their period
    (Rate Monotonic assignement)

    Args:
        tasks (list): a list of tasks (task set)
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

    return lcm.reduce(periods)


@dataclass
class TaskScheduling:
    """
    Class used to manage the schedule of a particular task
    task : the task we want to schedule
    jobs : a list containing all the jobs related to the task
    active_jobs : a list containing all the active jobs of the task
    """
    task: Task = Task()
    jobs: List[Job] = field(default_factory=list)
    active_jobs: List[Job] = field(default_factory=list)

    def is_release_time(self, instant: int):
        """Checks whether or not a new job is ready to be released

        Args:
            instant (int): instant where we will check whether or not a new job is ready to be released

        Returns:
            bool: true if the time 'instant' is a release time
        """
        return (instant - self.task.offset) % self.task.period == 0

    def add_job(self, instant: int):
        """Add a job to the TaskScheduling

        Args:
            instant (int): the time at which the job will be released
        """
        job = Job(release_time=instant, cpu_need=self.task.wcet, absolute_deadline=instant + self.task.deadline)
        self.jobs.append(job)
        self.active_jobs.append(job)

    def get_first_active_job(self):
        return self.active_jobs[0]

    def is_first_active_job_finished(self):
        return self.active_jobs[0].is_finished()

    def is_active_jobs_empty(self):
        return not self.active_jobs

    def feed_first_active_job(self):
        """
        Add a CPU unit to the first active job of the task
        If the first active job is finished, we remove it from
        the active jobs list.
        :return: none
        """
        self.get_first_active_job().add_cpu_unit()
        if self.is_first_active_job_finished():
            self.active_jobs.pop(0)

    def run_task(self, instant, is_same_task_index):
        """
        Run the task at instant 'instant' if possible
        (Add a cpu unit at that instant if possible)
        :param instant: the time at which we want to run the task
        :param is_same_task_index: boolean used to know if, at instant
        instant-1, the same task was fed by the CPU
        :return: true if we manage to feed the task, false otherwise
        """
        if not self.jobs:
            return False
        if not self.is_active_jobs_empty() and not self.is_deadline_missed(instant):
            if is_same_task_index:
                # TODO make a def
                if not self.get_first_active_job().job_executions:
                    # TODO make a func
                    self.get_first_active_job().start_new_job_execution(instant)
                    if self.is_first_active_job_finished():
                        self.active_jobs.pop(0)
                else:

                    self.feed_first_active_job()
            else:
                self.get_first_active_job().start_new_job_execution(instant)
                if self.is_first_active_job_finished():
                    self.active_jobs.pop(0)

            return True
        return False

    def get_scheduling_array(self):
        """
        :return: an array containing all the jobs executions tuples from all the jobs
        """
        arr = []
        for job in self.jobs:
            job_arr_tuple = job.get_as_array_of_jobs_exe()
            arr += job_arr_tuple
        return arr

    def is_deadline_missed(self, instant: int):
        """
        Check if a deadline has been missed for the considered task
        :param instant: the moment at which we want to know if a deadline has been missed
        :return: true if a deadline has been missed for the task, false otherwise
        """
        if not self.active_jobs:
            return False
        for job in self.active_jobs:
            if job.is_deadline_missed(instant):
                return True
        return False


class SystemScheduling:
    """
    Class representing a bounded scheduling of a task set
    schedules : list containing all the task schedules
    tasks : list containing all the tasks to schedule
    feasibility_interval : the feasibility interval of the system scheduling
    """

    def __init__(self, tasks):
        sched = []
        self.tasks = tasks
        for task in tasks:
            sched.append(TaskScheduling(task))
        self.schedules = sched
        self.feasibility_interval = self.get_feasibility_interval()

    def get_maximum_offset(self):
        """
        :return: the maximum offset off all the tasks of the task set
        """
        return max(self.tasks, key=lambda task: task.offset).offset

    def get_feasibility_interval(self):
        """
        :return: the feasibility interval of this task set scheduling
        """
        return self.get_maximum_offset() + (2 * get_lcm_tasks_period(self.tasks))

    def execute_FTP_schedule(self):
        """
        Execute the FTP scheduling algorithm on the task set
        Note: the task set is ordered by decreasing priorities
        :return: the list of all the task scheduling computed
        :raise DeadlineMissedException: raised when a deadline is missed
        only if we're considering a hard real-time task
        """
        schedules = self.schedules
        last_task_index = 0
        for i in range(self.feasibility_interval):
            is_task_run = False
            for task_index in range(len(self.tasks)):
                task_scheduling = schedules[task_index]

                if task_scheduling.task.is_hard:
                    if task_scheduling.is_deadline_missed(i):
                        raise DeadlineMissedException(
                            f"A deadline has been missed at instant {i} for task {task_index} ")

                if task_scheduling.is_release_time(i):
                    task_scheduling.add_job(i)
                if not is_task_run:
                    is_task_run = task_scheduling.run_task(i, task_index == last_task_index)
                    if is_task_run:
                        last_task_index = task_index

        self.schedules = schedules
        return schedules

    def get_array_of_schedules(self):
        """
        Method used to compute the string representation of the scheduling
        :return: the array containing arrays containing job executions tuples
        """
        arr = []
        for schedule in self.schedules:
            arr.append(schedule.get_scheduling_array())
        return arr

    def __str__(self) -> str:
        string = ""
        arr = self.get_array_of_schedules()
        for schedule in arr:
            string += str(schedule)
            string += "\n"
        return string
