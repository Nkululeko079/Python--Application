from prometheus_client import start_http_server, Counter
import time

# Create a counter to track the number of "Hello, World!" messages printed
HELLO_WORLD_COUNTER = Counter('hello_world_total', 'Total number of Hello, World! messages')

def print_hello_world():
    while True:
        print("Hello, World!")
        HELLO_WORLD_COUNTER.inc()
        time.sleep(2)

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    print_hello_world()
