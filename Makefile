test.once:
	nosetests test/unit

test.continuously:
	bundle exec guard start --clear --notify=false
