import logging
from pathlib import Path


def init_logging(log_dir: Path) -> None:
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / 'trynix.log'
    logging.basicConfig(
        level=logging.INFO,
        format='[%(asctime)s] %(levelname)s:%(name)s:%(message)s',
        handlers=[logging.FileHandler(log_file), logging.StreamHandler()]
    )
