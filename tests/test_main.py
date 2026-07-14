import io
import unittest
from contextlib import redirect_stdout

from llm_ros2_navigation_agent.main import main


class TestMain(unittest.TestCase):
    def test_main_prints_status_and_returns_none(self) -> None:
        output = io.StringIO()

        with redirect_stdout(output):
            result = main()

        self.assertIsNone(result)
        self.assertEqual(
            output.getvalue(),
            "LLM-ROS2-Navigation-Agent: V0.1 environment ready\n",
        )


if __name__ == "__main__":
    unittest.main()
