from rate_limiter import is_rate_limited

ip = "192.168.1.10"

for i in range(7):

    result = is_rate_limited(ip)

    print(
        f"Request {i+1}:",
        "BLOCKED" if result else "ALLOWED"
    )