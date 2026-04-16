.PHONY: install uninstall

install:
	@which pipx >/dev/null 2>&1 || (echo "Installing pipx..." && brew install pipx && pipx ensurepath)
	@which SwitchAudioSource >/dev/null 2>&1 || (echo "Installing switchaudio-osx..." && brew install switchaudio-osx)
	pipx install -e .
	@echo ""
	@echo "Run 'annoy install' to get the shell hook, then add it to your ~/.zshrc"

uninstall:
	pipx uninstall annoy-your-coworkers
