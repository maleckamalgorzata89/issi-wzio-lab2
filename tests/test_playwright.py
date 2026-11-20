"""Browser tests for the AGH website."""

from playwright.sync_api import Page, expect

def test_open_agh_website(page: Page):
    """Check open agh website"""
    page.goto("https://www.informatyka.agh.edu.pl/pl/")

    print(page.title())

    assert page.title() != ""

def test_subpage_header_is_displayed(page: Page) -> None:
    """Check subpage header"""
    page.goto("https://www.informatyka.agh.edu.pl/pl/")

    menu_element = page.get_by_role("link", name="Wydział", exact=True)
    menu_element.hover()

    link = page.get_by_role("link", name="O Wydziale")
    expect(link).to_be_visible()
    link.click()

    heading = page.get_by_role("heading", name="O Wydziale")
    expect(heading).to_be_visible()

def test_fields_of_study_subpage(page: Page) -> None:
    """Check fields of study subpage"""
    page.goto("https://www.informatyka.agh.edu.pl/pl/")

    menu_element = page.get_by_role("link", name="Kandydaci", exact=True)
    menu_element.hover()

    link = page.locator("#studenci-dla-kandydatow-kierunki").get_by_role(
        "link", name="Nasze kierunki"
    )
    expect(link).to_be_visible()
    link.click()

    field1 = page.get_by_role("link", name="Informatyka – Zarządzanie")
    expect(field1).to_be_visible()

    field2 = page.get_by_role("link", name="Tworzenie przestrzeni")
    expect(field2).to_be_visible()

    field3 = page.get_by_role("link", name="Informatyka", exact=True)
    expect(field3).to_be_visible()

    field4 = page.get_by_role("link", name="Informatyka – Uczenie")
    expect(field4).to_be_visible()

    field5 = page.get_by_role("link", name="Informatyka – Data Science")
    expect(field5).to_be_visible()

def test_subpage_url(page: Page) -> None:
    """Check subpage url"""
    page.goto("https://www.informatyka.agh.edu.pl/pl/")

    menu_element = page.get_by_role("link", name="Wydział", exact=True)
    menu_element.hover()

    link = page.get_by_role("link", name="O Wydziale")
    expect(link).to_be_visible()
    link.click()

    expect(page).to_have_url(
        "https://www.informatyka.agh.edu.pl/pl/wydzial/o-wydziale/"
    )
