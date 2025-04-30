import openpyxl
from datetime import datetime

web_questions = [
    {
        "question": "1.ウェブサーバーとクライアント間の通信で使用される主要なプロトコルは何ですか？",
        "options": {
        "A": "HTTP",
        "B": "FTP",
        "C": "SMTP",
        "D": "SSH"
        },
        "correct_option": "A"
    },
    {
        "question": "2.次のうち、サーバー側のスクリプト言語はどれですか？",
        "options": {
        "A": "HTML",
        "B": "CSS",
        "C": "JavaScript",
        "D": "PHP"
        },
        "correct_option": "D"
    },
    {
        "question": "3.次のうち、クライアント側のスクリプト言語はどれですか？",
        "options": {
        "A": "HTML",
        "B": "CSS",
        "C": "JavaScript",
        "D": "PHP"
        },
        "correct_option": "C"
    },
    {
        "question": "4.WWW（ワールドワイドウェブ）を構成する基本要素は何ですか？",
        "options": {
        "A": "URL",
        "B": "HTML",
        "C": "HTTP",
        "D": "すべての上記"
        },
        "correct_option": "D"
    },
    {
        "question": "5.次のうち、最も一般的なウェブサーバーのソフトウェアはどれですか？",
        "options": {
        "A": "Apache",
        "B": "IIS",
        "C": "Nginx",
        "D": "Tomcat"
        },
        "correct_option": "A"
    },
    {
        "question": "6.次のうち、どのHTTPメソッドがウェブサーバーから情報を取得するために使用されますか？",
        "options": {
        "A": "GET",
        "B": "POST",
        "C": "PUT",
        "D": "DELETE"
        },
        "correct_option": "A"
    },
    {
        "question": "7.次のうち、どのHTTPメソッドがウェブサーバーに情報を送信するために使用されますか？",
        "options": {
        "A": "GET",
        "B": "POST",
        "C": "PUT",
        "D": "DELETE"
        },
        "correct_option": "B"
    },
    {
        "question": "8.ウェブページのスタイリングに使用される言語は何ですか？",
        "options": {
        "A": "HTML",
        "B": "CSS",
        "C": "JavaScript",
        "D": "PHP"
        },
        "correct_option": "B"
    },
    {
        "question": "9.ウェブページのコンテンツや構造を記述する言語は何ですか？",
        "options": {
        "A": "HTML",
        "B": "CSS",
        "C": "JavaScript",
        "D":"PHP"
        },
        "correct_option": "A"
    },
    {
        "question": "10.次のうち、どのHTTPステータスコードがリクエストが成功したことを示していますか？",
        "options": {
        "A": "200 OK",
        "B": "404 Not Found",
        "C": "500 Internal Server Error",
        "D": "401 Unauthorized"
        },
        "correct_option": "A"
    }
]

apache_questions = [
    {
        "question": "1.Apacheのメイン設定ファイルは通常何と呼ばれますか？",
        "options": {
        "A": "apache.conf",
        "B": "httpd.conf",
        "C": "config.ini",
        "D": "apache.ini"
        },
        "correct_option": "B"
    },
    {
        "question": "2.Apacheで仮想ホストを設定する際に使用されるディレクティブは何ですか？",
        "options": {
        "A": "VirtualHost",
        "B": "Listen",
        "C": "ServerRoot",
        "D": "Directory"
        },
        "correct_option": "A"
    },
    {
        "question": "3.Apacheで新しいモジュールを有効にするために使用されるディレクティブは何ですか？",
        "options": {
        "A": "LoadModule",
        "B": "AddModule",
        "C": "EnableModule",
        "D": "RequireModule"
        },
        "correct_option": "A"
    },
    {
        "question": "4.Apacheの設定ファイルにおいて、特定のディレクトリに対する設定を適用するディレクティブは何ですか？",
        "options": {
        "A": "Directory",
        "B": "Location",
        "C": "VirtualHost",
        "D": "Files"
        },
        "correct_option": "A"
    },
    {
        "question": "5.LinuxでApache Webサーバーを再起動するコマンドは何ですか？",
        "options": {
        "A": "service apache restart",
        "B": "service httpd restart",
        "C": "apache restart",
        "D": "httpd restart"
        },
        "correct_option": "B"
    },
    {
        "question": "6.Apacheの設定ファイルで、特定のファイルに対する設定を適用するディレクティブは何ですか？",
        "options": {
        "A": "Directory",
        "B": "Location",
        "C": "VirtualHost",
        "D": "Files"
        },
        "correct_option": "D"
    },
    {
        "question": "7.Apacheのドキュメントルートディレクトリを設定するディレクティブは何ですか？",
        "options": {
        "A": "DocumentRoot",
        "B": "ServerRoot",
        "C": "DirectoryRoot",
        "D": "RootDirectory"
        },
        "correct_option": "A"
    },
    {
        "question": "8.Apache設定ファイルで、Listenディレクティブが何を設定するか？",
        "options": {
        "A": "サーバーのポート番号",
        "B": "仮想ホストの名前",
        "C": "サーバーの管理者のメールアドレス",
        "D": "ディレクトリのアクセス権"
        },
        "correct_option": "A"
    },
    {
        "question": "9.Apacheで特定のディレクトリへのアクセス制御を設定するために使用されるディレクティブは何ですか？",
        "options": {
            "A": "Require",
            "B": "Order",
            "C": "Allow",
            "D": "Deny"
        },
        "correct_option": "A"
    },
    {
        "question": "10.Apacheでエラーページをカスタマイズするディレクティブは何ですか？",
        "options": {
            "A": "ErrorDocument",
            "B": "CustomError",
            "C": "ErrorPage",
            "D": "ErrorHandler"
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
    print("1. WEB Service")
    print("2. Apache設定基礎知識")
    test_type = input("テストタイプを入力（1 または 2）:")

    # 選択に応じて問題リストをロード
    if test_type == "1":
        questions = web_questions
        test_type_name = "WEB Service"
    elif test_type == "2":
        questions = apache_questions
        test_type_name = "Apache設定基礎知識"       
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
