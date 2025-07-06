🛠️ SQLite 資料編輯小工具（Flask 版）
這是一個使用 Python + Flask + SQLite + Bootstrap 打造的簡易資料庫工具，適合 不懂 SQL 的使用者 快速瀏覽與編輯資料。

✅ 功能特色
支援多張資料表瀏覽（Table1、Table2、Table3、BigTable）

BigTable 支援 500 個欄位、超過 1000 筆資料

可直接在網頁上查詢、編輯資料

自動載入欄位名稱與資料，不需寫 SQL

分頁顯示與欄位限制避免卡頓

使用 Bootstrap 美化介面，適合內部工具或快速開發

🖥️ 使用方法
安裝依賴：

pip install flask sqlalchemy

執行應用程式：

python app.py
開啟瀏覽器進入：

http://localhost:5000/
📁 資料表說明
table1: 有姓名、分數、是否啟用

table2: 商品分類、價格、是否有庫存

table3: 標題、瀏覽數、是否發佈

bigtable: 自動產生 500 個欄位 + 1000 筆資料

🔧 技術架構
技術	用途
Flask	Web 應用主體
SQLAlchemy	ORM 模型
SQLite	資料儲存（免安裝）
Bootstrap	美化前端 UI
Jinja2	模板引擎

💡 適合用途
內部測試資料檢查

非技術人員快速操作資料

Demo 給前端或資料部門使用

模擬資料庫規格與大量欄位需求