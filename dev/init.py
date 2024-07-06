from pathlib import Path
import subprocess
from typing import Callable
import git
from git import Repo


OnVisit = Callable[[Repo], None]


def init_submodule_rec(repo_path: Path, on_visit: OnVisit):
    repo = git.Repo(repo_path)
    if len(repo.submodules) == 0:
        return
    on_visit(repo)
    for submodule in repo.submodules:
        init_submodule_rec(repo_path / submodule.path, on_visit)


def on_init_submodule(cwd: str):
    print(f"updating submodules on {cwd}...")
    subprocess.check_call(
        "git submodule update --init --recursive", shell=True, cwd=cwd
    )


init_submodule_rec(Path(), lambda repo: on_init_submodule(repo.working_dir))
