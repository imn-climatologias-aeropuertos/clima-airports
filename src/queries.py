from typing import Optional

import pandas as pd

columns = [
    "date",
    "year",
    "month",
    "day",
    "hour",
    "minute",
    "wind_direction",
    "wind_speed",
    "wind_gust",
    "visibility",
    "cavok",
    "weather_intensity",
    "weather_description",
    "weather_precipitation",
    "weather_obscuration",
    "sky_layer1_cover",
    "sky_layer1_height",
    "sky_layer1_cloud",
    "sky_layer2_cover",
    "sky_layer2_height",
    "sky_layer2_cloud",
    "sky_layer3_cover",
    "sky_layer3_height",
    "sky_layer3_cloud",
    "sky_layer4_cover",
    "sky_layer4_height",
    "sky_layer4_cloud",
    "temperature",
    "dewpoint",
    "pressure",
]


def read_metars_csv(
    station_name: str = "mroc",
    filepath: Optional[str] = None,
) -> pd.DataFrame:
    """Reads a METAR's CSV file and sets the 'date' column as the index.

    Args:
        station_name (str)
        filename (str, optional):  Defaults to "metars.csv".

    Returns:
        pd.DataFrame
    """
    if filepath:
        df = pd.read_csv(filepath, parse_dates=["date"], usecols=columns)
    else:
        df = pd.read_csv(
            f"./data/{station_name}/metars.csv", parse_dates=["date"], usecols=columns
        )
    df = df.set_index(["date"])

    return df


def by_year(df: pd.DataFrame, start: int, end: Optional[int] = None) -> pd.DataFrame:
    """Returns a DataFrame selected by the `start` and `end` (if provided, excluded) years.

    Args:
        df (pd.DataFrame)
        start (int)
        end (Optional[int], optional): Defaults to None.

    Returns:
        pd.DataFrame
    """
    if end is None:
        return df.query(f"index.dt.year == {start}")

    return df.query(f"index.dt.year >= {start} and index.dt.year < {end}")


def by_month(df: pd.DataFrame, start: int, end: Optional[int] = None) -> pd.DataFrame:
    """Returns a DataFrame selected by the `start` and `end` (if provided, excluded) months.

    Args:
        df (pd.DataFrame)
        start (int)
        end (Optional[int], optional): Defaults to None.

    Returns:
        pd.DataFrame
    """
    if end is None:
        return df.query(f"index.dt.month == {start}")

    return df.query(f"index.dt.month >= {start} and index.dt.month < {end}")


def by_day(df: pd.DataFrame, start: int, end: Optional[int] = None) -> pd.DataFrame:
    """Returns a DataFrame selected by the `start` and `end` (if provided, excluded) days.

    Args:
        df (pd.DataFrame)
        start (int)
        end (Optional[int], optional): Defaults to None.

    Returns:
        pd.DataFrame
    """
    if end is None:
        return df.query(f"index.dt.day == {start}")

    return df.query(f"index.dt.day >= {start} and index.dt.day < {end}")


def by_hour(df: pd.DataFrame, start: int, end: Optional[int] = None) -> pd.DataFrame:
    """Returns a DataFrame selected by the `start` and `end` (if provided, excluded) hours.

    Args:
        df (pd.DataFrame)
        start (int)
        end (Optional[int], optional): Defaults to None.

    Returns:
        pd.DataFrame
    """
    if end is None:
        return df.query(f"index.dt.hour == {start}")

    return df.query(f"index.dt.hour >= {start} and index.dt.hour < {end}")
