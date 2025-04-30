import openpyxl
from datetime import datetime

ec2_questions = [
    {
        "question": "1.EC2 インスタンスへのSSH接続に使用されるデフォルトのユーザー名は何ですか？",
        "options": {
            "A": "ec2-user",
            "B": "root",
            "C": "admin",
            "D": "ubuntu"
        },
        "correct_option": "A"
    },
    {
        "question": "2.WindowsベースのEC2インスタンスに接続するために使用されるプロトコルは何ですか？",
        "options": {
            "A": "SSH",
            "B": "RDP",
            "C": "HTTPS",
            "D": "Telnet"
        },
        "correct_option": "B"
    },
    {
        "question": "3.Amazon Linux 2 および Amazon Linux AMI でサポートされているデフォルトのシェルは何ですか？",
        "options": {
            "A": "bash",
            "B": "zsh",
            "C": "csh",
            "D": "ksh"
        },
        "correct_option": "A"
    },
    {
        "question": "4.LinuxベースのEC2インスタンスへのSSH接続に使用されるポート番号は何ですか？",
        "options": {
            "A": "21",
            "B": "22",
            "C": "23",
            "D": "3389"
        },
        "correct_option": "B"
    },
    {
        "question": "5.EC2 インスタンスの起動時にユーザーデータを渡すことで、どのような操作が可能になりますか？",
        "options": {
            "A": "インスタンスのアクセスキーを設定する",
            "B": "インスタンスの自動バックアップを設定する",
            "C": "インスタンスの起動時にスクリプトを実行する",
            "D": "インスタンスのタグを設定する"
        },
        "correct_option": "C"
    },
    {
        "question": "6.EC2 Windowsインスタンスのパスワードを取得するために使用するキーペアのファイル拡張子は何ですか？",
        "options": {
            "A": ".pem",
            "B": ".ppk",
            "C": ".key",
            "D": ".cert"
        },
        "correct_option": "A"
    },
    {
        "question": "7.EC2 インスタンスのモニタリングに使用されるサービスは何ですか？",
        "options": {
            "A": "Amazon CloudWatch",
            "B": "AWS CloudTrail",
            "C": "Amazon Inspector",
            "D": "AWS Trusted Advisor"
        },
        "correct_option": "A"
    },
    {
        "question": "8.EC2 インスタンスのモニタリングに使用されるサービスは何ですか？",
        "options": {
            "A": "Amazon CloudWatch",
            "B": "AWS CloudTrail",
            "C": "Amazon Inspector",
            "D": "AWS Trusted Advisor"
        },
        "correct_option": "A"
    },
    {
        "question": "9.EC2 インスタンスへの RDP 接続に使用されるデフォルトの Windows ユーザー名は何ですか？",
        "options": {
            "A": "Administrator",
            "B": "ec2-user",
            "C": "windows-user",
            "D": "root"
        },
        "correct_option": "A"
    },
    {
        "question": "10.EC2 インスタンスの EBS ボリュームの暗号化に使用される AWS サービスは何ですか？",
        "options": {
            "A": "AWS Key Management Service (KMS)",
            "B": "AWS Certificate Manager",
            "C": "AWS Identity and Access Management (IAM)",
            "D": "AWS CloudHSM"
        },
        "correct_option": "A"
    }
]

network_questions = [
    {
        "question": "1.HTTPプロトコルのデフォルトのポート番号は何ですか？",
        "options": {
        "A": "80",
        "B": "443",
        "C": "8080",
        "D": "53"
        },
        "correct_option": "A"
    },
    {
        "question": "2.HTTPSプロトコルは、どの暗号化技術を使用していますか？",
        "options": {
        "A": "SSL/TLS",
        "B": "SSH",
        "C": "SFTP",
        "D": "AES"
        },
        "correct_option": "A"
    },
    {
        "question": "3.TCP と UDP の主な違いは何ですか？",
        "options": {
        "A": "TCPは接続指向で、UDPは非接続指向",
        "B": "TCPは非接続指向で、UDPは接続指向",
        "C": "TCPは速度が速く、UDPは遅い",
        "D": "TCPは遅く、UDPは速度が速い"
        },
        "correct_option": "A"
    },
    {
        "question": "4.DNSクエリに通常使用されるプロトコルは何ですか？",
        "options": {
        "A": "TCP",
        "B": "UDP",
        "C": "HTTP",
        "D": "HTTPS"
        },
        "correct_option": "B"
    },
    {
        "question": "5.次のうち、HTTPステータスコード「200」の意味は何ですか？",
        "options": {
        "A": "リクエストが成功し、サーバーが要求に応じたアクションを実行しました。",
        "B": "リクエストされたリソースが別のURLに移動されました。",
        "C": "リクエストは無効であり、サーバーは処理しないでいます。",
        "D": "リクエストされたリソースは見つかりませんでした。"
        },
        "correct_option": "A"
    },
    {
        "question": "6.次のうち、HTTPステータスコード「404」の意味は何ですか？",
        "options": {
        "A": "リクエストが成功し、サーバーが要求に応じたアクションを実行しました。",
        "B": "リクエストされたリソースが別のURLに移動されました。",
        "C": "リクエストは無効であり、サーバーは処理しないでいます。",
        "D": "リクエストされたリソースは見つかりませんでした。"
        },
        "correct_option": "D"
    },
    {
        "question": "7.IPv4アドレスは何ビットですか？",
        "options": {
        "A": "32ビット",
        "B": "64ビット",
        "C": "128ビット",
        "D": "256ビット"
        },
        "correct_option": "A"
    },
    {
        "question": "8.IPv6アドレスは何ビットですか？",
        "options": {
        "A": "32ビット",
        "B": "64ビット",
        "C": "128ビット",
        "D": "256ビット"
        },
        "correct_option": "C"
    },
    {
        "question": "9.次のうち、OSIモデルの第3層（ネットワーク層）で動作するプロトコルはどれですか？",
        "options": {
        "A": "IP",
        "B": "TCP",
        "C": "UDP",
        "D": "HTTP"
        },
        "correct_option": "A"
    },
    {
        "question": "10.次のうち、OSIモデルの第4層（トランスポート層）で動作するプロトコルはどれですか？",
        "options": {
        "A": "IP",
        "B": "TCP",
        "C": "UDP",
        "D": "BとC"
        },
        "correct_option": "D"
    }
]

linux_questions = [
    {
        "question": "1.ファイルやディレクトリのリストを表示するLinuxコマンドは何ですか？",
        "options": {
        "A": "ls",
        "B": "cd",
        "C": "mkdir",
        "D": "touch"
        },
        "correct_option": "A"
    },
    {
        "question": "2.カレントディレクトリを変更するLinuxコマンドは何ですか？",
        "options": {
        "A": "ls",
        "B": "cd",
        "C": "mkdir",
        "D": "touch"
        },
        "correct_option": "B"
    },
    {
        "question": "3.新しいディレクトリを作成するLinuxコマンドは何ですか？",
        "options": {
        "A": "ls",
        "B": "cd",
        "C": "mkdir",
        "D": "touch"
        },
        "correct_option": "C"
    },
    {
        "question": "4.空のファイルを作成する、または既存のファイルのタイムスタンプを更新するLinuxコマンドは何ですか？",
        "options": {
        "A": "ls",
        "B": "cd",
        "C": "mkdir",
        "D": "touch"
        },
        "correct_option": "D"
    },
    {
        "question": "5.ファイルの内容を表示するLinuxコマンドは何ですか？",
        "options": {
        "A": "cat",
        "B": "cp",
        "C": "mv",
        "D": "rm"
        },
        "correct_option": "A"
    },
    {
        "question": "6.ファイルをコピーするLinuxコマンドは何ですか？",
        "options": {
        "A": "cat",
        "B": "cp",
        "C": "mv",
        "D": "rm"
        },
        "correct_option": "B"
    },
    {
        "question": "7.ファイルを移動または名前変更するLinuxコマンドは何ですか？",
        "options": {
        "A": "cat",
        "B": "cp",
        "C": "mv",
        "D": "rm"
        },
        "correct_option": "C"
    },
    {
        "question": "8.ファイルを削除するLinuxコマンドは何ですか？",
        "options": {
        "A": "cat",
        "B": "cp",
        "C": "mv",
        "D": "rm"
        },
        "correct_option": "D"
    },
    {
        "question": "9.プロセスを強制終了するLinuxコマンドは何ですか？",
        "options": {
        "A": "kill",
        "B": "ps",
        "C": "top",
        "D": "jobs"
        },
        "correct_option": "A"
    },
    {
        "question": "10.現在のシェルで実行中のプロセスの一覧を表示するLinuxコマンドは何ですか？",
        "options": {
        "A": "kill",
        "B": "ps",
        "C": "top",
        "D": "jobs"
    },
    "correct_option": "D"
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
    print("1. AWS EC2")
    print("2. ネットワーク基礎知識")
    print("3. Linuxコマンド知識")
    test_type = input("テストタイプを入力（1 または 2,3）:")

    # 選択に応じて問題リストをロード
    if test_type == "1":
        questions = ec2_questions
        test_type_name = "AWS EC2"
    elif test_type == "2":
        questions = network_questions
        test_type_name = "ネットワーク基礎知識"
    elif test_type == "3":
        questions = linux_questions
        test_type_name = "Linuxコマンド知識"        
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
