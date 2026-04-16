import json
import os
from pathlib import Path

CONFIG_DIR = Path(os.environ.get("ANNOY_CONFIG_DIR", "~/.config/annoy-your-coworkers")).expanduser()
CONFIG_FILE = CONFIG_DIR / "config.json"

EXAMPLE_CONFIG = {
    "rules": [
        {
            "pattern": "git push",
            "mp3": "/path/to/your/sound.mp3",
            "match_type": "prefix"
        }
    ]
}


def load_config() -> dict:
    if not CONFIG_FILE.exists():
        return {"rules": []}
    with CONFIG_FILE.open() as f:
        return json.load(f)


def create_example_config() -> bool:
    """Create an example config if none exists. Returns True if created."""
    if CONFIG_FILE.exists():
        return False
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    CONFIG_FILE.write_text(json.dumps(EXAMPLE_CONFIG, indent=2) + "\n")
    return True
