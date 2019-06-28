
#def main():
    #base = open('templates/base.html').read()

    #about = open('content/index.html').read()
    #experience = open('content/experience.html').read()
    #education = open('content/education.html').read()

    #about = top + about + bottom
    #open('docs/index.html', 'w+').write(about)
    #experience = top + experience + bottom
    #pen('docs/experience.html', 'w+').write(experience)
    #education = top + education + bottom
    #open('docs/education.html', 'w+').write(education)




pages = [
        {
    "input": "content/index.html",
    "output": "docs/index.html",
    "title": "About Me",
    },
        {
    "input": "content/experience.html",
    "output": "docs/experience.html",
    "title": "My Experience",
    },
        {
    "input": "content/education.html",
    "output": "docs/education.html",
    "title": "My Education",
    },
]


def main():
    for page in pages:
        base = open('templates/base.html').read()
        page_content = open(page["input"]).read()
        final_page = base.replace("{{content}}", page_content)
        open(page["output"], "w+").write(final_page)



if __name__ == "__main__":
    main()




######### Attempt to Phase 5 but couldn't figure out how  ###########

# def main():
#     for page in pages:
#         base = open('templates/base.html').read()
#         page_content = open_input()
#         final_page = create_final_page()
#         open(page["output"], "w+").write(final_page)



# def open_input():
#     open(page["input"]).read()


# def create_final_page():
#     base.replace("{{content}}", page_content)