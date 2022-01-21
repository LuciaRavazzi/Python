from setuptools import find_packages, setup

setup(
    name="RockPaperScissor",
    version="0.0.1",
    description="Rock, paper, scissor game.",
    author="Lucia Ravazzi",
    install_requires=["random", "time"],
    packages=find_packages(),
)
