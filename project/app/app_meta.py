from django.conf.urls import url
from objectpack import desktop
from .controller import controller
from .actions import *


def register_urlpatterns():
    """
	Регистрация конфигурации урлов для приложения
	"""
    return [url(*controller.urlpattern)]


def register_actions():
    """
	Регистрация экшен-паков
	"""
    return controller.packs.extend([
        UserPack(),
        GroupPack(),
        ContentTypePack(),
        PermissionPack()
    ])


def register_desktop_menu():
    """
	регистрация элементов рабочего стола
	"""
    desktop.uificate_the_controller(
        controller,
        menu_root=desktop.MainMenu.SubMenu('Demo')
    )
