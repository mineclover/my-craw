from app.core.database import Base

import pkgutil
import importlib
import pathlib

# 현재 디렉토리 내 모든 .py 파일을 동적으로 import
package_dir = pathlib.Path(__file__).parent
for (_, module_name, _) in pkgutil.iter_modules([str(package_dir)]):
    if module_name != "__init__":
        importlib.import_module(f"{__package__}.{module_name}") 