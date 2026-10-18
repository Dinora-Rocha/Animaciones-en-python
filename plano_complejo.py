
from manim import *

class PlanoComplejo(Scene):
    def construct(self):
        Text.set_default(font="sans-serif")

        # ==========================================
        # 1. INTRODUCCIÓN: LA RECTA NUMÉRICA
        # ==========================================

        titulo = Text(
            "El plano complejo",
            font_size=38,
            weight=BOLD
        ).to_edge(UP)

        subtitulo = Text(
            "De una dimensión a dos",
            font_size=23,
            color=GRAY_B
        ).next_to(titulo, DOWN, buff=0.12)

        self.play(Write(titulo), FadeIn(subtitulo))
        self.wait(0.5)

        recta = NumberLine(
            x_range=[-4, 4, 1],
            length=8,
            include_numbers=True,
            font_size=22,
            color=BLUE_B,
            include_tip=True
        ).shift(DOWN * 0.5)

        etiqueta_real = Text(
            "Números reales: una sola coordenada",
            font_size=24,
            color=BLUE_B
        ).next_to(recta, DOWN, buff=0.6)

        self.play(Create(recta), FadeIn(etiqueta_real))
        self.wait(1)

        # ==========================================
        # 2. TRANSICIÓN AL PLANO DE ARGAND
        # ==========================================

        texto_transicion = Text(
            "Los complejos necesitan dos coordenadas",
            font_size=25,
            color=YELLOW
        ).to_edge(DOWN, buff=0.35)

        self.play(
            FadeOut(subtitulo),
            FadeOut(etiqueta_real),
            FadeOut(recta),
            FadeIn(texto_transicion),
            run_time=1
        )

        plano = ComplexPlane(
            x_range=[-5, 5, 1],
            y_range=[-4, 5, 1],
            x_length=9,
            y_length=6.8,
            background_line_style={
                "stroke_color": BLUE_E,
                "stroke_opacity": 0.45,
                "stroke_width": 1
            },
            axis_config={
                "color": WHITE,
                "stroke_width": 2,
                "include_numbers": True,
                "font_size": 18,
            },
        ).add_coordinates()

        plano.shift(DOWN * 0.25)

        eje_real = Text(
            "Parte real (Re)",
            font_size=20,
            color=BLUE_B
        ).next_to(plano.x_axis.get_end(), RIGHT, buff=0.12)

        eje_imaginario = Text(
            "Parte imaginaria (Im)",
            font_size=20,
            color=GREEN_B
        ).next_to(plano.y_axis.get_end(), UP, buff=0.12)

        nombre_plano = Text(
            "Plano de Argand",
            font_size=23,
            color=YELLOW
        ).to_corner(UR).shift(DOWN * 0.7)

        self.play(
            Create(plano),
            FadeOut(texto_transicion),
            run_time=1.5
        )
        self.play(
            FadeIn(eje_real),
            FadeIn(eje_imaginario),
            Write(nombre_plano)
        )
        self.wait(1)

        # ==========================================
        # 3. REPRESENTACIÓN DE 3 + 4i
        # ==========================================

        explicacion = Text(
            "Un número complejo es un punto del plano",
            font_size=24
        ).to_edge(DOWN, buff=0.25)

        self.play(Write(explicacion))

        origen = plano.c2p(0, 0)
        punto_z = plano.c2p(3, 4)

        proyeccion_h = DashedLine(
            origen,
            plano.c2p(3, 0),
            color=BLUE_B,
            stroke_width=3
        )

        proyeccion_v = DashedLine(
            plano.c2p(3, 0),
            punto_z,
            color=GREEN_B,
            stroke_width=3
        )

        punto = Dot(punto_z, color=YELLOW, radius=0.09)

        vector = Arrow(
            origen,
            punto_z,
            buff=0,
            color=YELLOW,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.12
        )

        etiqueta_z = MathTex(
            "z=3+4i",
            color=YELLOW,
            font_size=34
        ).next_to(punto, UR, buff=0.15)

        etiqueta_tres = MathTex(
            "3",
            color=BLUE_B,
            font_size=27
        ).next_to(plano.c2p(1.5, 0), DOWN, buff=0.12)

        etiqueta_cuatro = MathTex(
            "4i",
            color=GREEN_B,
            font_size=27
        ).next_to(plano.c2p(3, 2), RIGHT, buff=0.12)

        self.play(Create(proyeccion_h), FadeIn(etiqueta_tres))
        self.play(Create(proyeccion_v), FadeIn(etiqueta_cuatro))
        self.play(
            GrowArrow(vector),
            FadeIn(punto),
            Write(etiqueta_z)
        )
        self.wait(1.5)

        # ==========================================
        # 4. MULTIPLICAR POR i: UNA ROTACIÓN
        # ==========================================

        explicacion_rotacion = Text(
            "Multiplicar por i = girar 90 grados",
            font_size=27,
            color=GOLD
        ).to_edge(DOWN, buff=0.25)

        self.play(
            FadeOut(explicacion),
            FadeOut(proyeccion_h),
            FadeOut(proyeccion_v),
            FadeOut(etiqueta_tres),
            FadeOut(etiqueta_cuatro),
            FadeIn(explicacion_rotacion)
        )

        # El punto (3,4) pasa a (-4,3).
        # Rotación antihoraria de 90 grados alrededor del origen.

        punto_final = plano.c2p(-4, 3)

        vector_final = Arrow(
            origen,
            punto_final,
            buff=0,
            color=RED,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.12
        )

        punto_final_obj = Dot(
            punto_final,
            color=RED,
            radius=0.09
        )

        etiqueta_final = MathTex(
            "(3+4i)i=-4+3i",
            color=RED,
            font_size=30
        ).next_to(punto_final, UL, buff=0.15)

        arco = Arc(
            radius=0.75,
            start_angle=0,
            angle=PI / 2,
            arc_center=origen,
            color=GOLD,
            stroke_width=4
        )

        angulo = MathTex(
            "90^\\circ",
            color=GOLD,
            font_size=27
        ).move_to(
            origen + 1.0 * np.array([0.7, 0.7, 0])
        )

        # Rotar el vector, el punto y su etiqueta juntos.
        grupo_inicial = VGroup(vector, punto, etiqueta_z)

        self.play(
            Rotate(
                grupo_inicial,
                angle=PI / 2,
                about_point=origen
            ),
            Create(arco),
            FadeIn(angulo),
            run_time=2.5,
            rate_func=smooth
        )

        # Sustituir la etiqueta girada por una expresión horizontal.
        etiqueta_resultado = MathTex(
            "(3+4i)\\cdot i=-4+3i",
            color=RED,
            font_size=29
        ).to_edge(UP, buff=0.9)

        self.play(
            Transform(vector, vector_final),
            Transform(punto, punto_final_obj),
            Transform(etiqueta_z, etiqueta_final),
            run_time=1
        )

        self.play(
            FadeIn(etiqueta_resultado),
            run_time=0.7
        )

        # ==========================================
        # 5. CONCLUSIÓN
        # ==========================================

        conclusion = Text(
            "Los números complejos describen giros y cambios.",
            font_size=23,
            color=WHITE
        ).to_edge(DOWN, buff=0.25)

        self.play(
            FadeOut(explicacion_rotacion),
            FadeIn(conclusion)
        )
        self.wait(2)