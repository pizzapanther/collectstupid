# Collect Stupid - A Faster Collect Static (sometimes) for Django

When using `collectstatic` with remote file systems like Amazon S3 it can often
slow down because up to 3 remote operations are needed for each file.

1. Determine file time stamp
2. Delete file if old
3. Copy the new file

This becomes very slow when your project grows. Sometimes 
it is just faster to upload everything. This is especially true if you
run collectstupid close to the your remote file system, for example from
Heroku to S3.

So speed up your static file deploy with collectstupid if the total size 
of your static files can be uploaded quickly.

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
split our process to by default collect without MP3s and MP4s so we weren't 
uploading any large files with every deploy. The deploy went down to 10 minutes 
without large files, and 15 minutes with large files. This also cut down memory 
usage to almost nothing when compared to 13GB.

With memory usage down, we can now move our collect static step back to Heroku
where the file copies are even faster to S3 and get the deploy time less
than 10 minutes.

## Future work

Make stupid a little smart: Cache which files were uploaded but still skip 
delete and exists checks.

## Feature requests

Feel free to open an issue
