import threading
from queue import Queue

from core.helper.logger import LogUtil

logger = LogUtil().get_logger()


class QuestionProducer(threading.Thread):
    def __init__(self, t_name: str, question_queue: Queue):
        threading.Thread.__init__(self, name=t_name)
        self.question_queue: Queue = question_queue

    def run(self) -> None:
        for i in range(1, 100):
            self.question_queue.put(f"{i}")
            logger.info(f"producer produce question:{i}")
        logger.info("producer finished")
