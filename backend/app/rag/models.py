from dataclasses import dataclass


@dataclass
class RetrievedContext:
    """A single retrieved chunk from the vector store."""

    content: str
    source: str
    score: float
