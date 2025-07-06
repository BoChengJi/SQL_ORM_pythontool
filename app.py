from flask import Flask, render_template, request, redirect, url_for
from models import db, init_db, get_table_data, get_table_by_name
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    init_db()

@app.route('/')
def index():
    table_names = ['table1', 'table2', 'table3', 'bigtable']
    selected_table = request.args.get('table', 'table1')
    page = int(request.args.get('page', 1))
    page_size = 50

    model = get_table_by_name(selected_table)
    query = model.query.order_by(model.ID).offset((page - 1) * page_size).limit(page_size)
    rows = query.all()
    columns = model.__table__.columns.keys()

    if selected_table == 'bigtable':
        columns = ['ID', 'Dtime'] + [f'col_{i}' for i in range(1, 11)]

    return render_template('index.html',
                           table_names=table_names,
                           selected_table=selected_table,
                           rows=rows,
                           columns=columns,
                           page=page)

@app.route('/update/<table_name>/<int:item_id>', methods=['GET', 'POST'])
def update(table_name, item_id):
    model = get_table_by_name(table_name)
    item = model.query.get(item_id)

    if not item:
        return "Item not found", 404

    if request.method == 'POST':
        editable_columns = model.__table__.columns.keys()
        for col in editable_columns:
            if col in ['ID', 'Dtime']:
                continue
            value = request.form.get(col)
            setattr(item, col, value)
        item.Dtime = datetime.now()
        db.session.commit()
        return redirect(url_for('index', table=table_name))

    return render_template('update.html', item=item, table_name=table_name)


if __name__ == '__main__':
    app.run(debug=True)
