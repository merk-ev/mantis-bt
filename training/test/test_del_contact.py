# test delete first contact in list
from model.contact import Contact
import random


def test_delete_some_contact(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname='TEST', middlename='Test middle', lastname='Test Last',
                                nickname='TTTT', title='TITlE', company='Company Name', address='RF', home='44-55',
                                mobile='+7-888', work='41-87', fax='47-88', email='e@m.ail', email2='--', email3='---',
                                homepage='home.page', bday='22', bmonth='May', byear='1984', aday='15',
                                amonth='March', ayear='2020', new_group='Test2', address2='street', phone2='non',
                                notes='designer from streets'))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)

