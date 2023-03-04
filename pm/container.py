import click
import subprocess

import proxmox


def run_command(container, command):
    if container.isdigit():
        container_id = container
    else:
        containers = proxmox.list_proxmox_containers()
        container_id = containers[container]

    click.echo("Running command")
    cmd_str = f"pct exec {container_id} -- {command}"
    proxmox.run_command_interactive(cmd_str)
