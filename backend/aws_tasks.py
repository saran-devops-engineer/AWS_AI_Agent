import boto3


def list_unused_eips():
    ec2 = boto3.client("ec2")
    addresses = ec2.describe_addresses()["Addresses"]
    unused = [addr["PublicIp"] for addr in addresses if "InstanceId" not in addr]

    if not unused:
        return "✅ No unused EIPs found."

    return "✅ Unused EIPs:\n" + "\n".join(unused)


def describe_all():
    ec2 = boto3.client("ec2")
    addresses = ec2.describe_addresses()["Addresses"]
    if not addresses:
        return "❌ No Elastic IPs found."

    result = "📡 Elastic IPs:\n"
    for addr in addresses:
        ip = addr.get("PublicIp", "N/A")
        instance = addr.get("InstanceId", "Not attached")
        result += f"- IP: {ip}, Instance: {instance}\n"
    return result


def list_running_instances():
    ec2 = boto3.client("ec2")
    response = ec2.describe_instances(Filters=[{"Name": "instance-state-name", "Values": ["running"]}])
    instances = []

    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            name = next((tag["Value"] for tag in instance.get("Tags", []) if tag["Key"] == "Name"), "N/A")
            instances.append(f"🟢 Name: {name}, ID: {instance['InstanceId']}")

    if not instances:
        return "❌ No running EC2 instances found."

    return "✅ Running EC2 Instances:\n" + "\n".join(instances)
