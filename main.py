from give_price import load, get_values, create_figure, normalize, normalize_list
from train_model import train_model
from matplotlib.pyplot import savefig, tight_layout, show, subplots, ylim


def main():
    df = load('data.csv')
    lhs = get_values(df, "km")
    rhs = get_values(df, "price")

    theta_0 = 0
    theta_1 = 0
    exp = 2
    it = 1000
    learning_rate = 0.01
    print("Please enter a mileage:")
    mileage = input()

    print("Before training: ", theta_1 + theta_0 * float(mileage))

    pred = []

    nlhs = normalize(lhs)
    nrhs = normalize(rhs)

    theta_1, theta_0 = train_model(lhs, rhs, it, learning_rate)
    print("theta__0", theta_0)
    print("theta__1", theta_1)

    for i, unit in enumerate(lhs):
        pred.insert(i, unit * theta_1 + theta_0)

    # pred.sort(reverse=True)
    # npred = normalize_list(pred)

    fig, ax = subplots()
    # print(pred)
    # print(normalize_list(npred))
    ax.plot(lhs, pred)
    ax.scatter(lhs, rhs)

    tight_layout()
    savefig('output_new')


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"{e}")
