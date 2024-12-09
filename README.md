# Dotfiles symlinked on my machine

### Install with stow:

```bash
stow  .

```

注意需要 tpm 的话需要自己下载 tpm

# clone this project

ZDOTDIR=~/.config/zsh
git clone --branch kickstart https://github.com/getantidote/zdotdir $ZDOTDIR

# source the .zshenv from ZDOTDIR

[[-f ~/.zshenv]] && mv -f ~/.zshenv ~/.zshenv.bak
echo ". $ZDOTDIR/.zshenv" > ~/.zshenv

# start a new zsh session

zsh

下载 tpm
git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm

### Homebrew installation:

```bash
# Leaving a machine
brew leaves > leaves.txt

# Fresh installation
xargs brew install < leaves.txt
```
