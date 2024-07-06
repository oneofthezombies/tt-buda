from pathlib import Path
import subprocess
import platform
import distro

import git


def run(*args, **kwargs):
    if not "shell" in kwargs:
        kwargs["shell"] = True
    subprocess.check_call(*args, **kwargs)


def get_os_distribution():
    os = platform.system()
    distribution = ""
    if os == "Darwin":
        return "macos"
    elif os == "Linux":
        distribution = distro.id()
        if distribution == "ubuntu":
            return "ubuntu"
    raise Exception(
        f"Not supported os distribution. os: {os} distribution: {distribution}"
    )


def init_git_submodule_rec(repo_path: Path):
    repo = git.Repo(repo_path)
    if len(repo.submodules) == 0:
        return

    cwd = repo.working_dir
    print(f"updating submodules on {cwd}...")
    run("git submodule update --init --recursive", cwd=cwd)
    run("git lfs fetch", cwd=cwd)
    run("git lfs checkout", cwd=cwd)

    for submodule in repo.submodules:
        init_git_submodule_rec(repo_path / submodule.path)


def install_docs_dependencies():
    print("install docs dependencies...")
    os_distribution = get_os_distribution()
    if os_distribution == "ubuntu":
        run("sudo apt-get update -y")
        run("sudo apt-get install -y doxygen")
        run("sudo apt-get install -y graphviz")
        run("sudo apt-get install -y texlive-full")
    elif os_distribution == "macos":
        run("brew install doxygen")
        run("brew install graphviz")
        run("brew install texlive")


init_git_submodule_rec(Path())
install_docs_dependencies()
