import openpyxl
from datetime import datetime

ELB_questions = [
    {
        "question": "1.AWSのApplication Load Balancer(ALB)とNetwork Load Balancer(NLB)の違いは何ですか？",
        "options": {
        "A": "ALBはレイヤー7、NLBはレイヤー4で動作する",
        "B": "ALBはレイヤー4、NLBはレイヤー7で動作する",
        "C": "ALBはHTTP/HTTPSのみ、NLBはTCP/UDPのみサポートする",
        "D": "ALBはTCP/UDPのみ、NLBはHTTP/HTTPSのみサポートする"
        },
        "correct_option": "A"
    },
    {
        "question": "2.どのAWSロードバランサーが静的IPアドレスをサポートしていますか？",
        "options": {
        "A": "Application Load Balancer (ALB)",
        "B": "Network Load Balancer (NLB)",
        "C": "Classic Load Balancer (CLB)",
        "D": "ALBとCLB"
        },
        "correct_option": "B"
    },
    {
        "question": "3.複数のTLS証明書を使用するロードバランサーはどれですか？",
        "options": {
        "A": "Application Load Balancer (ALB)",
        "B": "Network Load Balancer (NLB)",
        "C": "Classic Load Balancer (CLB)",
        "D": "ALBとNLB"
        },
        "correct_option": "A"
    },
    {
        "question": "4.UDPトラフィックをサポートするAWSロードバランサーはどれですか？",
        "options": {
        "A": "Application Load Balancer (ALB)",
        "B": "Network Load Balancer (NLB)",
        "C": "Classic Load Balancer (CLB)",
        "D": "ALBとNLB"
        },
        "correct_option": "B"
    },
    {
        "question": "5.リスナーを設定する際、ALBではどのプロトコルがサポートされていますか？",
        "options": {
        "A": "HTTPおよびHTTPS",
        "B": "TCPおよびUDP",
        "C": "TCPおよびHTTP",
        "D": "UDPおよびHTTPS"
        },
        "correct_option": "A"
    },
    {
        "question": "6.リスナーを設定する際、NLBではどのプロトコルがサポートされていますか？",
        "options": {
        "A": "HTTPおよびHTTPS",
        "B": "TCPおよびUDP",
        "C": "TCPおよびHTTP",
        "D": "UDPおよびHTTPS"
        },
        "correct_option": "B"
    },
    {
        "question": "7.AWSロードバランサーでターゲットグループのヘルスチェックを設定する際、どのプロトコルがサポートされていますか？",
        "options": {
        "A": "HTTP, HTTPS, TCP",
        "B": "HTTP, HTTPS, TCP, UDP",
        "C": "HTTP, HTTPSのみ",
        "D": "TCP, UDPのみ"
        },
        "correct_option": "A"
    },
    {
        "question": "8.アプリケーションロードバランサー(ALB)でコンテンツベースのルーティングを実現するには、どの機能を使用しますか？",
        "options": {
        "A": "ターゲットグループ",
        "B": "パスパターン",
        "C": "リスナールール",
        "D": "ヘルスチェック"
        },
        "correct_option": "C"
    },
    {
        "question": "9.AWSで高可用性を維持するために、ロードバランサーをどのように設定する必要がありますか？",
        "options": {
        "A": "複数のアベイラビリティーゾーンにまたがる",
        "B": "単一のアベイラビリティーゾーン内に配置",
        "C": "複数のリージョンにまたがる",
        "D": "単一のリージョン内に配置"
        },
        "correct_option": "A"
    },
    {
        "question": "10.ネットワークロードバランサー(NLB)がバックエンドのインスタンスにトラフィックを送信する際、どのタイプのアドレスが使用されますか？",
        "options": {
        "A": "パブリックIPアドレス",
        "B": "プライベートIPアドレス",
        "C": "Elastic IPアドレス",
        "D": "バーチャルIPアドレス"
        },
        "correct_option": "B"
    }
]

ami_questions = [
    {
        "question": "1.AMI（Amazon Machine Image）の主な目的は何ですか？",
        "options": {
        "A": "データを保存する",
        "B": "EC2インスタンスの起動時のテンプレートとして使用する",
        "C": "EC2インスタンスのモニタリング",
        "D": "アプリケーションのデプロイ"
        },
        "correct_option": "B"
    },
    {
        "question": "2.AMIにはどのようなコンポーネントが含まれていますか？",
        "options": {
        "A": "ルートボリュームテンプレート、カーネル、ラムディスク",
        "B": "ネットワーク設定、ボリューム構成、IAMロール",
        "C": "セキュリティグループ、キーペア、インスタンスタイプ",
        "D": "VPC設定、サブネット、ルートテーブル"
        },
        "correct_option": "A"
    },
    {
        "question": "3.AMIを共有する際に指定できる範囲はどれですか？",
        "options": {
        "A": "指定されたAWSアカウントのみ",
        "B": "同じリージョン内のすべてのAWSアカウント",
        "C": "すべてのAWSアカウント",
        "D": "同じVPC内のAWSアカウントのみ"
        },
        "correct_option": "C"
    },
    {
        "question": "4.AMIはどのAWSサービスと密接に関連していますか？",
        "options": {
        "A": "Amazon S3",
        "B": "Amazon EC2",
        "C": "AWS Lambda",
        "D": "Amazon RDS"
        },
        "correct_option": "B"
    },
    {
        "question": "5.異なるリージョンでAMIを使用したい場合、どうすればよいですか？",
        "options": {
        "A": "リージョン間でAMIを複製する",
        "B": "AMIを再作成する",
        "C": "AMIをエクスポートしてからインポートする",
        "D": "リージョン間でAMIを共有する"
        },
        "correct_option": "A"
    },
    {
        "question": "6.オペレーティングシステムに変更を加えた後、どのようにして新しいAMIを作成できますか？",
        "options": {
        "A": "EC2インスタンスを再起動する",
        "B": "EC2インスタンスからAMIを作成する",
        "C": "EC2インスタンスを停止してからAMIを作成する",
        "D": "EC2インスタンスを終了してからAMIを作成する"
        },
        "correct_option": "B"
    },
    {
        "question": "7.AMIでサポートされているファイルシステムは何ですか？",
        "options": {
        "A": "NTFS",
        "B": "ext4",
        "C": "HFS+",
        "D": "AMIはファイルシステムに依存しない"
        },
        "correct_option": "D"
    },
    {
        "question": "8.AWSマーケットプレイスからAMIを取得する際、どのようなオプションが利用可能ですか？",
        "options": {
        "A": "無料、有料、およびBYOL（Bring Your Own License）",
        "B": "無料および有料のみ",
        "C": "無料およびBYOLのみ",
        "D": "有料およびBYOLのみ"
        },
        "correct_option": "A"
    },
    {
        "question": "9.EC2インスタンスのAMIを作成すると、どのようなリソースが作成されますか？",
        "options": {
        "A": "EBSスナップショット",
        "B": "新しいEC2インスタンス",
        "C": "新しいEBSボリューム",
        "D": "新しいVPC"
        },
        "correct_option": "A"
    },
    {
        "question": "10.暗号化されたEBSボリュームを持つインスタンスからAMIを作成する場合、新しいAMIのボリュームはどのようになりますか？",
        "options": {
        "A": "暗号化されていない",
        "B": "暗号化された",
        "C": "暗号化の設定はAMIの作成時に選択可能",
        "D": "暗号化されたEBSボリュームからAMIを作成することはできません"
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
    print("1. AWS ELB")
    print("2. AWS AMI")
    test_type = input("テストタイプを入力（1 または 2）:")

    # 選択に応じて問題リストをロード
    if test_type == "1":
        questions = ELB_questions
        test_type_name = "AWS ELB"
    elif test_type == "2":
        questions = ami_questions
        test_type_name = "AWS AMI"       
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
