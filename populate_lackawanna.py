import os

def populate():
	user1 = add_user('lewism')
	user2 = add_user('davidw')
	user3 = add_user('karenr')
	user4 = add_user('matpat')

	#London Riot test data
	add_project(owner=user1,
		name="London Riots",
		description="Taking place over the summer of 2011, these riots caused widespread panic and worry",
		status='public')

	add_collection(owner=user1,
		name="Broom Army",
		description="Social media success or just to be expected?")

	add_collection(owner=user1,
		name="Hackney related media",
		description="Media that was specifically written about Hackney as a centre point of the riots.")

	#Rise of Tesla test data
	tesla = add_project(owner=user2,
		name="Rise of Tesla",
		description="Went from a small manufacturing startup to paying off $1 billion loan off 15 years early.",
		status='public')

	add_collection(owner=user2,
		project=tesla,
		name="Elon Musk",
		description="Data related to the real life Iron Man.",)

	add_collection(owner=user2,
		project=tesla,
		name="US Government interactions",
		description="US Gov's influence on the company's beginnings")


	##gamergate test data
	gamergate = add_project(owner=user3,
		name="#gamergate",
		description="A debate about ethics or just a fascade for the harassment of women in games?",
		status='public')

	add_collection(owner=user3,
		project=gamergate,
		name="Anita Sarkeesian",
		description="Key player against movement")

	add_collection(owner=user3,
		project=gamergate,
		name="Mainstream coverage",
		description="How have the mainstream media covered the topic.")


	#Apple test data
	apple_project = add_project(owner=user4,
		name="Apple: Post Steve Jobs",
		description="After his untimely death, what has changed at Steve Job's company without him?",
		status='public')

	add_collection(owner=user4,
		project=apple_project,
		name="Product Launches",
		description="New products the company have put out since")

	add_collection(owner=user3,
		project=apple_project,
		name="Key Personnel departures",
		description="How have the people who have left made their mark on the comapny's ongoing success")

	add_collection(owner=user4,
		project=apple_project,
		name="Shift from technology to lifestyle brand",
		description="Datapoints relating to their changing brand values and appearances.")

def add_user(username):
	u = User.objects.get_or_create(username=username, password="tester", email="email@email.com")
	return u

def add_project(owner, name, description, status):
	p = Project.objects.get_or_create(owner=owner, name=name, description=description, status=status)
	return p

def add_collection(owner, project, name, description):
	c = Collection.objects.get_or_create(owner=owner, project=project, name=name, description=description)


if __name__ == '__main__':
	print "Starting Lackawanna population script..."
	from configurations import importer
	importer.install()
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lackawanna.config.local')
	os.environ.setdefault('DJANGO_CONFIGURATION', 'config.local')
	from lackawanna.project.models import Project
	from lackawanna.collection.models import Collection
	from lackawanna.users.models import User
	populate()
