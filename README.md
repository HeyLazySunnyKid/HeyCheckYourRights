# HeyCheckYourRights
Check rights of your hosts and group them in inventory


This is ansible playbook for grouping your inventory hostnames on special groups:
- unreachable: the host is unreachable
- ping: ping from localhost to host is ok
- reachable: setup module execute without errors
- best: command under root run without errors

## Requirements
- python3
- ansible

## Usage

```bash
git clone https://github.com/HeyLazySunnyKid/HeyCheckYourRights.git
cd HeyCheckYourRights

# If you want group all your hosts in inventory file
ansible-playbook -i <inventory_file> heycheckyourrights.yml

# If you want limit hosts, always add localhost to your limit field
ansible-playbook -i <inventory_file> heycheckyourrights.yml --limit "localhost <limit group>"
```

## Example

Inventory file before execution:
```/tmp/inv
[mygroup]
a.example.com ansible_username=myuser
b.example.com 
c.example.com

[other]
a.win.com
g.example.com
f.example.com

[unreachable]
a.example.com ansible_username=myuser
b.example.com
f.example.com

[ping]
g.example.com
```

After command 
```
ansible-playbook -i /tmp/inv heycheckyourrights.yml --limit "localhost mygroup g.example.com"
```

Result:

```/tmp/inv
[mygroup]
a.example.com ansible_username=myuser
b.example.com 
c.example.com

[other]
a.win.com
g.example.com
f.example.com

[unreachable]
b.example.com
f.example.com

[ping]
a.example.com ansible_username=myuser

[best]
c.example.com
g.example.com
```
