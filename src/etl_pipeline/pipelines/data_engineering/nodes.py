import pandas as pd
import logging

from typing import Union, List

logger = logging.getLogger(__name__)


def interpolate_missing_values(
    df: pd.DataFrame,
    cols: Union[List[str], str]
) -> pd.DataFrame:
    """
    Interpolate missing values in specified columns using the average of adjacent valid values.

    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame containing time-series data.
    cols : Union[List[str], str]
        Column or list of columns to interpolate.

    Returns
    -------
    pd.DataFrame
        DataFrame with missing values interpolated in the specified columns.
    """
    if isinstance(cols, str):
        cols = [cols]

    missing_cols = set(cols) - set(df.columns)
    if missing_cols:
        raise ValueError(f"Missing required columns in DataFrame: {missing_cols}")

    df = df.sort_values("timestamp").reset_index(drop=True).copy()

    for col in cols:
        missing_before = df[col].isna().sum()
        logger.info(f"[{col}] Missing values before interpolation: {missing_before}")

        df[col] = df[col].interpolate(method="linear", limit_direction="both")

        missing_after = df[col].isna().sum()
        logger.info(f"[{col}] Missing values after interpolation: {missing_after}")

    return df

