import matplotlib.pyplot as plt
import numpy as np
from matplotlib.cm import get_cmap
from matplotlib.ticker import MultipleLocator
from task import Task
#from ftp_rm_scheduling import get_ftp_rm_schedule

# TODO clean this ugly code
# TODO use a schedules object
def gantt_of_schedule(schedules, time_limit , filename="gant_diagram.png"):
    """Save a png of the gant diagram of the given schedule

    Args:
        schedules (array): the schedule to draw
        time_limit ([type]): the time limit of the graph
    """
    TASKS_HEIGHT = 1
    # Declaring a figure "gnt"
    fig, gnt = plt.subplots()
    # Setting Y-axis limits
    gnt.set_ylim(0, len(schedules)*2 )
    #TASKS_HEIGHT /= 1.2
 
    # Setting X-axis limits
    gnt.set_xlim(0, time_limit)
    name = "tab10"
    cmap = get_cmap(name)  # type: matplotlib.colors.ListedColormap
    colors = cmap.colors  # type: list
    gnt.set_prop_cycle(color=colors)
    # Setting labels for x-axis and y-axis
    gnt.set_xlabel('CPU Moments')
    gnt.set_ylabel('Tasks')
    
    #should update
    ticks = []
    labels = []
    for i in range(len(schedules)):
        ticks.append(((i)*2))
        labels.append(i+1)
    # Setting ticks on y-axis
    #major_ticks = np.arange(0, time_limit, 5)
    minor_ticks = np.arange(0, time_limit, 1)
    #gnt.set_xticks(minor_ticks, )
    #gnt.set_xticks(major_ticks)
    #gnt.tick_params(which='minor', length=1)
    gnt.xaxis.set_minor_locator(MultipleLocator(1))

    # Initialize minor ticks
    #gnt.minorticks_on()

# Now minor ticks exist and are turned on for both axes

# Turn off x-axis minor ticks
    #gnt.yaxis.set_tick_params(which='minor', bottom=False)
    
    gnt.set_yticks(ticks)
    # Labelling tickes of y-axis
    gnt.set_yticklabels(labels)
    # Setting graph attribute
    gnt.grid(True)
    #plt.style.use('classic')
    #after
    for i, schedule in enumerate(reversed(schedules)):
        print(schedule)
        gnt.broken_barh(schedule, (i*2,  1), facecolors=colors[i])

    #before
    """
    for i, schedule in enumerate(reversed(schedules)):
        #for j, task in enumerate(schedule):
        T = []
        for j, job in enumerate(schedule):
            tup = (job.start, job.nb_cpu_units)
            T.append(tup)
        gnt.broken_barh(T, (i*2,  1), facecolors=colors[i])
    """
    plt.savefig(filename)
    return plt
    
#gantt_of_schedule(schedules, 25)
    
from scheduling import get_first_course_example_schedule
from scheduling import get_scheduling_course_exemple
# TODO doc
def test_drawing_with_two_tasks_same_period():
    t1 = Task(0, 3, 5, 5)
    t2 = Task(0, 2, 5, 5)
    tasks = [t1, t2]
    schedules = get_ftp_rm_schedule(tasks)
    gantt_of_schedule(schedules,6, 'simple_schedules.png')
# TODO doc
def test_drawing_with_first_course_example():
    tasks = get_first_course_example_schedule()
    schedules = get_ftp_rm_schedule(tasks)
    gantt_of_schedule(schedules, 26, "first_course_example.png")
def ultimate_test():
    schedules = get_scheduling_course_exemple()
    arr = schedules.get_array_of_schedules()
    gantt_of_schedule(arr, 26, "C:\\Users\\keser\\Desktop\\first_course_example2.png")


ultimate_test()