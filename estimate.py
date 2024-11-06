from utils import get_lists_from_dataframe
from matplotlib.pyplot import savefig, tight_layout, subplots


def main():
    lhs, rhs = get_lists_from_dataframe("data.csv", "km", "price")

    theta_0 = 0
    theta_1 = 0

    print("Please enter a mileage:")
    mileage = input()

    print("Estimated price is", int(theta_1 + theta_0 * float(mileage)))

    pred = []
    # print("theta_0 (y-interceipt) is: ", theta_0)
    # print("theta_1 (slope) is: ", theta_1)

    for i, unit in enumerate(lhs):
        pred.insert(i, unit * theta_1 + theta_0)

    fig, ax = subplots()

    ax.plot(lhs, pred)
    ax.scatter(lhs, rhs)

    tight_layout()
    savefig("output_no_training")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"{e}")
