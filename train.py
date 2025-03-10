from utils import get_lists_from_dataframe
# from linear_regression_test import train_model
from linear_regression import train_model
from matplotlib.pyplot import savefig, tight_layout, subplots, \
                              show


def main():
    """Program that trains the model with 1000 iterations and a
    learning rate of 0.01"""
    lhs, rhs = get_lists_from_dataframe("data.csv", "km", "price")

    theta_0 = 0
    theta_1 = 0

    learning_rate = 0.01

    pred = []

    theta_1, theta_0 = train_model(lhs, rhs, learning_rate)

    f = open("thetas.csv", "w")
    f.write(f"{theta_0}, {theta_1}")
    f.close()

    # print("theta_0 (y-interceipt) is: ", theta_0)
    # print("theta_1 (slope) is: ", theta_1)

    for i, unit in enumerate(lhs):
        pred.insert(i, unit * theta_1 + theta_0)

    fig, ax = subplots()

    ax.plot(lhs, pred)
    ax.scatter(lhs, rhs)

    tight_layout()
    savefig("output_training")
    show()


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"{e}")
