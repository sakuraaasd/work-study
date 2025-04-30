import openpyxl
from datetime import datetime

iam_questions = [
    {
        "question": "AWSアカウントの所有者が使用する特殊なユーザーは何ですか？",
        "options": {
            "A": "IAMユーザー",
            "B": "ルートユーザー",
            "C": "IAMロール",
            "D": "IAMポリシー"
        },
        "correct_option": "B"
    },
    {
        "question": "IAMユーザーとIAMロールの主な違いは何ですか？",
        "options": {
            "A": "IAMユーザーは永続的な資格情報を持ち、IAMロールは一時的な資格情報を持つ",
            "B": "IAMユーザーは一時的な資格情報を持ち、IAMロールは永続的な資格情報を持つ",
            "C": "IAMユーザーはAWSリソースにアクセスできず、IAMロールはアクセスできる",
            "D": "IAMユーザーはAWSリソースにアクセスでき、IAMロールはアクセスできない"
        },
        "correct_option": "A"
    },
    {
        "question": "IAMポリシーで設定できる2つの主要な要素は何ですか？",
        "options": {
            "A": "アクションとリソース",
            "B": "ユーザーとロール",
            "C": "パスワードポリシーとアクセスキー",
            "D": "アクセスキーとシークレットキー"
        },
        "correct_option": "A"
    },
    {
        "question": "IAMで、他のアカウントのリソースにアクセスするために使用される機能は何ですか？",
        "options": {
            "A": "スイッチロール",
            "B": "クロスアカウントアクセス",
            "C": "ロールチェーン",
            "D": "AとB"
        },
        "correct_option": "D"
    },
    {
        "question": "IAMユーザーのパスワードポリシーで設定できる要素はどれですか？",
        "options": {
            "A": "最小パスワード長",
            "B": "パスワードの履歴",
            "C": "パスワードの有効期限",
            "D": "すべての上記"
        },
        "correct_option": "D"
    },
    {
        "question": "IAM ロールはどのような目的で使用されますか？",
        "options": {
            "A": "AWSリソースにアクセス許可を付与する",
            "B": "IAMユーザーにパスワードポリシーを適用する",
            "C": "AWSアカウント間でリソースにアクセスするために切り替える",
            "D": "IAMユーザーにMFAデバイスを割り当てる"
        },
        "correct_option": "A"
    },
    {
        "question": "AWS IAMで、Switch Role機能の主な目的は何ですか？",
        "options": {
            "A": "IAMユーザーのパスワードを変更する",
            "B": "IAMユーザー間でアクセス許可を共有する",
            "C": "IAMユーザーとIAMロールを関連付ける",
            "D": "AWSアカウント間で一時的なアクセス許可を付与する"
        },
        "correct_option": "D"
    },
    {
        "question": "IAM ポリシーの種類にはどのようなものがありますか？",
        "options": {
            "A": "インラインポリシーとマネージドポリシー",
            "B": "インラインポリシーとデフォルトポリシー",
            "C": "マネージドポリシーとスタンダードポリシー",
            "D": "デフォルトポリシーとスタンダードポリシー"
        },
        "correct_option": "A"
    },
    {
        "question": "IAM ユーザーが他のAWSアカウントのリソースにアクセスできるようにするには、どの操作を行う必要がありますか？",
        "options": {
            "A": "IAMユーザーにロールを割り当てる",
            "B": "IAMユーザーに他のアカウントのリソースアクセス許可を持つポリシーを割り当てる",
            "C": "IAMユーザーに他のアカウントのリソースアクセス許可を持つインラインポリシーを作成する",
            "D": "他のアカウントのリソースにアクセスするために、IAMユーザーでSwitch Roleを使用する"
        },
        "correct_option": "D"
    },
    {
        "question": "IAM ユーザーにMFAデバイスを割り当てる目的は何ですか？",
        "options": {
            "A": "アカウントのセキュリティを強化する",
            "B": "アカウント間でリソースにアクセスするために",
            "C": "IAM ポリシーを編集する",
            "D": "アカウントのリージョンを変更する"
        },
        "correct_option": "A"
    }
]    

vpc_questions = [
    {
        "question": "AWS VPCの正式名称は何ですか？",
        "options": {
            "A": "Amazon Web Services Virtual Private Cloud",
            "B": "Amazon Web Services Virtual Public Cloud",
            "C": "Amazon Web Services Virtual Private Connection",
            "D": "Amazon Web Services Virtual Public Connection"
        },
        "correct_option": "A"
    },
    {
        "question": "AWS VPCで、デフォルトのネットワークアクセス制御リスト（NACL）ルールはどれですか？",
        "options": {
            "A": "すべての受信および送信トラフィックを許可する",
            "B": "すべての受信および送信トラフィックを拒否する",
            "C": "すべての受信トラフィックを許可し、すべての送信トラフィックを拒否する",
            "D": "すべての送信トラフィックを許可し、すべての受信トラフィックを拒否する"
        },
        "correct_option": "A"
    },
    {
        "question": "AWS VPCで、サブネットの目的は何ですか？",
        "options": {
            "A": "ネットワークをより小さな部分に分割して、セキュリティと管理性を向上させる",
            "B": "すべての仮想マシンが同じネットワークに接続されることを確認する",
            "C": "各ネットワークデバイスにパブリックIPアドレスを割り当てる",
            "D": "すべてのAWS VPC設定情報を保存する"
        },
        "correct_option": "A"
    },
    {
        "question": "AWS VPCのセキュリティグループ（SG）とネットワークアクセス制御リスト（NACL）の主な違いは何ですか？",
        "options": {
            "A": "SGはステートフルで、NACLはステートレスです",
            "B": "SGはステートレスで、NACLはステートフルです",
            "C": "SGは受信トラフィックを制御し、NACLは送信トラフィックを制御します",
            "D": "SGとNACLの両方が、受信および送信トラフィックの制御に使用されます"
        },
        "correct_option": "A"
    },
    {
        "question": "AWS VPCで、オンプレミスデータセンターをAWS VPCに接続する方法は？",
        "options": {
            "A": "VPN接続を使用する",
            "B": "Direct Connect（直接接続）を使用する",
            "C": "Elastic IPを使用する",
            "D": "AとB"
        },
        "correct_option": "D"
    },
    {
        "question": "AWS VPCのインターネットゲートウェイの主な目的は何ですか？",
        "options": {
            "A": "VPC内のリソースとインターネットを接続する",
            "B": "VPC内のリソース間でのみ通信を許可する",
            "C": "VPC内のリソースの負荷分散を実現する",
            "D": "VPC内のリソースのバックアップを作成する"
        },
        "correct_option": "A"
    },
    {
        "question": "AWS VPCのNATゲートウェイはどのような目的で使用されますか？",
        "options": {
            "A": "プライベートサブネット内のリソースがインターネットにアクセスできるようにする",
            "B": "プライベートサブネット内のリソース間で通信を許可する",
            "C": "インターネットトラフィックをVPC内のすべてのリソースに分散する",
            "D": "VPC内のリソースのスケーラビリティを向上させる"
        },
        "correct_option": "A"
    },
    {
        "question": "AWS VPCのエンドポイントはどのような目的で使用されますか？",
        "options": {
            "A": "VPC内のリソースとAWSサービス間のプライベート接続を確立する",
            "B": "VPC内のリソースとインターネット間の接続を確立する",
            "C": "VPC内のリソースとオンプレミスデータセンター間の接続を確立する",
            "D": "VPC内のリソースと他のVPC間の接続を確立する"
        },
        "correct_option": "A"
    },
    {
        "question": "AWS VPCのルートテーブルで主に何を行いますか？",
        "options": {
            "A": "サブネット間でのトラフィックのルーティング",
            "B": "NATゲートウェイの作成",
            "C": "インターネットゲートウェイの構成",
            "D": "セキュリティグループルールの定義"
        },
        "correct_option": "A"
    },
    {
        "question": "Elastic IPアドレスとは何ですか？",
        "options": {
            "A": "VPC内のリソースに割り当てられる静的なプライベートIPアドレス",
            "B": "VPC内のリソースに割り当てられる静的なパブリックIPアドレス",
            "C": "VPC内のリソースに割り当てられる動的なプライベートIPアドレス",
            "D": "VPC内のリソースに割り当てられる動的なパブリックIPアドレス"
        },
        "correct_option": "B"
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
    print("1. AWS VPC")
    print("2. AWS IAM")
    test_type = input("テストタイプを入力（1 または 2）：")

    # 選択に応じて問題リストをロード
    if test_type == "1":
        questions = vpc_questions
        test_type_name = "AWS VPC"
    elif test_type == "2":
        questions = iam_questions
        test_type_name = "AWS IAM"
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
