
from model.scheduling import SystemScheduling

from model.task import *
from view.scheduling_diagram import show_scheduling_diagram

t1 = Task(50, 20, 50, 50)
t2 = Task(0, 30, 100, 150)
t3 = Task(100, 10, 20, 30)
task_set = [t2, t3, t1]
t2.is_hard = False
t3.is_hard = False
sys_sched = SystemScheduling(task_set)
sys_sched.execute_FTP_schedule()
show_scheduling_diagram(sys_sched)