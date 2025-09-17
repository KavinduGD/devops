import boto3
import os
from fabric import Connection

REGION = "ap-south-1"

INSTANCE_NAME = "web-server"
AMI_ID = "ami-02d26659fd82cf299"
INSTANCE_TYPE = "t3.large"
KEY_NAME = "web-server-key"
SECURITY_GROUP = "web-server-sg"
USERNAME = "ubuntu"
KEY_PATH = "/home/kavindu-gihan/Downloads/web-server-key.pem"
VPC_ID = "Add correct vpc"
DESCRIPTION = "Security group for web server with SSH and HTTP access"

# Use client for key management
ec2_client = boto3.client("ec2", region_name=REGION)


def create_key(KEY_NAME, KEY_PATH):
    print("Checking if key pair exists...")

    try:
        ec2_client.describe_key_pairs(KeyNames=[KEY_NAME])
        print(f"Key pair '{KEY_NAME}' already exists in AWS.")

        if os.path.exists(KEY_PATH):
            print(f"Key file '{KEY_PATH}' already exists. Skipping.")
        else:
            print(
                f"⚠️ Key pair exists in AWS but PEM file missing locally.\n"
                f"You cannot download it again. Delete and recreate the key pair if needed."
            )
        return

    except ec2_client.exceptions.ClientError as e:
        if "InvalidKeyPair.NotFound" in str(e):
            print("Key not found in AWS. Creating new key pair...")
        else:
            raise  # re-raise unexpected errors

    # Create new key pair
    key_pair = ec2_client.create_key_pair(
        KeyName=KEY_NAME,
        KeyType="rsa",
        KeyFormat="pem"
    )

    with open(KEY_PATH, "w") as file:
        file.write(key_pair["KeyMaterial"])
    os.chmod(KEY_PATH, 0o400)

    print(f"✅ Key pair '{KEY_NAME}' created and saved to {KEY_PATH}")


def create_security_group(sg_name, description, vpc_id):
    print("Checking if security group exists...")

    try:
        response = ec2_client.describe_security_groups(GroupNames=[sg_name])
        sg_id = response["SecurityGroups"][0]["GroupId"]
        print(f"Security group '{sg_name}' already exists: {sg_id}")
        return sg_id
    except ec2_client.exceptions.ClientError as e:
        if "InvalidGroup.NotFound" in str(e):
            print("Security group not found. Creating new one...")
        else:
            raise

    # Create security group
    sg = ec2_client.create_security_group(
        GroupName=sg_name,
        Description=description,
        VpcId=vpc_id
    )
    sg_id = sg["GroupId"]
    print(f"✅ Created security group '{sg_name}' with ID: {sg_id}")

    # Add inbound rules (SSH + HTTP)
    ec2_client.authorize_security_group_ingress(
        GroupId=sg_id,
        IpPermissions=[
            {
                "IpProtocol": "tcp",
                "FromPort": 22,
                "ToPort": 22,
                "IpRanges": [{"CidrIp": "0.0.0.0/0"}],  # SSH
            },
            {
                "IpProtocol": "tcp",
                "FromPort": 80,
                "ToPort": 80,
                "IpRanges": [{"CidrIp": "0.0.0.0/0"}],  # HTTP
            }
        ]
    )
    print(f"✅ rules added to '{sg_name}'")

    return sg_id


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


def setup_web_server(ip, USERNAME, KEY_PATH):
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

    print("🚀 Installing Apache web server...")
    c.run("sudo apt update -y  > /dev/null  ")
    c.run("sudo apt install -y apache2  > /dev/null")
    c.run("sudo systemctl start apache2  > /dev/null")
    c.run("sudo systemctl enable apache2  > /dev/null")
    c.run("sudo systemctl status apache2 --no-pager")

    print("🚀 Installing wget , unzip...")
    c.run("sudo apt install -y wget unzip  > /dev/null")

    print("🚀 Downloading web files...")
    c.run("wget https://www.tooplate.com/zip-templates/2143_inner_peace.zip  -O /tmp/webfiles.zip  > /dev/null")
    c.run("unzip /tmp/webfiles.zip -d /tmp/  > /dev/null")

    print("🚀 Deploying web files...")
    c.run("sudo cp -r /tmp/2143_inner_peace/* /var/www/html/  > /dev/null")
    c.run("sudo systemctl restart apache2  > /dev/null")

    print(f"✅ Web server setup complete. Access it at http://{ip}")


create_key(KEY_NAME, KEY_PATH)
create_security_group(SECURITY_GROUP, DESCRIPTION, VPC_ID)
web_server_ip = create_instance(
    AMI_ID, INSTANCE_TYPE, KEY_NAME, SECURITY_GROUP, INSTANCE_NAME)
setup_web_server(web_server_ip, USERNAME, KEY_PATH)
