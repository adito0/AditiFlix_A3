from AditiFlix_App.domainmodel.actor import Actor

import pytest


@pytest.fixture
def actor():
    return Actor('Brad Pitt')


def test_init(actor):
    assert actor.actor_full_name == 'Brad Pitt'
    actor1 = Actor("Brad Pitt")
    assert repr(actor1) == "<Actor Brad Pitt>"
    actor2 = Actor("")
    assert actor2.actor_full_name is None
    actor3 = Actor(42)
    assert actor3.actor_full_name is None
    assert repr(actor2) == "<Actor None>"
    assert repr(actor3) == "<Actor None>"


def test_compare():
    actor1 = Actor("Brad Pitt")
    actor2 = Actor("Brad Pitt")
    assert actor1 == actor2
    actor2 = 4
    assert actor1 != actor2
    actor1 = Actor("")
    actor2 = Actor(45)
    assert actor1 == actor2


def test_lt():
    actor1 = Actor("Brad Pitt")
    actor2 = Actor("brad Pitt")
    assert actor1 < actor2


def test_hash():
    actor1 = Actor("Brad Pitt")
    actor2 = Actor("Brad Pitt")
    assert hash(actor1) == hash(actor2)
    actor2 = Actor("Taika Waititj")
    assert hash(actor1) != hash(actor2)
    dict1 = dict()
    dict1[actor1] = actor2
    assert dict1[actor1] == actor2
    assert repr(dict1[actor1]) == "<Actor Taika Waititj>"
    actor1 = Actor("")
    actor2 = Actor(9)
    dict1[actor1] = actor2
    assert dict1[actor1] == actor2
    assert repr(dict1[actor1]) == "<Actor None>"


def test_add_colleague(actor):
    result = actor.add_actor_colleague("")
    assert result == -1
    assert actor.actor_colleague_list == []
    actor1 = Actor("Joe Jonas")
    result = actor.add_actor_colleague(actor1)
    assert result == 1
    assert actor.actor_colleague_list == [actor1]
    actor2 = 'Henry Bagel'
    result = actor.add_actor_colleague(actor2)
    assert result == -1
    assert actor.actor_colleague_list == [actor1]
    actor3 = Actor("Jane Doe")
    result = actor.add_actor_colleague(actor3)
    assert result == 1
    assert actor.actor_colleague_list == [actor1, actor3]
    result = actor.add_actor_colleague(actor1)
    list1 = [actor1]
    assert result == 0
    assert actor.actor_colleague_list == [actor1, actor3]
    actor4 = Actor("")
    actor5 = Actor(45)
    result = actor.add_actor_colleague(actor4)
    assert result == 0
    result = actor.add_actor_colleague(actor5)
    assert result == 0
    assert len(actor.actor_colleague_list) == 2
    assert actor.actor_colleague_list == [actor1, actor3]


def test_check_colleague(actor):
    assert not actor.check_if_this_actor_worked_with(actor)
    actor1 = 'Henry Bagel'
    actor2 = Actor('Joe Jonas')
    actor3 = Actor('Amy Harris')
    actor4 = Actor("")
    actor5 = Actor(56)
    result = actor.add_actor_colleague(actor1)
    assert result == -1
    result = actor.add_actor_colleague(actor2)
    assert result == 1
    result = actor.add_actor_colleague(actor3)
    assert result == 1
    result = actor.add_actor_colleague(actor4)
    assert result == 0
    result = actor.add_actor_colleague(actor5)
    assert result == 0
    assert not actor.check_if_this_actor_worked_with(actor1)
    assert actor.check_if_this_actor_worked_with(actor2)
    assert actor.check_if_this_actor_worked_with(actor3)
    assert not actor.check_if_this_actor_worked_with(actor4)
    assert not actor.check_if_this_actor_worked_with(actor5)

def test_set_colleagues():
    actor2 = Actor('Joe Jonas')
    actor3 = Actor('Amy Harris')
    # TODO

def test_get_next_colleague():
    actor2 = Actor('Joe Jonas')
    actor3 = Actor('Amy Harris')
    # TODO
