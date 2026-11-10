import logging
import requests

logging.basicConfig(
    filename="hearttalk.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/1",
        timeout=5
    )
    response.raise_for_status()

except requests.RequestException:
    logging.exception("HeartTalk API request failed.")

else:
    logging.info("User data fetched successfully.")