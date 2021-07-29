from celery import Celery

app = Celery('tasks')
#
# broker = 'redis://localhost',
# backend = 'redis://localhost'

# app.conf.update(
#     task_serializer='json',
#     result_serializer='json'
# )

app.config_from_object('celeryconfig')
@app.task
def class_task(cls):
    print(cls)

@app.task
def add(x, y):
    return x + y

@app.task
def long_add(x, y):
    import time
    time.sleep(10)
    return x + y
