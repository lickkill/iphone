"""Handler for unlocking the equip menu."""
from typing import Any

from ... import helper


def unlock_equip(save_stats: dict[str, Any]) -> dict[str, Any]:
    """Unlocks the equip menu."""

    save_stats["menu_unlocks"][2] = 1
    helper.colored_text("장비 메뉴가 성공적으로 잠금 해제되었습니다.", helper.GREEN)
    return save_stats
