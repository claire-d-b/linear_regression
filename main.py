from give_price import load, get_values
from train_model import train_model
from matplotlib.pyplot import savefig, tight_layout, subplots


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

    fig, ax = subplots()

    ax.plot(lhs, pred)
    ax.scatter(lhs, rhs)

    tight_layout()
    savefig('output')


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"{e}")
