# Python and Jupyter

This Repo contains Python Devolopment Setup with Configurations and Jupyter Notebook.  

* My python setup enviropnment is based on `uv`. also cintains `requirements.txt` for `venv` setup.
* Contains `jupyter notebook` settings configurationes .. for [autocomplete and others things](mathml/README_setup.md)
* Also has `micromamba` and `conda` `ymal` settings [environment.yaml](learn/environment.yml)

**All setting can be declared completely in [`pyproject.toml` file](pyproject.toml)**

## So, To remove any conflict on vscode

**pylance causing the problem, so in code-OSS i Primarily use `pyright` or `basedpyright`, and mainly used it with `ruff`**.

* python default
* [ruff](https://docs.astral.sh/ruff/configuration/) / autopep8
* [pyright](https://microsoft.github.io/pyright/#/) or [basedpyright](https://docs.basedpyright.com/latest/configuration/config-files/)
* python debugger(not nexessary )
* but pylance works when using mypy
* i need to restart pylance everytime

### Use these only ..(maybe .or) [python tools referances](python_tools_ref.md)
