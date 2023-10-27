import click
from langchain.chat_models import AzureChatOpenAI


def answer_prompt(ctx: click.Context, prompt: str) -> None:
    """Answer a prompt."""

    model = AzureChatOpenAI(
        deployment_name="gpt-35-turbo",
        openai_api_key=ctx.obj["config"]["OPENAI_API_KEY"],
        openai_api_base=ctx.obj["config"]["OPENAI_API_BASE"],
        openai_api_version=ctx.obj["config"]["OPENAI_API_VERSION"],
    )
    print(model.predict(prompt))

    ctx.exit(0)
