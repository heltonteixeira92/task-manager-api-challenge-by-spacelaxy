import pytest

from core.models import Task


@pytest.fixture
def task(db):
    return Task.objects.create()


def test_list_tasks(client, task):
    resp = client.get('/tarefa')

    assert resp.status_code == 200
    assert resp.json() == [task.to_dict()]


@pytest.mark.django_db
def test_create_task(client):
    data = {
        'title': 'do something',
        'status': 'pending',
        'description': 'right now',
    }
    resp = client.post('/tarefa', data=data, content_type='application/json')

    assert resp.status_code == 201
    task = Task.objects.first()
    assert task is not None


def test_read_task(client, task):
    resp = client.get(f'/tarefa/{task.id}')

    assert resp.status_code == 200
    assert resp.json() == task.to_dict()


def test_update_task(client, task):
    data = {
        'id': task.id,
        'title': 'new title',
        'status': 'in progress',
        'description': 'lorem ipsum',
    }

    resp = client.put(f'/tarefa/{task.id}', data=data, content_type='application/json')
    assert resp.status_code == 200
    assert resp.json() == data


def test_delete_task(client, task):
    resp = client.delete(f'/tarefa/{task.id}')

    assert resp.status_code == 204
    assert not Task.objects.filter(id=task.id).exists()

