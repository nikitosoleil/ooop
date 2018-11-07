from help import current_time


class MyNote:
	def __init__(self, text, tag, created_at=None, edited_at=None):
		if not created_at:
			created_at = current_time()
		if not edited_at:
			edited_at = current_time()
		self.text = text
		self.created_at, self.edited_at = created_at, edited_at
		self.tag = tag
