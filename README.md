# **python_game1**
下記の書物を参考に、pythonの勉強中である。  
　Pythonでつくるゲーム開発入門講座  
　廣瀬　豪[著]  

1.[動作条件](#動作条件)  
2.[各Chapterの説明](#各chapterの説明)  
3.[この著書を選んだ理由](#この著書を選んだ理由)  

### *動作条件*
---
* OS:windows macどちらでも可  
* 言語：python3.x系がインストール済み  
* 各ファイルを読み込み、「Run Module」をクリック  


### *各chapterの説明*
---
#### Chapter1〜5
 CUIで、if文・for文などの処理の練習
<br>

#### Chapter6以降
 GUIを使用したgame
 * Chapter6<br>
   おみくじソフト<br>
  <説明>
   * 本日の運勢を占えるゲーム  
  <コードの特徴>
   * random.choiceで、運勢をランダムに選択<br>
   * label.updateで、label表示の切り替え<br>
 * Chapter7<br>
   診断ゲーム<br>
  <説明>
   * 当てはまる物にチェックを入れて、診断するゲーム<br>
  <コードの特徴>
   * BooleanVarのオブジェクト用リストの実装<br>
   * for文を用いて、チェック数をカウント<br>
   * text.insertで、文字列の挿入<br>
 * Chapter7<br>
   迷路を塗るゲーム<br>
   <説明>
   * 床を全て塗るゲーム
   * 左のshiftキーを押すとリセットされる。<br>
  <コードの特徴>
   * 二重for文で迷路を作成<br>
   * キャラクター移動時に、canvas.deleteで一旦キャラを消し、canvas.create_imageで再度表示<br>
   * 壁、塗る前の床、塗った床の3パターンの判定<br>
 * Chapter8〜13<br>
   現在作成中<br>

### *この著書を選んだ理由*
---
* Chapterごとに段階を踏んで、スキルアップできるように構成されている  
* 解説が、わかりやすかった  
* 別冊で上級編があり、より深く学べると感じた  

### *製作者*
---
onikunai  
Github: https://github.com/onikunai  