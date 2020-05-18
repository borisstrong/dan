import jinja2
import aiohttp_jinja2
from aiohttp import web
import sys
sys.path.append('./system')
import system

if __name__ == '__main__':
    system.router(123)