from pathlib import Path
from services import suggest_features, add_milestone


def test_suggest_features(monkeypatch, tmp_path):
    def fake_send(prompt, model="", key_path=""):
        return "- Idea1: Desc1\n- Idea2: Desc2"
    from services import wand
    monkeypatch.setattr(wand, "send_prompt", fake_send)
    workspace = tmp_path / "ws"
    workspace.mkdir()
    (workspace / "a.py").write_text("print('x')")
    milestones = tmp_path / "m.md"
    milestones.write_text("## ms")
    ideas = suggest_features(workspace, milestones)
    assert len(ideas) == 2
    assert ideas[0]["title"] == "Idea1"


def test_add_milestone(tmp_path):
    path = tmp_path / "m.md"
    path.write_text("header\n")
    add_milestone({"title": "TestMilestone", "description": "Do something"}, path)
    text = path.read_text()
    assert "TestMilestone" in text

