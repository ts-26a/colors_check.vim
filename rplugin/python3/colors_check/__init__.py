import os
from glob import glob
from shutil import move, rmtree
from subprocess import run
from requests import get
import re

import neovim


@neovim.plugin
class colors_check:
    def __init__(self, nvim):
        self.nvim = nvim

    def system(self, s):
        run(str(s).split())

    def echo(self, msg):
        self.nvim.command(f"echo '{msg}'")

    def colors_check_url(self, url):
        home_dir = os.path.expanduser("~")
        name = url.split("/")[-1]
        os.makedirs(f"{home_dir}/.cache/colors_check/{name}/colors", exist_ok=True)
        with open(f"{home_dir}/.cache/colors_check/{name}/colors/{name}.vim", "w") as f:
            f.write(get(url).text)
        self.nvim.command(f"set runtimepath+=~/.cache/colors_check/{name}")
        self.nvim.command(f"colorscheme {name}")

    @neovim.command("ColorsCheck", nargs="*")
    def colors_check(self, arg):
        home_dir = os.path.expanduser("~")
        rtp = None
        if not len(arg):
            self.nvim.command("echoerr 'Colorscheck must have at least one argument.'")
            raise SystemExit(1)
        elif len(arg) == 1:
            (repo,) = arg
            if re.search(r"https?://", repo):
                self.colors_check_url(repo)
                raise SystemExit(0)
            name = repo.split("/")[1]
            name = name.replace("vim-", "")
            name = name.replace(".vim", "")
            name = name.replace("-", "_")
        elif len(arg) == 2:
            repo, name = arg
        elif len(arg) == 3:
            repo, name, rtp = arg
        else:
            self.nvim.command(
                "echoerr 'Colorscheck can only take two arguments at most.'"
            )
            raise SystemExit(1)
        self.system(
            f"git clone https://github.com/{repo}.git {home_dir}/.cache/colors_check/{name}"
        )
        if rtp is not None:
            os.makedirs(f"{home_dir}/.cache/colors_check/tmp", exist_ok=True)
            dir_old = f"{home_dir}/.cache/colors_check/{name}/{rtp}"
            dir_ = f"{home_dir}/.cache/colors_check/{name}"
            for fle in glob(f"{dir_old}/*", recursive=True):
                move(fle, f"{home_dir}/.cache/colors_check/tmp")
            rmtree(dir_)
            os.makedirs(dir_)
            for fle in glob(f"{home_dir}/.cache/colors_check/tmp/*", recursive=True):
                move(fle, dir_)
            os.rmdir(f"{home_dir}/.cache/colors_check/tmp")
        self.nvim.command(f"set runtimepath+=~/.cache/colors_check/{name}")
        self.nvim.command(f"colorscheme {name}")
        return None

    @neovim.command("ColorsCacheClean")
    def colorscacheclean(self):
        home_dir = os.path.expanduser("~")
        rmtree(f"{home_dir}/.cache/colors_check")
        os.mkdir(f"{home_dir}/.cache/colors_check")
