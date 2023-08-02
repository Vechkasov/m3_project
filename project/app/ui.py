from m3_ext.ui import all_components as ext
from objectpack.ui import BaseEditWindow, make_combo_box

from .models import *


class UserEditWindow(BaseEditWindow):
    def _init_components(self):
        super(UserEditWindow, self)._init_components()

        groups = list(Group.objects.all())
        groups_tuple = tuple((item.id, item.name) for item in groups)

        self.field__name = ext.ExtStringField(
            label=u'Имя',
            name='name',
            allow_blank=False,
            anchor='100%')

        self.field__surname = ext.ExtStringField(
            label=u'Фамилия',
            name='surname',
            allow_blank=False,
            anchor='100%')

        self.field__gender = make_combo_box(
            label=u'Пол',
            name='gender',
            allow_blank=False,
            anchor='100%',
            data=User.GENDERS)

        self.field__group = make_combo_box(
            label=u'Группа',
            name='group_id',
            allow_blank=False,
            anchor='100%',
            data=groups_tuple)

    def _do_layout(self):
        super(UserEditWindow, self)._do_layout()
        self.form.items.extend((
            self.field__name,
            self.field__surname,
            self.field__gender,
            self.field__group
        ))

    def set_params(self, params):
        super(UserEditWindow, self).set_params(params)
        self.height = 'auto'


class PermissionEditWindow(BaseEditWindow):
    def _init_components(self):
        super(PermissionEditWindow, self)._init_components()

        content_types = list(ContentType.objects.all())
        content_types_tuple = tuple((item.id, item.name) for item in content_types)

        self.field__name = ext.ExtStringField(
            label=u'Название',
            name='name',
            allow_blank=False,
            anchor='100%')

        self.field__content_type = make_combo_box(
            label=u'Событие',
            name='content_type_id',
            allow_blank=False,
            anchor='100%',
            data=content_types_tuple)

        self.field__codename = ext.ExtStringField(
            label=u'Кодовое имя',
            name='codename',
            allow_blank=False,
            anchor='100%')

    def _do_layout(self):
        super(PermissionEditWindow, self)._do_layout()
        self.form.items.extend((
            self.field__name,
            self.field__content_type,
            self.field__codename
        ))

    def set_params(self, params):
        super(PermissionEditWindow, self).set_params(params)
        self.height = 'auto'
