from task import Task
# TODO complete this class
class JobExecution:
    """Describe a execution block of a job.
     A job have multiple JobExecution when a preemption is done
    
    A JobExecution is characterized by a start time and the number of cpu_units it lasts without preemption
    """


    def __init__(self, start=0, cpu_units=1):
        self.start=start
        self.cpu_units = cpu_units
class Job:
    """Represents a job of a Task Scheduling.

    A Job in the context of Task Scheduling has a list of JobExecution
    (refers to class above)
    A Start Time, when the Job begins it's first execution
    An absolute deadline
    CPU units tells the number of cpu units the job has consumed
    CPU need tells the number of cpu units the job need to consume
    """
    def __init__(self, job_executions=[] ,start=0, deadline=0, cpu_units=0, cpu_need=0):
        self.job_executions = job_executions
        self.start = start
        self.deadline = deadline
        #should make the cpu_units variable private
        self.cpu_units = cpu_units
        self.cpu_need = cpu_need    
    

    def is_finished(self):
        """Tells whether or not the current Job has consume all of it's CPU need (wcet)

        Returns:
            boolean : Yes if the job is finished.
        """
        return self.cpu_units == self.cpu_need

    def add_cpu_unit(self, nb_cpu_units = 1):
        """Add a specific number of cpu_units to the last JobExecution of the Job
        Update the cpu_units counter of the Job at the same time

        Args:
            nb_cpu_units (int, optional): the number of cpu units to add. Defaults to 1.
        """
        #should put execption if there is no job_execution
        #exception if cpu units will become sumperior to cpu need
        self.cpu_units += nb_cpu_units
        self.job_executions[-1].cpu_units+=nb_cpu_units
    
    def start_new_job_execution(self, start):
        """Start a new JobExecution in the Job

        Args:
            start (int): the time at which the JobExecution will start
        """
        if ( not self.job_executions):
            self.start=start
        self.job_executions.append(JobExecution(start=start))
        self.cpu_units += 1

    def get_end_of_job(self):
        """Get the time of end of execution of the job

        Returns:
            int: the time at which the Job ends #the same time a new job can begin
        """
        return self.job_executions[-1].start+self.job_executions[-1].cpu_units

    def get_response_time(self):
        """Get the response time of the job

        Returns:
            int: the response time of the job
        """
        return self.get_end_of_job - self.start


class TaskScheduling:
    
    def __init__(self, task):
        self.jobs = []
        self.task = task
    
    def add_job(self, start):
        """Add a job to the TaskScheduling

        Args:
            start (int): the time at which the job will start
        """
        self.jobs.append(Job(job_executions=[JobExecution()], start=start, cpu_need=self.task.wcet, cpu_units=1))

    def is_task_waiting(self, instant):
        job = self.jobs[-1]
        range_period_start = job.start//self.task.period
        range_period_instant = instant // self.task.period
        return  not (range_period_start == range_period_instant)

    def is_last_job_finished(self):
        if not self.jobs : return True
        return self.jobs[-1].is_finished()
    
    
    def run_task(self, instant):
        if not self.is_last_job_finished():
            self.jobs[-1].add_cpu_unit()
            return True
        if self.is_last_job_finished() and self.is_task_waiting(instant):
            self.add_job(instant)
            return True
        return False
class SystemScheduling:
    """
    Class representing a a bounded scheduling of a set of tasks
    """

    def __init__(self, tasks):
        sched = []
        for task in tasks:
            sched.append(TaskScheduling(task))
        self.schedules= sched
    
    def execute_FTP_schedule(self):
        pass

    def __str__(self) -> str:
        pass
    def print_schedules_in_line(self):

def get_first_course_example_schedule():
    t1 = Task(0, 3, 5, 5)
    t2 = Task(0, 2, 10, 10)
    t3 = Task(0, 4, 20, 20)
    return [t1, t2, t3]


"""
class Job:
    
    def __init__(self, start=0, nb_cpu_units=0):
        self.start = start
        self.nb_cpu_units = nb_cpu_units

    def __str__(self):
        return f"{self.start} {self.nb_cpu_units}"
"""
