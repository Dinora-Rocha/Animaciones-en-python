from manim import *

class CierreComplejos(Scene):
    def construct(self):
        Text.set_default(font="sans-serif")

        # --- PARTE 1: Iconos Cotidianos (Celular, Música, Wi-Fi) ---
        
        # 1. Batería / Celular
        bateria_rect = Rectangle(width=1.2, height=2.0, color=BLUE)
        bateria_tip = Rectangle(width=0.4, height=0.2, color=BLUE, fill_opacity=1).next_to(bateria_rect, UP, buff=0)
        icono_bateria = VGroup(bateria_rect, bateria_tip)
        carga = Rectangle(width=1.0, height=1.6, color=GREEN, fill_opacity=0.8).move_to(bateria_rect)
        rayo = MathTex("\\Downarrow", color=YELLOW, font_size=40).move_to(bateria_rect)
        celular_group = VGroup(icono_bateria, carga, rayo).scale(0.8)

        txt_celular = Text("Cargar Celular", font_size=18, color=WHITE).next_to(celular_group, DOWN, buff=0.3)
        item1 = VGroup(celular_group, txt_celular)

        # 2. Música / Audio
        nota1 = MathTex("\\sharp", font_size=48, color=TEAL)
        nota2 = MathTex("\\flat", font_size=56, color=TEAL_B)
        notas_group = VGroup(nota1, nota2).arrange(RIGHT, buff=0.3)
        txt_musica = Text("Música Comprimida", font_size=18, color=WHITE).next_to(notas_group, DOWN, buff=0.3)
        item2 = VGroup(notas_group, txt_musica)

        # 3. Wi-Fi / Señal
        wifi_base = Dot(point=ORIGIN, color=GOLD, radius=0.08)
        wifi_arc1 = Arc(radius=0.4, start_angle=PI/4, angle=PI/2, color=GOLD, stroke_width=4)
        wifi_arc2 = Arc(radius=0.7, start_angle=PI/4, angle=PI/2, color=GOLD, stroke_width=4)
        wifi_group = VGroup(wifi_base, wifi_arc1, wifi_arc2)
        txt_wifi = Text("Wi-Fi de casa", font_size=18, color=WHITE).next_to(wifi_group, DOWN, buff=0.3)
        item3 = VGroup(wifi_group, txt_wifi)

        # Agrupar las 3 tecnologías horizontalmente
        tecnologias = VGroup(item1, item2, item3).arrange(RIGHT, buff=1.2).shift(UP * 1.2)

        self.play(
            LaggedStart(
                FadeIn(item1, shift=UP),
                FadeIn(item2, shift=UP),
                FadeIn(item3, shift=UP),
                lag_ratio=0.4
            ),
            run_time=3
        )
        self.wait(2)

        # --- PARTE 2: La paradoja histórica vs actualidad ---

        txt_hace_400 = Text(
            "Hace 400 años: 'Una imposibilidad sin sentido'",
            font_size=24, color=RED_B
        ).next_to(tecnologias, DOWN, buff=0.8)

        self.play(Write(txt_hace_400))
        self.wait(2.5)

        # Transformación a conclusión final
        txt_hoy = Text(
            "Hoy: Una de las herramientas más poderosas jamás descubiertas.",
            font_size=26, color=GOLD
        ).next_to(tecnologias, DOWN, buff=0.8)

        marco_final = SurroundingRectangle(txt_hoy, color=GOLD, buff=0.25)

        self.play(
            Transform(txt_hace_400, txt_hoy),
            Create(marco_final)
        )
        self.wait(3.5)

        # --- PARTE 3: Cierre suave ---
        self.play(
            FadeOut(tecnologias),
            FadeOut(txt_hace_400),
            FadeOut(marco_final)
        )
        self.wait(1)