# aoai-chat

A command line tool for chatting with Large Language Models (LLMs) like GPT-3 powered by Azure OpenAI Service.

## Installation

```bash
$ pip install git+https://github.com/OpenJNY/aoai-chat.git
```

You also need to specify the following variables:

- `OPENAI_API_BASE`: Your OpenAI API base URL
- `OPENAI_API_KEY`: Your OpenAI API key
- `OPENAI_API_VERSION`: Your OpenAI API version

There are two ways to set those variables, through either a configuration file or environment variables.

### 1. config.yml

The default location of the configuration file is `${XDG_CONFIG_HOME}/aoai-chat/config.yml`, and it's automatically created when you run `aoai-chat` for the first time. On Linux, the `${XDG_CONFIG_HOME}` is typically `~/.config/`, whereas its' `%LOACLAPPDATA%` on Windows.

```yml
# ~/.config/aoai-chat/config.yml

OPENAI_API_BASE: <your-openai-api-base> # e.g. https://foo.openai.azure.com/
OPENAI_API_KEY: <your-openai-api-key> # e.g. 1234567890abcdef1234567890abcdef
OPENAI_API_VERSION: <your-openai-api-version> # e.g. '2023-05-15'
```

### 2. environment variables

Alternatively, you can set them via environment variables as follows:

```bash
export OPENAI_API_BASE=<your-openai-api-base> # e.g. https://foo.openai.azure.com/
export OPENAI_API_KEY=<your-openai-api-key> # e.g. 1234567890abcdef1234567890abcdef
export OPENAI_API_VERSION=<your-openai-api-version> # e.g. 2023-05-15
```


## Usage

```bash
# interactive mode
$ aoai-chat

# one-shot mode 
$ aoai-chat "Hi, there"

# input an additional context via stdin
$ cat README.md | aoai-chat "Summarize this markdown file"

# specify model
$ aoai-chat --model gpt4 "Show me what you got"
```
