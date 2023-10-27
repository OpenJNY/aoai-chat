# aoai-cli

A command line tool for chatting with Large Language Models (LLMs) like GPT-3 powered by Azure OpenAI Service.

## Installation

```bash
$ pip install git+https://github.com/OpenJNY/aoai-cli.git
```

You also need to set the following environment variables:

```bash
$ export OPENAI_API_KEY=<your-openai-api-key> # e.g. 1234567890abcdef1234567890abcdef
$ export OPENAI_API_BASE=<your-openai-api-base> # e.g. https://foo.openai.azure.com/
$ export OPENAI_API_VERSION=<your-openai-api-version> # e.g. 2023-05-15

# persist the environment variables
echo <<EOF >> ~/.bashrc
export OPENAI_API_KEY=
export OPENAI_API_BASE=
export OPENAI_API_VERSION=
EOF
```


## Usage

```bash
# interactive mode
$ aoai-cli

# one-shot mode 
$ aoai-cli --prompt "Hi, there"

# input an additional context via stdin
$ cat README.md | aoai-cli --prompt "Summarize this markdown file"
```
