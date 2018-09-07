from django.test import TestCase
from django.urls import reverse
from .models import Album, Artist, Contact, Booking

#Index page, doit renvoyer code 200
class IndexPageTestCase(TestCase):
    def test_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

#Detail page
class DetailPageTestCase(TestCase):
    def setUp(self):
        self.impossible = Album.objects.create(title="Transmission Impossible", reference=1)
        self.album_id = Album.objects.get(title='Transmission Impossible').id

    # test that detail page returns a 200 if the item exists.
    def test_detail_page_returns_200(self):
        response = self.client.get(reverse('store:detail', args=(self.album_id,)))
        self.assertEqual(response.status_code, 200)

    # test that detail page returns a 404 if the item not exists.
    def test_detail_page_returns_200(self):
        self.album_id+=1
        response = self.client.get(reverse('store:detail', args=(self.album_id,)))
        self.assertEqual(response.status_code, 404)

# Booking Page
class BookingPageTestCase(TestCase):
    def setUp(self):
        self.impossible = Album.objects.create(title="Transmission Impossible", reference=1)
        self.album_id = Album.objects.get(title='Transmission Impossible').id
        self.contact = Contact.objects.create(name="MOI", email='moi@moi.com')

    # test that a new booking is made
    def test_new_booking_is_registered(self):
        old_bookings = Booking.objects.count()  # count bookings before a request
        album_id = self.album_id
        name = self.contact.name
        email =  self.contact.email
        response = self.client.post(reverse('store:detail', args=(album_id,)), {
            'name': name,
            'email': email
        })
        new_bookings = Booking.objects.count()  # count bookings before a request
        self.assertEqual(old_bookings+1, new_bookings)

    # test that a booking belongs to a contact
    def test_new_booking_belongs_to_a_contact(self):
        album_id = self.album.id
        name = self.contact.name
        email = self.contact.email
        response = self.client.post(reverse('store:detail', args=(album_id,)), {
            'name': name,
            'email': email
        })
        booking = Booking.objects.first()
        self.assertEqual(self.contact, booking.contact)

    # test that a booking belong to an album
    def test_new_booking_belongs_to_an_album(self):
        album_id = self.album.id
        name = self.contact.name
        email = self.contact.email
        response = self.client.post(reverse('store:detail', args=(album_id,)), {
            'name': name,
            'email': email
        })
        booking = Booking.objects.first()
        self.assertEqual(self.album, booking.album)

    # test that an album is not available after a booking is made
    def test_album_not_available_if_booked(self):
        album_id = self.album.id
        name = self.contact.name
        email = self.contact.email
        response = self.client.post(reverse('store:detail', args=(album_id,)), {
            'name': name,
            'email': email
        })
        # Make the query again, otherwise `available` will still be set at `True`
        self.album.refresh_from_db()

        self.assertFalse(self.album.available)