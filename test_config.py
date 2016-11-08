import json

import pytest


@pytest.fixture
def config():
    """Load the project configuration.

    Implicitly tests that cookiecutter.json is actually JSON and encoded using
    UTF-8.
    """
    with open("cookiecutter.json", encoding="UTF-8") as file:
        return json.load(file)


@pytest.fixture
def vs_metadata(config):
    """Load the VS metadata.

    Implicitly tests that it exists.
    """
    return config["_visual_studio"]


@pytest.fixture
def public_config(config):
    """Create a public version of the configuration data.

    This simply minimizes boilerplate for having to filter out private items.
    """
    return {key: value for key, value in config.items()
            if not key.startswith("_")}


def test_full_vs_coverage(vs_metadata, public_config):
    """Make sure every public item has all Visual Studio metadata specified."""
    for key, value in public_config.items():
        assert key in vs_metadata
        vs_config = vs_metadata[key]
        assert "label" in vs_config
        assert "description" in vs_config
        assert "selector" in vs_config


def test_vs_selectors(vs_metadata, public_config):
    """Check that default values match the specified Visual Studio selector."""
    for key, default in public_config.items():
        selector = vs_metadata[key]["selector"]
        if selector in {"string", "odbcConnection"}:
            assert isinstance(default, str)
        elif selector == "list":
            assert isinstance(default, list)
        elif selector == "yesno":
            assert default in {"y", "n"}
        else:
            raise ValueError("unexpected selector type: {!r}".format(selector))
