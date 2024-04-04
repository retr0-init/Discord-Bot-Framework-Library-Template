'''
Discord-Bot-Library template. For detailed usages,
 check https://interactions-py.github.io/interactions.py/

Copyright (C) 2024  __retr0.init__

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''
import asyncio
import time
from typing import Optional, Any
from enum import Enum, unique

# Use the following method to import the internal module in the current same directory
from . import internal_t

# Use the following method to import functions from the other module or library
# There are some ugly package-module-class definitions to act as an import error fallback
## The line following import the function to parse the module Git URL to the module name
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
    print("The external library module does not exist! Please load the library module at first!")
    class library_package_def:
        def __init__(self) -> None:
            library_module = self.library_module_def()
            return None
        class library_module_def:
            pi: float = 3.1415926
            mut_list: list[str] = []
            def __init__(self) -> None:
                return None
            def sync_func(self, *a, **k) -> None:
                return None
            async def async_func(self, *a, **k) -> None:
                return None
            class ExampleLibrary:
                a = []
                b = 0
                def __init__(self, *a, **k) -> None:
                    return None
                def append(self, *a, **k) -> None:
                    return None
                async def get_b(self, *a, **k) -> None:
                    return None
    library_package = library_package_def()

'''
A constant variable
'''
pi: float = 3.141592654

'''
A mutable variable
'''
mut_list: list[str] = []

'''
An integer Enum for the other usage
'''
@unique
class ExampleEnum(int, Enum):
    Ex1 = 1
    Ex2 = 10
    Ex3 = 100

'''
A standalone synchronous function definition
'''
def sync_func(t: float) -> None:
    print(f"Synchronously Sleep for {t} seconds...")
    time.sleep(t)

'''
A standalone asynchronous function definition
'''
async def async_func(t: float) -> None:
    print(f"Asynchronously Sleep for {t} seconds...")
    await asyncio.sleep(t)

'''
A function try to call the objects from the other modules
'''
async def misc_func() -> None:
    print(library_package.library_module.pi)
    print(library_package.library_module.mut_list)
    library_package.library_module.sync_func(3)
    await library_package.library_module.aynsc_func(4)
    cc = library_package.library_module.ExampleLibrary()
    cc.append(4)
    await cc.got_b()
    print(cc.a, cc.b)

'''
Library Class definition
'''
class ExampleLibrary:
    __slots__ = ["a", "b"]

    a: list[Any] = []
    b: int = 0

    def __init__(self, a: Optional[list] = None, b: int = 0) -> None:
        if a is None:
            self.a = []
        else:
            self.a = a
        self.b = b

    def append(self, i: Any) -> list[Any]:
        '''
        Synchronous class method
        '''
        self.a.append(i)
        return self.a

    async def got_b(self) -> int:
        '''
        Asynchronous class method
        '''
        await asyncio.sleep(1)
        return self.b