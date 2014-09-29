"""Tests for the distance matrix module."""

import unittest
import googlemaps
import responses

class DistanceMatrixTest(unittest.TestCase):

    def setUp(self):
        self.key = 'AIzaasdf'
        self.ctx = googlemaps.Context(self.key)

    @responses.activate
    def test_basic_params(self):
        responses.add(responses.GET, 
                      'https://maps.googleapis.com/maps/api/distancematrix/json',
                      body='{"status":"OK","rows":[]}',
                      status=200,
                      content_type='application/json')

        origins = ["Perth, Australia", "Sydney, Australia",
                   "Melbourne, Australia", "Adelaide, Australia",
                   "Brisbane, Australia", "Darwin, Australia",
                   "Hobart, Australia", "Canberra, Australia"]
        destinations = ["Uluru, Australia",
                        "Kakadu, Australia",
                        "Blue Mountains, Australia",
                        "Bungle Bungles, Australia",
                        "The Pinnacles, Australia"]

        matrix = googlemaps.distance_matrix(self.ctx, origins, destinations)

        self.assertEquals(1, len(responses.calls))
        self.assertEquals('https://maps.googleapis.com/maps/api/distancematrix/json?'
                          'key=%s&origins=Perth%%2C+Australia%%7CSydney%%2C+'
                          'Australia%%7CMelbourne%%2C+Australia%%7CAdelaide%%2C+'
                          'Australia%%7CBrisbane%%2C+Australia%%7CDarwin%%2C+'
                          'Australia%%7CHobart%%2C+Australia%%7CCanberra%%2C+Australia&'
                          'destinations=Uluru%%2C+Australia%%7CKakadu%%2C+Australia%%7C'
                          'Blue+Mountains%%2C+Australia%%7CBungle+Bungles%%2C+Australia'
                          '%%7CThe+Pinnacles%%2C+Australia' % self.key,
                          responses.calls[0].request.url)

    @responses.activate
    def test_mixed_params(self):
        responses.add(responses.GET, 
                      'https://maps.googleapis.com/maps/api/distancematrix/json',
                      body='{"status":"OK","rows":[]}',
                      status=200,
                      content_type='application/json')
        
        origins = ["Bobcaygeon ON", [41.43206, -81.38992]]
        destinations = [(43.012486, -83.6964149),
                        {"lat": 42.8863855, "lng": -78.8781627}]

        matrix = googlemaps.distance_matrix(self.ctx, origins, destinations)

        self.assertEquals(1, len(responses.calls))
        self.assertEquals('https://maps.googleapis.com/maps/api/distancematrix/json?'
                          'key=%s&origins=Bobcaygeon+ON%%7C41.432060%%2C-81.389920&'
                          'destinations=43.012486%%2C-83.696415%%7C42.886386%%2C'
                          '-78.878163' % self.key,
                          responses.calls[0].request.url)

    @responses.activate
    def test_all_params(self):
        responses.add(responses.GET, 
                      'https://maps.googleapis.com/maps/api/distancematrix/json',
                      body='{"status":"OK","rows":[]}',
                      status=200,
                      content_type='application/json')

        origins = ["Perth, Australia", "Sydney, Australia",
                   "Melbourne, Australia", "Adelaide, Australia",
                   "Brisbane, Australia", "Darwin, Australia",
                   "Hobart, Australia", "Canberra, Australia"]
        destinations = ["Uluru, Australia",
                        "Kakadu, Australia",
                        "Blue Mountains, Australia",
                        "Bungle Bungles, Australia",
                        "The Pinnacles, Australia"]

        matrix = googlemaps.distance_matrix(self.ctx, origins, destinations,
                                            mode="driving",
                                            language="en-AU",
                                            avoid="tolls",
                                            units="imperial")

        self.assertEquals(1, len(responses.calls))
        self.assertEquals('https://maps.googleapis.com/maps/api/distancematrix/json?'
                          'origins=Perth%%2C+Australia%%7CSydney%%2C+Australia%%7C'
                          'Melbourne%%2C+Australia%%7CAdelaide%%2C+Australia%%7C'
                          'Brisbane%%2C+Australia%%7CDarwin%%2C+Australia%%7CHobart%%2C+'
                          'Australia%%7CCanberra%%2C+Australia&language=en-AU&'
                          'avoid=tolls&mode=driving&key=%s&units=imperial&'
                          'destinations=Uluru%%2C+Australia%%7CKakadu%%2C+Australia%%7C'
                          'Blue+Mountains%%2C+Australia%%7CBungle+Bungles%%2C+Australia'
                          '%%7CThe+Pinnacles%%2C+Australia' % self.key,
                          responses.calls[0].request.url)


    @responses.activate
    def test_lang_param(self):
        responses.add(responses.GET, 
                      'https://maps.googleapis.com/maps/api/distancematrix/json',
                      body='{"status":"OK","rows":[]}',
                      status=200,
                      content_type='application/json')

        origins = ["Vancouver BC", "Seattle"]
        destinations = ["San Francisco", "Victoria BC"]

        matrix = googlemaps.distance_matrix(self.ctx, origins, destinations,
                                            language="fr-FR",
                                            mode="bicycling")

        self.assertEquals(1, len(responses.calls))
        self.assertEquals('https://maps.googleapis.com/maps/api/distancematrix/json?'
                          'key=%s&language=fr-FR&mode=bicycling&'
                          'origins=Vancouver+BC%%7CSeattle&'
                          'destinations=San+Francisco%%7CVictoria+BC' %
                          self.key,
                          responses.calls[0].request.url)