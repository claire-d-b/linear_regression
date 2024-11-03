from matplotlib.pyplot import savefig, tight_layout, show, subplots, ylim
from pandas import DataFrame, read_csv
from train_model import train_model


def load(path: str) -> DataFrame:
    """Function that opens a file and display inner data in the shape
    of a datatable"""
    try:
        # Ici open est un gestionnaire de contexte qui retourne un
        # object-fichier
        file = read_csv(path)

    except Exception as e:
        raise AssertionError(f"Error: {e}")
    return file


def get_values(df: DataFrame, keyword: str) -> DataFrame:
    """Search for two keyword in the entire DataFrame, then compare
    the two keywords (countries) data"""
    try:
        isinstance(df, DataFrame)

        # Search for a keyword in the entire DataFrame
        col = df[keyword]

    except Exception as e:
        raise AssertionError(f"Error: {e}")

    return col


def normalize(values: DataFrame) -> DataFrame:

    nvalues = []
    for i, unit in enumerate(values):
        nvalues.insert(i, unit / values.max())

    return DataFrame(nvalues)


def normalize_list(values: list) -> list:
    nvalues = []
    for i, unit in enumerate(values):
        nvalues.insert(i, unit / max(values))

    return nvalues


def create_figure(exp: int, lhs: DataFrame, rhs: DataFrame) -> tuple:
    theta_0 = 0
    theta_1 = 0
    limit = float('inf')
    fig, ax = subplots()

    iterations = 100
    theta_0, theta_1, mse = train_model(lhs, rhs, iterations)

    return theta_0, theta_1, mse


def display_points(fig: any, ax: any, frame_x: DataFrame, frame_y: DataFrame,
                   b: float, coeff: float) -> None:

    y_pred = []

    for i, unit in enumerate(frame_x):
        y_pred.append(coeff * unit + b)

    ax.plot(normalize(frame_x), normalize_list(y_pred))
    ax.scatter(normalize(frame_x), normalize(frame_y))

    tight_layout()
    savefig('output_normalized')
    show()
