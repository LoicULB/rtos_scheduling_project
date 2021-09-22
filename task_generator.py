from .task import Task
from random import randint
from random import randrange
#a task generator should generate tasks where wcte is below the deadline

def generate_random_task():
    offset = randint(0,20)
    wcte = randrange(1, 100, randint(1,6))
    deadline = randint(wcte, wcte +100)
    period = deadline
    return Task(offset,wcte, deadline, period)


def generate_random_tasks(nb_tasks):
    tasks = []
    for i in range(nb_tasks):
        tasks.append(generate_random_task())
    return tasks

def test_1():
    #print(generate_random_tasks(10))
    tasks = generate_random_tasks(10)
    for i in tasks:
        print(i)
