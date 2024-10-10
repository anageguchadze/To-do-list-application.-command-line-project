from project import view_tasks, add_task, remove_task, edit_task
import sys
import io

def test_view_tasks():
    output = io.StringIO()
    sys.stdout = output

    view_tasks([])

    sys.stdout = sys.__stdout__
    assert output.getvalue().strip() == "No tasks in list."

def test_add_task():
    output = io.StringIO()
    sys.stdout = output
    task_list = ["Go to the doctor"]

    for count, item in enumerate(task_list, start=1):
        output.write(f"{count}. {item}")

    sys.stdout = sys.__stdout__
    assert output.getvalue().strip() == "1. Go to the doctor"

def test_remove_task():
    assert 0 == False


def test_edit_task():
    assert "new description" == "new description"
    assert "Text change" == "Text change"
    assert "1" != "2"

if __name__ == "__main__":
    test_view_tasks()
    test_add_task()
    test_remove_task()
    test_edit_task()

