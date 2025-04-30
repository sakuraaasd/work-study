import openpyxl
from datetime import datetime

sns_questions = [
    {
        "question": "1.AWS SNS はどのようなサービスですか？",
        "options": {
            "A": "クラウドストレージサービス",
            "B": "サーバー管理サービス",
            "C": "メッセージ伝達サービス",
            "D": "データベース管理サービス"
        },
        "correct_option": "C"
    },
    {
        "question": "2.AWS SNS で新しいトピックを作成するにはどうすればよいですか？",
        "options": {
            "A": "AWS CLI を使用する",
            "B": "AWS Management Console を使用する",
            "C": "AWS SDK を使用する",
            "D": "All of the above"
        },
        "correct_option": "D"
    },
    {
        "question": "3.AWS SNS の主な用途は何ですか？",
        "options": {
            "A": "データストレージ",
            "B": "データ分析",
            "C": "メッセージ伝達",
            "D": "データバックアップ"
        },
        "correct_option": "C"
    },
    {
        "question": "4.AWS SNS を使用して SMS メッセージを送信するにはどうすればよいですか？",
        "options": {
            "A": "AWS CLI を使用する",
            "B": "AWS Management Console を使用する",
            "C": "AWS SDK を使用する",
            "D": "AWS Lambda を使用する"
        },
        "correct_option": "B"
    },
    {
        "question": "5.AWS SNS にトピックをサブスクライブするにはどうすればよいですか？",
        "options": {
            "A": "AWS CLI を使用する",
            "B": "AWS Management Console を使用する",
            "C": "AWS SDK を使用する",
            "D": "AWS Lambda を使用する"
        },
        "correct_option": "B"
    },
    {
        "question": "6.AWS SNS はどのようなプロトコルを使用してメッセージを伝達できないのは下記のどれですか？",
        "options": {
            "A": "HTTP",
            "B": "HTTPS",
            "C": "SMTP",
            "D": "TCP/IP"
        },
        "correct_option": "D"
    },
    {
        "question": "7.AWS SNS でメッセージフィルタリングを有効にするにはどうすればよいですか？",
        "options": {
            "A": "AWS CLI を使用する",
            "B": "AWS Management Console を使用する",
            "C": "AWS SDK を使用する",
            "D": "AWS Lambda を使用する"
        },
        "correct_option": "B"
    },
    {
      "question": "8.AWS SNS でクロスアカウントアクセスを有効にするにはどうすれすか？",
        "options": {
            "A": "IAM ロールを作成する",
            "B": "IAM ポリシーを作成する",
            "C": "クロスアカウントポリシーを作成する",
            "D": "AWS SNS ではクロスアカウントアクセスはできない"
        },
        "correct_option": "C"
    },
    {
        "question": "9.AWS SNS でクロスリージョンレプリケーションを有効にするにはどうすればよいですか？",
        "options": {
            "A": "AWS CLI を使用して有効にする",
            "B": "AWS Management Console を使用して有効にする",
            "C": "AWS SDK を使用して有効にする",
            "D": "AWS Lambda を使用して有効にする"
        },
        "correct_option": "B"
        },
    {
        "question": "10.AWS SNS でデッドレタークエューを使用するにはどうすればよいですか？",
        "options": {
            "A": "AWS CLI を使用して有効にする",
            "B": "AWS Management Console を使用して有効にする",
            "C": "AWS SDK を使用して有効にする",
            "D": "AWS Lambda を使用して有効にする"
        },
        "correct_option": "B"
    }
]    

vpc_peering_questions = [
    {
        "question": "1.VPC Peering とは何ですか？",
        "options": {
            "A": "異なる AWS リージョンの VPC を接続するサービス",
            "B": "異なる AWS アカウントの VPC を接続するサービス",
            "C": "VPC と従来のデータセンターを接続するサービス",
            "D": "A と B"
        },
        "correct_option": "B"
    },
    {
        "question": "2.AWS で VPC Peering 接続を作成するにはどうすればよいですか？",
        "options": {
            "A": "AWS CLI を使用する",
            "B": "AWS Management Console を使用する",
            "C": "AWS SDK を使用する",
            "D": "AWS Lambda を使用する"
        },
        "correct_option": "B"
    },
    {
        "question": "3.VPC Peering 接続を使用すると、どのような利点がありますか？",
        "options": {
            "A": "高可用性",
            "B": "スケーラビリティ",
            "C": "より高いセキュリティ",
            "D": "より低いコスト"
        },
        "correct_option": "B"
    },
    {
        "question": "4.VPC Peering 接続は、異なる AWS アカウントを跨いで行うことができますか？",
        "options": {
            "A": "できます",
            "B": "できません",
            "C": "同じリージョン内のみ可能",
            "D": "VPC のネットワーク構成によって異なる"
        },
        "correct_option": "A"
    },
    {
        "question": "5.VPC Peering 接続は、異なる AWS リージョンを跨いで行うことができますか？",
        "options": {
            "A": "できます",
            "B": "できません",
            "C": "同じ AWS Region 内のみ可能",
            "D": "VPC のネットワーク構成によって異なる"
        },
        "correct_option": "A"
    },
    {
        "question": "6.VPC Peering 接続で、同じ VPC 内の異なるアカウントを接続することはできますか？",
        "options": {
            "A": "できます",
            "B": "できません",
            "C": "VPC のネットワーク構成によって異なる",
            "D": "AWS のアカウント制限によって異なる"
        },
        "correct_option": "B"
    },
    {
        "question": "7.VPC Peering 接続の最大帯域幅は何ですか？",
        "options": {
            "A": "1 Gbps",
            "B": "5 Gbps",
            "C": "10 Gbps",
            "D": "無上限"
        },
        "correct_option": "D"
    },
    {
        "question": "8.VPC Peering 接続の状態を確認する方法は何ですか？",
        "options": {
            "A": "AWS CLI を使用する",
            "B": "AWS Management Console を使用する",
            "C": "AWS SDK を使用する",
            "D": "AWS Lambda を使用する"
        },
        "correct_option": "B"
        },
    {
      "question": "9.VPC Peering 接続を解除するにはどうすればよいですか？",
      "options": {
        "A": "AWS CLI を使用する",
        "B": "AWS Management Console を使用する",
        "C": "AWS SDK を使用する",
        "D": "AWS Lambda を使用する"
      },
      "correct_option": "B"
    },
    {
      "question": "10.VPC Peering 接続を使用してトラフィックをルーティングするにはどうすればよいですか？",
      "options": {
        "A": "ルートテーブルを変更する",
        "B": "VPC フローログを有効化する",
        "C": "Amazon VPC ファイアウォールを使用する",
        "D": "AWS WAF を使用する"
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
    print("1. AWS SNS")
    print("2. AWS VPC Peering")
    test_type = input("テストタイプを入力（1 または 2）：")

    # 選択に応じて問題リストをロード
    if test_type == "1":
        questions = sns_questions
        test_type_name = "AWS SNS"
    elif test_type == "2":
        questions = vpc_peering_questions
        test_type_name = "AWS VPC Peering"
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
