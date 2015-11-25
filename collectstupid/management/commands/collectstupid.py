import json
import hashlib

from django.contrib.staticfiles.management.commands import collectstatic
from django.core.management.base import BaseCommand
from django.conf import settings

class Command (collectstatic.Command):
  help = "blindly run collectstatic without checking modified times"
  
  def handle (self, *args, **kwargs):
    cache_path = getattr(settings, 'STUPID_DEPLOY_CACHE', 'collectstupid-cache.json')
    self.set_options(**kwargs)
    
    if self.clear:
      self.deployed_files = {}
      
    else:
      try:
        with self.storage.open(cache_path) as fh:
          self.deployed_files = json.loads(fh.read())
          
      except IOError:
        self.deployed_files = {}
        
    super(Command, self).handle(*args, **kwargs)
    
    with self.storage.open(cache_path, 'w') as fh:
      fh.write(json.dumps(self.deployed_files, indent=2))
      
  def karen_scan (self, path, source_storage):
    hasher = hashlib.md5()
    with source_storage.open(path) as fh:
      hasher.update(fh.read())
      
    return hasher.hexdigest()
    
  def delete_file (self, path, prefixed_path, source_storage):
    hash_slinging_slasher = self.karen_scan(path, source_storage)
    
    if path in self.deployed_files:
      if self.deployed_files[path] == hash_slinging_slasher:
        return False
        
    self.deployed_files[path] = hash_slinging_slasher
    
    return True
    