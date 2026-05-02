import pandas as pd
from supabase import create_client, Client

# Supabaseの設定（image_04bad5.png の情報を入力）
SUPABASE_URL = "https://bgbnsdnqrahsjffstext.supabase.co"
SUPABASE_KEY = "nitokento17"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def migrate():
    try:
        df = pd.read_csv("ルーレッツ.csv")
        
        # データの整形（CSVの列名に合わせて調整してください）
        # 例：CSVの列が '日付', '名前', '結果' の場合
        for _, row in df.iterrows():
            data = {
                "developer": row["名前"], # CSVの列名
                "result": row["結果"],    # CSVの列名
                # created_atは自動で入りますが、過去の日時を保持したい場合は指定可能
            }
            supabase.table("dice_logs").insert(data).execute()
        
        print("移行が完了しました！")
    except Exception as e:
        print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    migrate()