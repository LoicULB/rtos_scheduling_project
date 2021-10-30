import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap
from matplotlib.lines import Line2D
from matplotlib.ticker import MultipleLocator

from model.scheduling import SystemScheduling


class SchedulingDiagram:
    """
    Class used to instanciate a Scheduling Gant Diagram
    """

    def __init__(self, sys_schedules: SystemScheduling, limit=-1, colors_class="tab10"):
        self.sys_schedules = sys_schedules
        if limit == -1:
            self.feasibility_interval = sys_schedules.feasibility_interval
        else:
            self.feasibility_interval = limit
        self.fig, self.gnt = plt.subplots()
        self.colors = self.get_list_of_colors(colors_class)

    def get_list_of_colors(self, colors_class: str):
        """
        Get the list of colors that will be used to color each tasks
        :param colors_class: a string identifier of the group of colors to use (see matplotlib doc)
        :return: a list of colors
        """
        name = colors_class
        cmap = get_cmap(name)
        return cmap.colors

    def set_limits_of_graph(self):
        """
        Set the y and x limits of the axis
        :return: none
        """
        self.gnt.set_ylim(0, len(self.sys_schedules.tasks) * 2)
        self.gnt.set_xlim(0, self.feasibility_interval)

    def set_axes_labels(self):
        """
        Set the labels of the x and y axes
        :return: none
        """
        self.gnt.set_xlabel('CPU Moments')
        self.gnt.set_ylabel('Tasks')

    def set_x_ticks(self):
        """
        Set the minor ticks of the x axis
        :return: none
        """
        self.gnt.xaxis.set_minor_locator(MultipleLocator((self.feasibility_interval / 10) + 1))

    def set_y_ticks(self):
        """
        Set the major ticks of the y axis (and labels of the tasks
        :return: none
        """
        tasks_len = len(self.sys_schedules.tasks)
        ticks = []
        labels = []
        for i in range(tasks_len):
            ticks.append((i * 2))
            labels.append(i + 1)
        self.gnt.set_yticks(ticks)
        self.gnt.set_yticklabels(labels)

    def draw_periods_for_task(self, task_index, task, color, len_tasks):
        """
        Draw the vertical lines describing the periods of the tasks
        :param task_index: the index of the task to draw the period
        :param task: the task object to draw the period
        :param color: the color of the task
        :param len_tasks: the number of tasks
        :return: none
        """
        tasks_len = len_tasks
        task_index = (len_tasks - task_index) - 1
        for i in range(task.offset + task.period, self.feasibility_interval + 1, task.period):
            max_i = 1 - ((task_index) * (1 / tasks_len))
            min_i = max_i - 1 / tasks_len
            self.gnt.axvline(x=i, ymin=min_i, ymax=max_i,
                             color=color, linewidth=4, alpha=0.50)

    def draw_deadline_task(self, task_index, task, color, len_tasks):
        """
        Draw the vertical lines describing the deadlines of the tasks
        :param task_index: the index of the task to draw the deadlines
        :param task: the task object to draw the deadlines
        :param color: the color of the task
        :param len_tasks: the number of tasks
        :return: none
        """
        tasks_len = len_tasks
        task_index = (len_tasks - task_index) - 1
        for i in range(task.offset + task.deadline, self.feasibility_interval + 1, task.deadline):
            max_i = 1 - ((task_index) * (1 / tasks_len))
            min_i = max_i - 1 / tasks_len
            self.gnt.axvline(x=i, ymin=min_i, ymax=max_i,
                             color=color, linestyle="--", linewidth=4)

    def draw_job(self, job, color, task_index):
        """
        Draw the job given in parameter in the graph
        :param job: the job to draw
        :param color: the color of the task of the job
        :param task_index: the index of the task of the job
        :return: None
        """
        is_deadline_missed = job.is_deadline_missed(self.feasibility_interval)

        for job_exe in job.job_executions:
            self.draw_job_execution(job_exe, color, task_index, is_deadline_missed)

    def draw_job_execution(self, job_execution, color, task_index, is_deadline_missed):
        """
        Draw the given job execution in the graph
        :param job_execution: the job execution to draw
        :param color: the color of the task of the job execution
        :param task_index: the index of the task
        :param is_deadline_missed: tells if the deadline of this job execution is missed
        :return: None
        """
        job_exe_t = job_execution.get_as_tuple()
        if is_deadline_missed:
            self.gnt.broken_barh([job_exe_t], (task_index * 2, 1), facecolors=color, hatch='/', alpha=0.5,
                                 edgecolor='black',
                                 linewidth=4)
        else:
            self.gnt.broken_barh([job_exe_t], (task_index * 2, 1), facecolors=color, edgecolor='black', linewidth=2)

    def draw_task_scheduling(self, task, color, task_index):
        """
        Draw the scheduling of a given task
        :param task: the task to draw
        :param color: the color of the task
        :param task_index: the index of the task
        :return: None
        """
        for job in task.jobs:
            self.draw_job(job, color, task_index)

    def draw_system_scheduling(self):
        """
        Draw the gantt diagram of the system scheduling
        :return: None
        """
        for i, schedule in enumerate(self.sys_schedules.schedules):
            self.draw_task_scheduling(schedule, self.colors[i], i)
            self.draw_periods_for_task(i, schedule.task, self.colors[i],
                                       len(self.sys_schedules.tasks))
            self.draw_deadline_task(i, schedule.task, self.colors[i], len(self.sys_schedules.tasks))

    def add_legend(self):
        """
        Add the legend of the graph (Deadline and Period)
        :return: None
        """
        handles, labels = plt.gca().get_legend_handles_labels()
        line1 = Line2D([0], [0], label='Deadline', color='blue', linestyle="--", linewidth=2)
        line2 = Line2D([1], [0], label='Period', color='blue', linewidth=2, alpha=0.50)
        handles.extend([line1, line2])
        plt.legend(handles=handles)

    def set_size_fig(self, width=12, height=4):
        """
        Set the size of the figure
        :param width: the width of the figure
        :param height: the height of the figure
        :return: None
        """
        self.fig.set_figwidth(width)
        self.fig.set_figheight(height)

    def add_error(self, error_text: str):
        """
        Add an error message
        :param error_text: the text to display as error message
        :return: None
        """
        plt.text(0, (len(self.sys_schedules.tasks) * 2), error_text, color="darkred")

    def draw(self):
        """
        Draw the scheduling diagram on the figure and show it
        :return: None
        """
        self.set_limits_of_graph()
        self.gnt.set_prop_cycle(color=self.colors)
        self.set_axes_labels()
        self.set_x_ticks()
        self.set_y_ticks()
        self.gnt.grid(True)
        self.draw_system_scheduling()
        self.add_legend()
        self.fig.canvas.manager.set_window_title('Scheduling Diagram')

        plt.show()


def show_scheduling_diagram(sys_schedules: SystemScheduling, error_text=""):
    """
    Show the scheduling diagram of the system schedules given in parameter
    :param sys_schedules: the System Scheduling to draw and show the diagram
    :param error_text: the eventual error text (if a deadline has been missed)
    :return: None
    """
    dia = SchedulingDiagram(sys_schedules)
    if error_text:
        dia.add_error(error_text)
    dia.draw()
