import openpyxl
from datetime import datetime

rds_questions = [
    {
      "question": "1.AWS RDS とは何ですか？",
      "options": {
        "A": "クラウドコンピューティングサービス",
        "B": "データベースソフトウェア",
        "C": "データストレージサービス",
        "D": "ネットワーキングサービス"
      },
      "correct_option": "B"
    },
    {
      "question": "2.AWS RDS でサポートされているデータベースエンジンは何ですか？",
      "options": {
        "A": "MySQL、PostgreSQL、MariaDB、Oracle、Microsoft SQL Server",
        "B": "MySQL、PostgreSQL、MariaDB、Oracle、Microsoft Access",
        "C": "MySQL、PostgreSQL、MongoDB、Oracle、Microsoft SQL Server",
        "D": "MySQL、PostgreSQL、MongoDB、Oracle、Microsoft Access"
      },
      "correct_option": "A"
    },
    {
      "question": "3.AWS RDS で、どのような種類のデータベースを作成できますか？",
      "options": {
        "A": "単一 AZ またはマルチ AZ の MySQL、PostgreSQL、MariaDB、Oracle、Microsoft SQL Server データベース",
        "B": "単一 AZ またはマルチ AZ の MySQL、PostgreSQL、MongoDB、Oracle、Microsoft SQL Server データベース",
        "C": "単一 AZ またはマルチ AZ の MySQL、PostgreSQL、MariaDB、Oracle、Microsoft Access データベース",
        "D": "単一 AZ またはマルチ AZ の MySQL、PostgreSQL、MongoDB、Oracle、Microsoft Access データベース"
      },
      "correct_option": "A"
    },
    {
      "question": "4.AWS RDS で、データベースをどのようにバックアップできますか？",
      "options": {
        "A": "手動でスナップショットを作成するか、自動バックアップを有効にする",
        "B": "手動でデータベースをエクスポートするか、自動バックアップを有効にする",
        "C": "手動でスナップショットを作成するか、自動バックアップを無効にする",
        "D": "手動でデータベースをエクスポートするか、自動バックアップを無効にする"
      },
      "correct_option": "A"
    },
    {
      "question": "5.AWS RDS で、どのようにリードレプリカを構成しますか？",
      "options": {
        "A": "手動で EC2 インスタンスを追加するか、リードレプリカを有効にする",
        "B": "手動で RDS インスタンスを追加するか、リードレプリカを有効にする",
        "C": "自動スケーリングを有効にするか、リードレプリカを有効にする",
        "D": "手動で RDS インスタンスを追加するか、自動バックアップを有効にする"
      },
      "correct_option": "B"
    },
    {
      "question": "6.AWS RDS で、どのようにマルチ AZ 構成を構成しますか？",
      "options": {
        "A": "手動で EC2 インスタンスを追加するか、マルチ AZ 構成を有効にする",
        "B": "手動で RDS インスタンスを追加するか、マルチ AZ 構成を有効にする",
        "C": "自動スケーリングを有効にするか、マルチ AZ 構成を有効にする",
        "D": "手動で RDS インスタンスを追加するか、自動バックアップを有効にする"
      },
      "correct_option": "B"
    },
    {
      "question": "7.AWS RDS で、どのようにデータベースインスタンスを監視しますか？",
      "options": {
        "A": "AWS CloudWatch を使用する",
        "B": "AWS CloudTrail を使用する",
        "C": "AWS CloudFormation を使用する",
        "D": "AWS CodeCommit を使用する"
      },
      "correct_option": "A"
    },
    {
      "question": "8.AWS RDS で、どのようにデータベースパフォーマンスを最適化しますか？",
      "options": {
        "A": "キャッシュサイズを増やす",
        "B": "ストレージサイズを増やす",
        "C": "データベースエンジンをアップグレードする",
        "D": "すべてのクエリにインデックスを追加する"
      },
      "correct_option": "C"
    },
    {
      "question": "9.AWS RDS と Amazon EC2 の違いは何ですか？",
      "options": {
        "A": "AWS RDS は、データベースを実行するための完全に管理されたサービスであり、Amazon EC2 は仮想マシンを実行するための IaaS サービスです。",
        "B": "AWS RDS は、オンプレミスデータベースを AWS に移行するためのサービスであり、Amazon EC2 は AWS のコンピューティングリソースを提供するためのサービスです。",
        "C": "AWS RDS は、Amazon EC2 上で動作するデータベースエンジンであり、Amazon EC2 は AWS のネットワーキングリソースを提供するためのサービスです。",
        "D": "AWS RDS は、AWS 内の別のリージョンとの間でデータを同期するためのサービスであり、Amazon EC2 は AWS のセキュリティグループを管理するためのサービスです。"
      },
      "correct_option": "A"
    },
    {
      "question": "10.AWS RDS で、どのように自動スケーリングを構成しますか？",
      "options": {
        "A": "手動で EC2 インスタンスを追加するか、自動スケーリングを有効にする",
        "B": "手動で RDS インスタンスを追加するか、自動スケーリングを有効にする",
        "C": "自動スケーリングを有効にするか、リードレプリカを有効にする",
        "D": "手動で RDS インスタンスを追加するか、自動バックアップを有効にする"
      },
      "correct_option": "B"
    },
]    

database_questions = [
    {
      "question": "1.データベースとは何ですか？",
      "options": {
        "A": "データの媒介",
        "B": "プログラミング言語",
        "C": "コンピュータのオペレーティングシステム",
        "D": "通信プロトコル"
      },
      "correct_option": "A"
    },
    {
      "question": "2.リレーショナルデータベースとは何ですか？",
      "options": {
        "A": "非構造化データを保存するデータベース",
        "B": "JSON ファイル形式のデータを保存するデータベース",
        "C": "データをテーブル形式で保存するデータベース",
        "D": "クラウド上で実行されるデータベース"
      },
      "correct_option": "C"
    },
    {
      "question": "3.主キーとは何ですか？",
      "options": {
        "A": "データベース内のすべてのデータを一意に識別するために使用されるフィールド",
        "B": "データベース内のデータを分類するために使用されるフィールド",
        "C": "データベース内のデータをグループ化するために使用されるフィールド",
        "D": "データベース内の特定のデータを検索するために使用されるフィールド"
      },
      "correct_option": "A"
    },
    {
      "question": "4.SQL とは何ですか？",
      "options": {
        "A": "Java のオブジェクト指向プログラミング言語",
        "B": "JavaScript のクライアントサイドスクリプト言語",
        "C": "データベースを操作するための言語",
        "D": "Python のデータ解析用プログラミング言語"
      },
      "correct_option": "C"
    },
    {
      "question": "5.トランザクションとは何ですか？",
      "options": {
        "A": "データベース内のテーブルを削除する操作",
        "B": "データベース内のデータを変更する一連の操作",
        "C": "データベースのスキーマを変更する操作",
        "D": "データベースにデータを追加する操作"
      },
      "correct_option": "B"
    },
    {
      "question": "6.インデックスとは何ですか？",
      "options": {
        "A": "データベースのテーブルにおいて、特定の列に対して高速な検索を可能にするデータ構造",
        "B": "データベース内のデータをバックアップする機能",
        "C": "データベースに保存されたデータを表示するためのアプリケーション",
        "D": "データベース内のデータを自動的に圧縮する機能"
      },
      "correct_option": "A"
    },
    {
      "question": "7.トランザクションの ACID 特性について説明してください。",
      "options": {
        "A": "Atomicity（原子性）、Consistency（一貫性）、Isolation（独立性）、Durability（永続性）",
        "B": "Availability（可用性）、Consistency（一貫性）、Integrity（整合性）、Durability（永続性）",
        "C": "Atomicity（原子性）、Concurrency（並行性）、Isolation（独立性）、Durability（永続性）",
        "D": "Availability（可用性）、Concurrency（並行性）、Integrity（整合性）、Durability（永続性）"
      },
      "correct_option": "A"
    },
    {
      "question": "8.ノンリレーショナルデータベースとは何ですか？",
      "options": {
        "A": "非構造化データを保存するデータベース",
        "B": "データをテーブル形式で保存するデータベース",
        "C": "JSON ファイル形式のデータを保存するデータベース",
        "D": "クラウド上で実行されるデータベース"
      },
      "correct_option": "A"
    },
    {
      "question": "9.クエリとは何ですか？",
      "options": {
        "A": "データベースに保存されたデータを変更するための操作",
        "B": "データベースからデータを取得するための操作",
        "C": "データベースのテーブルを削除するための操作",
        "D": "データベースのスキーマを変更するための操作"
      },
      "correct_option": "B"
    },
    {
      "question": "インサートとアップデートの違いは何ですか？",
      "options": {
        "A": "新しいデータをデータベースに追加する操作はインサートであり、既存のデータを更新する操作はアップデートです",
        "B": "データベース内のデータを削除する操作はインサートであり、既存のデータを更新する操作はアップデートです",
        "C": "データベース内のデータをコピーする操作はインサートであり、既存のデータを更新する操作はアップデートです",
        "D": "データベース内のデータを移動する操作はインサートであり、既存のデータを更新する操作はアップデートです"
      },
      "correct_option": "A"
    }
]

def ask_question(question):
    print(question["question"])
    for option, text in question["options"].items():
        print(f"{option}. {text}")

    while True:
        user_answer = input("あなたの答えを入力してください：")
        if user_answer.strip().upper() in question["options"]:
            break
        else:
            print("無効な入力です。有効なオプション（A, B, C, または D）を入力してください。")

    return user_answer.strip().upper() == question["correct_option"]

def calculate_score(questions):
    correct_count = 0
    for question in questions:
        if ask_question(question):
            correct_count += 1
    return correct_count * 10

def show_result(score):
    print(f"\nAWS IAM 段階テストを終了しました。あなたのスコアは{score}/100です。")
    if score >= 80:
        print("このテストで優れたパフォーマンスを発揮し、AWS IAM をしっかりと理解しています。継続してください！")
    elif score >= 60:
        print("このテストでは、ある程度の理解を示しました。スキルと知識をさらに向上させるために、関連する資料をもう一度見直し、実践操作を強化してください。頑張ってください！")
    else:
        print("このテストでのスコアは低かったです。関連する資料をもう一度学習し、実践操作で練習を強化することをお勧めします。がっかりしないで、引き続き努力してください！")


def create_excel_file(file_name):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "テスト結果"
    ws.append(["名前", "テストタイプ", "得点", "テスト時間"])
    wb.save(file_name)

def save_result_to_excel(file_name, user_name, test_type, score):
    wb = openpyxl.load_workbook(file_name)
    ws = wb["テスト結果"]
    test_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ws.append([user_name, test_type, score, test_time])
    wb.save(file_name)

def main():
    # 受講者の氏名を入力
    user_name = input("あなたの名前を入力してください：")

    # テストタイプを選択
    print("テストタイプを選択してください：")
    print("1. AWS RDS")
    print("2. データベース基礎知識")
    test_type = input("テストタイプを入力（1 または 2）：")

    # 選択に応じて問題リストをロード
    if test_type == "1":
        questions = rds_questions
        test_type_name = "AWS RDS"
    elif test_type == "2":
        questions = database_questions
        test_type_name = "データベース基礎知識"
    else:
        print("無効な入力。プログラムを再実行し、有効なテストタイプを入力してください。")
        return

    # 得点を計算
    score = calculate_score(questions)

    # 結果を表示
    show_result(score)

    # 受講者の名前で命名された Excel ファイルに保存
    file_name = f"{user_name}_results.xlsx"
    try:
        save_result_to_excel(file_name, user_name, test_type_name, score)
    except FileNotFoundError:
        create_excel_file(file_name)
        save_result_to_excel(file_name, user_name, test_type_name, score)

    print("テスト結果が Excel ファイルに保存されました。")

if __name__ == "__main__":
    main()
