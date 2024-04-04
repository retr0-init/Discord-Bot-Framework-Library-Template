- [中文](#discord机器人框架通用库模板)
- [English](#discord-bot-framework-library-template)

# Discord机器人框架通用库模板
这是针对[Discord机器人内核](https://github.com/retr0-init/Discord-Bot-Framework-Kernel.git)配套的通用库模板。其开发可以参考[interactions.py](https://interactions-py.github.io/interactions.py/)。

## 开发中需要考虑的事
- 通用库开发禁止在[`main.py`](main.py)中。
- 你可以用另一个`.py`文件来定义内部模块函数。这个文件需要与`main.py`同级。注意你要像以下来引入内部模块：
```python
from . import xxx # xxx是内部模块的名字
```
- 只能读写模块本地的文件。如果要读写本地文件，路径为`f"{os.path.dirname{__file__}/<文件名>"`.
- 在[`requirements.txt`](requirements.txt)中写入模块所需的第三方库。
- 在[`CHANGELOG`](CHANGELOG)中更新改动。
- 在机器人内核文件夹以外的文件访问会被拒绝。
- 外部程序执行会被拒绝。
- 用以下方式引入通用库
```python
# 用以下方式从其他模块或者通用库引入实体
## 以下几行引入用于将Git网址解析为模块名
from src.moduleutil import giturl_parse
from importlib import import_module
from types import ModuleType
try:
    url, modname, validated = giturl_parse("https://github.com/retr0-init/Discord-Bot-Framework-Library-Template.git")
    if validated:
        library_package: ModuleType = import_module(f"...{modname}", package=__name__)
    # 等价于：
    # from .. import com_d_github__Discord_h_Discord_h_Bot_h_Framework_h_Library_h_Template as library_package
except ImportError:
    print(f"Module Library {modname} import error or is not loaded!")
```

# Discord-Bot-Framework-Library-Template
This is the library template for [Discord-Bot-Framework-Kernel](https://github.com/retr0-init/Discord-Bot-Framework-Kernel.git). The development refers to [interactions.py](https://interactions-py.github.io/interactions.py/).

## Things to consider for development
- The library's logic should not be developed in [`main.py`](main.py).
- You can use another `.py` file for internal module under the same directory as `main.py`. Be aware that you need to import it like
```python
from . import xxx # xxx is the internal module script name
```
- Only local files in the module directory can be read/written. THe path to the file is `f"{os.path.dirname{__file__}/<filename>` to interact with local files.
- Put python module requirements in [`requirements.txt`](requirements.txt). Do NOT delete this file.
- Update your changes in [`CHANGELOG`](CHANGELOG).
- The file access to the files other than the kernel directory will be denied.
- The external program execution will be denied.
- Use the following method to import the library
```python
# Use the following method to import functions from the other module or library
## The lines following import the function to parse the module Git URL to the module name
from src.moduleutil import giturl_parse
from importlib import import_module
from types import ModuleType
try:
    url, modname, validated = giturl_parse("https://github.com/retr0-init/Discord-Bot-Framework-Library-Template.git")
    if validated:
        library_package: ModuleType = import_module(f"...{modname}", package=__name__)
    # Equivalent to:
    # from .. import com_d_github__Discord_h_Discord_h_Bot_h_Framework_h_Library_h_Template as library_package
except ImportError:
    print(f"Module Library {modname} import error or is not loaded!")
```