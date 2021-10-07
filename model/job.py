from dataclasses import dataclass, field


@dataclass
class JobExecution:
    """Describe a execution block of a job.
     A job have multiple JobExecution when a preemption is done
     A JobExecution is characterized by a start time and the number of cpu_units it lasts without preemption
    """

    start: int = 0
    cpu_units: int = 1

    def get_as_tuple(self):
        return self.start, self.cpu_units

    def __str__(self) -> str:
        return f"( {self.start} , {self.cpu_units} )"


@dataclass
class Job:
    """Represents a job of a Task Scheduling.

    A Job in the context of Task Scheduling has a list of JobExecution
    (refers to class above)
    A release time, when the Job is released
    An absolute deadline
    CPU units tells the number of cpu units the job has consumed
    CPU need tells the number of cpu units the job need to consume
    """
    release_time: int = 0
    absolute_deadline: int = 0
    cpu_units: int = 0
    cpu_need: int = 0
    job_executions: list[int] = field(default_factory=list)

    def is_finished(self):
        """Tells whether or not the current Job has consume all of it's CPU need (wcet)

        Returns:
            boolean : Yes if the job is finished.
        """
        if self.cpu_units > self.cpu_need:
            raise Exception("Jobs cannot have more cpu units than it needs")
        return self.cpu_units == self.cpu_need

    def add_cpu_unit(self, nb_cpu_units=1):
        """Add a specific number of cpu_units to the last JobExecution of the Job
        Update the cpu_units counter of the Job at the same time

        Args:
            nb_cpu_units (int, optional): the number of cpu units to add. Defaults to 1.
        """

        if not self.job_executions:
            raise Exception("Impossible to add a cpu unit to empty job execution")

        self.cpu_units += nb_cpu_units
        self.job_executions[-1].cpu_units += nb_cpu_units

    def start_new_job_execution(self, start: int):
        """Start a new JobExecution in the Job

        Args:
            start (int): the time at which the JobExecution will start
        """
        self.job_executions.append(JobExecution(start))
        self.cpu_units += 1

    def is_deadline_missed(self, instant: int):
        """
        Check wether or not a deadline has been missed at instant 'instant'
        :param instant: the time at which we want to check if a deadline has been missed
        :return: true if a deadline has been missed, no otherwise
        """
        if instant >= self.absolute_deadline:
            return not self.is_finished()
        return False

    def get_as_array_of_jobs_exe(self):
        """
        :return: an array containing all the job executions as tuples
        """
        arr = []
        for job_exe in self.job_executions:
            arr.append(job_exe.get_as_tuple())
        return arr
