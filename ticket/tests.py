from django.test import TestCase
from ticket.models import Ticket


class TicketTestCase(TestCase):
    def setUp(self):
        Ticket.objects.create(title="test", body="text")

    def test_ticket_fields(self):
        """Ticket created has its correct default values"""
        ticket = Ticket.objects.get(title="test")
        self.assertEqual(ticket.upvotes, 0)
        self.assertEqual(ticket.ticket_type, '1')
        self.assertEqual(ticket.progress, 'To do')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/ticket/all_tickets/')
        self.assertEqual(response.status_code, 200)
