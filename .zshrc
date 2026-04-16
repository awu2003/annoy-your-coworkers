export PATH="$HOME/.local/bin:$PATH"

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
add-zsh-hook precmd _annoy_precmd
