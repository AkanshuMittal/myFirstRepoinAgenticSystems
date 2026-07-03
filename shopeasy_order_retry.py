import os
import logging
from tenacity import retry, stop_after_attempt, wait_exponential, before_sleep_log

# Attempt counter
attempt_counter = {"count": 0}

# Create logs folder if not exists
os.makedirs("logs", exist_ok=True)

# Logger setup
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")

# File handler
file_handler = logging.FileHandler("logs/api_retries.log")
file_handler.setFormatter(formatter)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)


@retry(
    stop=stop_after_attempt(4),
    wait=wait_exponential(multiplier=1, min=1, max=10),
    before_sleep=before_sleep_log(logger, logging.WARNING)
)
def lookup_order_status(order_id: str) -> str:
    attempt_counter["count"] += 1

    if attempt_counter["count"] <= 2:
        raise Exception("HTTP 429 Too Many Requests")

    return f"Order {order_id} — out for delivery. Expected by 6 PM today."


if __name__ == "__main__":
    result = lookup_order_status("ORD-7842")
    print(result)
    print(f"Total API attempts: {attempt_counter['count']}")