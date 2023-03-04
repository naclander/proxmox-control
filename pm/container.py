import click

import proxmox


def run_command(container, command):
    if container.isdigit():
        container_id = container
    else:
        containers = proxmox.list_proxmox_containers()
        container_id = containers[container].container_id
        click.echo(
            click.style(
                f"container {container} matched to container id {container_id}",
                fg="yellow",
            )
        )

    click.echo(
        click.style(f"Running command on container ", fg="green")
        + click.style(f"{container_id}", fg="green", bold=True)
    )
    cmd_str = f"pct exec {container_id} -- {command}"
    proxmox.run_command_interactive(cmd_str)


def update_all(no_confirm=False, cleanup=False, noconfirm_cleanup=False):
    containers = proxmox.list_proxmox_containers()
    for c in containers.values():
        cmd_str = f'pct exec {c.container_id} -- bash -c "pacman -Syu '
        if no_confirm:
            cmd_str += "--noconfirm "
        if cleanup:
            cmd_str += "&& pacman -Sc "
            if noconfirm_cleanup:
                cmd_str += "--noconfirm "
        cmd_str += '"'

        click.echo(
            click.style(f"Running command on container ", fg="green")
            + click.style(f"{c.container_id}", fg="green", bold=True)
        )
        proxmox.run_command_interactive(cmd_str)
