import unittest
from dataclasses import FrozenInstanceError

from llm_ros2_navigation_agent.models import NavigationTask


class TestNavigationTask(unittest.TestCase):
    def test_stores_instruction_and_waypoints(self) -> None:
        task = NavigationTask(
            raw_instruction="先去门口，再到桌子旁，最后返回充电点",
            waypoints=("门口", "桌子旁", "充电点"),
        )

        self.assertEqual(
            task.raw_instruction,
            "先去门口，再到桌子旁，最后返回充电点",
        )
        self.assertEqual(
            task.waypoints,
            ("门口", "桌子旁", "充电点"),
        )
    def test_is_immutable(self) -> None:
        task = NavigationTask(
            raw_instruction="去门口",
            waypoints=("门口",),
        )

        with self.assertRaises(FrozenInstanceError):
            task.raw_instruction = "去厨房"
if __name__ == "__main__":
    unittest.main()
