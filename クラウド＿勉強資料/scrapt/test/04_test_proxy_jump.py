import openpyxl
from datetime import datetime


ssh_jump_questions = [
    {
        "question": "1.踏み台サーバー（ジャンプサーバー）の主な目的は何ですか？",
        "options": {
        "A": "リソース節約",
        "B": "セキュリティ向上",
        "C": "パフォーマンス向上",
        "D": "データの圧縮"
        },
        "correct_option": "B"
    },
    {
        "question": "2.踏み台サーバーを使用すると、どのようなセキュリティ上の利点がありますか？",
        "options": {
        "A": "中間サーバーを経由することで、外部からの直接アクセスを制限できる",
        "B": "踏み台サーバーが暗号化を強制する",
        "C": "踏み台サーバーでのみ認証情報が保存される",
        "D": "SSHトラフィックを分散させる"
        },
        "correct_option": "A"
    },
    {
        "question": "3.次のうち、SSHトンネリングを使用して踏み台サーバーに接続する方法はどれですか？",
        "options": {
        "A": "ssh -J user@jump_server user@target_server",
        "B": "ssh -L user@jump_server user@target_server",
        "C": "ssh -R user@jump_server user@target_server",
        "D": "ssh -T user@jump_server user@target_server"
        },
        "correct_option": "A"
    },
    {
        "question": "4.踏み台サーバーを使用して、プライベートネットワーク内のリソースにアクセスできるようにするために使用される技術は何ですか？",
        "options": {
        "A": "VPN",
        "B": "SSHトンネリング",
        "C": "ポートフォワーディング",
        "D": "NAT"
        },
        "correct_option": "B"
    },
    {
        "question": "5.踏み台サーバーで最も一般的に使用されるプロトコルは何ですか？",
        "options": {
        "A": "HTTP",
        "B": "FTP",
        "C": "SSH",
        "D": "TLS"
        },
        "correct_option": "C"
    },
    {
        "question": "6.踏み台サーバーにSSH接続する際に使用するデフォルトのTCPポートは何ですか？",
        "options": {
        "A": "21",
        "B": "22",
        "C": "23",
        "D": "80"
        },
        "correct_option": "B"
    },
    {
        "question": "7.踏み台サーバーを使用して内部サーバーへのアクセスを制限する方法の一つは、どれですか？",
        "options": {
        "A": "すべてのユーザーに同じアクセス権を与える",
        "B": "内部サーバーのIPアドレスを変更する",
        "C": "外部からの直接アクセスを許可する",
        "D": "内部サーバーへのSSHアクセスを踏み台サーバーからのみ許可する"
        },
        "correct_option": "D"
    },
    {
        "question": "8.踏み台サーバーに関連するセキュリティリスクの軽減策はどれですか？",
        "options": {
        "A": "パスワード認証の代わりに公開鍵認証を使用する",
        "B": "踏み台サーバーのSSHポートをデフォルトのままにする",
        "C": "すべてのユーザーにルート権限を与える",
        "D": "踏み台サーバー上のすべてのアクティビティを記録しない"
        },
        "correct_option": "A"
    },
    {
        "question": "9.踏み台サーバーを設定する際に推奨されるセキュリティ機能の1つは、何ですか？",
        "options": {
        "A": "デフォルトのSSHポートを使用する",
        "B": "パスワード認証を無効にする",
        "C": "踏み台サーバーへのアクセスを全員に許可する",
        "D": "踏み台サーバーに複数のユーザーアカウントを作成しない"
        },
        "correct_option": "B"
    },
    {
        "question": "10.踏み台サーバーを使用する主な欠点は何ですか？",
        "options": {
        "A": "接続が遅くなる可能性がある",
        "B": "セキュリティが低下する",
        "C": "内部サーバーへのアクセスが制限される",
        "D": "ネットワークトラフィックが増加する"
        },
        "correct_option": "A"
    }
]

proxy_server_questions = [
    {
        "question": "1.プロキシーサーバーの主な目的は何ですか？",
        "options": {
        "A": "ネットワークトラフィックを暗号化する",
        "B": "クライアントとサーバー間の通信を中継する",
        "C": "データストレージを提供する",
        "D": "メールサーバーを管理する"
        },
        "correct_option": "B"
    },
    {
        "question": "2.プロキシーサーバーが提供するセキュリティ上の利点は何ですか？",
        "options": {
        "A": "ネットワークトラフィックの速度を向上させる",
        "B": "ウイルス対策ソフトウェアを提供する",
        "C": "外部からのアクセスを制限し、内部ネットワークを保護する",
        "D": "メールのスパムフィルタリングを行う"
        },
        "correct_option": "C"
    },
    {
        "question": "3.プロキシーサーバーが使用される主な理由は何ですか？",
        "options": {
        "A": "データベース管理",
        "B": "ウェブコンテンツのキャッシュとフィルタリング",
        "C": "データのバックアップと復元",
        "D": "ユーザーアカウントの管理"
        },
        "correct_option": "B"
    },
    {
        "question": "4.次のうち、プロキシーサーバーを介してインターネットにアクセスする際の利点はどれですか？",
        "options": {
        "A": "アクセス速度の向上",
        "B": "データの圧縮",
        "C": "ユーザー認証の強化",
        "D": "通信の暗号化"
        },
        "correct_option": "A"
    },
    {
        "question": "5.リバースプロキシーサーバーの主な機能は何ですか？",
        "options": {
        "A": "クライアントのリクエストを複数のサーバーに分散させる",
        "B": "ネットワークトラフィックを軽減する",
        "C": "ユーザー認証を管理する",
        "D": "データのバックアップを行う"
        },
        "correct_option": "A"
    },
    {
        "question": "6.プロキシーサーバーを使用して、特定のウェブサイトへのアクセスをブロックする方法は何ですか？",
        "options": {
        "A": "ファイアウォールルールを設定する",
        "B": "ウェブサイトのURLをブラックリストに追加する",
        "C": "ウェブサイトのDNSレコードを変更する",
        "D": "ウェブサイトへのアクセスを暗号化する"
        },
        "correct_option": "B"
    },
    {
        "question": "7.プロキシーサーバーがバンド幅使用量を削減する主な方法は何ですか？",
        "options": {
        "A": "ウェブコンテンツをキャッシュする",
        "B": "ウェブサイトのデータを圧縮する",
        "C": "通信を暗号化する",
        "D": "トラフィックを別のプロキシーサーバーに転送する"
        },
        "correct_option": "A"
    },
    {
        "question": "8.プロキシーサーバーが提供するプライバシー保護機能は何ですか？",
        "options": {
        "A": "ユーザーのIPアドレスを隠す",
        "B": "すべてのウェブサイトで匿名ブラウジングを有効にする",
        "C": "ユーザーのパスワードを保護する",
        "D": "ユーザーのメールアドレスを隠す"
        },
        "correct_option": "A"
    },
    {
        "question": "9.プロキシーサーバーを構成する際に、クライアントが設定を変更できないようにする方法は何ですか？",
        "options": {
        "A": "クライアントのパスワードを変更する",
        "B": "プロキシーサーバーのアクセス権限を制限する",
        "C": "クライアントのネットワーク設定を固定にする",
        "D": "プロキシーサーバーの設定ファイルを暗号化する"
        },
        "correct_option": "C"
    },
    {
        "question": "10.プロキシーサーバーの潜在的な欠点は何ですか？",
        "options": {
        "A": "ウェブページの読み込み速度が遅くなる可能性がある",
        "B": "プロキシーサーバーがユーザーのプライバシーを侵害する",
        "C": "セキュリティリスクが増加する",
        "D": "ネットワーク管理が複雑になる"
        },
        "correct_option": "A"
    }
]

squid_questions = [
    {
        "question": "1.Squidはどのようなタイプのプロキシサーバーですか？",
        "options": {
        "A": "リバースプロキシ",
        "B": "フォワードプロキシ",
        "C": "VPNプロキシ",
        "D": "SOCKSプロキシ"
        },
        "correct_option": "B"
    },
    {
        "question": "2.Squidがデフォルトで使用するポート番号は何ですか？",
        "options": {
        "A": "8080",
        "B": "80",
        "C": "3128",
        "D": "22"
        },
        "correct_option": "C"
    },
    {
        "question": "3.Squidの主な設定ファイルは何ですか？",
        "options": {
        "A": "/etc/squid/squid.conf",
        "B": "/etc/squid.conf",
        "C": "/var/squid/squid.conf",
        "D": "/usr/local/squid/etc/squid.conf"
        },
        "correct_option": "A"
    },
    {
        "question": "4.Squidでアクセス制限を行う際に使用する設定ディレクティブは何ですか？",
        "options": {
        "A": "acl",
        "B": "http_access",
        "C": "deny",
        "D": "allow"
        },
        "correct_option": "A"
    },
    {
        "question": "5.Squidで特定のドメインへのアクセスを許可するホワイトリストを作成するには、どの設定ディレクティブを使用する必要がありますか？",
        "options": {
        "A": "acl",
        "B": "http_access",
        "C": "deny",
        "D": "allow"
        },
        "correct_option": "A"
    },
    {
        "question": "6.Squidで特定のドメインへのアクセスを拒否するブラックリストを作成するには、どの設定ディレクティブを使用する必要がありますか？",
        "options": {
        "A": "acl",
        "B": "http_access",
        "C": "deny",
        "D": "allow"
        },
        "correct_option": "B"
    },
    {
        "question": "7.Squidで特定のIPアドレスに対してアクセス制限を設定するために、どのaclタイプを使用しますか？",
        "options": {
        "A": "src",
        "B": "dst",
        "C": "url_regex",
        "D": "dstdomain"
        },
        "correct_option": "A"
    },
    {
        "question": "8.Squidでキャッシュされたコンテンツのサイズ制限を設定するために使用される設定ディレクティブは何ですか？",
        "options": {
        "A": "cache_mem",
        "B": "cache_dir",
        "C": "maximum_object_size",
        "D": "minimum_object_size"
        },
        "correct_option": "C"
    },
    {
        "question": "9.Squidでキャッシュされたコンテンツを削除するために使用されるコマンドは何ですか？",
        "options": {
        "A": "squid -k reconfigure",
        "B": "squid -k shutdown",
        "C": "squid -k rotate",
        "D": "squid -k clear"
        },
        "correct_option": "A"
    },
    {
        "question": "10.Squidでログファイルのローテーションを設定するために使用されるディレクティブは何ですか？",
        "options": {
        "A": "access_log",
        "B": "cache_log",
        "C": "logfile_rotate",
        "D": "log_mime_hdrs"
        },
        "correct_option": "C"
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
    print("1. 踏み台サーバ")
    print("2. プロキシサーバ")
    print("3. squid基礎知識")
    test_type = input("テストタイプを入力（1 または 2,3）:")

    # 選択に応じて問題リストをロード
    if test_type == "1":
        questions = ssh_jump_questions
        test_type_name = "踏み台サーバ"
    elif test_type == "2":
        questions = proxy_server_questions
        test_type_name = "プロキシサーバ"   
    elif test_type == "3":
        questions = squid_questions
        test_type_name = "squid基礎知識"             
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
