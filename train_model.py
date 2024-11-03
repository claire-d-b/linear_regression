from pandas import DataFrame


def get_affine_function(mileage: list, price: list, theta_0: float, theta_1: float) -> tuple:
    # y = w * x + b
    mse = 0.0
    m = len(mileage)
    theta_0 = (price[1] - price[0]) / (mileage[1] - mileage[0])

    for mileage_unit, price_unit in zip(mileage, price):
        print("mileage", mileage_unit)
        b, w, se = minimize_cost(len(mileage), theta_0, theta_1, mileage_unit, price_unit)
        theta_0 += b
        theta_1 += w
    mse += 1/2*m * se
    theta_0 /= len(mileage)
    theta_1 /= len(mileage)
    
    return theta_0, theta_1, mse


def minimize_cost(m: int, theta_0: float, theta_1: float, real_mileage: float, real_price: float) -> tuple:
    limit = float("inf")
    w = 0.0
    b = 0.0

    for i in range(-100, 100, 1):
        theta_1 = float(i / (m * 100))
        print("index", theta_1)
        # real_price = theta_1 * real_mileage + theta_0
        # real_price - theta_0 = theta_1 * real_mileage
        # -theta_0 = theta_1 * real_mileage - real_price
        # theta_0 = -(theta_1 * real_mileage - real_price)
        theta_0 = -theta_1 * real_mileage + real_price
        mse = ((theta_1 * real_mileage + theta_0) - real_price) ** 2
        if mse < limit:
            print("limit")
            limit = mse
            b = theta_0
            w = theta_1
    return b, w, limit
 
# b = -a * x + y
# a = y2 - y1 / x2 - x1
# diff entre deux ordonnées / diff entre 2 abscisses

def train_model(lhs: DataFrame, rhs: DataFrame, it: int, learning_rate: float) -> tuple:
    theta_0 = 0.0
    theta_1 = 0.0
    minimum = float("inf")
    w = 0.0
    b = 0.0

    mileage = list(float(x) for x in lhs)
    price = list(float(x) for x in rhs)

    for i in range(it):
        theta_0, theta_1, mse = get_affine_function(mileage, price, theta_0, theta_1)

        if mse < minimum:
            print("msew", w)
            print("mseb", b)
            minimum = mse
            w = theta_1
            b = theta_0
        print("theta_0", theta_0)
        print("theta_1", theta_1)
    return w, b

def get_points(lhs: DataFrame, rhs: DataFrame) -> None:
    a = (rhs[1] - rhs[0]) / (lhs[1] - lhs[0])
    b = - a * lhs[0] + rhs[0]
    


