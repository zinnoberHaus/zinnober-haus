"""Validate portfolio metadata and required coordination artifacts (not product functionality)."""
import json
from pathlib import Path
root = Path(__file__).resolve().parents[1]
data = json.loads((root / "registry/repos.json").read_text())
assert data["owner"] == "zinnoberHaus"
assert {r["name"] for r in data["repositories"]} == {"zinnober-haus", "zettel", "carthouse"}
for repo in data["repositories"]:
    assert repo["url"] == f"https://github.com/{data['owner']}/{repo['name']}"
    assert repo["status"] in {"planning", "active", "alpha", "beta", "stable"}
for path in ["AGENTS.md", "README.md", "CONTRIBUTING.md", "SECURITY.md", "GOVERNANCE.md", "CODE_OF_CONDUCT.md", "docs/operations/workflow.md", "docs/research/zettel.md", "docs/research/carthouse.md", "docs/research/open-source-strategy.md"]:
    assert (root / path).is_file(), f"Missing {path}"
print("Portfolio metadata and required documents validated; no product readiness claim.")
