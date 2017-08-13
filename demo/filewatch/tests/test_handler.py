
import unittest
import mock
from watchdog.events import FileCreatedEvent
from demo.filewatch.handler import MyHandler


class TestHandler(unittest.TestCase):

    def test_on_created_CallsProcessorWithCorrectArgs(self):
        mock_created_event = FileCreatedEvent("DUMMY_PATH")
        mock_processor = mock.MagicMock()
        mock_processor.handle = mock.MagicMock()

        handler = MyHandler(mock_processor)
        handler.on_created(mock_created_event)
        mock_processor.handle.assert_called_once_with("DUMMY_PATH")
