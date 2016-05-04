
from os import getcwd

import click

from platformio import app, exception, util
from platformio.commands.platforms import platforms_install as cli_platforms_install
from platformio.ide.projectgenerator import ProjectGenerator


@click.command("ide", short_help="Configure IDE for this PlatformIO project")
@click.option("--environment", "-e", metavar="<environment>")
@click.option("--project-dir", "-d", default=getcwd,
              type=click.Path(exists=True, file_okay=False, dir_okay=True,
                              writable=True, resolve_path=True))
@click.option("--ide", type=click.Choice(ProjectGenerator.get_supported_ides()))
@click.pass_context
def cli(ctx, environment, project_dir, ide):
    with util.cd(project_dir):
        config = util.get_project_config()

        if not config.sections():
            raise exception.ProjectEnvsNotAvailable()

        if not environment and config.has_option("platformio", "env_default"):
            env_default = [
                e.strip()
                for e in config.get("platformio", "env_default").split(",")]
            if len(env_default) == 1:
                environment = env_default[0]
        
        known = set([s[4:] for s in config.sections() if s.startswith("env:")])
        if environment and not environment in known:
            raise exception.UnknownEnvNames(environments, ", ".join(known))

        for section in config.sections():
            # skip main configuration section
            if section == "platformio":
                continue

            if not section.startswith("env:"):
                raise exception.InvalidEnvName(section)

            envname = section[4:]
            if not environment or envname == environment:
                pg = ProjectGenerator(project_dir, ide, config.get(section, 'board'))
                pg.generate()
