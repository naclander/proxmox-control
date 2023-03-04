import subprocess
from dataclasses import dataclass


@dataclass
class ContainerData:
    container_id: str
    status: str
    container_name: str


def run_command_interactive(command):
    subprocess.run(command, shell=True)


def run_command_noninteractive(command):
    result = subprocess.run([command.split(" ")], stdout=subprocess.PIPE)
    return [x.split() for x in result.stdout.decode("utf-8").split("\n")]


def list_proxmox_containers():
    # result = subprocess.run(["pct", "list"], stdout=subprocess.PIPE)
    # containers_list = [x.split() for x in result.stdout.decode("utf-8").split("\n")]

    containers_list = run_command_noninteractive("pct list")
    containers_data_dict = {}
    for c in containers_list[1:-1]:
        container_id = container[0]
        container_status = container[1]
        container_name = container[2]

        containers_data_dict[container_name] = ContainerData(
            container_id, container_status, container_name
        )

    print(containers_data_dict)
    return containers_data_dict
