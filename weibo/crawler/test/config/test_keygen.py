# -*- coding: utf-8 -*-
import unittest
from crawler.config.keygen import *
from crawler.config.readconf import ReadConf

class ProcessAbstractTest(unittest.TestCase):
	def setUp(self):
		self.name = '@qq.com'
		self.password = ''
		ProcessAbstract.encryProcess(Encryption(),self.name,self.password)
		self.readConf = ReadConf()
		self.decry = Decryption()

	def tearDown(self):
		del self.decry
		del self.readConf

	def test_decryProcess(self):
		name,password = ProcessAbstract.decryProcess(self.decry,self.readConf)
		assert name is not None
		assert password is not None
		self.assertEqual(name,self.name)
		self.assertEqual(password,self.password)
