
import unittest
import mock
from watchdog.events import FileCreatedEvent
import demo.filewatch.handler as handler


class TestHandler(unittest.TestCase):

    def test_on_created_CallsProcessorWithCorrectArgs(self):
        mock_created_event = FileCreatedEvent("DUMMY_PATH")
        mock_processor = mock.MagicMock()
        mock_processor.handle = mock.MagicMock()

        file_handler = handler.MyHandler(mock_processor)
        file_handler.on_created(mock_created_event)
        mock_processor.handle.assert_called_once_with("DUMMY_PATH")

    @mock.patch.object(handler, 'gzip')
    @mock.patch.object(handler, 'tarfile')
    def test_process_DoesUntarThenGunzip(self, mock_tarfile, mock_gunzip):
        mock_tar = mock.MagicMock()
        mock_tar.getmembers.side_effect = lambda: [x for x in ["BLAH"]]
        mock_tar.extractfile.return_value = "CONTENTS"

        mock_enter = mock.MagicMock()
        mock_enter.return_value = mock_tar

        mock_open = mock.MagicMock()
        mock_open.return_value.__enter__ = mock_enter

        mock_tarfile.open = mock_open

        mock_gunzip.decompress.return_value = b'DECOMPRESSED'

        result = handler.process("PATH")

        mock_open.assert_called_once_with("PATH")
        mock_tar.extractfile.assert_called_once()
        mock_gunzip.decompress.assert_called_once_with("CONTENTS")
        self.assertEqual(result, "DECOMPRESSED")
