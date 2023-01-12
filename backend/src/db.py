from sqlalchemy import create_engine

# 修改为 'mysql+pymysql://<user name>:<password>@localhost:<port>/bs'
DB_URI = 'mysql+pymysql://root:0322@localhost:3306/bs'

db = create_engine(DB_URI, encoding='utf-8')

