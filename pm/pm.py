import click
import container as ct
import vm


@click.group()
def proxmox_manage():
    pass


@proxmox_manage.group()
def container():
    pass


@proxmox_manage.group()
def vm():
    pass


@container.command(help="Run a command on the container")
@click.option("--container", required=True, help="container id or name")
@click.option("--command", required=True, help="command to run on container")
def run(container, command):
    ct.run_command(container, command)


@container.command(help="Update all containers using pacman")
@click.option("--noconfirm", is_flag=True, show_default=True, default=False)
@click.option("--cleanup", is_flag=True, show_default=True, default=False)
@click.option("--noconfirm-cleanup", is_flag=True, show_default=True, default=False)
def update_all(noconfirm, cleanup, noconfirm_cleanup):
    ct.update_all(noconfirm, cleanup, noconfirm_cleanup)


if __name__ == "__main__":
    proxmox_manage()
