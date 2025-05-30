# プロジェクト名
Parlantを使用したチャットボット

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

- Parlant CLI例:
    ```bash
    parlant agent list
    parlant session create --agent <AGENT_ID>
    ```
- エージェント定義やチャット履歴など、詳細な操作方法は[Wiki](./docs/)または公式ドキュメント参照

## 開発・カスタマイズ (Development & Customization)

- Parlant/本プロジェクトのコードやエージェントのカスタマイズは`src/`ディレクトリ配下で行ってください
- Poetryでパッケージ管理
    ```bash
    poetry install
    ```

## ライセンス (License)

このプロジェクトは[Apache License 2.0](./LICENSE)のもと公開しています。

> ※保証や責任は一切負いません。詳細はライセンスファイル参照。

## その他・注意点 (Notes)

- 商標利用は含まれません
- 個人利用/教育利用/商用利用いずれも可能（ただし自己責任で運用してください）