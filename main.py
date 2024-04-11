import flet as ft
from flet import Row, Text


def main(page: ft.Page):
    page.title = "Counting ball ORT test"
    page.theme_mode = 'dark'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def change_them(e):
        page.theme_mode = 'light' if page.theme_mode == 'dark' else 'dark'
        page.update()

    them = Row([ft.IconButton(ft.icons.LIGHTBULB_OUTLINED, on_click=change_them)],
               alignment=ft.MainAxisAlignment.SPACE_AROUND)

    def validate(e):
        if all([basic_test_math.value, basic_test_grammar.value, basic_test_read.value]) or subject_ball.value:
            btn_count.disabled = False
            btn_count_subject.disabled = False
        else:
            btn_count.disabled = True
            btn_count_subject.disabled = True
        page.update()

    ball_sum = ft.Text('', size=23, font_family='Candara')
    error_msg = ft.Text("")
    basic_ball = ft.Text("", size=23)

    def counting_basic_test(e):
        try:
            all_sum = sum(map(float, [basic_test_math.value, basic_test_read.value, basic_test_grammar.value]))
            answer_ball = int(all_sum * 245 / 300)
            print(answer_ball)
            ball_sum.value = "Your ball : " + str(answer_ball)
            page.update()
        except ValueError:
            error_msg.value = "You need write number , not the letters !!!"
            print(error_msg)
            page.update()

    def counting_subject_test(e):
        try:
            sum_subject = int((float(subject_ball.value) * 150) / 100)
            basic_ball.value = "Your ball : " + str(sum_subject)

            page.update()
        except ValueError:
            error_msg.value = "You need write number , not the letters !!!"
            print(error_msg)
            page.update()

    basic_test_math = ft.TextField(label='Math', width=300, height=60, on_change=validate)
    basic_test_read = ft.TextField(label='Reading and understanding', width=300, height=60, on_change=validate)
    basic_test_grammar = ft.TextField(label='Grammar', width=300, height=60, on_change=validate)
    btn_count = ft.ElevatedButton(text='Answer', width=300, on_click=counting_basic_test, disabled=True,
                                  color=ft.colors.BLUE)

    subject_ball = ft.TextField(label='Subject ball', width=300, height=60, on_change=validate)
    btn_count_subject = ft.ElevatedButton(text='Answer', width=300, on_click=counting_subject_test, disabled=True,
                                          color=ft.colors.BLUE)

    basic_test = ft.Row([ft.Column([
        Text("Your ORT Basic Ball", color=ft.colors.BLUE_ACCENT_100, size=16),
        basic_test_math,
        basic_test_grammar,
        basic_test_read,
        btn_count,
        ball_sum,
        error_msg])
    ], alignment=ft.MainAxisAlignment.CENTER)

    subject_test = ft.Row([ft.Column([
        Text("Your ORT Subject Ball", color=ft.colors.BLUE_ACCENT_100, size=16),
        subject_ball,
        btn_count_subject,
        basic_ball,
        error_msg])
    ], alignment=ft.MainAxisAlignment.CENTER)

    def navigate(e):
        index = page.navigation_bar.selected_index
        page.clean()

        if index == 0:
            page.add(them, basic_test)
        elif index == 1:
            page.add(them, subject_test)
        page.update()

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.TEXT_SNIPPET, label='Basic ball'),
            ft.NavigationDestination(icon=ft.icons.TEXT_SNIPPET_OUTLINED, label='Subject ball')
        ], on_change=navigate
    )

    page.add(them, basic_test)


ft.app(target=main, view=ft.AppView.WEB_BROWSER)
