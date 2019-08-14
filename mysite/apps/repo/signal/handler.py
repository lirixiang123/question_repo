"""
@file: hander.py
"""
from django.core.signals import request_finished
from django.db.models.signals import post_save
from django.dispatch import receiver
from . import signals
from ..models import Answers, UserLog, QuestionsCollection, AnswersCollection

#当请求完成之后，打印一个日志
@receiver(request_finished)
def all_log(sender,**kwargs):
    print(sender,kwargs)
    print("使用信号记日志")

#当创建一条日志记录maillog，会自动执行发送邮件

@receiver(signals.mysignal)
def user_log(sender, arg1=None, arg2=None, **kwargs):
    print(sender, arg1, arg2)
    print('some log')
@receiver(post_save, sender=Answers)
# post_save => 对象保存后
# sender => 指定发送信号的模型
# def answer_log(sender, instance, created, raw, using, update_fields, **kwargs):
def answer_log(sender, instance, created, **kwargs):
    # instance => answer object
    UserLog.objects.create(user=instance.user, operate=3, question=instance.question)
    # UserLog.objects.create(user=request.user, question=self.get_object(), operate=3)
# 收藏题目日志
@receiver(post_save, sender = QuestionsCollection)
def question_collection_log(sender, instance, created, **kwargs):
    if instance.status:
        operate = 1
    else:
        operate = 2
    UserLog.objects.create(user=instance.user, operate=3, question=instance.question)


# 收藏答案日志(1：收藏、2：取消收藏)
@receiver(post_save, sender = AnswersCollection)
def answer_collection_log(sender, instance, created, **kwargs):
    if instance.status:
        operate = 1
    else:
        operate = 2
    UserLog.objects.create(user=instance.user, operate=operate, answer=instance.answer)
