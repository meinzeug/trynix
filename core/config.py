from dataclasses import dataclass
from pathlib import Path
import json

@dataclass
class Config:
    db_path: Path = Path('.trynix/trynix.db')
    log_dir: Path = Path('.trynix/logs')
    workspace_dir: Path = Path('workspace')
    tts_enabled: bool = True
    github_user: str | None = None
    github_token: str | None = None

    @classmethod
    def load(cls, path: Path | str) -> 'Config':
        path = Path(path)
        if path.exists():
            data = json.loads(path.read_text())
            return cls(
                db_path=Path(data.get('db_path', cls.db_path)),
                log_dir=Path(data.get('log_dir', cls.log_dir)),
                workspace_dir=Path(data.get('workspace_dir', cls.workspace_dir)),
                tts_enabled=data.get('tts_enabled', cls.tts_enabled),
                github_user=data.get('github_user'),
                github_token=data.get('github_token'),
            )
        return cls()

    def save(self, path: Path | str) -> None:
        path = Path(path)
        path.write_text(
            json.dumps(
                {
                    'db_path': str(self.db_path),
                    'log_dir': str(self.log_dir),
                    'workspace_dir': str(self.workspace_dir),
                    'tts_enabled': self.tts_enabled,
                    'github_user': self.github_user,
                    'github_token': self.github_token,
                },
                indent=2,
            )
        )


CONFIG_PATH = Path('config.json')
CONFIG = Config.load(CONFIG_PATH)
