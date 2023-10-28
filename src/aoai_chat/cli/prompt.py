import click
from langchain.chat_models import AzureChatOpenAI
from rich.markdown import Markdown
from rich.console import Console
from langchain.prompts import PromptTemplate


def answer_prompt(ctx: click.Context, prompt: str) -> None:
    """Answer a prompt."""

    console = Console()
    model = AzureChatOpenAI(
        deployment_name=ctx.params["model"],
        openai_api_key=ctx.obj["config"]["OPENAI_API_KEY"],
        openai_api_base=ctx.obj["config"]["OPENAI_API_BASE"],
        openai_api_version=ctx.obj["config"]["OPENAI_API_VERSION"],
    )

    if "input" in ctx.obj:
        prompt = """{}. Take into account the following input.

Input:
---
{}
""".format(
            prompt, ctx.obj["input"]
        )

    output = model.predict(prompt)
    console.print(Markdown(output))

    ctx.exit(0)
