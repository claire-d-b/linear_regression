from pandas import DataFrame, read_csv


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
