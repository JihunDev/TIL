# Shell Setting

## Homebrew

```shell
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

 [Homberw HomePage](https://brew.sh/index_ko)



## iTerm2

### Theme
[oceanic-next-iterm](https://github.com/mhartington/oceanic-next-iterm)
- Preferences > Profiles > Colors > Color Persets 선택

## zsh and oh-my-zsh

### zsh with brew install
```shell
$ brew update
$ brew install zsh
```

### install with curl
```shell
$ sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```

### Change Shell
```shell
$ chsh -s `which zsh`
```



## oh-my-zsh Setting



## Powerlevel9k Themes

```shell
$ git clone https://github.com/bhilburn/powerlevel9k.git ~/.oh-my-zsh/custom/themes/powerlevel9k

$ vim ~/.zshrc

# Theme
ZSH_THEME="powerlevel9k/powerlevel9k"

POWERLEVEL9K_MODE='awesome-fontconfig'
POWERLEVEL9K_SHORTEN_DIR_LENGTH=2
POWERLEVEL9K_RIGHT_PROMPT_ELEMENTS=(status node_version)
POWERLEVEL9K_LEFT_PROMPT_ELEMENTS=(dir vcs newline)

POWERLEVEL9K_OS_ICON_BACKGROUND="white"
POWERLEVEL9K_OS_ICON_FOREGROUND="blue"
POWERLEVEL9K_DIR_HOME_FOREGROUND="white"
POWERLEVEL9K_DIR_HOME_SUBFOLDER_FOREGROUND="white"
POWERLEVEL9K_DIR_DEFAULT_FOREGROUND="white"

# Disable dir/git icons
POWERLEVEL9K_HOME_ICON=''
POWERLEVEL9K_HOME_SUB_ICON=''
POWERLEVEL9K_FOLDER_ICON=''
POWERLEVEL9K_VCS_GIT_ICON=''
POWERLEVEL9K_VCS_STAGED_ICON='\u00b1'
POWERLEVEL9K_VCS_UNTRACKED_ICON='\u25CF'
POWERLEVEL9K_VCS_UNSTAGED_ICON='\u00b1'
POWERLEVEL9K_VCS_INCOMING_CHANGES_ICON='\u2193'
POWERLEVEL9K_VCS_OUTGOING_CHANGES_ICON='\u2191'
```



## fonts

```shell
$ brew tap caskroom/fonts
$ brew cask install font-meslo-nerd-font
```



## plugins

### zsh-autosuggestions
```shell
# 설치
$ brew install zsh-autosuggestions
$ vi .zshrc
# 추가
plugins=(git
zsh-autosuggestions)
```

### Syntax highlighting

```shell
# 설치
$ brew install zsh-syntax-highlighting
$ vi .zshrc
# 추가
plugins=(git
zsh-syntax-highlighting
zsh-autosuggestions)
```
### autojump

```shell
# 설치
$ brew install autojump
$ vi .zshrc
# 추가
plugins=(git
autojump
zsh-syntax-highlighting
zsh-autosuggestions)
```

### 코드 적용

```shell
$ source ~/.zshrc
```