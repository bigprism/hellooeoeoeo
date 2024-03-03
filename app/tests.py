from django.test import TestCase

from .models import Task

from .views import task_list, task_detail, task_create, task_update, task_delete

from .forms import TaskForm

from .views import task_list_api, task_detail_api, task_create_api, task_update_api, task_delete_api



class TaskModelTest(TestCase):

    def test_create_task(self):
        task = Task.objects.create(title='Test Task', description='This is a test task.', status='new', priority=1)
        self.assertEqual(task.title, 'Test Task')
        self.assertEqual(task.description, 'This is a test task.')
        self.assertEqual(task.status, 'new')
        self.assertEqual(task.priority, 1)



class TaskViewTest(TestCase):

    def test_task_list_view(self):
        response = self.client.get('/task_list/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'task_list.html')

    def test_task_detail_view(self):
        task = Task.objects.create(title='Test Task', description='This is a test task.', status='new', priority=1)
        response = self.client.get(f'/task_detail/{task.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'task_detail.html')

    def test_task_create_view(self):
        response = self.client.get('/task_create/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'task_create.html')

    def test_task_update_view(self):
        task = Task.objects.create(title='Test Task', description='This is a test task.', status='new', priority=1)
        response = self.client.get(f'/task_update/{task.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'task_update.html')

    def test_task_delete_view(self):
        task = Task.objects.create(title='Test Task', description='This is a test task.', status='new', priority=1)
        response = self.client.get(f'/task_delete/{task.id}/')
        self.assertEqual(response.status_code, 200)



class TaskFormTest(TestCase):

    def test_valid_data(self):
        form = TaskForm(data={'title': 'Test Task', 'description': 'This is a test task.', 'status': 'new', 'priority': 1})
        self.assertTrue(form.is_valid())

    def test_invalid_data(self):
        form = TaskForm(data={'title': '', 'description': '', 'status': '', 'priority': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {'title': ['This field is required.'], 'description': ['This field is required.'], 'status': ['This field is required.'], 'priority': ['This field is required.']})



class TaskAPITest(TestCase):

    def test_task_list_api(self):
        response = self.client.get('/task_list_api/')
        self.assertEqual(response.status_code, 200)

    def test_task_detail_api(self):
        task = Task.objects.create(title='Test Task', description='This is a test task.', status='new', priority=1)
        response = self.client.get(f'/task_detail_api/{task.id}/')
        self.assertEqual(response.status_code, 200)

    def test_task_create_api(self):
        response = self.client.post('/task_create_api/', {'title': 'Test Task', 'description': 'This is a test task.', 'status': 'new', 'priority': 1})
        self.assertEqual(response.status_code, 201)

    def test_task_update_api(self):
        task = Task.objects.create(title='Test Task', description='This is a test task.', status='new', priority=1)
        response = self.client.put(f'/task_update_api/{task.id}/', {'title': 'Updated Test Task', 'description': 'This is an updated test task.', 'status': 'in progress', 'priority': 2})
        self.assertEqual(response.status_code, 200)

    def test_task_delete_api(self):
        task = Task.objects.create(title='Test Task', description='This is a test task.', status='new', priority=1)
        response = self.client.delete(f'/task_delete_api/{task.id}/')
        self.assertEqual(response.status_code, 204)