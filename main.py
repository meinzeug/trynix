from core.config import Config
from core.logger import init_logging
from db.init_db import init_db


def main() -> None:
    config = Config.load('config.json')
    init_logging(config.log_dir)
    init_db(config.db_path)
    print('trynix initialized. database at', config.db_path)


if __name__ == '__main__':
    main()
