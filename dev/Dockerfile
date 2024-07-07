FROM --platform=linux/amd64 ubuntu:22.04

SHELL ["/bin/bash", "-c"]

RUN apt update -y
RUN apt install -y make
RUN apt install -y curl
RUN apt install -y build-essential
RUN apt install -y libssl-dev
RUN apt install -y zlib1g-dev
RUN apt install -y libbz2-dev
RUN apt install -y libreadline-dev
RUN apt install -y libsqlite3-dev
RUN apt install -y git
RUN apt install -y libncursesw5-dev
RUN apt install -y xz-utils
RUN apt install -y tk-dev
RUN apt install -y libxml2-dev
RUN apt install -y libxmlsec1-dev
RUN apt install -y libffi-dev
RUN apt install -y liblzma-dev

RUN curl https://pyenv.run | bash

RUN echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
RUN echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
RUN echo 'eval "$(pyenv init -)"' >> ~/.bashrc

ENV PYENV_ROOT="$HOME/.pyenv"
ENV PATH="$PYENV_ROOT/bin:$PATH"

RUN eval "$(pyenv init -)" && \
    pyenv install 3.10.13 && \
    pyenv global 3.10.13
