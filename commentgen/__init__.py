import click


def get_comment_chars(lang) -> (str, str):
    c_style = ("/*", "*/")
    markup_style = ("<!-", "->")
    shell_style = ("#", "#")

    # https://en.wikipedia.org/wiki/Comparison_of_programming_languages_(syntax)
    lang_map = {
        "shell": shell_style,
        "java": c_style,
        "scala": c_style,
        "kotlin": c_style,
        "rust": c_style,
        "r": shell_style,
        "objectiveC": c_style,
        "erlang": ("%", "%"),
        "perl": shell_style,
        "ruby": shell_style,
        "elixir": shell_style,
        "swift": c_style,
        "go": c_style,
        "curl": ("|#", "#|"),
        "julia": ("#=", "=#"),
        "haskell": ("{-", "-}"),
        "clojure": (";;", ";;"),
        "python": shell_style,
        "js": c_style,
        "ts": c_style,
        "sql": ("--", "--"),
        "c": c_style,
        "cpp": c_style,
        "csharp": c_style,
        "html": markup_style,
        "xml": markup_style,
        "php": c_style,
        "lua": ("--", "--"),
        "ps": ("<#", "#>"),
        "lisp": ("#|", "|#"),
        "pascal": ("{", "}"),
        "jsp": ("<%--", "--%>"),
    }
    return lang_map[lang] if lang in lang_map else c_style


@click.command()
@click.option("--lang", type=click.STRING, default="c")
@click.option("--length", type=click.INT, default=80)
@click.option("--pattern", type=click.STRING, default="-")
@click.argument("text", type=str)
def cli(lang: str, length: int, pattern: str, text: str):
    start, end = get_comment_chars(lang)
    text = text.strip()
    pattern = pattern[0]
    l1 = len(start) + len(end) + 4 + len(text)
    if l1 > length:
        print(f"{start}  {text}  {end}", end="")
    else:
        l2 = length - l1
        times = l2 // 2
        if l2 % 2 == 0:
            a = "".join([pattern for _ in range(times)])
            print(f"{start} {a} {text} {a} {end}", end="")
        else:
            times += 1
            a = "".join([pattern for _ in range(times)])
            print(f"{start} {a} {text} {a[:-1]} {end}", end="")
    pass
