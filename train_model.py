from pandas import DataFrame


def get_affine_function(mileage: list, price: list, theta_0: float, theta_1: float, learning_rate: float) -> tuple:
    # y = w * x + b
    mse = 0.0
    m = len(mileage)
    theta_0 = (price[1] - price[0]) / (mileage[1] - mileage[0])

    for mileage_unit, price_unit in zip(mileage, price):

        b, w, se = minimize_cost(m, theta_0, theta_1, mileage_unit, price_unit, learning_rate)
        theta_0 += b
        theta_1 += w

    mse += 1 / (2 * m) * se
    theta_0 /= len(mileage)
    theta_1 /= len(mileage)
    
    return theta_0, theta_1, mse


def minimize_cost(m: int, theta_0: float, theta_1: float, real_mileage: float, real_price: float, learning_rate: float) -> tuple:
    limit = float("inf")
    w = 0.0
    b = 0.0

    for i in range(-100, 100, 1):
        theta_1 = float(i / ((2 * m) / learning_rate))

        # real_price = theta_1 * real_mileage + theta_0
        # real_price - theta_0 = theta_1 * real_mileage
        # -theta_0 = theta_1 * real_mileage - real_price
        # theta_0 = -(theta_1 * real_mileage - real_price)
        theta_0 = -theta_1 * real_mileage + real_price
        mse = ((theta_1 * real_mileage + theta_0) - real_price) ** 2
        if mse < limit:

            limit = mse
            b = theta_0
            w = theta_1

    return b, w, limit
 

def train_model(lhs: DataFrame, rhs: DataFrame, it: int, learning_rate: float) -> tuple:
    theta_0 = 0.0
    theta_1 = 0.0
    minimum = float("inf")
    w = 0.0
    b = 0.0

    mileage = list(float(x) for x in lhs)
    price = list(float(x) for x in rhs)

    for i in range(it):
        theta_0, theta_1, mse = get_affine_function(mileage, price, theta_0, theta_1, learning_rate)

        if mse < minimum:
            minimum = mse
            w = theta_1
            b = theta_0

    return w, b


