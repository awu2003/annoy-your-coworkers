import fnmatch
from typing import Optional


def find_match(command: str, rules: list) -> Optional[dict]:
    """Return the first rule whose pattern matches the given command, or None."""
    command = command.strip()
    for rule in rules:
        pattern = rule.get("pattern", "")
        match_type = rule.get("match_type", "prefix")
        if match_type == "exact" and command == pattern:
            return rule
        elif match_type == "prefix" and command.startswith(pattern):
            return rule
        elif match_type == "glob" and fnmatch.fnmatch(command, pattern):
            return rule
    return None
