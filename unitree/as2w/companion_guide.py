"""Published, operator-performed ISS 3.0 steps for As2-W X."""
MANUAL = "https://marketing.unitree.com/article/zh/As2-W/User_Manual.html"
SDK = "https://github.com/unitreerobotics/unitree_sdk2/blob/aaf69cb56c9d5ed63d8b284008ec3a8ab999bec1/include/unitree/robot/as2/sport/sport_client.hpp"

DESCRIPTION = ("AS2-W 伴随遥控器操作指引。先将伴随遥控器开机并连接，在右腰佩戴、天线向上。"
               "按 M 进入，按 P 或拨摇杆退出。模式由现场操作员通过机器狗语音确认。")
STEPS = {
    "prepare": ["让机器狗在平整开阔处完成站立。短按伴随遥控器电源，等指示灯稳定、听到连接提示。",
                "人站在狗的左侧，双方朝向一致。遥控器位于右腰，摇杆面朝右，天线竖直向上。"],
    "enter": ["确认机器狗在遥控器右侧，遥控器离狗头小于 2.4 米。短按 M，听到进入伴随的语音。"],
    "exit": ["按伴随遥控器的 P 或拨动其摇杆，听到退出提示后恢复摇杆控制。"
             "双手遥控器按键或拨杆也会退出。"],
}


def tool():
    return {"name": "companion_guide", "type": "resource", "description": DESCRIPTION,
            "inputSchema": {"type": "object", "properties": {}}}


def read_guide():
    return {"control": "physical_remote", "command_sent": False, "mode_readback": "unavailable",
            "steps": STEPS, "manual": MANUAL, "printed_pages": [19, 20, 21], "sdk_checked": SDK}
