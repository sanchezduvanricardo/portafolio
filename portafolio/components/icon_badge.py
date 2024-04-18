import reflex as rx

from portafolio.styles.styles import EmSize


def icon_badge(icon: str) -> rx.Component:
    return rx.badge(
        rx.icon(
            icon,
            size=32
        ),
        aspect_ratio="1",
        variant="soft"
    )

def icon_text(icon: str) -> rx.Component:
    return rx.badge(
        rx.icon(
            icon,
            size=16,
            style={"background_color": "rgba(255, 255, 255, 0)"}
        ),
        )