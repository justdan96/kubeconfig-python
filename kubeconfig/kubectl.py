import subprocess

from shutil import which

from . import exceptions


def run(kubeconfig=None, subcmd_args=None):
    """Run a kubectl command.

    :param kubeconfig:
    :param subcmd_args:
    :raise: KubectlCommandError when kubectl exits with an error.
    :rtype: bytes
    """
    if not which("kubectl"):
        raise exceptions.KubectlNotFoundError

    args = ["kubectl"]
    if kubeconfig:
        args += ["--kubeconfig", kubeconfig]
    if subcmd_args:
        args += subcmd_args
    proc = subprocess.run(
        args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
        universal_newlines=True)
    if proc.returncode:
        raise exceptions.KubectlCommandError(proc.stdout)
    return proc.stdout.strip()
