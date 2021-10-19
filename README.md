# HeyCheckYourRights
Check rights of your hosts from ansible inventory and show errors on them.

## Requirements
- python3
- ansible

## Usage

```bash
git clone https://github.com/HeyLazySunnyKid/HeyCheckYourRights.git
# This is just bash script in bin directory.
export PATH=$PATH:`pwd`/bin
heycheckyourrights --help # read help message

### Examples

```bash
# Check access to all hosts in /etc/ansible/hosts
heycheckyourrights

# Check access to mygroup in ./myinventory
heycheckyourrights -i myinventory --limit='mygroup'

# Doesn't ping to all hosts in ./myinventory
heycheckyourrights -i myinventory --skip-tags='ping'
```
