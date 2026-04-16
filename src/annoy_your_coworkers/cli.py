import argparse
import subprocess
from pathlib import Path

from .config import CONFIG_FILE, load_config, create_example_config
from .matcher import find_match

SHELL_HOOK = """\
# annoy-your-coworkers shell hook
# Add this to your ~/.zshrc, then run: source ~/.zshrc
_annoy_last_cmd=""

function _annoy_preexec() {
    _annoy_last_cmd="$1"
}

function _annoy_precmd() {
    if [[ -n "$_annoy_last_cmd" ]]; then
        (annoy check "$_annoy_last_cmd" &>/dev/null &)
        _annoy_last_cmd=""
    fi
}

autoload -Uz add-zsh-hook
add-zsh-hook preexec _annoy_preexec
add-zsh-hook precmd _annoy_precmd"""


def cmd_install(_args):
    created = create_example_config()
    config_note = "(An example config was created for you)" if created else ""

    print(f"""\
{SHELL_HOOK}

{"─" * 60}
Setup instructions:

  1. Add the hook above to your ~/.zshrc
  2. Run: source ~/.zshrc
  3. Edit your config: {CONFIG_FILE}
     {config_note}

Config format:
  {{
    "rules": [
      {{
        "pattern": "git push",
        "mp3": "/path/to/sound.mp3",
        "match_type": "prefix"
      }}
    ]
  }}

match_type options:
  prefix  command starts with pattern  (default)
          e.g. "git push" matches "git push origin main"
  glob    fnmatch wildcard pattern
          e.g. "make *" matches "make build"
  exact   exact string match\
""")


def cmd_check(args):
    config = load_config()
    rule = find_match(args.cmd, config.get("rules", []))
    if rule is None:
        return
    mp3 = rule.get("mp3", "")
    if not mp3 or not Path(mp3).exists():
        return
    subprocess.Popen(
        ["afplay", mp3],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        start_new_session=True,
    )


def main():
    parser = argparse.ArgumentParser(
        prog="annoy",
        description="Play audio files when terminal commands complete.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("install", help="Print shell hook snippet and setup instructions")

    p_check = sub.add_parser("check", help="(Internal) Check command and play audio if matched")
    p_check.add_argument("cmd", help="The command that just ran")

    args = parser.parse_args()
    if args.command == "install":
        cmd_install(args)
    elif args.command == "check":
        cmd_check(args)


if __name__ == "__main__":
    main()
