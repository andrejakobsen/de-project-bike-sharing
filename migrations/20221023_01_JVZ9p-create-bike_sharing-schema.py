"""
create bike_sharing schema
"""

from typing import Any

from yoyo import step

__depends__: Any = {}

steps = [
    step(
        "CREATE SCHEMA bike_sharing",
        "DROP SCHEMA bike_sharing"
    ),
]
