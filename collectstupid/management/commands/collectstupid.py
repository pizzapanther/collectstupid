from django.contrib.staticfiles.management.commands import collectstatic
from django.core.management.base import BaseCommand

class Command (collectstatic.Command):
  help = "blindly run collectstatic without checking modified times"
  
  def delete_file (self, *args, **kwargs):
    return True
    