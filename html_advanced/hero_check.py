from bs4 import BeautifulSoup

html = """
<main>
    <section>
        <h1>Hero section</h1>
        <!-- Content for the Hero section goes here -->
    </section>
    <section>
        <h1>Services section</h1>
        <!-- Content for the Services section goes here -->
    </section>
    <!-- ... other sections ... -->
</main>
"""

soup = BeautifulSoup(html, 'html.parser')

# Find the text content of the 'h1' tag in the Hero section
hero_section = soup.find('section', text='Herosection')
if hero_section:
    hero_text = hero_section.find('h1').text
    print(hero_text)
else:
    print("Herosection not found")

# Repeat the above process for other sections as needed
