from pathlib import Path
import subprocess
from typing import Callable
import git
from git import Repo


OnVisit = Callable[[Repo], None]


def visit_submodule_owners(repo_path: Path, on_visit: OnVisit):
    repo = git.Repo(repo_path)
    if len(repo.submodules) == 0:
        return
    on_visit(repo)
    for submodule in repo.submodules:
        visit_submodule_owners(repo_path / submodule.path, on_visit)


def init_submodule(cwd: str):
    print(f"updating submodules on {cwd}...")
    subprocess.check_call(
        "git submodule update --init --recursive", shell=True, cwd=cwd
    )


visit_submodule_owners(Path(), lambda repo: init_submodule(repo.working_dir))
