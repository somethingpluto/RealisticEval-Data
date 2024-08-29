from typing import Any, List, TypeVar, Type, cast, Callable

T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


class Metadata:
    repo: str
    path: str
    task_type: str

    def __init__(self, repo: str, path: str, task_type: str) -> None:
        self.repo = repo
        self.path = path
        self.task_type = task_type

    @staticmethod
    def from_dict(obj: Any) -> 'Metadata':
        assert isinstance(obj, dict)
        repo = from_str(obj.get("repo"))
        path = from_str(obj.get("path"))
        task_type = from_str(obj.get("task_type"))
        return Metadata(repo, path, task_type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["repo"] = from_str(self.repo)
        result["path"] = from_str(self.path)
        result["task_type"] = from_str(self.task_type)
        return result


class OriginCode:
    metadata: Metadata
    code: str

    def __init__(self, metadata: Metadata, code: str) -> None:
        self.metadata = metadata
        self.code = code

    @staticmethod
    def from_dict(obj: Any) -> 'OriginCode':
        assert isinstance(obj, dict)
        metadata = Metadata.from_dict(obj.get("metadata"))
        code = from_str(obj.get("code"))
        return OriginCode(metadata, code)

    def to_dict(self) -> dict:
        result: dict = {}
        result["metadata"] = to_class(Metadata, self.metadata)
        result["code"] = from_str(self.code)
        return result


class TestClass:
    code: str
    case_list: List[Any]

    def __init__(self, code: str, case_list: List[Any]) -> None:
        self.code = code
        self.case_list = case_list

    @staticmethod
    def from_dict(obj: Any) -> 'TestClass':
        assert isinstance(obj, dict)
        code = from_str(obj.get("code"))
        case_list = from_list(lambda x: x, obj.get("caseList"))
        return TestClass(code, case_list)

    def to_dict(self) -> dict:
        result: dict = {}
        result["code"] = from_str(self.code)
        result["caseList"] = from_list(lambda x: x, self.case_list)
        return result


class Test:
    task_id: str
    program_language: str
    origin_code: OriginCode
    question_summary: str
    code_signature: str
    test: TestClass
    humane_solution_code: str

    def __init__(self, task_id: str, program_language: str, origin_code: OriginCode, question_summary: str,
                 code_signature: str, test: TestClass, humane_solution_code: str) -> None:
        self.task_id = task_id
        self.program_language = program_language
        self.origin_code = origin_code
        self.question_summary = question_summary
        self.code_signature = code_signature
        self.test = test
        self.humane_solution_code = humane_solution_code

    @staticmethod
    def from_dict(obj: Any) -> 'Test':
        assert isinstance(obj, dict)
        task_id = from_str(obj.get("task_id"))
        program_language = from_str(obj.get("program_language"))
        origin_code = OriginCode.from_dict(obj.get("origin_code"))
        question_summary = from_str(obj.get("question_summary"))
        code_signature = from_str(obj.get("code_signature"))
        test = TestClass.from_dict(obj.get("test"))
        humane_solution_code = from_str(obj.get("humane_solution_code"))
        return Test(task_id, program_language, origin_code, question_summary, code_signature, test,
                    humane_solution_code)

    def to_dict(self) -> dict:
        result: dict = {}
        result["task_id"] = from_str(self.task_id)
        result["program_language"] = from_str(self.program_language)
        result["origin_code"] = to_class(OriginCode, self.origin_code)
        result["question_summary"] = from_str(self.question_summary)
        result["code_signature"] = from_str(self.code_signature)
        result["test"] = to_class(TestClass, self.test)
        result["humane_solution_code"] = from_str(self.humane_solution_code)
        return result
