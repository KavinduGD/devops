import boto3

REGION = "ap-south-1"

# Resources
ec2 = boto3.resource("ec2", region_name=REGION)
client = boto3.client("ec2", region_name=REGION)


def delete_instance_and_resources(instance_name, key_name, security_group):
    print(f"🗑️ Deleting resources for {instance_name}...")

    # Find instance by tag:Name
    instances = ec2.instances.filter(
        Filters=[{"Name": "tag:Name", "Values": [instance_name]}]
    )

    instance_ids = [i.id for i in instances]
    if not instance_ids:
        print(f"❌ No instance found with name {instance_name}")
    else:
        print(f"📌 Found instance(s): {instance_ids}")
        client.terminate_instances(InstanceIds=instance_ids)
        waiter = client.get_waiter("instance_terminated")
        waiter.wait(InstanceIds=instance_ids)
        print(f"✅ Instance(s) {instance_ids} terminated")

        # Delete attached EBS volumes (except root if needed)
        for i in instances:
            i.reload()
            for dev in i.block_device_mappings:
                vol_id = dev["Ebs"]["VolumeId"]
                try:
                    ec2.Volume(vol_id).delete()
                    print(f"   📦 Deleted EBS volume {vol_id}")
                except Exception as e:
                    print(f"   ⚠️ Could not delete volume {vol_id}: {e}")

    # Delete Security Group
    try:
        client.delete_security_group(GroupName=security_group)
        print(f"🛡️ Security group {security_group} deleted")
    except Exception as e:
        print(f"⚠️ Could not delete security group {security_group}: {e}")

    # Delete Key Pair
    try:
        client.delete_key_pair(KeyName=key_name)
        print(f"🔑 Key pair {key_name} deleted")
    except Exception as e:
        print(f"⚠️ Could not delete key pair {key_name}: {e}")


if __name__ == "__main__":
    delete_instance_and_resources(
        "web-server", "web-server-key", "web-server-sg")
    # delete_instance_and_resources("web2", "web2-key", "web2-sg")
