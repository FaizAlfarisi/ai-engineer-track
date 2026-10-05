from pathlib import Path

from noisy_shop.shop import run, setup_logging

if __name__ == "__main__":
    setup_logging(True)
    ok, bad = run(str(Path(__file__).with_name("data.csv")))
    print(f"summary: ok={ok} skipped={bad}")
