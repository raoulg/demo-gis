from loguru import logger

def calculate_sum(a, b):
    """Return the sum of two numbers."""
    logger.info(f"Calculating sum of {a} and {b}.")
    total = a + b
    logger.success(f"The sum of {a} and {b} is {total}.")
    return total

class Demo:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        logger.info(f"Demo initialized with a={a} and b={b}.")

    def get_sum(self):
        return calculate_sum(self.a, self.b)

    def get_product(self):
        product = self.a * self.b
        logger.info(f"The product of {self.a} and {self.b} is {product}.")
        return product

if __name__ == "__main__":
    MESSAGE = "Hello there nice to do the demo"
    print(MESSAGE)
    demo = Demo(3, 4)
    sum_result = demo.get_sum()
    product_result = demo.get_product()
    print(f"Sum: {sum_result}, Product: {product_result}")