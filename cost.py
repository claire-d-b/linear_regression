from utils import get_lists_from_dataframe
from linear_regression import train_model
from numpy import meshgrid, zeros_like, mean
from matplotlib.pyplot import savefig, show, \
                              title, figure


def main():
    """Program that builds a 3D shape figure to show the cost function
    / mean squared error"""
    lhs, rhs = get_lists_from_dataframe("data.csv", "km", "price")

    theta_0 = 0
    theta_1 = 0

    it = 1000
    learning_rate = 0.01
    print("Please enter a mileage:")
    mileage = input()

    theta_1, theta_0 = train_model(lhs, rhs, it, learning_rate)

    print("Estimated price is", int(theta_0 + theta_1 * float(mileage)))
    # print("theta_0 (y-interceipt) is: ", theta_0)
    # print("theta_1 (slope) is: ", theta_1)

    # Create a grid of a and b values
    A, B = meshgrid(lhs, rhs)

    # Calculate the squared error for each combination of a and b
    squared_error = zeros_like(A)

    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            predicted_y = A[i, j] * theta_1 + theta_0  # Predicted function
            squared_error[i, j] = mean((predicted_y - B[i, j]) ** 2)
            # Mean squared error

    # 111: These are subplot grid parameters encoded as a single integer.
    # For example, "111" means "1x1 grid, first subplot" and "234" means
    # "2x3 grid, 4th subplot".
    # Alternative form for add_subplot(111) is add_subplot(1, 1, 1).
    fig = figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    surface = ax.plot_surface(A, B, squared_error, cmap='viridis',
                              edgecolor='none')
    fig.colorbar(surface, ax=ax, shrink=0.5, aspect=5)
    # Color bar to show the scale of error
    title("3D surface plot for Squared Error")
    ax.set_xlabel("mileage")
    ax.set_ylabel("price")
    ax.set_zlabel("cost")
    savefig("cost")
    show()


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"{e}")
