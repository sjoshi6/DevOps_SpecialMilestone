import boto.ec2
import sys

def chaos_monkey():
    conn = boto.ec2.connect_to_region(sys.argv[1],aws_access_key_id=sys.argv[2], aws_secret_access_key=sys.argv[3])
    reservations = conn.get_all_reservations()
    instance_list = []
    for reservation in reservations:
        instances = reservation.instances

        for instance in instances:
            instance_list.append(instance)

    print("Below is the list of available os/ instance id's specify which one to kill?")

    for instance in instance_list:
        print(str(instance.id)+ "    "+ str(instance.instance_type))

chaos_monkey()
