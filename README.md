# vrc_log_viewer
## これは何
- VRCのログを見たいときに使うやつ

## 依存パッケージ
- pyyaml
```
$ pip install pyyaml
```

## 実行方法
### pythonで実行
- vrc_log_viewer.pyと同じ階層に設定ファイル`config.yml`を配置して以下のコマンドを実行
```
$ python vrc_log_viewer.py
```
### 実行ファイル生成
```
$ pyinstaller.exe vrc_log_viewer.py [-F -w]
  オプションはお好みで
  -F : ファイルを1つにまとめる
  -w : 実行時にウィンドウを表示しない(タスクマネージャーからkill)
```
dist以下に実行ファイルが生成されるのでexeファイルと同じ階層に設定ファイル`config.yml`を配置してexeファイルを実行

## 設定ファイル
- 例


```yaml:config.yml
# 見るログファイルの名前(指定無しの場合作成日時が一番新しいファイルを開く)
logfile: ""
# trueの場合起動する前に書き込まれたログも出力
past: true
# 出力するログを正規表現で表記(グループ化してある部分を出力)
# 2019.08.28 23:06:46 Log        -  [NetworkManager] OnPlayerJoined 27Cobalter が
# 2019.08.28 23:06:46 OnPlayerJoined 27Cobalter のように出力される
reg:
  - '([0-9]{4}\.[0-9]{2}\.[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}).*?\[NetworkManager\] (OnPlayerJoined .*)'
  - '([0-9]{4}\.[0-9]{2}\.[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}).*?\[NetworkManager\] (OnPlayerLeft .*)'
  - '([0-9]{4}\.[0-9]{2}\.[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}).*?\[RoomManager\] (Joining wrld.*)'
```
