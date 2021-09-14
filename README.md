# create_image_file
テキストファイルの内容を画像にするツール

## 使い方
1. 本ツールと同階層にfile.txtを配置する。これがテキストファイルになる
2. py create_image_file.py  
⇒これで、image.pngが作成され、クリップボードにimage.pngのデータが格納される。

## 作成までの経緯
DB管理GUIだとエクセルにDBデータコピーしたときに、データが見切れるのが気に入らなかった。  
なので、DBデータをtabulateで良い感じにテキスト化したものの、テキストファイルのデータをそのままエクセルに貼り付けたらレイアウトが崩れるという問題があった。  
なら画像にしてしまえばレイアウトは崩れない・・・という発想から生まれたツール。

## Special Thanks
以下のサイトの記述を参考にしました。ありがとうございました。  
https://qiita.com/implicit_none/items/a9bf7eebe125c9d773eb  
https://water2litter.net/rum/post/python_win32clipboard_set/
