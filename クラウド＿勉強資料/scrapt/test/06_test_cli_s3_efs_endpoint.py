import openpyxl
from datetime import datetime

awscli_questions = [
    {
        "question": "1.AWS CLIをインストールするために推奨される方法は何ですか？",
        "options": {
        "A": "pipを使ってインストールする",
        "B": "apt-getを使ってインストールする",
        "C": "インストーラーをダウンロードしてインストールする",
        "D": "GitHubからソースコードをクローンしてインストールする"
        },
        "correct_option": "A"
    },
    {
        "question": "2.AWS CLIでの認証情報の設定方法は何ですか？",
        "options": {
        "A": "aws configureコマンドを使用する",
        "B": "環境変数を設定する",
        "C": "AWS Management Consoleで設定する",
        "D": "AとBの両方"
        },
        "correct_option": "D"
    },
    {
        "question": "3.AWS CLIでJSON、テキスト、およびテーブルの形式のうち、デフォルトの出力形式は何ですか？",
        "options": {
        "A": "JSON",
        "B": "テキスト",
        "C": "テーブル",
        "D": "YAML"
        },
        "correct_option": "A"
    },
    {
        "question": "4.AWS CLIのプロファイルを使用して複数のアカウントを管理する方法は何ですか？",
        "options": {
        "A": "aws configureコマンドでプロファイルを作成する",
        "B": "環境変数でプロファイルを設定する",
        "C": "CLIコマンドのオプションでプロファイルを指定する",
        "D": "AとCの両方"
        },
        "correct_option": "D"
    },
    {
        "question": "5.AWS CLIでサポートされているプログラミング言語は何ですか？",
        "options": {
        "A": "Python",
        "B": "Java",
        "C": "Ruby",
        "D": "CLIはプログラミング言語に依存しない"
        },
        "correct_option": "A"
    },
    {
        "question": "6.AWS CLIでS3バケット内のオブジェクトの一覧を表示するコマンドは何ですか？",
        "options": {
        "A": "aws s3 ls s3://バケット名",
        "B": "aws s3 list s3://バケット名",
        "C": "aws s3 get s3://バケット名",
        "D": "aws s3 show s3://バケット名"
        },
        "correct_option": "A"
    },
    {
        "question": "7.AWS CLIでEC2インスタンスを起動するために必要な最低限の情報は何ですか？",
        "options": {
        "A": "インスタンスタイプとAMI ID",
        "B":"インスタンスタイプ、AMI ID、およびキーペア名",
        "C": "インスタンスタイプ、AMI ID、およびセキュリティグループ",
        "D": "インスタンスタイプ、AMI ID、キーペア名、およびセキュリティグループ"
        },
        "correct_option": "A"
    },
    {
        "question": "8.AWS CLIでAWSリソースのタグを設定するコマンドは何ですか？",
        "options": {
        "A": "aws tag set",
        "B": "aws create-tags",
        "C": "aws tag-resource",
        "D": "aws resource-tag"
        },
        "correct_option": "B"
    },
    {
        "question": "9.AWS CLIで特定のリージョンのEC2インスタンスの一覧を取得する方法は何ですか？",
        "options": {
        "A": "aws ec2 describe-instances --region リージョン名",
        "B": "aws ec2 list-instances --region リージョン名",
        "C": "aws ec2 get-instances --region リージョン名",
        "D": "aws ec2 show-instances --region リージョン名"
        },
        "correct_option": "A"
    },
    {
        "question": "10.AWS CLIで新しいS3バケットを作成するコマンドは何ですか？",
        "options": {
        "A": "aws s3 mb s3://バケット名",
        "B": "aws s3 create s3://バケット名",
        "C": "aws s3 new s3://バケット名",
        "D": "aws s3 add s3://バケット名"
        },
        "correct_option": "A"
    }
]

endpoint_questions = [
    {
        "question": "1.VPCエンドポイントを使用する利点は何ですか？",
        "options": {
        "A": "インターネットを経由せずにAWSサービスへアクセスできる",
        "B": "VPC内のすべてのリソースが自動的に可用性が高まる",
        "C": "データ転送費用が無料になる",
        "D": "VPC内のすべてのリソースが自動的にスケーリングされる"
        },
        "correct_option": "A"
    },
    {
        "question": "2.次のうち、VPCエンドポイントがサポートしているAWSサービスはどれですか？",
        "options": {
        "A": "Amazon S3",
        "B": "Amazon EC2",
        "C": "AWS Lambda",
        "D": "Amazon RDS"
        },
        "correct_option": "A"
    },
    {
        "question": "3.VPCエンドポイントのどのタイプがAmazon S3にアクセスするために使用されますか？",
        "options": {
        "A": "インターフェースVPCエンドポイント",
        "B": "ゲートウェイVPCエンドポイント",
        "C": "プライベートリンク",
        "D": "NATゲートウェイ"
        },
        "correct_option": "B"
    },
    {
        "question": "4.次のうち、インターフェースVPCエンドポイントがサポートしているAWSサービスはどれですか？",
        "options": {
        "A": "Amazon S3",
        "B": "Amazon EC2",
        "C": "AWS Lambda",
        "D": "Amazon RDS"
        },
        "correct_option": "C"
    },
    {
        "question": "5.VPCエンドポイントサービスを利用する際、サービスプロバイダーが顧客に対して課金する方法はどれですか？",
        "options": {
        "A": "データ転送量に基づく",
        "B": "リクエスト数に基づく",
        "C": "使用時間に基づく",
        "D": "固定料金"
        },
        "correct_option": "A"
    },
    {
        "question": "6.VPCエンドポイントポリシーを使用する目的は何ですか？",
        "options": {
        "A": "VPC内のリソースへのアクセスを制限する",
        "B": "VPCエンドポイントへのアクセスを制限する",
        "C": "VPCエンドポイントを通じてアクセスできるAWSサービスを制限する",
        "D": "VPCエンドポイントに接続されたインスタンスの数を制限する"
        },
        "correct_option": "C"
    },
    {
        "question": "7.VPCエンドポイントを設定する際に使用するAWSリソースはどれですか？",
        "options": {
        "A": "サブネット",
        "B": "ルートテーブル",
        "C": "セキュリティグループ",
        "D": "すべての上記"
        },
        "correct_option": "D"
    },
    {
        "question": "8.インターフェースVPCエンドポイントを構成する際に使用されるAWSサービスはどれですか？",
        "options": {
        "A": "AWS Direct Connect",
        "B": "Amazon Route 53",
        "C": "AWS PrivateLink",
        "D": "Amazon API Gateway"
        },
        "correct_option": "C"
    },
    {
        "question": "9.インターフェースVPCエンドポイントを作成する際、どのAWSリソースが自動的に作成されますか？",
        "options": {
        "A": "Elastic IPアドレス",
        "B": "ENI（Elastic Network Interface）",
        "C": "NATゲートウェイ",
        "D": "VPN接続"
        },
        "correct_option": "B"
    },
    {
        "question": "10.次のうち、VPCエンドポイントを設定するために必要なAWSコンポーネントはどれですか？",
        "options": {
        "A": "VPCエンドポイントサービス",
        "B": "VPCエンドポイントポリシー",
        "C": "VPCエンドポイントゲートウェイ",
        "D": "すべての上記"
        },
        "correct_option": "D"
    }
]    

s3_questions = [
    {
        "question": "1.AWS S3は何ですか？",
        "options": {
        "A": "ファイルストレージサービス",
        "B": "データベースサービス",
        "C": "コンピューティングサービス",
        "D": "ネットワークサービス"
        },
        "correct_option": "A"
    },
    {
        "question": "2.S3バケット内のオブジェクトに割り当てられる最大サイズはいくつですか？",
        "options": {
        "A": "5 GB",
        "B": "10 GB",
        "C": "50 GB",
        "D": "100 GB"
        },
        "correct_option": "D"
    },
    {
        "question": "3.S3バケットに保存されたオブジェクトのデフォルトのアクセス許可は何ですか？",
        "options": {
        "A": "パブリックアクセスが許可されています。",
        "B": "パブリックアクセスが拒否されています。",
        "C": "アクセス許可は設定されていません。",
        "D": "アクセス許可は設定によって異なります。"
        },
        "correct_option": "B"
    },
    {
        "question": "4.S3バケット内のオブジェクトに割り当てられるキーの長さの最大値は何ビットですか？",
        "options": {
        "A": "1024ビット",
        "B": "2048ビット",
        "C": "4096ビット",
        "D": "8192ビット"
        },
        "correct_option": "C"
    },
    {
        "question": "5.AWS S3の料金はどのように計算されますか？",
        "options": {
        "A": "オブジェクトの格納量のみに基づいて",
        "B": "オブジェクトのアクセス数のみに基づいて",
        "C": "オブジェクトの格納量とアクセス数の両方に基づいて",
        "D": "オブジェクトの削除に基づいて"
        },
        "correct_option": "C"
    },
    {
        "question": "6.S3のバケットに対するデフォルトのアクセス許可を設定するために使用するAWSサービスは何ですか？",
        "options": {
        "A": "AWS Identity and Access Management (IAM)",
        "B": "Amazon Simple Notification Service (SNS)",
        "C": "Amazon Simple Queue Service (SQS)",
        "D": "Amazon CloudWatch"
        },
        "correct_option": "A"
    },
    {
        "question": "7.S3に保存されたオブジェクトに対する暗号化に使用されるAWSサービスは何ですか？",
        "options": {
        "A": "AWS Identity and Access Management (IAM)",
        "B": "AWS CloudHSM",
        "C": "AWS Key Management Service (KMS)",
        "D": "AWS Certificate Manager (ACM)"
        },
        "correct_option": "C"
    },
    {
        "question": "8.S3で利用可能な転送タイプはどれですか？",
        "options": {
        "A": "PUT",
        "B": "GET",
        "C": "POST",
        "D": "すべての選択肢"
        },
        "correct_option": "D"
    },
    {
        "question": "9.S3に保存されたオブジェクトに対して自動的に実行されるAWSサービスは何ですか？",
        "options": {
        "A": "AWS Lambda",
        "B": "Amazon SNS",
        "C": "Amazon SQS",
        "D": "AWS KMS"
        },
        "correct_option": "A"
    },
    {
        "question": "10.S3でオブジェクトを転送するために使用できるストレージクラスは何ですか？",
        "options": {
        "A": "標準",
        "B": "標準-Infrequent Access",
        "C": "スタンダード-IA Deep Archive",
        "D": "オールオブザアバブ"
        },
        "correct_option": "D"
    }
]
efs_questions = [
    {
        "question": "1.EFSとは何ですか？",
        "options": {
        "A": "Elastic File System",
        "B": "Elastic File Storage",
        "C": "Elastic File Server",
        "D": "Elastic File Sharing"
        },
        "correct_option": "A"
    },
    {
        "question": "2.EFSはどのようなストレージタイプですか？",
        "options": {
        "A": "オブジェクトストレージ",
        "B": "ファイルストレージ",
        "C": "ブロックストレージ",
        "D": "テープストレージ"
        },
        "correct_option": "B"
    },
    {
        "question": "3.EFSでマウントできるプロトコルは何ですか？",
        "options": {
        "A": "SFTP",
        "B": "SMB",
        "C": "FTP",
        "D": "NFS"
        },
        "correct_option": "D"
    },
    {
        "question": "4.EFSはどのようなスケーラビリティを持っていますか？",
        "options": {
        "A": "スケールアップのみ",
        "B": "スケールアウトのみ",
        "C": "スケールアップおよびスケールダウン",
        "D": "スケールインおよびスケールアウト"
        },
        "correct_option": "C"
    },
    {
        "question": "5.EFSでファイルのアクセスを制限するために使用される機能は何ですか？",
        "options": {
        "A": "VPCエンドポイント",
        "B": "AWS WAF",
        "C": "IAM",
        "D": "SG"
        },
        "correct_option": "D"
    },
    {
        "question": "6.EFSでファイルの暗号化に使用されるAWSサービスは何ですか？",
        "options": {
        "A": "AWS Certificate Manager",
        "B": "AWS Key Management Service (KMS)",
        "C": "AWS Identity and Access Management (IAM)",
        "D": "AWS CloudHSM"
        },
        "correct_option": "B"
    },
    {
        "question": "7.EFSでファイルのアクセス制御に使用されるマウントオプションは何ですか？",
        "options": {
        "A": "posixacl",
        "B": "noacl",
        "C": "posix",
        "D": "nfs4_acl"
        },
        "correct_option": "C"
    },
    {
        "question": "8.EFSでファイルのバックアップに使用できるAWSサービスは何ですか？",
        "options": {
        "A": "Amazon S3",
        "B": "Amazon Glacier",
        "C": "Amazon EBS",
        "D": "Amazon Backup"
        },
        "correct_option": "D"
    },
    {
        "question": "9.EC2で使用されるファイルシステムは何ですか？",
        "options": {
            "A": "NTFS",
            "B": "HFS+",
            "C": "ext4",
            "D": "EFS"
        },
        "correct_option": "D"
    },
    {
        "question": "10.EFSで使用できるストレージクラスは何ですか？",
        "options": {
            "A": "S3 Standard-IC2",
            "B": "S3 Intelligent-Tiering",
            "C": "S3 Glacier",
            "D": "S3 Standard"
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
    print("1. AWS CLI")
    print("2. AWS Endpoint")
    print("3. AWS S3")
    print("4. AWS EFS")    
    test_type = input("テストタイプを入力（1 または 2,3,4）:")

    # 選択に応じて問題リストをロード
    if test_type == "1":
        questions = awscli_questions
        test_type_name = "AWS CLI"
    elif test_type == "2":
        questions = endpoint_questions
        test_type_name = "AWS Endpoint"
    elif test_type == "3":
        questions = s3_questions
        test_type_name = "AWS S3" 
    elif test_type == "4":
        questions = efs_questions
        test_type_name = "AWS EFS"                       
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
