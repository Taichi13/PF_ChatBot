# プロジェクト名
Parlantを使用したチャットボット

**※ Azure OpenAI APIキーの部分に変更を加えたため、私のParlantリポジトリ（private）にアクセスする権限があなたになければ、このプロジェクト使用することはできません。**

## 使用技術
- Python 3.10.17
- Parlant 2.1.0
- Docker / Docker Compose
- Azure OpenAI API
- poetry

## プロジェクトの概要
ParlantをベースにしたカスタムAIチャットシステムの研究開発プロジェクトです。
- Parlant公式サイト: https://www.parlant.io/
- Parlant GitHub: https://github.com/emcie-co/parlant


## 必要要件 (Requirements)

- Python 3.10+
- Docker / Docker Compose
- Poetry

## セットアップ (Setup)

1. **リポジトリのクローン**
    ```bash
    git clone https://github.com/Taichi13/PF_ChatBot.git
    cd PF_ChatBot
    ```

2. **環境変数の設定**
    - `.env_template`をコピーして`.env`を作成し、APIキーなど必要な値を設定
        - AZURE_API_KEY: APIキー指定する
        - AZURE_ENDPOINT: エンドポイント指定する
        - AZURE_CHAT_API_VERSION: dev環境のAPIバージョン指定する
        - AZURE_CHAT_DEPLOYMENT_NAME: dev環境のmodel名を指定する
        - AZURE_EMBEDDING_API_VERSION: embedding環境のAPIバージョンを指定する
        - AZURE_EMBEDDING_DEPLOYMENT_NAME: embedding環境のmodelを指定する


3. **Docker環境の起動**
- ghp_xxxxxxxxxxxxxxxxxに各自のPAT（Personal Access Token）を入れる（Token発行ページ https://github.com/settings/tokens）
    - 「repo」スコープ（権限）があればOK（最低でも「repo:read」
    - PATは絶対に漏らさないように
    ```bash
    docker compose build --build-arg GITHUB_TOKEN=ghp_xxxxxxxxxxxxxxxxx
    ```

4. **サービスアクセス**
    - `http://localhost:8800`

## 使い方 (Usage)
1. generate_yaml.pyでベースのyamlファイルを作成
2. yamlファイルを書き換える
3. create_agent.pyでAgent・Guideline・Glossaryを作成

- Agent定義やチャット履歴など、詳細な操作方法は公式ドキュメント参照（https://www.parlant.io/docs/quickstart/introduction/）
- Parlant yamlでAgentを管理する例:
    - descriptionについて、「'」と「'''」どちらで囲んでも反映されます。     
  <img width="872" alt="image" src="https://github.com/user-attachments/assets/a5fd8c19-7a9f-4ec7-bcb4-7f581f7243eb" />
- Parlant CLI例:（CLIで反映した変更をyamlファイルに適用する際に、export_yaml.pyを使って反映できるが、手動で変更するため、使用しない方が良い。）
    ```bash
    parlant agent list
    parlant session create --agent <AGENT_ID>
    ```

## 開発・カスタマイズ (Development & Customization)

- Parlant/本プロジェクトのコードやAgentのカスタマイズは`src/`ディレクトリ配下で行ってください
- Poetryでパッケージ管理
    ```bash
    poetry install
    ```

## ライセンス (License)

このプロジェクトは[Apache License 2.0]のもと公開しています。

> ※保証や責任は一切負いません。詳細はライセンスファイル参照。

## その他・注意点 (Notes)

- 商標利用は含まれません
- 個人利用/教育利用/商用利用いずれも可能（ただし自己責任で運用してください）
