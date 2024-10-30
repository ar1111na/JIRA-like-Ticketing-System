from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Ticket, Comment, Attachment
from rest_framework.test import APIClient
from rest_framework import status
from datetime import date

class TicketModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.ticket = Ticket.objects.create(
            title='Test Ticket',
            description='Test Description',
            priority='High',
            status='Open',
            reporter=self.user,
            due_date=date.today()
        )

    def test_ticket_creation(self):
        self.assertEqual(self.ticket.title, 'Test Ticket')
        self.assertEqual(self.ticket.status, 'Open')
        self.assertEqual(self.ticket.reporter.username, 'testuser')

class CommentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.ticket = Ticket.objects.create(
            title='Test Ticket',
            description='Test Description',
            priority='High',
            status='Open',
            reporter=self.user,
            due_date=date.today()
        )
        self.comment = Comment.objects.create(
            ticket=self.ticket,
            user=self.user,
            comment_text='This is a test comment'
        )

    def test_comment_creation(self):
        self.assertEqual(self.comment.comment_text, 'This is a test comment')
        self.assertEqual(self.comment.ticket.title, 'Test Ticket')
        self.assertEqual(self.comment.user.username, 'testuser')

class TicketViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.ticket = Ticket.objects.create(
            title='Test Ticket',
            description='Test Description',
            priority='High',
            status='Open',
            reporter=self.user,
            due_date=date.today(),
            assignee=self.user 
        )

    def test_ticket_list_view(self):
        response = self.client.get(reverse('ticket_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Ticket')

    def test_create_ticket_view(self):
        response = self.client.post(reverse('create_ticket'), {
            'title': 'New Ticket',
            'description': 'New Description',
            'priority': 'Medium',
            'status': 'Open',
            'due_date': date.today(),
            'assignee': self.user.id
        })
        self.assertEqual(response.status_code, 302) 
        self.assertEqual(Ticket.objects.last().title, 'New Ticket')

    def test_update_ticket_view(self):
        response = self.client.post(reverse('update_ticket', args=[self.ticket.pk]), {
            'title': 'Updated Ticket',
            'description': 'Updated Description',
            'priority': 'Low',
            'status': 'In Progress',
            'due_date': date.today(),
            'assignee': self.user.id 
        })
        self.assertEqual(response.status_code, 302)  
        self.ticket.refresh_from_db()
        self.assertEqual(self.ticket.title, 'Updated Ticket')
        self.assertEqual(self.ticket.status, 'In Progress')

    def test_delete_ticket_view(self):
        response = self.client.post(reverse('delete_ticket', args=[self.ticket.pk]))
        self.assertEqual(response.status_code, 302) 
        self.assertFalse(Ticket.objects.filter(pk=self.ticket.pk).exists())

class TicketAPITest(TestCase):
    def setUp(self):
        self.api_client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.api_client.force_authenticate(user=self.user)
        self.ticket = Ticket.objects.create(
            title='Test Ticket',
            description='Test Description',
            priority='High',
            status='Open',
            reporter=self.user,
            due_date=date.today(),
            assignee=self.user
        )

    def test_get_ticket_list_api(self):
        response = self.api_client.get(reverse('ticket-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test Ticket')

    def test_update_ticket_api(self):
        response = self.api_client.patch(reverse('ticket-detail', args=[self.ticket.pk]), {
            'status': 'Resolved'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.ticket.refresh_from_db()
        self.assertEqual(self.ticket.status, 'Resolved')

    def test_delete_ticket_api(self):
        response = self.api_client.delete(reverse('ticket-detail', args=[self.ticket.pk]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Ticket.objects.filter(pk=self.ticket.pk).exists())
