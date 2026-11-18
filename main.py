from flet import *
def main (page:Page):
  page.bgcolor = Colors.BLUE
  def home_page ():
    return View(
      route = "/",
      controls = [
        Text(
          "home page",
          color="blue",
          size=20
        ),
      FilledButton(
        "الاعدادات",
        icon= Icons.SETTINGS,
        on_click = lambda e: page.navigate("/settings")
      ),

      FilledButton(
        "املف الشخص",
        icon= Icons.PERSON,
        on_click = lambda e: page.navigate("/person")
      )
      ]
    )

  def setting_page ():
    return View(
      route = "/settings",
      controls = [
        Text(
          "setting page",
          color="blue",
          size=20
        ),
      FilledButton(
        "الرئىسىه",
        icon= Icons.HOME,
        on_click = lambda e: page.navigate("/")
      ),

      FilledButton(
        "املف الشخص",
        icon= Icons.PERSON,
        on_click = lambda e: page.navigate("/person")
      )
      ]
    )

  def person_page ():
    return View(
      route = "/person",
      controls = [
        Text(
          "person page",
          color="blue",
          size=20
        ),
      FilledButton(
        "الاعدادات",
        icon= Icons.SETTINGS,
        on_click = lambda e: page.navigate("/settings")
      ),

      FilledButton(
        "hgvznsni",
        icon= Icons.PERSON,
        on_click = lambda e: page.navigate("/")
      )
      ]
    )

  def route_change(e):
        page.views.clear()

        if page.route == "/":
            page.views.append(home_page())

        elif page.route == "/settings":
            page.views.append(setting_page())

        elif page.route == "/person":
            page.views.append(person_page())

        page.update()

  page.on_route_change = route_change
  route_change(None)

run(main)
