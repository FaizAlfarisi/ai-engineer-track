import logging

log = logging.getLogger(__name__)

def totals(rows):
    log.info("read %s rows", len(rows))
    out = {}
    for r in rows:
        out[r["team"]] = out.get(r["team"], 0.0) + float(r["score"])
    return out
