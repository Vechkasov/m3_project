from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'Название группы', db_index=True)

    def __unicode__(self):
        return u"%s" % self.name

    class Meta:
        verbose_name = u'Группа'
        verbose_name_plural = u'Группы'


class User(models.Model):
    GENDERS = (
        (1, u'Мужской'),
        (2, u'Женский'),
    )

    name = models.CharField(max_length=30, verbose_name=u'Имя')
    surname = models.CharField(max_length=30, verbose_name=u'Фамилия')
    gender = models.PositiveSmallIntegerField(
        choices=GENDERS,
        default=GENDERS[0][0],
        verbose_name=u'Пол')
    group = models.ForeignKey(to=Group, on_delete=models.CASCADE)

    def __unicode__(self):
        return u"%s %s" % (self.surname, self.name)

    class Meta:
        verbose_name = u'Пользователь'
        verbose_name_plural = u'Пользователи'


class ContentType(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'Название события', db_index=True)

    def __unicode__(self):
        return u"%s" % self.name

    class Meta:
        verbose_name = u'Событие'
        verbose_name_plural = u'События'


class Permission(models.Model):
    name = models.CharField(max_length=150, verbose_name=u'Название')
    codename = models.CharField(max_length=50, verbose_name=u'Кодовое имя')
    content_type = models.ForeignKey(to=ContentType, on_delete=models.CASCADE)

    def __unicode__(self):
        return u"%s " % self.name

    class Meta:
        verbose_name = u'Разрешение'
        verbose_name_plural = u'Разрешения'


