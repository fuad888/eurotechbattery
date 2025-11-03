# ~/.zshrc - Fuad üçün təmiz və işlək konfiqurasiya

# --- PATH ---
export PATH="$HOME/.local/bin:$PATH"

# --- Homebrew (Apple Silicon / Intel) ---
if [ -x "/opt/homebrew/bin/brew" ]; then
  eval "$(/opt/homebrew/bin/brew shellenv)"
elif [ -x "/usr/local/bin/brew" ]; then
  eval "$(/usr/local/bin/brew shellenv)"
fi

# --- Python & Django (Virtualenv) ---
export PYENV_ROOT="$HOME/.pyenv"
[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"

# Pyenv (isteğe bağlı - əgər quraşdırmısansa)
# eval "$(pyenv init -)"
# eval "$(pyenv virtualenv-init -)"

# --- Keg-only paketlər (libffi, openssl) ---
export LDFLAGS="-L$(brew --prefix)/opt/libffi/lib -L$(brew --prefix)/opt/openssl@3/lib"
export CPPFLAGS="-I$(brew --prefix)/opt/libffi/include -I$(brew --prefix)/opt/openssl@3/include"
export PKG_CONFIG_PATH="$(brew --prefix)/opt/libffi/lib/pkgconfig:$(brew --prefix)/opt/openssl@3/lib/pkgconfig"

# --- Django Layihəsi (eurotechbattery) ---
export DJANGO_SETTINGS_MODULE=eurotechbattery.settings
export PYTHONPATH="$PYTHONPATH:/Users/fuad/Desktop/eurotechbattery"

# --- Aliaslar (qısa yollar) ---
alias ll="ls -la"
alias gs="git status"
alias gp="git pull"
alias python="python3"
alias pip="pip3"

# --- Virtualenv aktivləşdirmə (avtomatik) ---
# Əgər eurotechbattery qovluğuna girsən, .venv avtomatik aktivləşsin
eurotech_venv() {
  if [[ "$PWD" == *"/eurotechbattery"* ]] && [[ -d ".venv" ]]; then
    source .venv/bin/activate 2>/dev/null || true
  fi
}
autoload -U add-zsh-hook
add-zsh-hook chpwd eurotech_venv
eurotech_venv
