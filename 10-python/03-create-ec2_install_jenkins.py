import boto3
import time
from fabric import Connection


REGION = "ap-south-1"


INSTANCE_NAME_1 = "web1"
AMI_ID_1 = "ami-02d26659fd82cf299"
INSTANCE_TYPE_1 = "t3.large"
KEY_NAME_1 = "web1-key"
SECURITY_GROUP_1 = "web1-sg"
USERNAME_1 = "ubuntu"
KEY_PATH_1 = "/home/kavindu-gihan/Downloads/web1-key.pem"


INSTANCE_NAME_2 = "web2"
AMI_ID_2 = "ami-01b6d88af12965bb6"
INSTANCE_TYPE_2 = "t3.large"
KEY_NAME_2 = "web2-key"
SECURITY_GROUP_2 = "web2-sg"
USERNAME_2 = "ec2-user"
KEY_PATH_2 = "/home/kavindu-gihan/Downloads/web2-key.pem"


def instance_exists(REGION, INSTANCE_NAME):
    ec2 = boto3.resource("ec2", region_name=REGION)
    instances = ec2.instances.filter(
        Filters=[
            {"Name": "tag:Name", "Values": [INSTANCE_NAME]},
            {"Name": "instance-state-name",
                "Values": ["pending", "running", "stopping", "stopped"]},
        ]
    )
    for instance in instances:
        return instance
    return None


def create_instance(AMI_ID, INSTANCE_TYPE, KEY_NAME, SECURITY_GROUP, INSTANCE_NAME):

    existing_instance = instance_exists(
        REGION=REGION, INSTANCE_NAME=INSTANCE_NAME)

    if existing_instance:
        print(f" Ec2 instance {INSTANCE_NAME} already exits ")
        return existing_instance.public_ip_address

    else:
        ec2 = boto3.resource("ec2", region_name=REGION)

        print("🚀 Creating EC2 instance...")
        instance = ec2.create_instances(
            ImageId=AMI_ID,
            InstanceType=INSTANCE_TYPE,
            KeyName=KEY_NAME,
            MinCount=1,
            MaxCount=1,
            SecurityGroups=[SECURITY_GROUP],
            TagSpecifications=[
                {
                    "ResourceType": "instance",
                    "Tags": [
                        {"Key": "Name", "Value": INSTANCE_NAME}
                    ],
                }
            ],
        )[0]

        instance.wait_until_running()
        instance.reload()

        print(
            f"✅ EC2 Instance created: {instance.id}, Public IP: {instance.public_ip_address}")
        return instance.public_ip_address


def setup_jenkins(ip, USERNAME, KEY_PATH):
    print("🔗 Connecting via SSH...")
    c = Connection(
        host=ip,
        user=USERNAME,
        # Ensure your PEM file is in the same folder
        connect_kwargs={"key_filename": f"{KEY_PATH}"}
    )

    # check connection success
    try:
        c.open()
        print("✅ SSH connection established.")
    except Exception as e:
        print(f"❌ SSH connection failed: {e}")
        return

    print("⚙️ Updating system and installing Jenkins...")
    c.run("sudo apt update -y")
    c.run("sudo apt install -y fontconfig openjdk-21-jre wget gnupg2")

    # Add Jenkins repo & key
    c.run("sudo wget -O /etc/apt/keyrings/jenkins-keyring.asc  https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key > /dev/null")
    c.run('echo "deb [signed-by=/etc/apt/keyrings/jenkins-keyring.asc]"  https://pkg.jenkins.io/debian-stable binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null')

    c.run("sudo apt update -y")
    c.run("sudo apt install -y jenkins")

    print("🚀 Starting Jenkins service...")
    c.run("sudo systemctl enable jenkins")
    c.run("sudo systemctl start jenkins")
    c.run("sudo systemctl status jenkins --no-pager")

    print("🎉 Jenkins installed! Access it at: http://{}:8080".format(ip))
    print("👉 To get the initial admin password, run:")


instance1_ip = create_instance(AMI_ID=AMI_ID_1, INSTANCE_NAME=INSTANCE_NAME_1,
                               INSTANCE_TYPE=INSTANCE_TYPE_1, KEY_NAME=KEY_NAME_1, SECURITY_GROUP=SECURITY_GROUP_1)


instance2_ip = create_instance(AMI_ID=AMI_ID_2, INSTANCE_NAME=INSTANCE_NAME_2,
                               INSTANCE_TYPE=INSTANCE_TYPE_2, KEY_NAME=KEY_NAME_2, SECURITY_GROUP=SECURITY_GROUP_2)


print(f'instance 1 ip {instance1_ip}')
print(f'instance 2 ip {instance2_ip}')

setup_jenkins(ip=instance1_ip, USERNAME=USERNAME_1, KEY_PATH=KEY_PATH_1)
# setup_jenkins(ip=instance2_ip, USERNAME=USERNAME_2, KEY_PATH=KEY_PATH_2)
