from dataclasses import dataclass
from pathlib import Path
import json

@dataclass
class Config:
    db_path: Path = Path('.trynix/trynix.db')
    log_dir: Path = Path('.trynix/logs')

    @classmethod
    def load(cls, path: Path | str) -> 'Config':
        path = Path(path)
        if path.exists():
            data = json.loads(path.read_text())
            return cls(db_path=Path(data.get('db_path', cls.db_path)),
                       log_dir=Path(data.get('log_dir', cls.log_dir)))
        return cls()
