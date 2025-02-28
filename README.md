# PreReqs
`vagrant plugin install vagrant-hostmanager`


# Research and Development
- A review/recreation of past projects
- identify the relevant technologies for stock trading

Steps:
  1. Obtain relevant/valid Vagrant file or run `vagrant init` to get the template
  2. vagrant up | vagrant up $box e.g. --> vagrant up web01
  3. vagrant ssh | vagrant ssh $box e.g. --> vagrant ssh web01
  4. vagrant destroy | vagrant destroy $box --> vagrant destroy db01

  5. vagrant status

# check entire system for vms IMU
# vagrant global-status  
# vagrant global-status --prune # i believe cleans up cache. look this up
# use the ids to do: vagrant destroy $id

