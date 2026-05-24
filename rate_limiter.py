from collections import defaultdict
import time

request_log = defaultdict(list)

LIMIT = 5
WINDOW = 60


def is_rate_limited(ip):

    now = time.time()

    request_log[ip] = [
        t for t in request_log[ip]
        if now - t < WINDOW
    ]

    request_log[ip].append(now)

    return len(request_log[ip]) > LIMIT