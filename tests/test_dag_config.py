"""Test module import."""
from __future__ import annotations

import pathlib

import pytest
from hatcht.hello import hello_world

def test_hello_world():
    """Test Config."""
    assert hello_world() == "Hello World"

