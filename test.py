# check_install.py
import sys
import subprocess

def check_package(package_name):
    try:
        __import__(package_name)
        print(f"✅ {package_name} установлен")
        return True
    except ImportError:
        print(f"❌ {package_name} НЕ установлен")
        return False

def get_version(package_name):
    try:
        module = __import__(package_name)
        if hasattr(module, '__version__'):
            return module.__version__
        return "версия не определена"
    except:
        return "не установлен"

print("=== Проверка установки пакетов ===\n")

packages = ['torch', 'transformers', 'diffusers', 'onnxruntime', 'optimum', 'PIL']

for package in packages:
    installed = check_package(package)
    if installed:
        print(f"  Версия: {get_version(package)}")
    print()

print("\n=== Информация о системе ===")
print(f"Python: {sys.version}")
print(f"Платформа: {sys.platform}")