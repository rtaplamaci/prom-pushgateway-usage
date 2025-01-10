from prometheus_client import CollectorRegistry, Gauge, Counter, Summary, Histogram, Info, Enum, push_to_gateway

# Create a registry to hold the metrics
registry = CollectorRegistry()

# Create a Gauge metric to track a custom field
g = Gauge('rtaplamaci_custom_field', 'Custom Field', registry=registry)
g.set(63)  # Set the gauge to 63

# Create a Summary metric to track request latency
s = Summary('request_latency_seconds', 'Description of summary', registry=registry)
s.observe(4.7)  # Observe 4.7 (seconds in this case)

# Create a Counter metric to track failures
c = Counter('my_failures', 'Description of counter', registry=registry)
c.inc()  # Increment by 1
c.inc(1.6)  # Increment by given value

# Create a Counter metric with labels to track failures by method and endpoint
cc = Counter('my_failures_lb', 'Description of counter label', ['method', 'endpoint'], registry=registry)
cc.labels(method='get', endpoint='/').inc()  # Increment for GET /
cc.labels(method='post', endpoint='/submit').inc()  # Increment for POST /submit

# Create a Counter metric with exemplars to track requests by method and endpoint
ccc = Counter('my_requests_total_ex', 'Description of counter examplar', ['method', 'endpoint'], registry=registry)
ccc.labels('get', '/').inc(exemplar={'trace_id': 'abc123'})  # Increment with exemplar for GET /
ccc.labels('post', '/submit').inc(1.0, {'trace_id': 'def456'})  # Increment with exemplar for POST /submit

# Create another Gauge metric to track in-progress requests
g = Gauge('my_inprogress_requests', 'Description of gauge', registry=registry)
g.inc()  # Increment by 1
g.dec(10)  # Decrement by given value
g.set(4.2)  # Set to a given value

# Push the metrics to the Pushgateway
push_to_gateway('localhost:9091', job='batchA', registry=registry)


