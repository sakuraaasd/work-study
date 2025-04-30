import openpyxl
from datetime import datetime

cloudwatch_questions = [
    {
        "question": "1.CloudWatchはどのAWSサービスと統合していますか？",
        "options": {
        "A": "Amazon S3",
        "B": "Amazon EC2",
        "C": "Amazon RDS",
        "D": "すべてのAWSサービス"
        },
        "correct_option": "D"
    },
    {
        "question": "2.CloudWatchでサポートされているデータタイプは何ですか？",
        "options": {
        "A": "数値と文字列",
        "B": "数値とブール値",
        "C": "数値、文字列、およびログデータ",
        "D": "数値、文字列、ブール値、およびログデータ"
        },
        "correct_option": "D"
    },
    {
        "question": "3.CloudWatch Logsは、どのような種類のログを処理できますか？",
        "options": {
        "A": "アプリケーションログ",
        "B": "Webサーバーログ",
        "C": "システムログ",
        "D": "すべてのログタイプ"
        },
        "correct_option": "D"
    },
    {
        "question": "4.CloudWatchアラームで設定できるしきい値の最大数はいくつですか？",
        "options": {
        "A": "1",
        "B": "2",
        "C": "5",
        "D": "10"
        },
        "correct_option": "D"
    },
    {
        "question": "5.CloudWatchアラームをトリガーすることができるメトリックスの種類は何ですか？",
        "options": {
        "A": "データベースメトリックス",
        "B": "EC2メトリックス",
        "C": "S3メトリックス",
        "D": "すべてのAWSメトリックス"
        },
        "correct_option": "D"
    },
    {
        "question": "6.CloudWatchで使用されるスケジュール式の例は何ですか？",
        "options": {
        "A": "cron(0/5 * * * ? )",
        "B": "cron(/5 * * * ? *)",
        "C": "cron(5 * * * ? *)",
        "D": "cron(0 5 * * ? *)"
        },
        "correct_option": "D"
    },
    {
        "question": "7.CloudWatchメトリックスを取得するために使用されるAWSサービスは何ですか？",
        "options": {
        "A": "Amazon EC2",
        "B": "Amazon S3",
        "C": "AWS Lambda",
        "D": "すべてのAWSサービス"
        },
        "correct_option": "D"
    },
    {
        "question": "8.CloudWatchの無料利用枠は何ですか？",
        "options": {
        "A": "10メトリクス",
        "B": "100メトリクス",
        "C": "1000メトリクス",
        "D": "無制限"
        },
        "correct_option": "A"
    },
    {
    "question": "9.CloudWatch Logsにデータを書き込むために使用できないAWSサービスは何ですか？",
    "options": {
        "A": "CloudTrail",
        "B": "CloudFormation",
        "C": "CloudWatch Events",
        "D": "Lambda"
    },
    "correct_option": "B"
    },
    {
        "question": "10.CloudWatchダッシュボードに含めることができるものは何ですか？",
        "options": {
            "A": "アラーム",
            "B": "ログファイル",
            "C": "AWSリソースの状態",
            "D": "All of the Above"
        },
        "correct_option": "D"
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
        "correct_option": "D"
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

auto_scaling_questions = [
    {
        "question": "1.Auto Scalingグループの最小および最大サイズを設定するために使用される値は何ですか？",
        "options": {
        "A": "ミリ秒",
        "B": "メガバイト",
        "C": "カウント",
        "D": "パーセント"
        },
        "correct_option": "C"
    },
    {
        "question": "2.Auto Scalingグループで設定できるメトリックスには何が含まれますか？",
        "options": {
        "A": "CPU使用率、メモリ使用率",
        "B": "ネットワーク入力/出力",
        "C": "ディスク入力/出力",
        "D": "すべての選択肢"
        },
        "correct_option": "D"
    },
    {
        "question": "3.Auto Scalingグループで、新しいEC2インスタンスが作成されたときに自動的に実行されるスクリプトは何ですか？",
        "options": {
        "A": "ユーザーデータスクリプト",
        "B": "フックスクリプト",
        "C": "スタートアップスクリプト",
        "D": "クリーンアップスクリプト"
        },
        "correct_option": "A"
    },
    {
        "question": "4.Auto Scalingグループで、EC2インスタンスを自動的に停止するための条件を指定するには、どの機能を使用しますか？",
        "options": {
        "A": "CloudFormation",
        "B": "CloudWatch",
        "C": "Elastic Load Balancing",
        "D": "Auto Scaling Policies"
        },
        "correct_option": "D"
    },
    {
        "question": "5.Auto Scalingグループを作成するとき、どのリソースが必要ですか？",
        "options": {
        "A": "IAMロール",
        "B": "Amazon RDSデータベース",
        "C": "Amazon S3バケット",
        "D": "Amazon VPC"
        },
        "correct_option": "D"
    },
    {
        "question": "6.Auto Scalingグループで、異なるAZにあるEC2インスタンスにトラフィックを分散するために使用されるAWSサービスは何ですか？",
        "options": {
        "A": "Amazon CloudFront",
        "B": "Amazon Route 53",
        "C": "Amazon Elastic Load Balancing",
        "D": "AWS Direct Connect"
        },
        "correct_option": "C"
    },
    {
        "question": "7.Auto Scalingグループで、どのメトリックスを使用してスケーリングポリシーを設定できますか？",
        "options": {
            "A": "CPU使用率",
            "B": "ネットワーク入力/出力",
            "C": "ディスク使用率",
            "D": "すべての上記"
        },
        "correct_option": "D"
    },
    {
        "question": "8.Auto Scalingグループのスケーリングイベントの一つは何ですか？",
        "options": {
        "A": "Launch",
        "B": "Stop",
        "C": "Terminate",
        "D": "Start"
        },
        "correct_option": "A"
    },
    {
        "question": "9.Auto Scalingグループで使用される2つのアクションタイプは何ですか？",
        "options": {
        "A": "Scaling In、Scaling Up",
        "B": "Add Instance、Remove Instance",
        "C": "Launch、Terminate",
        "D": "Create、Delete"
        },
        "correct_option": "C"
    },
    {
        "question": "10.Auto Scalingグループで、どのスケーリングポリシーで、指定された台数または割合に応じてインスタンスをスケーリングできますか？",
        "options": {
        "A": "単純スケーリングポリシー",
        "B": "ステップスケーリングポリシー",
        "C": "ターゲットトラッキングスケーリングポリシー",
        "D": "詳細設定"
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
    print("1. AWS CloudWatch")
    print("2. AWS AutoScaling")
    test_type = input("テストタイプを入力（1 または 2）：")

    # 選択に応じて問題リストをロード
    if test_type == "1":
        questions = cloudwatch_questions
        test_type_name = "AWS CloudWatch"
    elif test_type == "2":
        questions = auto_scaling_questions
        test_type_name = "AWS AutoScaling"
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
