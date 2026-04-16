# annoy-your-coworkers
cli tools to annoy your coworkers while you work

## annoy

Plays an mp3 through your laptop speakers whenever a terminal command completes.

### Installation

```bash
make install
annoy install  # copy the printed snippet into ~/.zshrc
source ~/.zshrc
```

### Configuration

Edit `~/.config/annoy-your-coworkers/config.json`:

```json
{
  "rules": [
    {
      "pattern": "git push",
      "mp3": "/path/to/sound.mp3",
      "match_type": "prefix"
    }
  ]
}
```

`match_type` options:
- `prefix` — command starts with pattern (default) — e.g. `"git push"` matches `git push origin main`
- `glob` — fnmatch wildcard — e.g. `"make *"` matches `make build`
- `exact` — exact string match
