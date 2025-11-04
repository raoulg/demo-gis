import os
from loguru import logger
from mypackage.demo import calculate_sum

logger.add("app.log", rotation="1 MB")

def locatie():
    """Return the absolute path of the current script's directory."""
    logger.info("Determining the script's directory path.")
    return os.path.dirname(os.path.abspath(__file__))


if __name__ == "__main__":
    print(locatie())
    total = calculate_sum(5, 7)
    logger.info(f"The total sum is {total}.")