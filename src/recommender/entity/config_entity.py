"""
What is a Dataclass?

A dataclass is a Python class whose main job is to store data.

Think of it as a container.

For example...

Instead of

student = {
    "name": "Vishal",
    "age": 22,
    "cgpa": 8.87
}

we write

Student(
    name="Vishal",
    age=22,
    cgpa=8.87
)


"""


"""
Why frozen=True?


Imagine someone does this:

config.movies_path = "abc.csv"

Oops.

They accidentally changed the configuration.

Configuration should not change while the program is running.

So we freeze it.

"""

from dataclasses import dataclass

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: str

    movies_path: str
    ratings_path: str
    tags_path: str
    links_path: str


@dataclass(frozen=True)
class DataValidationConfig:

    root_dir: str
    status_file: str
    data_ingestion_dir: str