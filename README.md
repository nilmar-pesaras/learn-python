# Setting up Python Environment using UV Python Packaging


This repository provides initial setup for your python development. Using UV Python packaging you can now fire up your project without taking much time in setting up your environment.

<br>

## Installation

>*note: I am using windows operating system(OS). This guide is intended for windows OS. If you are using other OS, please refer to the official uv python docs.*

<br>

**Set the powershell execution policy for the current user.**

```powershell
Set-ExecutionPolicy -ExecutionPolicy AllSigned -Scope CurrentUser
```

**Use `irm` to download the script and execute it with `iex`**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

<br>

## Shell autocompletion

To enable shell autocompletion for uv commands, run one of the following
```powershell
Add-Content -Path $PROFILE -Value '(& uv generate-shell-completion powershell) | Out-String | Invoke-Expression'
```
