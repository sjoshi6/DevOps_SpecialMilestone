# DevOps_SpecialMilestone

For CSC 791, as the Special milestone holds more weightage, we have implemeted
the Special Milestone as a combination of two seperate milestone tasks.

##Task 1: Setup a Ganglia Monitoring System across the deployed servers.

Ganglia is used for monitoring the CPU, I/O Statistics, and Network performance of servers in a distributed environment.
A ganglia Monitoring system has two components 
- 1. A master called Gmetad
- 2. Multiple slaves --> each of which is a deployment server (in our case 2 Nodes)

####The master setup steps are as follows:

Before the setup begins we need a user with root permission to edit the conf files.

######Setup:

- 1. Installing the Ganglia master and PHP frontend 
```
sudo apt-get install -y ganglia-monitor rrdtool gmetad ganglia-webfrontend
```
- 2. Copying the necessary files 
```
sudo cp /etc/ganglia-webfrontend/apache.conf /etc/apache2/sites-enabled/ganglia.conf
```
- 3. sudo vi /etc/ganglia/gmetad.conf    --> Edit the code snippet shown below
```
data_source "devops_server_cluster" localhost
```

- 4. sudo vi /etc/ganglia/gmond.conf     --> Make the changes shown below
```
[...]
cluster {
  name = "devops_server_cluster" 
  owner = "unspecified"
  latlong = "unspecified"
  url = "unspecified"
}
[...]
//////////////////////////////////////////////////////
[...]
udp_send_channel   {
  #mcast_join = 239.2.11.71 ## commented out this line
  host = localhost
  port = 8649
  ttl = 1
}
[...]
/////////////////////////////////////////////////////
[...]
udp_recv_channel {
  #mcast_join = 239.2.11.71 ## commented out this line
  port = 8649
  #bind = 239.2.11.71 ## commented out this line
}
```
- 5. Restart Ganglia-monitor, Gmetad and Apache.
```
sudo service ganglia-monitor restart && sudo service gmetad restart && sudo service apache2 restart
```
####The slave setup steps are as follows:

The below steps have to be manually performed on all slave nodes.

######Setup:

- 1. Installing the Ganglia Gmond process on Slaves
```
sudo apt-get install -y ganglia-monitor
```
- 2. Similar to the master edit the slave config file
```
sudo vi /etc/ganglia/gmond.conf

//////////////////////////////////

[...]
cluster {
  name = "devops_server_cluster"
  owner = "unspecified"
  latlong = "unspecified"
  url = "unspecified"
[...]

///////////////////////////////////

[...]
udp_send_channel {
  #mcast_join = 239.2.11.71   ## Commented this line
  host = x.x.x.x   ## IP address of master node
  port = 8649
  ttl = 1
}
[...]

///////////////////////////////////
Comment the udp_recv_channels block
```

- 3. Restarting the monitors on all slaves
```
sudo service ganglia-monitor restart
```

Screenshot of the Ganglia Monitoring Tool.
