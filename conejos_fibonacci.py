from manim import *


class ParejasConejosFibonacci(Scene):
    def construct(self):
        self.camera.background_color = "#07080A"

        # -------------------------------------------------------------
        # 1. TÍTULO E INTRODUCCIÓN
        # -------------------------------------------------------------
        titulo = Text("El Problema de los Conejos de Fibonacci", font_size=32, color=WHITE)
        titulo.to_edge(UP, buff=0.4)
        
        pregunta = Text("¿Cuántas parejas de conejos habrá en 1 año?", font_size=22, color=GOLD)
        pregunta.next_to(titulo, DOWN, buff=0.2)

        self.play(Write(titulo), FadeIn(pregunta), run_time=2.0)
        self.wait(1.0)

        # -------------------------------------------------------------
        # 2. REGLAS DEL PROBLEMA
        # -------------------------------------------------------------
        regla1 = Text("• Cada pareja adulta produce una nueva pareja cada mes.", font_size=18, color=GRAY_A)
        regla2 = Text("• Una pareja joven tarda 1 mes en madurar antes de reproducirse.", font_size=18, color=GRAY_A)
        reglas = VGroup(regla1, regla2).arrange(DOWN, aligned_edge=LEFT, buff=0.15).shift(UP * 1.5)

        self.play(FadeIn(reglas, shift=DOWN * 0.2), run_time=2.0)
        self.wait(2.0)
        self.play(FadeOut(reglas), run_time=1.0)

        # -------------------------------------------------------------
        # 3. SIMULACIÓN MES A MES (12 MESES / 1 AÑO)
        # -------------------------------------------------------------
        # Datos: (Mes, Adultas, Jóvenes, Total)
        # Mes 1: 0 ad, 1 jov = 1
        # Mes 2: 1 ad, 0 jov = 1
        # Mes 3: 1 ad, 1 jov = 2
        # ...
        datos_meses = [
            ("Mes 1", "0", "1", "1"),
            ("Mes 2", "1", "0", "1"),
            ("Mes 3", "1", "1", "2"),
            ("Mes 4", "2", "1", "3"),
            ("Mes 5", "3", "2", "5"),
            ("Mes 6", "5", "3", "8"),
            ("Mes 7", "8", "5", "13"),
            ("Mes 8", "13", "8", "21"),
            ("Mes 9", "21", "13", "34"),
            ("Mes 10", "34", "21", "55"),
            ("Mes 11", "55", "34", "89"),
            ("Mes 12 (1 año)", "89", "55", "144"),
        ]

        # Iconos de pareja: Joven (chica/azul) y Adulta (grande/dorada)
        icono_joven = Text("🐇", font_size=24)
        icono_adulta = Text("🐇✨", font_size=28)

        m_tex = Text("Mes: 1", font_size=28, color=BLUE_B).move_to(UP * 1.2 + LEFT * 3)
        ad_tex = Text("Adultas: 0", font_size=22, color=WHITE).next_to(m_tex, DOWN, aligned_edge=LEFT, buff=0.2)
        jov_tex = Text("Jóvenes: 1", font_size=22, color=WHITE).next_to(ad_tex, DOWN, aligned_edge=LEFT, buff=0.2)
        tot_tex = Text("Total Parejas: 1", font_size=30, color=GOLD).next_to(jov_tex, DOWN, aligned_edge=LEFT, buff=0.4)

        panel_info = VGroup(m_tex, ad_tex, jov_tex, tot_tex)

        # Muestra gráfica representativa
        parejas_vis = VGroup(icono_joven.copy()).move_to(RIGHT * 2)

        self.play(FadeIn(panel_info), FadeIn(parejas_vis), run_time=1.5)
        self.wait(0.5)

        # Iteración de los meses (avances dinámicos para que sumen ~15 segundos)
        for mes_nombre, ad, jov, tot in datos_meses[1:]:
            nuevo_m = Text(f"{mes_nombre}", font_size=28, color=BLUE_B).move_to(m_tex)
            nuevo_ad = Text(f"Adultas: {ad}", font_size=22, color=WHITE).move_to(ad_tex)
            nuevo_jov = Text(f"Jóvenes: {jov}", font_size=22, color=WHITE).move_to(jov_tex)
            nuevo_tot = Text(f"Total Parejas: {tot}", font_size=30, color=GOLD).move_to(tot_tex)

            # Para no saturar la pantalla con 144 conejos, mostramos representación simbólica
            num_tot = int(tot)
            if num_tot <= 8:
                vis_items = [icono_adulta.copy() for _ in range(int(ad))] + [icono_joven.copy() for _ in range(int(jov))]
                nuevas_vis = VGroup(*vis_items).arrange_in_grid(rows=2, buff=0.3).move_to(RIGHT * 2)
            else:
                nuevas_vis = VGroup(
                    Text("🐇", font_size=40),
                    Text(f"x {tot} parejas", font_size=28, color=GOLD)
                ).arrange(RIGHT, buff=0.3).move_to(RIGHT * 2)

            self.play(
                Transform(m_tex, nuevo_m),
                Transform(ad_tex, nuevo_ad),
                Transform(jov_tex, nuevo_jov),
                Transform(tot_tex, nuevo_tot),
                Transform(parejas_vis, nuevas_vis),
                run_time=0.8,
            )
            self.wait(0.4)

        self.wait(1.0)

        # -------------------------------------------------------------
        # 4. CONCLUSIÓN Y SECUENCIA RESULTANTE
        # -------------------------------------------------------------
        self.play(
            FadeOut(panel_info),
            FadeOut(parejas_vis),
            FadeOut(pregunta),
            run_time=1.0,
        )

        resultado_texto = Text("¡Al resolver el problema, descubrió la Sucesión!", font_size=22, color=WHITE)
        resultado_texto.shift(UP * 1.0)

        secuencia = MathTex(
            "1,", "1,", "2,", "3,", "5,", "8,", "13,", "21,", "34,", "55,", "89,", "144",
            font_size=34, color=GOLD
        ).next_to(resultado_texto, DOWN, buff=0.4)

        explicacion = Text("Cada número es la suma de los dos anteriores", font_size=20, color=GREEN_B)
        explicacion.next_to(secuencia, DOWN, buff=0.5)

        self.play(Write(resultado_texto), run_time=1.5)
        self.play(Write(secuencia), run_time=2.5)
        self.play(FadeIn(explicacion), run_time=1.0)
        self.wait(3.0)