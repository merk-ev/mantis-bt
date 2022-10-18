# test
# -*- coding: utf-8 -*-
import pytest
from training.fixture.application_group import ApplicationGroup
from training.model.group import Group


@pytest.fixture
def app(request):
    fixture = ApplicationGroup()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.session.login()
    app.create_group(Group(name="Test 2", header="header 2", footer="footer 2"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login()
    app.create_group(Group(name="", header="", footer=""))
    app.session.logout()
