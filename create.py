import os

# カレントディレクトリ内のフォルダを取得
current_dir = os.getcwd()
folders = [f for f in os.listdir(current_dir) if os.path.isdir(f) and len(f) == 10 and f.isdigit()]

# HTMLファイルの作成
html_content = """
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>フォルダ一覧</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f9;
            color: #333;
        }

        h1 {
            text-align: center;
            margin: 20px 0;
            font-size: 2rem;
            color: #444;
        }

        ul {
            list-style: none;
            padding: 0;
            margin: 20px auto;
            max-width: 600px;
        }

        li {
            background: #fff;
            margin: 10px 0;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            transition: transform 0.2s, box-shadow 0.2s;
        }

        li:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
        }

        a {
            display: block;
            padding: 15px 20px;
            text-decoration: none;
            color: #007bff;
            font-size: 1.1rem;
            font-weight: bold;
            transition: color 0.2s;
        }

        a:hover {
            color: #0056b3;
        }

        @media (max-width: 600px) {
            h1 {
                font-size: 1.5rem;
            }

            a {
                font-size: 1rem;
            }
        }
    </style>
</head>
<body>
    <h1>フォルダ一覧</h1>
    <ul>
"""

# フォルダ名をリストに追加
for folder in folders:
    html_content += f'<li><a href="./{folder}">{folder}</a></li>\n'

# HTMLファイルの結末
html_content += """
    </ul>
</body>
</html>
"""

# HTMLファイルを保存
with open("folder_list.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("folder_list.html が作成されました。")
