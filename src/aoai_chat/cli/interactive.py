import click


def run_interactive_mode(ctx: click.Context) -> None:
    print("interactive")
    ctx.exit(0)
