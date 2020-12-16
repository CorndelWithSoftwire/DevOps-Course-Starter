FROM python:3.8-buster
WORKDIR /todo
ENV PYENV_ROOT="$HOME/.pyenv"
ENV PATH="$PYENV_ROOT/bin:$PATH"
COPY . .
RUN pip install poetry
RUN poetry install --no-root

EXPOSE 5000

ENTRYPOINT ["./run.sh"]