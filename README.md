Populate data to Json file and db

Step 1:
make load (it will load in Json file)

Step 2:
make loaddata (it will load in database)


For Celery Server
celery -A fashionic worker --loglevel=info
celery -A fashionic beat --loglevel=info
celery -A fashionic worker -l INFO

To run servers using celery
---------------------------
# Start Celery worker in the background
make celery-worker &

# Start Celery beat in the background
make celery-beat &

# Start Django server
make run
