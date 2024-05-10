# OLED_V5
# ラズパイ5 BookWorm対応 液晶、LED、SWの付いた電子工作お助けツール

<h4><<概要>></h4>
  最新ラズパイ5、最新OS:BookWorm対応。<br>
　ＯＬＥＤ表示器とスイッチ２個、ＬＥＤ２個を実装したテスト用のラズパイ専用基板です。<br>
　ブレッドボードで何か作ろうとしたときに、最低限のＵＩが必要ですが、それらをブレッドボード上に作るのは面倒です。<br>
　最低限のＵＩを備えたこの基板があれば、作るべき物だけに集中できるので、作業がはかどります。<br>
<br>
 ・サンプルプログラム一覧<br>
　　　test_LED.py　(Lチカを行います)<br>
　　　test_sw.py　(SWの押下を確認します)<br>
　　　test_Servo.py　(サーボを動作させます)<br>
　　　breathing_LEDx.py　(LEDを蛍のようにゆっくり点滅させます)<br>
　　　AHTx0_demo.py　(温度・湿度センサーのデータをOLEDに表示します)<br>
　　　OLED_01〜5.py　(OLEDに文字、点、四角、線、画像を表示します)<br>
　　　lib_oled.py　(OLEDに文字、点、四角、線、画像を表示する関数群です)<br>
　　　OLED_demo.py　(lib_oled.pyを使ってデモを行います)<br>
　すべてのソースプログラムを開示いたします。<br>
<br>
・LEDの色等指定はできません。<br>
・部品の仕様が変わる場合があります。 <br>
・基板のバージョンが変わる場合がありますが、機能等に違いはありません。<br>
・ラズパイは付属しません。<br>
・サーボモーターは付属しません。<br>
<br>
*OLED_V5の位置付け<br>
Bullseye版までは、
git clone https://github.com/momorara/OLED<br>
にてNode-REDで動作しますが、<br>
ラズパイ5(Bookworm)完全対応のNode-REDがまだリリースしてい無いと思いますので、<br>
python3ベースのプログラムでラズパイ5対応としています。<br>
ただし、Bullseye、Busterでも動作します。<br>

<h4><<使用方法>></h4>
git clone https://github.com/momorara/OLED_V5<br>
でラズパイにダウンロードしてください。<br>
インストールについては、インストール文書に従いインストールを行ってください。<br>

<h4><<動作環境>></h4>
2024/3/5 対応OS：Bullseye版11.9<br>
2024/3/7 対応OS：Buster版10.13での動作を確認しています。<br>
2024/4/16 対応OS:BookWorm版12.5での動作確認<br>
   
<h4><<使用説明資料>></h4>
説明書類の中の資料を確認ください。
お問い合わせに関しては、サポート.txtを参照ください。

<h4><<アップデート>></h4>
2024/4/5 お詫び　新しく作った基板にパターン間違いがありサーボのGPIOピンが27になっています。そのため、基板の型番がOLED_V5-1となっているものは、サーボのテストをする際に test_Servo_27.pyを使用してください。<br>
2024/4/13 お詫び AHT30を使用するとシステムフリーズする(現時点ではPi5 bookwormでのみ確認)<br>
2024/4/16 bookwormでのインストール方法を別にしました。<br>
