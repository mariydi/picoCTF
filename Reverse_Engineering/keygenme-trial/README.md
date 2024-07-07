フラグそのものがキーになっている

３分割されていて、`key_part_dynamic1_trial`の部分がマスクされている。

色々見ていると、`check_key`という関数が見つかる。
それを見ると、以下のことがわかる。

1. if len(key) != len(key_full_template_trial):
   1. 入力したkeyが22行目の`key_full_template_trial`と長さが同じか
2. `for c in key_part_static1_trial`
   1. 最初が`key_part_static1_trial`で始まるかを確認する。
3. `if key[i] != hashlib.sha256(username_trial).hexdigest()[4]`
   1. keyのマスクされていた部分の1文字目が、`username_trial`をSHA256でハッシュ化したあとに16進数に置き換えた文字列のうちの`4`つめ（戦闘から数えると`5`つ目）の値と同一かを確認する。
   2. これを8回繰り返す。参照する場所は変える。

なので、ユーザネームとして指定されているもののusername_trialをSHA256でハッシュ化したあとに16進数にしたものを作成して
その後でその順番通りに並べてあげればフラグのマスキングされている部分がでてくることがわかる。

なのでそれになるようにプログラムを組んで実行する。

ちょっと詰まったのが悔しいので頑張る。
