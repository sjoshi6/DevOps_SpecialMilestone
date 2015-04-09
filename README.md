# DevOps_SpecialMilestone

For CSC 791, as the Special milestone holds more weightage, we have implemeted
the Special Milestone as a combination of two seperate milestone tasks.

##Task 1: Setup a Ganglia Monitoring System across the deployed servers.

A ganglia Monitoring system has two components 
- 1. A master called Gmetad
- 2. Multiple slaves --> each of which is a deployment server (in our case 2 Nodes)

####The master setup steps are as follows:

Before the setup begins we need a user with root permission to edit the conf files.

########Setup:

- 1. sudo apt-get install -y ganglia-monitor rrdtool gmetad ganglia-webfrontend
- 2. sudo cp /etc/ganglia-webfrontend/apache.conf /etc/apache2/sites-enabled/ganglia.conf
- 3. sudo vi /etc/ganglia/gmetad.conf    --> Edit the code snippet shown below

```
data_source "devops_server_cluster" localhost
```

- 4. sudo vi /etc/ganglia/gmond.conf     --> Make the changes shown below
```
[...]
cluster {
  name = "my cluster" ## use the name from gmetad.conf
  owner = "unspecified"
  latlong = "unspecified"
  url = "unspecified"
}
[...]
//////////////////////////////////////////////////////
[...]
udp_send_channel   {
  #mcast_join = 239.2.11.71 ## comment out
  host = localhost
  port = 8649
  ttl = 1
}
[...]
/////////////////////////////////////////////////////
[...]
udp_recv_channel {
  #mcast_join = 239.2.11.71 ## comment out
  port = 8649
  #bind = 239.2.11.71 ## comment out
}
```
