from utils import load, get_values
from train_model import train_model
from numpy import meshgrid, zeros_like, mean
from matplotlib.pyplot import savefig, tight_layout, subplots, \
                              title, xlabel, ylabel


def main():
    df = load('data.csv')
    lhs = get_values(df, "km")
    rhs = get_values(df, "price")

    theta_0 = 0
    theta_1 = 0

    it = 1000
    learning_rate = 0.01
    print("Please enter a mileage:")
    mileage = input()

    print("Before training: ", theta_1 + theta_0 * float(mileage))

    pred = []

    theta_1, theta_0 = train_model(lhs, rhs, it, learning_rate)
    # print("theta__0", theta_0)
    # print("theta__1", theta_1)

    print("After training: ", theta_0 + theta_1 * float(mileage))

    for i, unit in enumerate(lhs):
        pred.insert(i, unit * theta_1 + theta_0)

    # Create a grid of a and b values
    A, B = meshgrid(lhs, rhs)

    # Calculate the squared error for each combination of a and b
    squared_error = zeros_like(A)

    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            predicted_y = A[i, j] * theta_1 + theta_0  # Predicted function
            squared_error[i, j] = mean((predicted_y - B[i, j]) ** 2)
            # Mean squared error

    fig, ax = subplots()

    ax.plot(lhs, pred)
    ax.scatter(lhs, rhs)

    tight_layout()
    savefig('output')

    fig, ax = subplots()
    # 111: These are subplot grid parameters encoded as a single integer.
    # For example, "111" means "1x1 grid, first subplot" and "234" means
    # "2x3 grid, 4th subplot".
    # Alternative form for add_subplot(111) is add_subplot(1, 1, 1).

    ax = fig.add_subplot(111, projection='3d')

    surface = ax.plot_surface(A, B, squared_error, cmap='viridis',
                              edgecolor='none')
    fig.colorbar(surface, ax=ax, shrink=0.5, aspect=5)
    # Color bar to show the scale of error
    title("Contour Plot of Squared Error")
    xlabel("Slope (a)")
    ylabel("Intercept (b)")
    savefig("cost")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"{e}")
