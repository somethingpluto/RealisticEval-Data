import textwrap


def wrap_content_generator(content, width=80):
    for line in content.splitlines(keepends=True):
        if line.strip() == '':
            yield '\n'
        else:
            for line2 in textwrap.wrap(line, width=width):
                yield line2