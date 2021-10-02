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


def test_is_task_lowest_priority_viable():
    task_set = get_first_course_example_schedule()
    assert is_task_lowest_priority_viable(0, task_set)


def test_is_not_lowest_priority_viable():
    task_set = get_deadline_missed_example()
    assert is_task_lowest_priority_viable(0, task_set)
    assert is_task_lowest_priority_viable(1, task_set)
    assert not is_task_lowest_priority_viable(2, task_set)


def test_audsley_empty_set():
    task_set = []
    assert audsley_recur(task_set, task_set.copy())


def test_audsley_only_one_task():
    task_set = [Task(0, 2, 10, 10)]
    assert audsley_recur(task_set, task_set.copy())


def test_audsley_two_tasks():
    task_set = get_second_example_schedule()
    assert audsley_recur(task_set, task_set.copy())


def test_audsley_deadlines_misses_example():
    task_set = get_deadline_missed_example()
    make_all_tasks_soft(task_set)
    assert not audsley_recur(task_set, task_set.copy())


# Find why this test doesn't pass when it should
def test_is_task_lowest_priority_viable_deadline_miss():
    task_set = get_deadline_missed_example()
    task_index = 0

    assert not is_task_lowest_priority_viable(task_index, task_set)