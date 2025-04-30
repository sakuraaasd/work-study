import openpyxl
from datetime import datetime

rds_questions = [
    {
      "question": "1.Dockerとは何ですか？",
      "options": {
        "B": "アプリケーションをコンテナ内にパッケージ化するプラットフォーム",
        "A": "クラウドネットワークを構築するプラットフォーム",
        "C": "アプリケーションをデプロイするプラットフォーム",
        "D": "アプリケーションを監視するプラットフォーム"
      },
      "correct_option": "B"
    },
    {
      "question": "2.Dockerイメージとは何ですか？",
      "options": {
        "C": "Dockerコンテナを作成するための静的ファイル",
        "B": "Dockerホストを作成するための静的ファイル",
        "A": "Dockerネットワークを作成するための静的ファイル",
        "D": "Dockerイメージを表示するための静的ファイル"
      },
      "correct_option": "C"
    },
    {
      "question": "3.Dockerイメージを作成する方法について説明してください。",
      "options": {
        "D": "Dockerfileを作成し、そのファイルを使用してイメージをビルドする",
        "B": "Dockerホスト上でアプリケーションを実行し、その状態からイメージを作成する",
        "C": "Dockerネットワークを作成し、そのネットワークからイメージを作成する",
        "A": "Dockerイメージをダウンロードして、そのイメージから新しいイメージを作成する"
      },
      "correct_option": "D"
    },
    {
      "question": "4.Dockerコンテナとは何ですか？",
      "options": {
        "A": "Dockerイメージの実行可能なインスタンス",
        "B": "Dockerイメージを編集するためのインターフェース",
        "C": "Dockerイメージを共有するためのプラットフォーム",
        "D": "Dockerイメージをダウンロードするためのプラットフォーム"
      },
      "correct_option": "A"
    },
    {
        "question": "5. Docker Hubとは何ですか？",
        "options": {
          "B": "Dockerコンテナの管理と配布のためのオンラインレジストリ",
          "A": "Dockerイメージを作成するためのオンラインIDE",
          "C": "Dockerコンテナを監視するためのオンラインプラットフォーム",
          "D": "Dockerコンテナをデプロイするためのオンラインプラットフォーム"
      },
        "correct_option": "B"
    },
    {
        "question": "6. Dockerコンテナの起動方法について説明してください。",
        "options": {
          "A": "docker runコマンドを使用してコンテナを起動する",
          "B": "docker stopコマンドを使用してコンテナを起動する",
          "C": "docker createコマンドを使用してコンテナを起動する",
          "D": "docker buildコマンドを使用してコンテナを起動する"
      },
        "correct_option": "A"
    },
    {
        "question": "7. Dockerコンテナの停止方法について説明してください。",
        "options": {
          "C": "docker stopコマンドを使用してコンテナを停止する",
          "B": "docker removeコマンドを使用してコンテナを停止する",
          "A": "docker deleteコマンドを使用してコンテナを停止する",
          "D": "docker killコマンドを使用してコンテナを停止する"
      },
        "correct_option": "C"
    },
    {
        "question": "8. Dockerイメージの削除方法について説明してください。",
        "options": {
            "A": "docker rmiコマンドを使用してイメージを削除する",
            "B": "docker rmコマンドを使用してイメージを削除する",
            "C": "docker deleteコマンドを使用してイメージを削除する",
            "D": "docker killコマンドを使用してイメージを削除する"
      },
        "correct_option": "A"
    },
    {
        "question": "9. Dockerネットワークとは何ですか？",
        "options": {
          "A": "Dockerコンテナ間の通信を可能にする仮想ネットワーク",
          "B": "Dockerイメージ間の通信を可能にする仮想ネットワーク",
          "C": "Dockerホスト間の通信を可能にする仮想ネットワーク",
          "D": "DockerコンテナとホストOS間の通信を可能にする仮想ネットワーク"
        },
          "correct_option": "A"
    },
    {
        "question": "10. Dockerボリュームとは何ですか？",
        "options": {
          "C": "Dockerコンテナがデータを永久保存するためのディレクトリまたはファイル",
          "B": "Dockerコンテナがアクセスするための仮想ネットワーク",
          "A": "Dockerイメージを配布するためのレジストリ",
          "D": "Dockerコンテナを管理するためのプラットフォーム"
        },
        "correct_option": "C"
    },
    {
        "question": "11. Dockerコンテナのポートフォワーディングについて説明してください。",
        "options": {
            "A": "DockerコンテナのポートをホストOSのポートにマッピングすることで、外部からコンテナ内のアプリケーションにアクセスできるようにする",
            "B": "DockerコンテナのネットワークをホストOSのネットワークにマッピングすることで、外部からコンテナ内のアプリケーションにアクセスできるようにする",
            "C": "DockerコンテナのファイルシステムをホストOSのファイルシステムにマウントすることで、外部からコンテナ内のファイルにアクセスできるようにする",
            "D": "DockerコンテナのコマンドをホストOSのシェルで実行することで、外部からコンテナ内のプログラムを実行できるようにする"
      },
      "correct_option": "A"
    },
    {
        "question": "12. Docker Composeとは何ですか？",
        "options": {
            "A": "複数のDockerコンテナを定義し、管理するためのツール",
            "B": "Dockerイメージをビルドするためのツール",
            "C": "Dockerコンテナを監視するためのツール",
            "D": "Dockerコンテナをデプロイするためのツール"
        },
        "correct_option": "A"
    },
    {
        "question": "13. Docker Composeで定義された複数のコンテナを起動するコマンドは何ですか？",
        "options": {
            "D": "docker-compose up",
            "B": "docker-compose start",
            "C": "docker-compose run",
            "A": "docker-compose create"
        },
        "correct_option": "D"
    },
    {
        "question": "14. Docker Composeで定義された複数のコンテナを停止するコマンドは何ですか？",
        "options": {
            "D": "docker-compose down",
            "B": "docker-compose stop",
            "C": "docker-compose kill",
            "A": "docker-compose remove"
        },
        "correct_option": "D"
    },
    {
        "question": "15. Dockerfileとは何ですか？また、Dockerイメージをビルドするためにどのように使用されますか？",
        "options": {
            "A": "アプリケーションの構成を定義し、Dockerイメージをビルドするために使用されます。",
            "B": "アプリケーションをデプロイするためのファイル",
            "C": "Dockerコンテナを起動するためのスクリプト",
            "D": "Dockerホストを作成するためのファイル"
        },
        "correct_option": "A"
    },
    {
        "question": "16. Dockerfileで使用される命令について説明してください。",
        "options": {
            "C": "RUN、CMD、COPYなどがあり、それぞれ異なる目的で使用されます。",
            "B": "DOCKER、IMAGE、BUILDなどがあり、それぞれ異なる目的で使用されます。",
            "A": "COMPOSE、SERVICE、NETWORKなどがあり、それぞれ異なる目的で使用されます。",
            "D": "BUILD、RUN、STARTなどがあり、それぞれ異なる目的で使用されます。"
        },
        "correct_option": "C"
    },
    {
        "question": "17. Dockerfileで使用されるFROM命令について説明してください。",
        "options": {
            "A": "ベースイメージを指定します。",
            "B": "コンテナを作成するためのファイルを指定します。",
            "C": "Dockerイメージを削除するための命令を指定します。",
            "D": "Dockerイメージに追加するファイルを指定します。"
        },
        "correct_option": "A"
    },
    {
        "question": "18. Dockerfileで使用されるCMD命令について説明してください。",
        "options": {
            "C": "コンテナの実行時に実行されるコマンドを指定します。",
            "B": "Dockerイメージをビルドする際に実行されるコマンドを指定します。",
            "A": "コンテナを起動するためのスクリプトを指定します。",
            "D": "Dockerイメージに必要な依存関係をインストールするためのコマンドを指定します。"
        },
        "correct_option": "C"
    },
    {
        "question": "19. Dockerfileで使用されるWORKDIR命令について説明してください。",
        "options": {
            "B": "作業ディレクトリを指定します。",
            "A": "Dockerイメージに必要なパッケージをインストールするためのディレクトリを指定します。",
            "C": "Dockerイメージに含まれるファイルの場所を指定します。",
            "D": "Dockerイメージに含まれるファイルを実行するためのディレクトリを指定します。"
        },
        "correct_option": "B"
    },
    {
        "question": "20. Dockerfileで使用されるENV命令について説明してください。",
        "options": {
            "A": "環境変数を設定します。",
            "B": "Dockerイメージをビルドするための環境変数を設定します。",
            "C": "コンテナを起動するための環境変数を設定します。",
            "D": "Dockerイメージに必要な依存関係をインストールするための環境変数を設定します。"
        },
        "correct_option": "A"
    }
]    

cloudformation_questions = [
    {
      "question": "1. AWS CloudFormationとは何ですか？",
      "options": {
          "A": "AWSのマネージドサービスで、アプリケーションのデプロイやインフラストラクチャの管理を自動化するためのツール",
          "B": "AWSのコンテナオーケストレーションサービス",
          "C": "AWSのDNS管理サービス",
          "D": "AWSのロードバランシングサービス"
      },
      "correct_option": "A"
    },
    {
        "question": "2. CloudFormationのテンプレートで使用される言語は何ですか？",
        "options": {
            "A": "TEXT",
            "B": "YAML",
            "C": "XML",
            "D": "HTML"
        },
        "correct_option": "B"
    },
    {
        "question": "3. CloudFormationでデプロイできるリソースの例は何ですか？",
        "options": {
            "A": "Amazon S3バケット、Amazon EC2インスタンス、Amazon RDSデータベース",
            "B": "Amazon CloudFront、Amazon API Gateway、AWS Lambda",
            "C": "Amazon Route 53、Amazon SQS、Amazon SNS",
            "D": "すべてのオプションが正しい"
        },
        "correct_option": "D"
    },
    {
        "question": "4. CloudFormationテンプレートで使用される要素にはどのようなものがありますか？",
        "options": {
            "A": "パラメータ、リソース、マッピング、出力",
            "B": "パラメータ、リソース、フィールド、出力",
            "C": "パラメータ、エンドポイント、マッピング、出力",
            "D": "パラメータ、リソース、スキーマ、出力"
        },
        "correct_option": "A"
    },
    {
        "question": "5. CloudFormationスタックとは何ですか？",
        "options": {
            "D": "CloudFormationテンプレートから作成されるAWSリソースのグループ",
            "B": "AWS EC2インスタンスのグループ",
            "C": "AWS Lambda関数のグループ",
            "A": "AWS S3バケットのグループ"
        },
        "correct_option": "D"
    },
    {
        "question": "6. CloudFormationスタックを作成する方法は何ですか？",
        "options": {
            "A": "AWSマネジメントコンソール、AWS CLI、AWS SDKを使用してスタックを作成できます。",
            "B": "AWS Lambdaを使用してスタックを作成できます。",
            "C": "AWS CloudFrontを使用してスタックを作成できます。",
            "D": "AWS SNSを使用してスタックを作成できます。"
        },
        "correct_option": "A"
    },
    {
        "question": "7. CloudFormationスタックを更新する方法にはどのようなものがありますか？",
        "options": {
            "A": "手動で更新する、変更セットを使用して更新する",
            "B": "AWS CLIを使用して更新する、AWS SDKを使用して更新する",
            "C": "AWS S3を使用して更新する、AWS Lambdaを使用して更新する",
            "D": "CloudFormationスタックは更新できない"
        },
        "correct_option": "A"
    },
    {
        "question": "8. CloudFormationの変更セットとは何ですか？",
        "options": {
            "A": "スタックの変更内容を確認し、レビューしてから実際に変更を適用することができる機能",
            "B": "CloudFormationテンプレートのバージョン管理機能",
            "C": "CloudFormationスタックのバックアップ機能",
            "D": "CloudFormationスタックを自動的にデプロイする機能"
        },
        "correct_option": "A"
    },
    {
        "question": "9. CloudFormationテンプレートの条件付き処理にはどのようなものがありますか？",
        "options": {
            "C": "Fn::If、Fn::Switch、Fn::Case",
            "B": "If、Switch、Case",
            "A": "If、Case、When",
            "D": "Fn::If、Fn::Case、Fn::When"
        },
        "correct_option": "C"
    },
    {
        "question": "10. CloudFormationスタックの削除方法にはどのようなものがありますか？",
        "options": {
            "A": "AWSマネジメントコンソール、AWS CLI、AWS SDKを使用して削除できます。",
            "B": "AWS Lambdaを使用して削除できます。",
            "C": "AWS CloudFrontを使用して削除できます。",
            "D": "AWS SNSを使用して削除できます。"
        },
        "correct_option": "A"
    },
    {
        "question": "11. CloudFormationのスタックポリシーについて説明してください。",
        "options": {
            "B": "スタックに対するアクションの許可または拒否を管理するためのポリシー",
            "A": "スタックの作成に必要なリソースを管理するためのポリシー",
            "C": "スタック内のリソースの依存関係を管理するためのポリシー",
            "D": "スタック内のリソースのアクセス権を管理するためのポリシー"
        },
        "correct_option": "B"
    },
    {
        "question": "12. CloudFormationのスタックポリシーのタイプについて説明してください。",
        "options": {
            "B": "変更セットスタックポリシーと更新スタックポリシーの2つがあり、変更セットの処理やスタックの更新時に適用されます。",
            "A": "許可スタックポリシーと拒否スタックポリシーの2つがあり、IAMポリシーのようにAWSリソースへのアクセスを制御します。",
            "C": "変更セットのみスタックポリシーがあり、変更セットの処理時に自動的に適用され、安全性と信頼性を高めます。",
            "D": "監査スタックポリシーとアクションスタックポリシーの2つがあり、CloudFormationスタック内のリソースの監視や自動アクションを設定します。"
        },
        "correct_option": "B"
    },
    {
        "question": "13. CloudFormationで使用されるインプットパラメータについて説明してください。",
        "options": {
            "C": "CloudFormationスタックの作成時に指定されるパラメーター",
            "B": "CloudFormationスタックに属するリソースのパラメーター",
            "A": "CloudFormationスタックに関連するIAMユーザーのパラメーター",
            "D": "CloudFormationスタックに関連するS3バケットのパラメーター"
        },
        "correct_option": "C"
    },
    {
        "question": "14. CloudFormationのテンプレートのバージョン管理に使用される機能は何ですか？",
        "options": {
            "A": "AWS CloudFormation Registry",
            "B": "AWS CloudFormation Console",
            "C": "AWS CloudFormation Designer",
            "D": "AWS CloudFormation Change Sets"
        },
        "correct_option": "A"
    },
    {
        "question": "15. CloudFormationで使用されるFn::ImportValueについて説明してください。",
        "options": {
            "C": "別のスタックでエクスポートされた値をインポートするために使用される関数",
            "B": "スタック内の値をインポートするために使用される関数",
            "A": "スタックのリソースをエクスポートするために使用される関数",
            "D": "スタックのリソースをインポートするために使用される関数"
        },
        "correct_option": "C"
    },
    {
        "question": "16. CloudFormationのスタックに対するアクションの許可または拒否を管理するためのポリシーにはどのようなものがありますか？",
        "options": {
            "A": "Identityポリシー、Resourceポリシー、Permissionポリシー",
            "B": "Identityポリシー、Resourceポリシー、Stackポリシー",
            "C": "Stackポリシー、Resourceポリシー、Actionポリシー",
            "D": "Stackポリシー、Actionポリシー、Permissionポリシー"
        },
        "correct_option": "B"
    },
    {
        "question": "17. CloudFormationのFn::Join関数について説明してください。",
        "options": {
            "A": "文字列を連結するための関数",
            "B": "配列の値を結合するための関数",
            "C": "複数の値を結合するための関数",
            "D": "繰り返し処理を行うための関数"
        },
        "correct_option": "A"
    },
    {
        "question": "18. CloudFormationのFn::Sub関数について説明してください。",
        "options": {
            "D": "文字列の置換を行うための関数",
            "B": "文字列を連結するための関数",
            "C": "配列の値を結合するための関数",
            "A": "複数の値を結合するための関数"
        },
        "correct_option": "D"
    },
    {
        "question": "19. CloudFormationのFn::ImportValue関数を使用する際、エクスポートされたスタックの名前は何ですか？",
        "options": {
            "A": "ExportName",
            "B": "StackName",
            "C": "ResourceName",
            "D": "ImportName"
        },
        "correct_option": "A"
    },
    {
        "question": "20. CloudFormationのAWS::CloudFormation::WaitConditionリソースについて説明してください。",
        "options": {
            "A": "CloudFormationスタックが特定の状態に達するまで待機するためのリソース",
            "B": "CloudFormationスタック内のリソースを監視するためのリソース",
            "C": "CloudFormationスタックのエラーを検出するためのリソース",
            "D": "CloudFormationスタックの実行を制御するためのリソース"
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
    return int(correct_count * (100/len(questions)))


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
    print("1. Docker")
    print("2. AWS Cloudformation")
    test_type = input("テストタイプを入力（1 または 2）：")

    # 選択に応じて問題リストをロード
    if test_type == "1":
        questions = rds_questions
        test_type_name = "Docker"
    elif test_type == "2":
        questions = cloudformation_questions
        test_type_name = "AWS Cloudformation"
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
