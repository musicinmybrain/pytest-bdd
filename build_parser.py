import pathlib

import tatsu
from setuptools.command.sdist import sdist as original_sdist


class sdist(original_sdist):
    def run(self) -> None:
        # Build the generated parser (_gherkin.py)
        grammar = pathlib.Path("pytest_bdd/parser_data/gherkin.tatsu").read_text(encoding="utf-8")
        compiled_py = tatsu.to_python_sourcecode(grammar)
        pathlib.Path("pytest_bdd/_gherkin.py").write_text(compiled_py, encoding="utf-8")

        return super().run()