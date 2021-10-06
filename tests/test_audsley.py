from audsley import is_task_lowest_priority_viable
from audsley import make_all_tasks_soft, audsley_recur
from scheduling import get_deadline_missed_example
from scheduling import get_first_course_example_schedule, get_second_example_schedule
from task import Task


def test_make_all_tasks_soft():
    task_set = get_first_course_example_schedule()
    make_all_tasks_soft(task_set)

    for task in task_set:
        assert task.is_hard == False

def test_is_not_lowest_priority_viable():
    task_set = get_deadline_missed_example()
    assert not is_task_lowest_priority_viable(0, task_set)
    assert not is_task_lowest_priority_viable(1, task_set)
    assert not is_task_lowest_priority_viable(2, task_set)

def test_is_task_lowest_priority_viable_deadline_miss():
    task_set = get_deadline_missed_example()
    task_index = 0
    assert not is_task_lowest_priority_viable(task_index, task_set)


def test_audsley_empty_set():
    task_set = []
    assert audsley_recur(task_set, task_set.copy())


def test_audsley_only_one_task():
    task_set = [Task(0, 2, 10, 10)]
    assert audsley_recur(task_set, task_set.copy())

def test_audsley_one_task_impossible():
    task_set = [Task(0, 20, 10, 10)]
    assert not audsley_recur(task_set, task_set.copy())

def test_audsley_one_task_impossible2():
    task_set = [Task(0, 2, 1, 10)]
    assert not audsley_recur(task_set, task_set.copy())

def test_audsley_two_tasks():
    task_set = get_second_example_schedule()
    assert audsley_recur(task_set, task_set.copy())

def test_audsley_two_tasks_impossible():
    t1 = Task(0, 2, 2, 2)
    t2 = Task(0, 1, 1, 1)
    task_set = [t1, t2]
    assert not audsley_recur(task_set, task_set.copy())

def test_audsley_three_tasks_ok():
    task_set = get_first_course_example_schedule()
    assert audsley_recur(task_set, task_set.copy())

def test_audsley_three_tasks_changed_priority():
    t1 = Task(0, 3, 5, 5)
    t2 = Task(0, 2, 10, 10)
    t3 = Task(0, 4, 20, 20)
    task_set = [t2, t3, t1]
    assert audsley_recur(task_set, task_set.copy())
    print(task_set)

def test_audsley_deadlines_misses_example():
    task_set = get_deadline_missed_example()
    make_all_tasks_soft(task_set)
    assert not audsley_recur(task_set, task_set.copy())