"""Handler for setting into the future timed scores"""
from typing import Any, Union

from ... import item
from . import main_story


def set_scores(
    scores: list[list[int]], usr_scores: list[Union[int, None]]
) -> list[list[int]]:
    """Set the scores for a stage"""
    for i, usr_score in enumerate(usr_scores):
        if usr_score is None:
            continue
        scores[i] = ([usr_score] * 48) + ([0] * 3)
    return scores


def timed_scores(save_stats: dict[str, Any]) -> dict[str, Any]:
    """Handler for setting into the future timed scores"""

    scores = save_stats["itf_timed_scores"]
    print("다음 장의 점수를 입력하세요.:")
    usr_scores = item.IntItemGroup.from_lists(
        names=main_story.CHAPTERS[3:6],
        values=None,
        maxes=9999,
        group_name="미래의 시간 초과 점수",
    )
    usr_scores.edit()
    save_stats["itf_timed_scores"] = set_scores(scores, usr_scores.get_values_none())

    print("시간 제한 점수를 성공적으로 설정했습니다.")
    return save_stats
