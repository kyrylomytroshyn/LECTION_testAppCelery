broker_url = 'redis://localhost'
result_backend = 'redis://localhost'

task_serializer = 'json'

task_routes = {
    'main.add': 'low_priority',
    'main.long': 'long_running'
}

task_annotations = {
    'simple_tasks.add': {
        'rate_limit': '10/m',
    }
}

timezone = "Europe/Kiev"
