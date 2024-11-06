# RealisticCodeBenchmark

# Project structure

> ├─data  			# RealisticCodeBenchmark question jsonl data
> ├─executor	  # LLM answer code test component	
> ├─llm				# 13 LLM call component
> └─statistics	  # Answer result  pass@k calculate component	

The individual folders are explained in more detail below

## data

> RealisticCodeBench.jsonl						# total question of RealisticCodeBenchmark
> RealisticCodeBench_c&cpp.jsonl		   # original code is c&cpp
> RealisticCodeBench_java.jsonl			   # original code is java 
> RealisticCodeBench_javascript.jsonl	 # original code is javascript
> RealisticCodeBench_python.jsonl		 # original code is python
> RealisticCodeBench_typescript.jsonl	# original code is typescript

### JSONL Item example

```json
{
    "task_id": 1,  // task unique id in benchmark
    "code_type": "method", // code type method or class
    "original_language": "python", // code origianl program language
    "question_type": "Data processing and transformation",	// question type
    "summary": "", // summary of the code implementation functionality
    "language_version_list": { // Other language adaptations
        "python": {
            "code_signature": "", // Code signature adapted for python
            "test_code": "", // python test code
            "prompt": "", // llm prompt
            "addition_info": "" // addition info for code or testcode or qeusiton
        },
        "javascript": {
            "code_signature": "", // Code signature adapted for python
            "test_code": "", // javascript test code
            "prompt": "", // llm prompt
            "addition_info": "" // addition info for code or testcode or qeusiton
        },
        "typescript": {
            "code_signature": "", // Code signature adapted for typescript
            "test_code": "", // typescript test code
            "prompt": "", // llm prompt
            "addition_info": "" // addition info for code or testcode or qeusiton
        },
        "c&cpp": {
           	"code_signature": "", // Code signature adapted for c++
            "test_code": "", // c++ test code
            "prompt": "", // llm prompt
            "addition_info": "" // addition info for code or testcode or qeusiton
        },
        "java": {
 			"code_signature": "", // Code signature adapted for java
            "test_code": "", // java test code
            "prompt": "", // llm prompt
            "addition_info": "" // addition info for code or testcode or qeusiton
        }
    }
}
```



### question statistics

|  language  | question number |
| :--------: | :-------------: |
|   python   |       392       |
| JavaScript |       376       |
| TypeScript |       372       |
|   C&CPP    |       353       |
|    Java    |       339       |

### question type

| Tpoic                                          | Description                                                  | Examlpes                                                     | Number |
| ---------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------ |
| Data Structures and Algorithms                 | Utilizing common data structures (such as lists, stacks, trees, etc.) for processing non-text data, along with fundamental algorithms | Implementation of linked lists, queues and other data structures, sorting algorithms, search algorithms, dictionary lists into list dictionaries | 106    |
| Text Processing                                | Perform formatting conversions on strings, regular expression matching, content extraction, and other text operations. | Regularly match specific strings, convert string types to other types, extract content between specified characters. | 100    |
| File Handling                                  | Read and write files, modify content, convert encodings, change file types, and handle file retrieval in directories. | Convert JSON files to YAML, modify CSV file content based on specific rules, filter files in directories. | 67     |
| Mathematical Problems and Scientific Computing | Programming for mathematical problems, matrix and vector operations, data statistics, and related scientific computing. | Matrix multiplication, BMI calculation, deflection angle conversion, calculus computations. | 67     |
| Date and Time Processing                       | Perform date format conversions, time calculations, and time unit conversions. | Convert timestamps to specific timezone formats, convert dates to milliseconds. | 32     |
| Data Visualization and Graphic Applications    | Involve data display and image file processing.              | Convert images to grayscale, color statistics of images, generate gradient colors. | 20     |
| Network Programming                            | Involve IP address and network interfaces, URL requests, and domain name resolutions. | Obtain local IP address and port, parse URLs to extract specified parameters, extract domain levels. | 12     |
| Frontend                                       | Parse and process web content HTML, CSS, modify styles, compress HTML. | Remove page ads, implement specific element highlighting, switch page themes. | 8      |
| Security                                       | Involve data encryption and decryption, complexity checks of data, etc. | Encrypt user passwords, check if input data meets security requirements, decrypt specific encoded data. | 5      |

## executor

The llm answering test component collects the question answers answered by the llm and the test cases of the corresponding question for testing, and determines whether the test cases can pass.

**different language need test env**

- Pytbon:`python:3.8`	`pytest:8.3.2`	`unittest`
- JavaScript:`jest:29.7.0`	`jest-environment-jsdom:29.7.0`
- TypeScript:`jest:29.7.0`	`jestenviroment-jsdom:29.7.0`	`ts-jest:29.2.5`	`typescript:5.6.2`
- C&CPP:`catch2`	`MinGW`	`GCC`
- Java:`java:11`	`Junit:4.13.2`

>     ccpp_executor.py		# test c&cpp answer
>     javascript_executor.py	# test javascript answer
>     java_executor.py		# test java answer
>     python_executor.py		# test python answer
>     typescript_executor.py	# test typescript answer

Executors of each language, support single test and batch test.The single-question test only needs to input the LLM responses and test cases each time.Batch testing requires you to specify a file to save the LLM answer results (jsonl file in the code) and a file to output the test results (csv file in the code).

### single question test usage

just call this class function

```python
def single_run(self, code, test_code):
```

### Batch testusage

At the command line, execute the following sh command

```shell
<language>_executor.py --model_answer_file_path=<llm answer file path> --result_save_file_path=<test answer file path>
```

## llm

This folder contains python files for 12 large language model calls.The following table lists how all models can be invoked, either locally or via the official API.

>     chatglm-6b.py
>     codegeex4-all-9b.py
>     codegen25-7b-instruct_P.py
>     codellama-7b-instruct-hf.py
>     deepseek-coder-6.7b-instruct.py
>     deepseek-coder-v2.5.py
>     gpt-3.5.py
>     gpt-4.py
>     Meta-Llama-3.1-8B-Instruct.py
>     Mistral-7B-Instruct-v0.3.py
>     Phi-3-small-8k-instruct.py
>     starcoder2-7b.py

|   model name   | local | API  | Organization | size | open-source | release time |
| :------------: | :---: | :--: | :----------: | :--: | :---------: | :----------: |
|     GPT-4      |   -   |  ✅   |    OpenAI    |  -   |      -      |     2023     |
|    GPT-3.5     |   -   |  ✅   |    OpenAI    |  -   |      -      |     2022     |
| DeepSeek-V2.5  |   -   |  ✅   |   DeepSeek   | 236B |      ✅      |     2024     |
|    Llama3.1    |   ✅   |  -   |     Meta     |  8B  |      ✅      |     2024     |
|     Phi-3      |   ✅   |  -   |  Microsoft   |  7B  |      ✅      |     2024     |
|    Mistral     |   ✅   |  -   |  MistralAI   |  7B  |      ✅      |     2024     |
|    ChatGLM     |   ✅   |  -   |    THUDM     |  6b  |      ✅      |     2024     |
|   CodeGeex4    |   ✅   |  -   |    THUDM     |  9B  |      ✅      |     2023     |
| DeepSeek-Coder |   ✅   |  -   |   DeepSeek   | 6.7B |      ✅      |     2024     |
|   StarCoder2   |   ✅   |  -   |   BigCode    |  7B  |      ✅      |     2024     |
|   CodeGen2.5   |   ✅   |  -   |  Salesforce  |  7B  |      ✅      |     2023     |
|   CodeLlama    |   ✅   |  -   |     Meta     |  7B  |      ✅      |     2023     |

### local llm py file usage

⭐⭐⭐

**Make sure you have the model and the accompanying Python environment deployed on your local environment before calling the large model**

⭐⭐⭐

After the above work is completed, the corresponding answer can be obtained by calling each model inference through the following sh command

```sh
chatglm-6b.py --languages=<language you need answer> --type=<pass type> --question_file_path=<question file paht> --answer_file_path=<answer file path>
```

`languages`:The language you want to generate answers in currently supports **python, javascript, typescript, c&cpp, java**，also you can choose all to above this language.

`type`:The amount of generated code,At present, the code supports **pass1** and **pass10** two options, which can be customized by modifying the code.

`question_file_path`:Path to the problem file.The **jsonl** file format is currently supported in the code.

`answer_file_path`:LLM answer file storage path, currently supported in the code for **jsonl** files

### API llm py file usage

For large model answers called through the API, use is similar to above. However, please note that you need to fill in the API Key and the base URL that you request from the platform.

```python
client = OpenAI(
    # TODO: change to your api_key,base url
    api_key="",
    base_url=""
)
```

## statistics	 

> passk_calculate.py

Calculate pass@k of LLM answer results

```python
import numpy as np


def pass_at_k(n, c, k):
    """
    Calculate the unbiased estimate of the pass@k metric.

    :param n: Total number of samples
    :param c: Number of correct samples
    :param k: The k value in pass@k
    :return: Unbiased estimate of pass@k
    """
    if n - c < k:  # If the number of incorrect samples is less than k
        return 1.0  # Directly return 1.0, indicating all problems are considered solved

    # Calculate the unbiased estimate of pass@k
    return 1.0 - np.prod(1.0 - k / np.arange(n - c + 1, n + 1))
```

You can invoke it with the following command

```sh
passk_calculate.py --k=<pass@k k value set> --answer_file_path=<llm answer file path> --result_save_file_path=<pass@k result save file path> 
```

## env

This folder contains the test environment of five languages in the experiment: Python, JavaScript, TypeScript, Java, C&CPP.Make sure to do the following before using each environment

### Python

1. Check your project python version is **3.8**
2. Run command pip install **pytest=8.3.2**

### JavaScript

1. Check your computer have install **node 18.19.1**
2. Run `npm install` command in project/env/javascript dir

### TypeScript

1. Check your computer have install **node 18.19.1**
2. Run `npm install`command in project/env/typescript dir

### Java

1. Check your computer have install **java11**
2. Check your computer have insttall **mvn3.9.6**
3. After update pom.xml refresh maven

### C&CPP

1. Check your computer  have install **GCC or G++**
2. Make sure your complier support c++11 or c++17(we used MinGW)
3. Modify the test code according to your operating system, and the compiled executable will be called differently depending on the operating system 
