# プロジェクト名
Parlantを使用したチャットボット

## 使用技術
- Python 3.10
- Parlant
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
    git clone https://github.com/xxxxxx/nflabs-parlant.git
    cd nflabs-parlant
    ```

2. **環境変数の設定**
    - `.env_template`をコピーして`.env`を作成し、APIキーなど必要な値を設定

3. **Docker環境の起動**
    ```bash
    docker compose up --build
    ```

4. **サービスアクセス**
    - `http://localhost:8000` など（実際のポートはdocker-compose.ymlで確認）

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
- データディレクトリ`data/`は.gitignore推奨です