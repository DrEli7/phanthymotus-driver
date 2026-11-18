"""The AS2 guide is an operator resource and never reports an SDK mode transition."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import companion_guide


def test_guide_distinguishes_remote_action_from_machine_state():
    card = companion_guide.tool()
    guide = companion_guide.read_guide()
    assert card["type"] == "resource" and card["name"] == "companion_guide"
    assert "M" in card["description"] and "P" in card["description"] and "摇杆" in card["description"]
    assert guide["command_sent"] is False and guide["mode_readback"] == "unavailable"
    assert set(guide["steps"]) == {"prepare", "enter", "exit"}
    assert guide["manual"].endswith("As2-W/User_Manual.html")
