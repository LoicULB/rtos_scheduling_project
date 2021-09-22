from ..ftp_rm_scheduling import get_ftp_rm_schedule
from task import Task

def test_execution_of_single_task():
    t = Task(0, 3, 5, 5)
    tasks = [t]
    schedules = get_ftp_rm_schedule(tasks)
    assert (len(schedules)) == 1
    
