from environs import Env
import os

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()
BOT_TOKEN = str(os.environ.get("BOT_TOKEN"))
ADMINS = str(os.environ.get("ADMINS"))
IP = str(os.environ.get("ip"))
PROVIDER_TOKEN = str(os.environ.get("PROVIDER_TOKEN"))