from dotenv import find_dotenv, load_dotenv
import os


load_dotenv(find_dotenv())
tg_token = os.getenv('TG_KEY')
operator_username = os.getenv('operator_username')
admin_id = os.getenv('admin_id')