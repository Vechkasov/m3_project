from m3 import OperationResult
from objectpack.actions import ObjectPack
from objectpack.ui import ModelEditWindow

from .models import User, Group, ContentType, Permission
from .ui import UserEditWindow, PermissionEditWindow


class UserPack(ObjectPack):
    model = User
    add_window = edit_window = UserEditWindow

    add_to_desktop = True
    can_delete = True

    columns = [
        {
            'data_index': 'name',
            'header': u'Имя',
            'width': 2,
        },
        {
            'data_index': 'surname',
            'header': u'Фамилия',
            'width': 2,
        },
        {
            'data_index': 'group_id',
            'header': u'Группа',
            'width': 1,
        },
        {
            'data_index': 'gender',
            'header': u'Пол',
            'width': 1,
            'filter': {
                'type': 'list',
                'options': User.GENDERS
            }
        }
    ]

    def pre_run(self, request, context):
        groups = list(Group.objects.all())
        print(groups)
        if len(groups) == 0:
            return OperationResult(success=False, message=u'Для начала добавьте группу')


class GroupPack(ObjectPack):
    model = Group
    add_window = edit_window = ModelEditWindow.fabricate(model)

    add_to_desktop = True
    can_delete = True

    columns = [
        {
            'data_index': 'name',
            'header': u'Название группы',
            'width': 2,
        }
    ]


class PermissionPack(ObjectPack):
    model = Permission
    add_window = edit_window = PermissionEditWindow

    add_to_desktop = True
    can_delete = True

    columns = [
        {
            'data_index': 'name',
            'header': u'Название',
            'width': 2,
        },
        {
            'data_index': 'codename',
            'header': u'Кодовое имя',
            'width': 1,
        },
        {
            'data_index': 'content_type.name',
            'header': u'Событие',
            'width': 1,
        }
    ]

    def pre_run(self, request, context):
        content_types = list(ContentType.objects.all())
        print(content_types)
        if len(content_types) == 0:
            return OperationResult(success=False, message=u'Для начала добавьте событие')


class ContentTypePack(ObjectPack):
    model = ContentType
    add_window = edit_window = ModelEditWindow.fabricate(model)

    add_to_desktop = True
    can_delete = True

    columns = [
        {
            'data_index': 'name',
            'header': u'Название события',
            'width': 2,
        }
    ]
