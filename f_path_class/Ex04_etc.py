"""
경로 이동은  Path 모듈로 안되어 os 모듈이 필요하다
"""

from pathlib import Path
import os

print(Path.cwd()) #현재경로
os.chdir('..')
print(Path.cwd())

print(os.environ["HOMEPATH"])
print(os.environ["JAVA_HOME"])
print(os.environ["CATALINA_HOME"])
