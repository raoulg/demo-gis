import matplotlib.pyplot as plt

def show(x : int, y : int) -> None:
    """Display a simple plot with given x and y coordinates."""
    plt.plot(x, y, 'o')
    plt.title('Simple Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid(True)
    plt.show()