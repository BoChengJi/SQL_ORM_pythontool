from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
import random

db = SQLAlchemy()

# ✅ 定義資料表
class BigTable(db.Model):
    __tablename__ = 'bigtable'
    ID = db.Column(db.Integer, primary_key=True)
    Dtime = db.Column(db.DateTime, default=datetime.now)
    for i in range(1, 501):
        locals()[f'col_{i}'] = db.Column(db.String(20))

class Table1(db.Model):
    __tablename__ = 'table1'
    ID = db.Column(db.Integer, primary_key=True)
    Dtime = db.Column(db.DateTime, default=datetime.now)
    Name = db.Column(db.String(50))
    Score = db.Column(db.Integer)
    Active = db.Column(db.Boolean)

class Table2(db.Model):
    __tablename__ = 'table2'
    ID = db.Column(db.Integer, primary_key=True)
    Dtime = db.Column(db.DateTime, default=datetime.now)
    Category = db.Column(db.String(100))
    Price = db.Column(db.Float)
    InStock = db.Column(db.Boolean)

class Table3(db.Model):
    __tablename__ = 'table3'
    ID = db.Column(db.Integer, primary_key=True)
    Dtime = db.Column(db.DateTime, default=datetime.now)
    Title = db.Column(db.String(100))
    Views = db.Column(db.Integer)
    Published = db.Column(db.Boolean)

# ✅ 假資料產生
def generate_fake_data(model, fields):
    for _ in range(20):
        item = model()
        for field in fields:
            if 'Name' in field or 'Title' in field or 'Category' in field:
                setattr(item, field, f'{field}_{random.randint(1, 100)}')
            elif 'Score' in field or 'Views' in field:
                setattr(item, field, random.randint(0, 1000))
            elif 'Price' in field:
                setattr(item, field, round(random.uniform(10, 500), 2))
            elif 'Active' in field or 'Published' in field or 'InStock' in field:
                setattr(item, field, random.choice([True, False]))
        db.session.add(item)

def generate_bigtable_data():
    for _ in range(1000):
        item = BigTable()
        item.Dtime = datetime(2022, 1, 1) + timedelta(days=random.randint(0, 1000))
        for i in range(1, 501):
            setattr(item, f'col_{i}', f'v{random.randint(100,999)}')
        db.session.add(item)

# ✅ 資料庫初始化
def init_db():
    db.drop_all()
    db.create_all()
    generate_fake_data(Table1, ['Name', 'Score', 'Active'])
    generate_fake_data(Table2, ['Category', 'Price', 'InStock'])
    generate_fake_data(Table3, ['Title', 'Views', 'Published'])
    generate_bigtable_data()
    db.session.commit()

# ✅ 工具函數
def get_table_data(name):
    model = get_table_by_name(name)
    rows = model.query.all()
    columns = model.__table__.columns.keys()
    return rows, columns

def get_table_by_name(name):
    return {
        'table1': Table1,
        'table2': Table2,
        'table3': Table3,
        'bigtable': BigTable  # ⬅️ 加上這行
    }[name]
