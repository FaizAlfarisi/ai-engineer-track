"""H1-[DEBUG] - PROVIDED, contains 3 planted bugs. Fix this file only."""
import numpy as np
import pandas as pd

from models import EmptyDataError, ReviewRecord


def analyze_reviews(
    records: list[ReviewRecord], min_len: int, max_len: int
) -> dict:
    df = pd.DataFrame([r.model_dump() for r in records])
    df["title"] = df["title"].str.strip()
    df["body"] = df["body"].str.strip()

    body_lengths = df["body"].str.len().to_numpy(dtype=np.int64)
    duplicate_count = int(
        df.duplicated(subset=["title", "body"], keep=False).sum()
    )
    missing_note_ratio = float((df["note"] == None).mean())  # noqa: E711
    outlier_mask = (body_lengths < min_len) | (body_lengths > max_len)

    return {
        "rows": int(len(df)),
        "duplicate_count": duplicate_count,
        "missing_note_ratio": round(missing_note_ratio, 4),
        "mean_body_len": round(float(np.mean(body_lengths)), 2),
        "outlier_count": int(np.sum(outlier_mask)),
    }
