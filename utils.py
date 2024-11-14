from pandas import DataFrame, read_csv


def open_thetas_file(name: str) -> tuple:
    theta_0 = 0
    theta_1 = 0
    try:
        f = open("thetas.txt", "r")
        values = f.read().split(",")
        theta_1 = float(values[1])
        theta_0 = float(values[0])
    except Exception:
        raise AssertionError("Unreadable theta values")
    finally:
        return theta_0, theta_1


def get_lists_from_dataframe(df_name: str, keyword_lhs: str,
                             keyword_rhs: str) -> tuple:
    try:
        df = load(df_name)
        lhs = get_values(df, keyword_lhs)
        rhs = get_values(df, keyword_rhs)
        len(lhs) == len(rhs)
        for i, (lhs_unit, rhs_unit) in enumerate(zip(lhs, rhs)):
            if lhs_unit != lhs_unit or rhs_unit != rhs_unit:
                raise AssertionError("Incorrect data format")
    except Exception:
        raise AssertionError("Incorrect data format")
    else:
        return lhs, rhs


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
    """Search for a keyword in the entire DataFrame and
    returns associated values"""
    try:
        isinstance(df, DataFrame)

        # Search for a keyword in the entire DataFrame
        col = df[keyword]

    except Exception as e:
        raise AssertionError(f"Error: {e}")

    return col


def normalize(values: DataFrame) -> DataFrame:
    """Scale values do they are between 0 and 1
    in a DataFrame"""
    nvalues = []
    for i, unit in enumerate(values):
        nvalues.insert(i, unit / values.max())

    return DataFrame(nvalues)


def normalize_list(values: list) -> list:
    """Scale values do they are between 0 and 1
    in a list"""
    nvalues = []
    for i, unit in enumerate(values):
        nvalues.insert(i, unit / max(values))

    return nvalues
