from task import Task
from random import randint
from random import randrange
#a task generator should generate tasks where wcte is below the deadline

def generate_random_task():
    """
    Generate a random implicit deadline task

    Returns:
        n: the random implicit deadline task generated
    """
    offset = randint(0,20)
    wcte = randrange(1, 100, randint(1,6))
    deadline = randint(wcte, wcte +100)
    period = deadline
    return Task(offset,wcte, deadline, period)


def generate_random_tasks(nb_tasks):
    """Generate a list of a given number of random tasks

    Args:
        nb_tasks (int): the number of tasks to generate

    Returns:
       a list of random generated tasks
    """
    tasks = []
    for i in range(nb_tasks):
        tasks.append(generate_random_task())
    return tasks

# TODO make a test
def test_1():
    # TODO second todo
    #print(generate_random_tasks(10))
    tasks = generate_random_tasks(10)
    for i in tasks:
        print(i)
