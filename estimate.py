from utils import get_lists_from_dataframe, open_thetas_file
from matplotlib.pyplot import savefig, tight_layout, subplots


def main():
    """Program that estimates the price with theta_0 = 0 and theta_1 = 0"""
    lhs, rhs = get_lists_from_dataframe("data.csv", "km", "price")

    theta_0 = 0
    theta_1 = 0

    print("Please enter a mileage:")
    mileage = input()

    theta_0, theta_1 = open_thetas_file("thetas.csv")

    if int(theta_0 + theta_1 * float(mileage)) > 0:
        print("Estimated price is", int(theta_0 + theta_1 *
                                        float(mileage)))
    else:
        print("The car cannot be sold: its value is 0.")

    pred = []
    # print("theta_0 (y-interceipt) is: ", theta_0)
    # print("theta_1 (slope) is: ", theta_1)

    for i, unit in enumerate(lhs):
        pred.insert(i, unit * theta_1 + theta_0)

    fig, ax = subplots()

    ax.plot(lhs, pred)
    ax.scatter(lhs, rhs)

    tight_layout()
    savefig("output")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"{e}")
