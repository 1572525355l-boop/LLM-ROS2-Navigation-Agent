from dataclasses import dataclass


@dataclass(frozen=True)
class NavigationTask:
    """Represent an ordered mobile robot navigation task."""

    raw_instruction: str
    waypoints: tuple[str, ...]
