# macOS-cpu-alart

## .appファイルの作成
python setup.py py2app
-> cpu_monitor.app

## macOS起動時に自動的にCPUモニタリングを開始するための設定
1. Finderでcpu_monitor.appを右クリックして「開く」を選択し、動作確認をします。
2. システム設定 > ユーザとグループ > ログイン項目に移動します。
3. 「+」ボタンをクリックして、cpu_monitor.appを選択します。
