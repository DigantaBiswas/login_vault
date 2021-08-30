from django.core.management.base import BaseCommand, CommandError

from blog.tasks.login_post_scrapper import get_page, scrape_data


class Command(BaseCommand):
    # help = 'Closes the specified poll for voting'
    #
    # def add_arguments(self, parser):
    #     parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        scrape_data()
