from django.core.management.base import BaseCommand
from datetime import timedelta
from django.utils import timezone
from tickets.models import Ticket  # Ensure 'tickets' is your app name

class Command(BaseCommand):
    help = 'Deletes tickets that were resolved more than 30 days ago'

    def handle(self, *args, **kwargs):
        # Calculate the date threshold (30 days ago)
        thirty_days_ago = timezone.now() - timedelta(days=30)

        # Find tickets where status is 'Resolved' and updated_at is older than 30 days
        resolved_tickets = Ticket.objects.filter(
            status='Closed',  # Match the status field value exactly
            updated_at__lt=thirty_days_ago
        )

        # Delete the matching tickets and count how many were deleted
        deleted_count, _ = resolved_tickets.delete()

        # Print a confirmation message in the terminal
        self.stdout.write(self.style.SUCCESS(f'Successfully deleted {deleted_count} old closed tickets'))
