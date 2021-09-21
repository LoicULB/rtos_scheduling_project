class scheduling:
    def __init__(self, array=[]):
        self.scheduling=array

class Job:
    def __init__(self, start=0, nb_cpu_units=0):
        self.start = start
        self.nb_cpu_units = nb_cpu_units

    def __str__(self):
        return f"{self.start} {self.nb_cpu_units}"
