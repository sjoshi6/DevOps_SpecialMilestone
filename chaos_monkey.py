import boto.ec2
import sys
import random


######################################################################
#### Usage : python chaos_monkey.py us-west-2 accesskey secretkey ####
######################################################################


def chaos_monkey():
    conn = boto.ec2.connect_to_region(sys.argv[1],aws_access_key_id=sys.argv[2], aws_secret_access_key=sys.argv[3])
    reservations = conn.get_all_reservations()
    instance_list = []
    for reservation in reservations:
        instances = reservation.instances

        for instance in instances:
            if instance.state == "running":
                instance_list.append(instance)

    print("Below is the list of Running instances ")

    for instance in instance_list:
        print(str(instance.id)+ "    "+ str(instance.instance_type)+ " "+str(instance.image_id))

    print("Specify an image id whose machine will be destroyed at random")
    image_id = input()

    destroy_list = []

    for instance in instance_list:
        if instance.image_id == image_id:
            destroy_list.append(instance)

    destroy_number = random.randint(0, len(destroy_list)-1)

    print(destroy_number)

    print("One of the below instances will be destoryed at random !")

    print(destroy_list)

    destroy_instance = destroy_list[destroy_number]

    # Terminating a random instance

    conn.terminate_instances(instance_ids=[destroy_instance.id])

chaos_monkey()
