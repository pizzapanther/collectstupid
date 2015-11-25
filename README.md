# Collect Stupid - A Faster Collect Static for Django

When using `collectstatic` with remote file systems like Amazon S3 it can often
slow down because up to 3 remote operations are needed for each file.

1. Determine file time stamp
2. Delete file if old
3. Copy the new file

collectstupid speeds up your static file deploy with two tricks

1. The Stupid One: Never checks remote file timestamps and never deletes the 
   old file. It just overwrites the file blindly. This saves two remote
   operations.
2. The Smart One: Stores a list of deployed file md5sums on the remote file 
   system. This keeps track of what files need to be deployed and md5sums are 
   only computed at the source for speed. This can be faster than other 
   collectstatic libraries which a lot of times use local cache and thus other 
   developers don't benefit from the last deploy. Also the deployment tracking 
   is more permanent and not subject to cache clearing unless you explicitly 
   need to clear it.

## Installation and Usage

`pip install collectstupid`

Add **collectstupid** to **INSTALLED_APPS**

Run: `python manage.py collectstupid`

## Storage Mixin

Some storage implementations execute an *exists* and *delete* on the storage
class even when using `collectstupid`. You can add the 
**collectstupid.storage.StupidStorageMixin** to your storage class to skip 
those requests.

## Personal Example Where CollectStupid Improved Deployment Speed

For a project, whenever we deployed, a huge amount of memory (+13GB) was used 
and the whole process took more than 30 minutes on a fast Mac and over 2 hours 
on a virtual machine. Through investigation, we found that every check of 
whether a file existed caused the bucket to do a full file list because of a
very inefficient S3 storage implementation. We implemented `collectstupid` and 
after the initial deploy of large files, subsequent deploys went down to less
than 5 minutes. This also cut down memory usage to almost nothing when compared 
to 13GB.

## Settings

`STUPID_DEPLOY_CACHE`: File where md5sums are stored on the remote filesystem

Default: collectstupid-cache.json

## Feature requests

Feel free to open an issue
