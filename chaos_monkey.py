import boto.ec2
import sys

def chaos_monkey():
    conn = boto.ec2.connect_to_region(sys.argv[1],aws_access_key_id=sys.argv[2], aws_secret_access_key=sys.argv[3])
    reservations = conn.get_all_reservations()
    instances = reservations[0].instances
    instance= instances[0]
    print(instance.instance_type)


chaos_monkey()
