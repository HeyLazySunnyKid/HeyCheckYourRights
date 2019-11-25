# HeyCheckYourRights
Check rights of your hosts and group them in inventory


This is ansible playbook for grouping your inventory hostnames on special groups:
    - unreachable
    - ping
    - reachable
    - best

## Usage


```bash
git clone https://github.com/HeyLazySunnyKid/HeyCheckYourRights.git
cd HeyCheckYourRights

# If you want group all your hosts in inventory file
ansible-playbook -i <inventory_file> heycheckyourrights.yml

# If you want limit hosts, always add localhost to your limit field
ansible-playbook -i <inventory_file> heycheckyourrights.yml --limit "localhost <limit group>"
```


