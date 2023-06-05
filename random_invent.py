import random
import yaml

servers = [
    {'name': 'semaphore', 'ip': '10.70.39.249'},
    {'name': 'rundeck', 'ip': '10.70.39.250'},
]

server = random.choice(servers)

inventory = {
    server['name']: {
        'hosts': [server['ip']]
    }
}

print(yaml.dump(inventory))
