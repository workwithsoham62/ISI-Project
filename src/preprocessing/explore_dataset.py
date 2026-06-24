"""Explore dataset utilities."""

def summarize(df):
    """Return a brief summary of a DataFrame-like object.

    Args:
        df: DataFrame-like object with `shape` and `head`.

    Returns:
        dict: summary statistics placeholder.
    """
    return {"rows": getattr(df, "shape", (None,))[0]}
