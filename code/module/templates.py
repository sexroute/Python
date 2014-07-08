""" templates
summary:
	details
"""
import fileinput, re

# Matches fields enclosed in square brackets:
field_pat = re.compile(r'\[(.+?)\]')
# We'll collect variables in this:
scope = {}

def replacement(match):
	code = match.group(1)
	try:
		return str(eval(code, scope))
	except SyntaxError:
		# raise
		exec(code, scope)
		return ''
lines = []
for line in fileinput.input():
	lines.append(line)
text = ''.join(lines)

print(field_pat.sub(replacement, text))
