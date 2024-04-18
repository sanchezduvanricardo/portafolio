import reflex as rx
from portafolio.components.heading import heading
from portafolio.data import Technology
from portafolio.styles.styles import EmSize, Size

textless_technologies = ["UiPath","Power Apps","Power Automate"]

def tech_stack(technologies: list[Technology]) -> rx.Component:
    return rx.vstack(
        heading("Technologies"),
        rx.flex(
            *[
                rx.badge(
                    rx.cond(
                        technology.name not in  textless_technologies  ,
                        rx.box(
                            class_name=technology.icon,
                            font_size="24px"
                        ),
                        rx.box(
                          rx.image(src=technology.icon, width="24px", height="auto"),  # Asegúrate de que la ruta a tu imagen sea correcta
                            font_size="24px"
                        ),
                    ),
                    rx.text(technology.name),
                    size="2"
                )
                for technology in technologies
            ],
            wrap="wrap",
            spacing=Size.SMALL.value
        ),
        spacing=Size.DEFAULT.value
    )
# def tech_stack(technologies: list[Technology]) -> rx.Component:
#     return rx.vstack(
#         heading("Tecnologías"),
#         rx.flex(
#             *[
#                 rx.badge(
#                     rx.box(
#                         class_name=technology.icon,
#                         font_size="24px"
#                     ),
#                     rx.text(technology.name),
#                     size="2"
#                 )
                
#                 for technology in technologies
#             ],
#             wrap="wrap",
#             spacing=Size.SMALL.value
#         ),
#         spacing=Size.DEFAULT.value
#     )
