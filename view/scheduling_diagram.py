import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap
from matplotlib.ticker import MultipleLocator
from matplotlib.lines import Line2D
from model.scheduling import SystemScheduling


class SchedulingDiagram:
    """
    Class used to instanciate a Scheduling Gant Diagram
    """


    def __init__(self, sys_schedules: SystemScheduling, limit=-1, colors_class = "tab10"):
        self.sys_schedules = sys_schedules
        if limit == -1 :
            self.feasibility_interval = sys_schedules.feasibility_interval
        else :
            self.feasibility_interval = limit
        self.fig, self.gnt = plt.subplots()
        self.colors = self.get_list_of_colors(colors_class)

    def get_list_of_colors(self, colors_class: str):
        name = colors_class
        cmap = get_cmap(name)  # type: matplotlib.colors.ListedColormap
        return cmap.colors  # type: list

    def set_limits_of_graph(self):
        self.gnt.set_ylim(0, len(self.sys_schedules.tasks) * 2)
        self.gnt.set_xlim(0, self.feasibility_interval)

    def set_axes_labels(self):
        self.gnt.set_xlabel('CPU Moments')
        self.gnt.set_ylabel('Tasks')

    def set_x_ticks(self):
        self.gnt.xaxis.set_minor_locator(MultipleLocator((self.feasibility_interval/10)+1))

    def set_y_ticks(self):
        tasks_len = len(self.sys_schedules.tasks)
        # should update
        ticks = []
        labels = []
        for i in range(tasks_len):
        #for i in range(tasks_len-1, -1, -1):
            ticks.append((i * 2))
            labels.append(i + 1)
        self.gnt.set_yticks(ticks)
        # Labelling tickes of y-axis
        self.gnt.set_yticklabels(labels)

    def draw_periods_for_task(self,task_index, task, color, len_tasks):
        tasks_len = len_tasks
        task_index = (len_tasks - task_index) - 1
        for i in range(task.offset + task.period, self.feasibility_interval + 1, task.period):
            max_i = 1 - ((task_index) * (1 / tasks_len))
            min_i = max_i - 1 / tasks_len
            self.gnt.axvline(x=i, ymin=min_i, ymax=max_i,
                        color=color, linewidth=4, alpha=0.50)

    def draw_deadline_task(self, task_index, task, color, len_tasks):
        tasks_len = len_tasks
        task_index = (len_tasks - task_index) - 1
        for i in range(task.offset + task.deadline, self.feasibility_interval + 1, task.deadline):
            max_i = 1 - ((task_index) * (1 / tasks_len))
            min_i = max_i - 1 / tasks_len
            self.gnt.axvline(x=i, ymin=min_i, ymax=max_i,
                    color=color, linestyle="--", linewidth=4)

    def draw_job_execution(self, job_execution, color, task_index, is_deadline_missed):
        job_exe_t = job_execution.get_as_tuple()
        if is_deadline_missed:
            self.gnt.broken_barh([job_exe_t], (task_index * 2, 1), facecolors=color, hatch='/', alpha=0.5, edgecolor='black',
                            linewidth=4)
        else:
            self.gnt.broken_barh([job_exe_t], (task_index * 2, 1), facecolors=color, edgecolor='black', linewidth=2)

    def draw_job(self, job, color, task_index):

        is_deadline_missed = job.is_deadline_missed(self.feasibility_interval)

        for job_exe in job.job_executions:
            self.draw_job_execution(job_exe, color, task_index, is_deadline_missed)

    def draw_task_scheduling(self,task, color, task_index):
        for job in task.jobs:
            self.draw_job( job, color, task_index)

    def draw_system_scheduling(self):
        for i, schedule in enumerate(self.sys_schedules.schedules):

            self.draw_task_scheduling(schedule, self.colors[i], i)
            self.draw_periods_for_task(i, schedule.task, self.colors[i],
                                  len(self.sys_schedules.tasks))
            self.draw_deadline_task(i, schedule.task, self.colors[i], len(self.sys_schedules.tasks))

    def add_legend(self):
        handles, labels = plt.gca().get_legend_handles_labels()
        line1 = Line2D([0], [0], label='Deadline', color='blue', linestyle="--", linewidth=2)
        line2 = Line2D([1], [0], label='Period', color='blue', linewidth=2, alpha=0.50)
        handles.extend([line1, line2])
        plt.legend(handles=handles)

    def set_size_fig(self, width=12, height=4):
        self.fig.set_figwidth(width)
        self.fig.set_figheight(height)

    def add_error(self, error_text:str):
        plt.text(0, (len(self.sys_schedules.tasks) * 2), error_text)

    def draw(self):
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


def show_scheduling_diagram(sys_schedules: SystemScheduling, error_text = ""):
    dia = SchedulingDiagram(sys_schedules)
    if error_text:
        dia.add_error(error_text)
    dia.draw()
