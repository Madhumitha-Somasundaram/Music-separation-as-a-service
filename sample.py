import redis

# Connect to Redis
r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

# Inspect current queue
queue = r.lrange("toWorker1", 0, -1)
print("Current queue:", queue)
print("Queue length:", len(queue))

# Push test jobs without affecting production jobs
test_jobs = ["testjob1", "testjob2"]
for job in test_jobs:
    r.rpush("toWorker1", job)

queue = r.lrange("toWorker1", 0, -1)
print("Queue after push:", queue)
print("Queue length:", len(queue))
