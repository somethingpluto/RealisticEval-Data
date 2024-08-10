from queue import Queue

from core.ask_answer.llm_asker import LLMAsker
from core.ask_answer.question_producer import QuestionProducer

if __name__ == '__main__':
    question_queue = Queue()
    asker_list = []
    question_producer = QuestionProducer(t_name="question_producer", question_queue=question_queue)
    for i in range(0, 3):
        asker_list.append(LLMAsker(t_name=f"llm_asker[{i}]", question_queue=question_queue))

    question_producer.start()
    for t in asker_list:
        t.start()
    for t in asker_list:
        t.join()
    question_producer.join()
