ansible-playbook -i inventory.ini playbook.yml

1. create vm
2. add ssh key to metadata
3. specify user when user on host machine is different from the target machine

gcloud auth login
gcloud config get project
gcloud compute ssh <VM-NAME>

TODO: 
1. add teardown