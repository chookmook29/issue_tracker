from django.test import TestCase
from ticket.models import Ticket


class TicketTestCase(TestCase):
    def setUp(self):
        Ticket.objects.create(title="test", body="text", id=1)

    def test_ticket_fields(self):
        """Ticket created has its correct default values"""
        ticket = Ticket.objects.get(title="test")
        self.assertEqual(ticket.upvotes, 0)
        self.assertEqual(ticket.id, 1)
        self.assertEqual(ticket.ticket_type, '1')
        self.assertEqual(ticket.progress, 'To do')

    def test_all_tickets(self):
        response = self.client.get('/ticket/all_tickets/')
        self.assertEqual(response.status_code, 200)

    def test_single_ticket(self):
        response = self.client.get('/ticket/show/1')
        self.assertEqual(response.status_code, 200)
