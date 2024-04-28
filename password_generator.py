# Password Generator
from string import ascii_letters, digits, punctuation
from random import choice, randint, shuffle


class Password:
	def __init__(self):
		"""Create lists for alphabet, numbers and symbols for password generator"""
		self.letters = ascii_letters
		self.numbers = digits
		self.symbols = punctuation

	def generate(self):
		"""Generates random password"""
		letters = [choice(self.letters) for _ in range(randint(8, 15))]
		numbers = [choice(self.numbers) for _ in range(randint(2, 5))]
		symbols = [choice(self.symbols) for _ in range(randint(2, 5))]
		password_list = letters + numbers + symbols
		shuffle(password_list)
		password = "".join(password_list)

		return password
