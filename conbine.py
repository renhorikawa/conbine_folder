import os
import shutil
from concurrent.futures import ThreadPoolExecutor, as_completed

def copy_item(src, dest):
    try:
        # ファイルかフォルダかを確認し、適切にコピー
        if os.path.isdir(src):
            shutil.copytree(src, dest)  # フォルダの場合はcopytreeを使用
            print(f"Copied directory {src} to {dest}")
        else:
            shutil.copy2(src, dest)  # ファイルの場合はcopy2を使用
            print(f"Copied file {src} to {dest}")
    except Exception as e:
        print(f"Error copying {src} to {dest}: {e}")

def organize_files_by_id(base_dir, max_workers=8):
    # 新しい親フォルダをカレントディレクトリ内に作成
    new_base_dir = os.path.join(base_dir, "Combined_files")
    os.makedirs(new_base_dir, exist_ok=True)
    
    # カレントディレクトリ内の年月フォルダを探す
    year_month_folders = [f for f in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, f)) and f.isdigit()]
    
    id_groups = {}

    # 年月ごとのフォルダ内のIDフォルダを検索
    for year_month in year_month_folders:
        year_month_path = os.path.join(base_dir, year_month)
        
        # 年月フォルダ内のIDフォルダを探す
        for folder in os.listdir(year_month_path):
            id_folder_path = os.path.join(year_month_path, folder)
            if os.path.isdir(id_folder_path):
                id = folder  # フォルダ名をIDとして扱う
                if id not in id_groups:
                    id_groups[id] = []

                # IDフォルダ内のファイルをリストに追加
                for file in os.listdir(id_folder_path):
                    file_path = os.path.join(id_folder_path, file)
                    if os.path.isdir(file_path):
                        id_groups[id].append(file_path)  # フォルダもコピー対象に追加
                    elif os.path.isfile(file_path):
                        id_groups[id].append(file_path)
    
    # 新しい親フォルダ内にIDごとのフォルダを作成し、ファイルまたはフォルダをコピー
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = []
        for id, item_list in id_groups.items():
            target_dir = os.path.join(new_base_dir, id)  # 新しい親フォルダ内にIDごとのフォルダ
            os.makedirs(target_dir, exist_ok=True)
            
            for item_path in item_list:
                dest = os.path.join(target_dir, os.path.basename(item_path))
                futures.append(executor.submit(copy_item, item_path, dest))
        
        for future in as_completed(futures):
            try:
                future.result()  
            except Exception as e:
                print(f"Error during file/folder organization: {e}")

base_directory = "."  # カレントディレクトリを指定
organize_files_by_id(base_directory, max_workers=8)

