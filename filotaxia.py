from manim import *
import numpy as np


class FilotaxiaGirasol(MovingCameraScene):
    def construct(self):
        self.camera.background_color = "#07080A"

        # -------------------------------------------------------------
        # 1. TÍTULO E INTRODUCCIÓN
        # -------------------------------------------------------------
        titulo = Text("Fibonacci en la Naturaleza: Eficiencia", font_size=32, color=WHITE)
        titulo.to_edge(UP, buff=0.4)
        titulo.set_z_index(100)

        subtitulo = Text(
            "Empaquetado óptimo de semillas sin desperdiciar espacio",
            font_size=20,
            color=GRAY_A,
        )
        subtitulo.next_to(titulo, DOWN, buff=0.2)
        subtitulo.set_z_index(100)

        self.play(Write(titulo), FadeIn(subtitulo), run_time=1.8)
        self.wait(0.5)

        # -------------------------------------------------------------
        # 2. COMPARACIÓN DE ÁNGULOS (Ángulo Simple vs Ángulo Dorado)
        # -------------------------------------------------------------
        centro = DOWN * 0.3

        # Función para generar semillas según un ángulo dado
        def generar_semillas(angulo_grados, num=150):
            angulo_rad = angulo_grados * DEGREES
            semillas = VGroup()
            for i in range(1, num + 1):
                r = 0.22 * np.sqrt(i)
                theta = i * angulo_rad
                pos = centro + np.array([r * np.cos(theta), r * np.sin(theta), 0])
                dot = Dot(point=pos, radius=0.06, color=DORADO_PETALO if 'DORADO_PETALO' in globals() else GOLD)
                semillas.add(dot)
            return semillas

        # Texto del ángulo actual
        texto_angulo = Text("Ángulo: 90° (Ineficiente)", font_size=24, color=RED_B)
        texto_angulo.move_to(UP * 1.5 + LEFT * 3.2)

        semillas_90 = generar_semillas(90, 80)
        
        self.play(Write(texto_angulo), FadeIn(semillas_90, lag_ratio=0.02), run_time=1.5)
        self.wait(1)

        # Cambiar a Ángulo Dorado
        texto_angulo_dorado = Text("Ángulo Dorado: 137.5° (Eficiencia Óptima)", font_size=24, color=GREEN_B)
        texto_angulo_dorado.move_to(UP * 1.5)

        semillas_doradas = generar_semillas(137.508, 220)

        self.play(
            FadeOut(texto_angulo),
            Transform(semillas_90, semillas_doradas),
            FadeIn(texto_angulo_dorado),
            run_time=2.0,
        )
        self.wait(1.5)

        # -------------------------------------------------------------
        # 3. MUESTRA DE ESPIRALES Y CONEXIÓN CON FIBONACCI
        # -------------------------------------------------------------
        info_espirales = Text(
            "Espirales: 34 en un sentido, 55 en el otro",
            font_size=22,
            color=GOLD,
        ).next_to(semillas_90, DOWN, buff=0.5)

        conclusion = Text(
            "No es magia ni coincidencia: es selección natural y matemática.",
            font_size=18,
            color=WHITE,
        ).next_to(info_espirales, DOWN, buff=0.2)

        self.play(Write(info_espirales), run_time=1.5)
        self.play(FadeIn(conclusion), run_time=1.2)
        self.wait(3.0)