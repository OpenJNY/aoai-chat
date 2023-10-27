import logging
import os
import yaml
from pathlib import Path
from typing import Any, Optional, Union

import click


def config_dir() -> Path:
    xdg_config_home = os.environ.get("XDG_CONFIG_HOME")
    if xdg_config_home and Path(xdg_config_home).is_absolute():
        return Path(xdg_config_home)
    return Path.home() / ".config"


def mkdir_if_needed(path: Union[str, Path]) -> None:
    """create a directory recuresively if it doesn't exist"""
    path = Path(path)
    if not path.exists():
        os.makedirs(path, exist_ok=False)


CONFIG_BASE = config_dir() / "aoai_chat"
CONFIG_FILE = CONFIG_BASE / "config.yaml"


def load_config(ctx: click.Context, param: click.Parameter, value: Optional[str]) -> None:
    # Create a default config file if it doesn't exist
    mkdir_if_needed(CONFIG_BASE)
    if not CONFIG_FILE.is_file():
        with open(CONFIG_FILE, "w") as f:
            f.write(
                """# config.yaml
OPENAI_API_BASE: 
OPENAI_API_KEY: 
OPENAI_API_VERSION: '2023-05-15'
"""
            )

    # Load the config file
    if value and Path(value).is_file():
        config_file = Path(value)
    else:
        config_file = CONFIG_FILE

    with open(config_file, "r") as f:
        config = yaml.safe_load(f)

    # Set from environment variables if needed
    for key in ["OPENAI_API_BASE", "OPENAI_API_KEY", "OPENAI_API_VERSION"]:
        if config[key] is None:
            config[key] = os.environ.get(key)

    ctx.ensure_object(dict)
    ctx.obj["config"] = config


@click.command(help="A cli tool to interact with LLMs powered by Azure OpenAI")
@click.option(
    "--prompt",
    "prompt",
    type=str,
    help="Prompt text for the one-shot interaction mode.",
)
@click.option(
    "-v",
    "--verbose",
    is_flag=True,
    help="Enables verbose mode for debugging purposes.",
)
@click.option(
    "--config",
    type=click.Path(
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
        allow_dash=False,
        path_type=str,
    ),
    is_eager=True,
    callback=load_config,
    help="Path to the config file.",
)
@click.pass_context
def main(ctx: click.Context, prompt: str, verbose: bool, config: str) -> None:
    """Main entry point of the app."""

    for key, value in ctx.params.items():
        print(key, value)

    ctx.ensure_object(dict)
    for key, value in ctx.obj.items():
        print(key, value)
