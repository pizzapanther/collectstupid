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