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
        self.cpu_units += 1
        self.job_executions[-1].cpu_units+=nb_cpu_units
    
    def start_new_job_execution(self, start):
        """Start a new JobExecution in the Job

        Args:
            start (int): the time at which the JobExecution will start
        """
        self.job_executions.append(JobExecution(start=start))

    def get_end_of_job(self):
        """Get the time of end of execution of the job

        Returns:
            int: the time at which the Job ends
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
        self.jobs.append(Job(start=start, cpu_need=self.task.wcet))
class SystemScheduling:
    """
    Class representing a a bounded scheduling of a set of tasks
    """

    def __init__(self, array=[]):
        self.scheduling=array

def get_first_course_example_schedule():
    t1 = Task(0, 3, 5, 5)
    t2 = Task(0, 2, 10, 10)
    t3 = Task(0, 4, 20, 20)
    return [t1, t2, t3]


"""
class Job:
    """
    """
    Class representing a job

    A job is defined by a start (offset) and the number of cpu units it has received yet
    """
    """
    def __init__(self, start=0, nb_cpu_units=0):
        self.start = start
        self.nb_cpu_units = nb_cpu_units

    def __str__(self):
        return f"{self.start} {self.nb_cpu_units}"
"""