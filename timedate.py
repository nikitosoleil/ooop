import re


class TimeDate:
	day_of_week_name = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Wed', 'Sun']
	month_name = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
	days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	seconds_in_quadricentennial = int(400 * (365 + 1 / 4 - 1 / 100 + 1 / 400) * 24 * 60 * 60)
	seconds_in_centennial = int(100 * (365 + 1 / 4 - 1 / 100) * 24 * 60 * 60)
	seconds_in_quadrennial = int(4 * (365 + 1 / 4) * 24 * 60 * 60)
	seconds_in_annual = 365 * 24 * 60 * 60
	our_epoch_start = 1601
	# we will start counting from year 1601 for convenience while unix epoch starts from 1970
	seconds_between_two_epochs = seconds_in_centennial * 3 + seconds_in_quadrennial * 17 + seconds_in_annual

	def __init__(self, str=None):
		self.seconds_since_our_epoch = None
		self.year, self.leap, self.month = None, None, None
		self.day_of_year, self.day_of_month, self.day_of_week = None, None, None
		self.hours, self.minutes, self.seconds = None, None, None
		self.days_in_months = None
		if str:
			self.year, self.month, self.day_of_month, self.hours, self.minutes, self.seconds = map(int, re.findall(r'\d+', str))
			td = TimeDate.from_date_and_time(self.year, self.month, self.day_of_month, self.hours, self.minutes, self.seconds)
			self.month, self.day_of_month = self.month - 1, self.day_of_month - 1
			self.seconds_since_our_epoch, self.leap = td.seconds_since_our_epoch, td.leap
			self.day_of_year, self.day_of_week = td.day_of_year, td.day_of_week
			self.days_in_months = td.days_in_months

	@staticmethod
	def from_timestamp(seconds_since_unix_epoch):
		td = TimeDate()
		td.seconds_since_our_epoch = int(seconds_since_unix_epoch) + TimeDate.seconds_between_two_epochs
		td.seconds = td.seconds_since_our_epoch
		td.day_of_week = TimeDate.get_day_of_week(td.seconds)

		quadricentennials = td.seconds // TimeDate.seconds_in_quadricentennial
		td.seconds %= TimeDate.seconds_in_quadricentennial

		centennials = td.seconds // TimeDate.seconds_in_centennial
		td.seconds %= TimeDate.seconds_in_centennial

		quadrennials = td.seconds // TimeDate.seconds_in_quadrennial
		td.seconds %= TimeDate.seconds_in_quadrennial

		annuals = td.seconds // TimeDate.seconds_in_annual
		td.seconds %= TimeDate.seconds_in_annual

		td.year = TimeDate.our_epoch_start + 400 * quadricentennials + 100 * centennials + 4 * quadrennials + annuals
		td.leap = TimeDate.is_leap_year(td.year)
		td.days_in_months = TimeDate.get_days_in_months(td.leap)

		td.day_of_year = td.seconds // (24 * 60 * 60)
		td.seconds %= (24 * 60 * 60)

		td.hours = td.seconds // (60 * 60)
		td.seconds %= (60 * 60)

		td.minutes = td.seconds // 60
		td.seconds %= 60

		sum = 0
		for i in range(12):
			if sum <= td.day_of_year:
				td.month = i
				td.day_of_month = td.day_of_year - sum
			sum += td.days_in_months[i]

		return td

	@staticmethod
	def from_date_and_time(year, month, day, hours=0, minutes=0, seconds=0):
		if not TimeDate.check_date_and_time(year, month, day, hours, minutes, seconds):
			raise ValueError('something must be wrong with provided date or time')

		td = TimeDate()
		td.year, td.month, td.day_of_month, td.hours, td.minutes, td.seconds = year, month - 1, day - 1, hours, minutes, seconds
		td.leap = TimeDate.is_leap_year(td.year)
		td.days_in_months = TimeDate.get_days_in_months(td.leap)

		tmp = td.year - TimeDate.our_epoch_start
		td.seconds_since_our_epoch = (tmp // 400) * TimeDate.seconds_in_quadricentennial
		tmp %= 400
		td.seconds_since_our_epoch += (tmp // 100) * TimeDate.seconds_in_centennial
		tmp %= 100
		td.seconds_since_our_epoch += (tmp // 4) * TimeDate.seconds_in_quadrennial
		tmp %= 4
		td.seconds_since_our_epoch += tmp * TimeDate.seconds_in_annual

		td.day_of_year = 0
		for i in range(td.month):
			td.seconds_since_our_epoch += td.days_in_months[i] * (24 * 60 * 60)
			td.day_of_year += td.days_in_months[i]

		td.seconds_since_our_epoch += td.day_of_month * (24 * 60 * 60)
		td.day_of_year += td.day_of_month

		td.seconds_since_our_epoch += td.hours * 60 * 60
		td.seconds_since_our_epoch += td.minutes * 60
		td.seconds_since_our_epoch += td.seconds
		td.day_of_week = TimeDate.get_day_of_week(td.seconds_since_our_epoch)

		return td

	@staticmethod
	def is_leap_year(year):
		return (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)

	@staticmethod
	def get_days_in_months(leap):
		ret = TimeDate.days_in_months
		if leap:
			ret[1] += 1  # additional day in February
		return ret

	@staticmethod
	def get_day_of_week(seconds):
		return (seconds // (24 * 60 * 60)) % 7  # 1st Jan 1961 was Monday

	@staticmethod
	def check_date_and_time(year, month, day, hours, minutes, seconds):
		if not isinstance(year, int):
			return False
		days_in_months = TimeDate.get_days_in_months(TimeDate.is_leap_year(year))
		if not isinstance(month, int) or month > 12 or month < 1:
			return False
		if not isinstance(day, int) or day > days_in_months[month - 1] or day < 1:
			return False
		if not isinstance(hours, int) or hours > 23 or hours < 0:
			return False
		if not isinstance(minutes, int) or minutes > 59 or minutes < 0:
			return False
		if not isinstance(seconds, int) or seconds > 59 or seconds < 0:
			return False
		return True

	def __str__(self):
		return '{} {}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}'.format(TimeDate.day_of_week_name[self.day_of_week], self.year, self.month + 1,
																 self.day_of_month + 1, self.hours, self.minutes, self.seconds)

	def __int__(self):
		return self.seconds_since_our_epoch - TimeDate.seconds_between_two_epochs

	def __sub__(self, td):
		if isinstance(td, TimeDate):
			if self.seconds_since_our_epoch < td.seconds_since_our_epoch:
				ret = td - self
				ret.pure_seconds = -ret.pure_seconds
				ret.years = -ret.years
				ret.months = -ret.months
				ret.days = -ret.days
				ret.hours = -ret.hours
				ret.minutes = -ret.minutes
				ret.seconds = -ret.seconds
			else:
				ret = TimeDelta()
				ret.pure_seconds = self.seconds_since_our_epoch - td.seconds_since_our_epoch
				ret.years = self.year - td.year
				ret.months = self.month - td.month
				ret.days = self.day_of_month - td.day_of_month
				ret.hours = self.hours - td.hours
				ret.minutes = self.minutes - td.minutes
				ret.seconds = self.seconds - td.seconds
				if ret.seconds < 0:
					ret.seconds += 60
					ret.minutes -= 1
				if ret.minutes < 0:
					ret.minutes += 60
					ret.hours -= 1
				if ret.hours < 0:
					ret.hours += 24
					ret.days -= 1
				if ret.days < 0:
					ret.days += td.days_in_months[td.month]
					ret.months -= 1
				if ret.months < 0:
					ret.months += 12
					ret.years -= 1
			return ret
		elif isinstance(td, TimeDelta):
			return TimeDate.from_timestamp(self.seconds_since_our_epoch - TimeDate.seconds_between_two_epochs - td.pure_seconds)
		else:
			raise ValueError('second operand must be of TimeDate or TimeDelta type')

	def __add__(self, td):
		if isinstance(td, TimeDelta):
			return TimeDate.from_timestamp(self.seconds_since_our_epoch - TimeDate.seconds_between_two_epochs + td.pure_seconds)
		else:
			raise ValueError('second operand must be of TimeDelta type')


class TimeDelta:
	def __init__(self):
		self.pure_seconds = None
		self.years, self.months, self.days, self.hours, self.minutes, self.seconds = [None] * 6

	def __str__(self):
		return '{} years, {} months, {} days, {} hours, {} minutes, {} seconds'.format(self.years, self.months, self.days, self.hours, self.minutes,
																					   self.seconds)

	def __int__(self):
		return self.pure_seconds