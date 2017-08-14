
import collections
import gzip
import sys
import tarfile
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileCreatedEvent


class MyHandler(FileSystemEventHandler):

    def __init__(self, file_processor):
        super().__init__()
        self.file_processor = file_processor

    def on_created(self, event):
        if type(event) is FileCreatedEvent:
            self.file_processor.handle(event.src_path)


def process(path):
    with tarfile.open(path) as tar:
        for member in tar.getmembers():
            contents = tar.extractfile(member)
            decompressed = gzip.decompress(contents)
            return str(decompressed, 'utf-8')


def main(watch_folder):
    Processor = collections.namedtuple('Processor', 'handle')
    file_processor = Processor(handle=lambda x: print(x))

    observer = Observer()
    observer.schedule(MyHandler(file_processor), watch_folder)

    try:
        while True:
            time.sleep(5)
    except:
        observer.stop()

    observer.join()


if __name__ == "__main__":
    main(sys.argv[1])
