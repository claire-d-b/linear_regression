from pandas import DataFrame


def get_affine_function(mileage: list, price: list, theta_0: float,
                        theta_1: float, learning_rate: float) -> tuple:
    """Take all values from x-axis and y-axis lists and calculate the
    mean square error smallest value, and corresponding thetas"""
    # y = w * x + b
    mse = 0.0
    m = len(mileage)

    for mileage_unit, price_unit in zip(mileage, price):

        b, w, se = minimize_cost(m, theta_0, theta_1, mileage_unit,
                                 price_unit, learning_rate)
        theta_0 += b
        theta_1 += w

        mse += se
    ret_mse = mse * 1 / (2 * m)
    theta_0 /= len(mileage)
    theta_1 /= len(mileage)

    return theta_0, theta_1, ret_mse


def minimize_cost(m: int, theta_0: float, theta_1: float, real_mileage: float,
                  real_price: float, learning_rate: float) -> tuple:
    """Test with a slope value between -1 and 1, update y-interceipt value,
    and take the smallest square error"""
    limit = float("inf")
    w = 0.0
    b = 0.0

    minimum = int(- 1 / learning_rate)
    maximum = int(1 / learning_rate)

    for i in range(minimum, maximum, 1):
        theta_1 = float(i / ((2 * m) / learning_rate))

        # real_price = theta_1 * real_mileage + theta_0
        # real_price - theta_0 = theta_1 * real_mileage
        # -theta_0 = theta_1 * real_mileage - real_price
        # theta_0 = -(theta_1 * real_mileage - real_price)
        theta_0 = -theta_1 * real_mileage + real_price
        se = ((theta_1 * real_mileage + theta_0) - real_price) ** 2
        if se < limit:

            limit = se
            b = theta_0
            w = theta_1

    return b, w, limit


def train_model(lhs: DataFrame, rhs: DataFrame, it: int,
                learning_rate: float) -> tuple:
    """Take the smallest value of mean square error and
    update thetas accordingly"""
    theta_0 = 0.0
    theta_1 = 0.0
    minimum = float("inf")
    w = 0.0
    b = 0.0

    mileage = list(float(x) for x in lhs)
    price = list(float(x) for x in rhs)

    for i in range(it):
        theta_0, theta_1, mse = get_affine_function(mileage, price,
                                                    theta_0, theta_1,
                                                    learning_rate)

        if mse < minimum:
            minimum = mse
            w = theta_1
            b = theta_0

    return w, b