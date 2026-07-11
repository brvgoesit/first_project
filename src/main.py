from dotenv import load_dotenv
import os

load_dotenv('.env')

author = os.getenv('AUTHOR')
print(author)