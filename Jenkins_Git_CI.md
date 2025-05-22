Jenkins＿Git＿CI

开放EC2 8080端口 22端口

# Amazon Linux 2023 上安装 Jenkins（推荐使用 Java 17）
## 安装JAVA环境
sudo dnf install java-17-amazon-corretto -y
java -version
## 安装Jenkins
curl -LO https://get.jenkins.io/redhat-stable/jenkins-2.504.1-1.1.noarch.rpm
sudo rpm -ivh jenkins-2.504.1-1.1.noarch.rpm
sudo systemctl start jenkins
sudo systemctl enable jenkins
## 首次访问Jenkins时的默认密码
http://<你的EC2公网IP>:8080

sudo cat /var/lib/jenkins/secrets/initialAdminPassword

# Git关联
## 设定Github目标存储桶的Webhook
setting　→ Webhook　→　Payload URL「http://XXX.XXX.XXX.XXX(公有IP):8080/github-webhook/」
## 创建Github token
setting → Developer settings → personal access token 

# 用Jenkins做成新的Job
①「Git」にチェックをつける。
リポジトリURLは、下記のような形式で記載する。
「XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX」の部分は、Githubのトークンを記載する。{YourName}は、Githubでの名前を記載する。
https://XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX@github.com/{YourName}/リポジトリ名/
配置 Git 分支（例如 */main）
②「GitHub hook trigger for GITScm polling」にチェックをつける。
③「Build Steps 」の項目があるはずです。「シェルの実行」を選択して、スクリプトを記載する

# Jenkins 主节点处于“离线”状态 
没有可用的执行器（executor）来实际执行构建任务。

方法 1：重启 Jenkins Built-In Node
打开 Jenkins 左侧菜单：点击 “Manage Jenkins（Jenkinsの管理）”。
进入 “Manage Nodes and Clouds（ノードとクラウドの管理）”。
找到“Built-In Node”或“master”节点，点击进去。
如果它显示为“离线（offline）”，点击 “Mark this node online” 或 “Bring online”。

方法 2：确认是否有足够资源运行 executor
即使 Jenkins 是在线的，执行器可能都被占用或设置为 0：
　
Manage Jenkins → Manage Nodes and Clouds → Built-In Node
确保 # of executors 设置大于等于 1（建议至少设置为 2）
如果是 0，则构建永远不会执行。

# 磁盘不够了怎么办
原因：Jenkins 使用的是 /tmp 挂载在 tmpfs（内存） 上

解决策：
①运行下面的命令来找到 Jenkins 的服务定义位置
systemctl status jenkins

sudo vim /usr/lib/systemd/system/jenkins.service
　<< ExecStart
- - - - - - - - 
　>> ExecStart=/usr/bin/java -Djava.io.tmpdir=/var/tmp -Djava.awt.headless=true -jar /usr/share/java/jenkins.war --webroot=/var/cache/jenkins/war --httpPort=8080

②保存并重新加载 systemd 服务
sudo systemctl daemon-reload
sudo systemctl restart jenkins

③确认 Jenkins 启动成功并使用了新的临时目录
ps aux | grep jenkins


# 在 Jenkins 服务器上生成 SSH 密钥对
sudo su - jenkins   # 切换到 Jenkins 用户
ssh-keygen -t rsa -b 4096 -C "zhangke970424@gmail.com"
# 推荐保存到：~/.ssh/id_rsa
默认 回车两次

~/.ssh/id_rsa	私钥（不要泄露）
~/.ssh/id_rsa.pub	公钥（要拷贝给 GitHub）

# 将公钥添加到 GitHub（两种方式）
①仓库级别
打开 GitHub 仓库 → Settings → Deploy keys
点右上角 Add deploy key
Title 填个名字，比如 Jenkins Key
粘贴 id_rsa.pub 内容
勾选 Allow write access（如果需要 push）

②个人账号级别（用于多个仓库）
GitHub → Settings → SSH and GPG keys
New SSH key → 粘贴 id_rsa.pub 内容即可

③将私钥添加到 Jenkins 中
Jenkins 左侧菜单 → Manage Jenkins → Credentials（或 Global credentials）
进入 (global) 域或你选择的域
点击 Add Credentials
类型选择：SSH Username with private key

设置如下：
项目	内容
Username	git（必须写 git）
Private Key	粘贴 ~/.ssh/id_rsa 内容（或选从文件）

打开项目，将Repository URL 改为 SSH 格式：
git@github.com:yourusername/your-repo.git

# 补充小技巧（验证）!!!!!!我觉得很重要
sudo su - jenkins
ssh -T git@github.com

# 总结的URL：
https://chatgpt.com/canvas/shared/682f1fa6be308191a963197c745efb54