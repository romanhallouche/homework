# First, get the template files
top = open('templates/top.html').read()
bottom = open('templates/bottom.html').read()

# Read in index HTML code
about = open('content/index.html').read()
experience = open('content/experience.html').read()
education = open('content/education.html').read()

# Combine template HTML code with content HTML code
about = top + about + bottom
open('docs/index.html', 'w+').write(about)

# Rinse and repeat, but with blog HTML code
experience = top + experience + bottom
open('docs/experience.html', 'w+').write(experience)

# And again, this time with art HTML code
education = top + education + bottom
open('docs/education.html', 'w+').write(education)



