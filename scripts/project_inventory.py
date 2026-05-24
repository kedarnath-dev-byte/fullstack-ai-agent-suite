from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROJECTS_DIR = ROOT / "projects"


@dataclass(frozen=True)
class ProjectInventory:
    name: str
    agents: int
    tools: int
    models: int
    has_api: bool
    has_frontend: bool
    has_architecture_doc: bool
    has_code_doc: bool


def count_python_files(path: Path) -> int:
    if not path.exists():
        return 0
    return sum(1 for file_path in path.glob("*.py") if file_path.name != "__init__.py")


def collect_project(project_path: Path) -> ProjectInventory:
    return ProjectInventory(
        name=project_path.name,
        agents=count_python_files(project_path / "agents"),
        tools=count_python_files(project_path / "tools"),
        models=count_python_files(project_path / "models"),
        has_api=(project_path / "api" / "app.py").exists(),
        has_frontend=(project_path / "frontend" / "package.json").exists(),
        has_architecture_doc=(project_path / "ARCHITECTURE.md").exists(),
        has_code_doc=(project_path / "CODE.md").exists(),
    )


def collect_inventory() -> list[ProjectInventory]:
    if not PROJECTS_DIR.exists():
        return []

    project_paths = [
        path for path in PROJECTS_DIR.iterdir()
        if path.is_dir() and (path / "README.md").exists()
    ]
    return [collect_project(path) for path in sorted(project_paths)]


def format_bool(value: bool) -> str:
    return "yes" if value else "no"


def main() -> None:
    inventory = collect_inventory()
    if not inventory:
        print("No projects found.")
        return

    print("Outskill AI Lab project inventory")
    print("=" * 35)
    for project in inventory:
        print(f"\n{project.name}")
        print(f"  agents: {project.agents}")
        print(f"  tools: {project.tools}")
        print(f"  models: {project.models}")
        print(f"  api: {format_bool(project.has_api)}")
        print(f"  frontend: {format_bool(project.has_frontend)}")
        print(f"  architecture docs: {format_bool(project.has_architecture_doc)}")
        print(f"  code docs: {format_bool(project.has_code_doc)}")


if __name__ == "__main__":
    main()
