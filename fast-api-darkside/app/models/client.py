from tortoise import fields
from tortoise.models import Model


class Client(Model):
    id = fields.BigIntField(pk=True)
    name = fields.CharField(max_length=255)
    created_at = fields.DatetimeField(auto_now_add=True)
    deleted_at = fields.DatetimeField(null=True)

    class Meta:
        table = "clients"

    def __str__(self):
        return self.name


# __str__メソッドを定義しない場合
# オブジェクトのクラス名と一緒に一意の識別子（メモリ上のアドレス）が表示される
# ことが一般的。例えば、<Client object at 0x10e75e2e8>のような形式になる
# Clientインスタンスを出力した際にクライアントの名前が表示されなくなるよ
