import unittest
from tests.dummy import DummySong
from lyrico.lyrico_sources.musix_match import download_from_musix_match

class TestMusixMatch(unittest.TestCase):

	def test_download_from_musix_match(self):
		song = DummySong('Sarah Connor', 'Unendlich')
		download_from_musix_match(song)
		self.assertIsNone(song.error)
		self.assertIsNotNone(song.lyrics)
		self.assertEqual(song.lyrics[0:21], 'Immer wenn ich tiefer')
		self.assertEqual(song.lyrics[-12:], ', unendlich\n')

	def test_download_from_musix_match_single_quote_end_of_word(self):
		song = DummySong('Ronan Keating', "Lovin' Each Day")
		download_from_musix_match(song)
		self.assertIsNone(song.error)
		self.assertIsNotNone(song.lyrics)
		self.assertEqual(song.lyrics[0:15], 'Ah c′mon, yeah\n')
		self.assertEqual(song.lyrics[-26:], 'Oh, baby, I need you here\n')

	def test_download_from_musix_match_eminem_unauthorized(self):
		song = DummySong('Eminem', 'The Real Slim Shady')
		download_from_musix_match(song)
		self.assertEqual(song.error, 'Musixmatch may not show the lyrics')
