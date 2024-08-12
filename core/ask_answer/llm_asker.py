import threading
from queue import Queue

from core.helper.logger import LogUtil

logger = LogUtil().get_logger()


class LLMAsker(threading.Thread):
    def __init__(self, t_name: str, question_queue: Queue):
        threading.Thread.__init__(self, name=t_name)
        self.question_queue: Queue = question_queue

    def run(self) -> None:
        while self.question_queue.not_empty:
            try:
                question = self.question_queue.get(timeout=10)
                logger.info(question)
            except Exception:
                logger.warning("get queue item timeout break")
                break
        logger.info("finished")
