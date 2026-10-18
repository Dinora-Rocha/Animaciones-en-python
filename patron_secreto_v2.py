from manim import *
import numpy as np

MARRON_PROFUNDO = ManimColor("#1A0C06")
MARRON_OSCURO = ManimColor("#381E11")
MARRON_SEMILLA = ManimColor("#59331D")
MARRON_CLARO = ManimColor("#8C5835")
DORADO_PETALO = ManimColor("#F7B32B")
DORADO_PETALO_OSCURO = ManimColor("#C47B14")
AMARILLO_LUZ = ManimColor("#FFE17D")
ROSA_PETALO = ManimColor("#E8A5C8")
ROSA_PETALO_OSCURO = ManimColor("#B85B88")
VERDE_TALLO = ManimColor("#2D5A27")
VERDE_HOJA = ManimColor("#3A7233")
GRIS_BOCETO = ManimColor("#CFCFCF")
CREMA_CONEJO = ManimColor("#F5EBE6")
SOMBRA_CONEJO = ManimColor("#D4C4BC")


class PatronSecreto(MovingCameraScene):
    def construct(self):
        self.camera.background_color = "#07080A"

        # -------------------------------------------------------------
        # TÍTULO FIJO
        # -------------------------------------------------------------
        titulo = Text("El Patrón Oculto en la Naturaleza", font_size=30, color=WHITE)
        titulo.to_edge(UP, buff=0.4)
        titulo.set_z_index(100)
        self.play(Write(titulo))
        self.wait(0.3)

        # -------------------------------------------------------------
        # ESCENA 1: FLOR Y PÉTALOS
        # -------------------------------------------------------------
        def crear_petalo_suave(color_borde, color_relleno, largo=1.6, ancho=0.55):
            petalo = VMobject(stroke_width=0.8, color=color_borde)
            petalo.set_points_smoothly([
                ORIGIN,
                np.array([ancho * 0.3, largo * 0.25, 0]),
                np.array([ancho * 0.55, largo * 0.6, 0]),
                np.array([ancho * 0.15, largo * 0.98, 0]),
                np.array([0, largo, 0]),
                np.array([-ancho * 0.15, largo * 0.98, 0]),
                np.array([-ancho * 0.55, largo * 0.6, 0]),
                np.array([-ancho * 0.3, largo * 0.25, 0]),
                ORIGIN,
            ])
            petalo.set_fill(color=[color_relleno, color_borde], opacity=0.85)
            return petalo

        centro_flor = Circle(radius=0.35, color=MARRON_PROFUNDO, fill_opacity=1, stroke_width=0)
        estambres = VGroup(*[
            Dot(point=0.22 * np.array([np.cos(a), np.sin(a), 0]), radius=0.02, color=AMARILLO_LUZ)
            for a in np.linspace(0, TAU, 20, endpoint=False)
        ])

        petalos = VGroup()
        sepalos = VGroup()
        num_petalos = 5

        for i in range(num_petalos):
            p = crear_petalo_suave(ROSA_PETALO_OSCURO, ROSA_PETALO)
            p.rotate(i * (2 * PI / num_petalos), about_point=ORIGIN)
            petalos.add(p)

            s = Triangle(color=VERDE_TALLO, fill_opacity=0.9, stroke_width=0)
            s.set(width=0.22, height=0.5)
            s.move_to(UP * 0.16)
            s.rotate(PI)
            s.rotate(i * (2 * PI / num_petalos), about_point=ORIGIN)
            sepalos.add(s)

        flor = VGroup(sepalos, petalos, centro_flor, estambres).scale(0.95).shift(DOWN * 0.3)
        self.play(
            FadeIn(sepalos),
            GrowFromCenter(centro_flor),
            LaggedStart(*[GrowFromCenter(p) for p in petalos], lag_ratio=0.1),
            run_time=1.8,
        )
        self.play(FadeIn(estambres, lag_ratio=0.03))

        num_text = MathTex("5", font_size=64, color=DORADO_PETALO).next_to(flor, RIGHT, buff=1.2)
        etiqueta_petalos = Text("pétalos", font_size=22, color=WHITE).next_to(num_text, DOWN)

        self.play(Write(num_text), FadeIn(etiqueta_petalos))
        self.wait(1)

        # -------------------------------------------------------------
        # TRANSICIÓN A GIRASOL PROPORCIONADO
        # -------------------------------------------------------------
        self.play(
            Unwrite(etiqueta_petalos),
            Unwrite(num_text),
            FadeOut(sepalos),
            FadeOut(petalos),
            FadeOut(estambres),
            centro_flor.animate.scale(0.1).move_to(UP * 0.8),
        )

        centro_girasol = UP * 0.8

        # Tallo proporcionado que nace debajo de la flor
        tallo = VMobject(color=VERDE_TALLO, stroke_width=14)
        tallo.set_points_smoothly([
            centro_girasol + DOWN * 0.8,
            DOWN * 0.8 + LEFT * 0.2,
            DOWN * 2.2 + RIGHT * 0.1,
            DOWN * 4.0 + LEFT * 0.1,
        ])
        tallo.set_z_index(0)

        # Hojas a los lados del tallo
        hoja_izq = VMobject(color=VERDE_HOJA, stroke_width=0)
        hoja_izq.set_points_smoothly([
            DOWN * 0.9 + LEFT * 0.1,
            DOWN * 1.1 + LEFT * 1.5,
            DOWN * 1.8 + LEFT * 1.8,
            DOWN * 1.6 + LEFT * 0.5,
            DOWN * 0.9 + LEFT * 0.1,
        ])
        hoja_izq.set_fill(color=[VERDE_HOJA, VERDE_TALLO], opacity=0.9)
        hoja_izq.set_z_index(0)

        hoja_der = VMobject(color=VERDE_HOJA, stroke_width=0)
        hoja_der.set_points_smoothly([
            DOWN * 1.8 + RIGHT * 0.05,
            DOWN * 2.0 + RIGHT * 1.4,
            DOWN * 2.6 + RIGHT * 1.6,
            DOWN * 2.4 + RIGHT * 0.4,
            DOWN * 1.8 + RIGHT * 0.05,
        ])
        hoja_der.set_fill(color=[VERDE_HOJA, VERDE_TALLO], opacity=0.9)
        hoja_der.set_z_index(0)

        disco_base = Circle(radius=1.1, color=MARRON_PROFUNDO, fill_opacity=1, stroke_width=0).move_to(centro_girasol)
        disco_base.set_z_index(1)

        def crear_petalo_girasol_capa(largo, ancho, col_base, col_punta):
            p = VMobject(stroke_width=0.3, color=DORADO_PETALO_OSCURO)
            p.set_points_smoothly([
                ORIGIN,
                np.array([ancho * 0.45, largo * 0.3, 0]),
                np.array([ancho * 0.3, largo * 0.75, 0]),
                np.array([0, largo, 0]),
                np.array([-ancho * 0.3, largo * 0.75, 0]),
                np.array([-ancho * 0.45, largo * 0.3, 0]),
                ORIGIN,
            ])
            p.set_fill(color=[col_base, col_punta], opacity=0.95)
            return p

        petalos_ext = VGroup()
        petalos_int = VGroup()
        num_petalos_girasol = 34

        for i in range(num_petalos_girasol):
            p_ext = crear_petalo_girasol_capa(1.3, 0.22, DORADO_PETALO, AMARILLO_LUZ)
            p_ext.shift(centro_girasol + UP * 1.0)
            p_ext.rotate(i * (TAU / num_petalos_girasol), about_point=centro_girasol)
            p_ext.set_z_index(2)
            petalos_ext.add(p_ext)

            p_int = crear_petalo_girasol_capa(1.0, 0.18, DORADO_PETALO_OSCURO, DORADO_PETALO)
            p_int.shift(centro_girasol + UP * 0.85)
            p_int.rotate((i + 0.5) * (TAU / num_petalos_girasol), about_point=centro_girasol)
            p_int.set_z_index(3)
            petalos_int.add(p_int)

        angulo_dorado = 2.3999632297286533
        semillas = VGroup()
        num_semillas = 250

        for i in range(1, num_semillas + 1):
            r = 0.068 * np.sqrt(i)
            theta = i * angulo_dorado
            pos = centro_girasol + np.array([r * np.cos(theta), r * np.sin(theta), 0])

            factor = i / num_semillas
            if factor < 0.3:
                color_semilla = MARRON_PROFUNDO.interpolate(MARRON_OSCURO, factor / 0.3)
            else:
                color_semilla = MARRON_OSCURO.interpolate(MARRON_CLARO, (factor - 0.3) / 0.7)

            tam = 0.025 + 0.01 * (i / num_semillas)
            semilla = Ellipse(width=tam, height=tam * 2.2, color=color_semilla, fill_opacity=1, stroke_width=0)
            semilla.rotate(theta + PI / 2)
            semilla.move_to(pos)
            semilla.set_z_index(4)
            semillas.add(semilla)

        girasol_completo = VGroup(tallo, hoja_izq, hoja_der, disco_base, petalos_ext, petalos_int, semillas)

        self.play(Create(tallo), FadeIn(hoja_izq), FadeIn(hoja_der), run_time=0.8)
        self.play(
            FadeIn(disco_base, scale=0.8),
            LaggedStart(*[GrowFromCenter(p) for p in petalos_ext], lag_ratio=0.02),
            run_time=1.4,
        )
        self.play(
            LaggedStart(*[GrowFromCenter(p) for p in petalos_int], lag_ratio=0.02),
            run_time=1.0,
        )
        self.play(
            LaggedStart(*[Create(s) for s in semillas], lag_ratio=0.003),
            run_time=2.2,
        )
        self.wait(1)

        # -------------------------------------------------------------
        # ZOOM A SEMILLA
        # -------------------------------------------------------------
        semilla_target = semillas[140]
        pos_target = semilla_target.get_center()

        self.play(
            self.camera.frame.animate.scale(0.22).move_to(pos_target),
            run_time=1.8,
        )
        self.wait(0.3)

        semilla_dibujo = VMobject(color=GRIS_BOCETO, stroke_width=1.2)
        semilla_dibujo.set_points_smoothly([
            pos_target + np.array([0, -0.18, 0]),
            pos_target + np.array([0.08, -0.07, 0]),
            pos_target + np.array([0.065, 0.08, 0]),
            pos_target + np.array([0.025, 0.17, 0]),
            pos_target + np.array([0, 0.21, 0]),
            pos_target + np.array([-0.025, 0.17, 0]),
            pos_target + np.array([-0.065, 0.08, 0]),
            pos_target + np.array([-0.08, -0.07, 0]),
            pos_target + np.array([0, -0.18, 0]),
        ])
        semilla_dibujo.set_fill(color=[MARRON_SEMILLA, MARRON_PROFUNDO], opacity=1)
        semilla_dibujo.set_z_index(10)

        franjas = VGroup()
        offsets = np.linspace(-0.048, 0.048, 5)
        for j, off in enumerate(offsets):
            col = GRIS_BOCETO if j % 2 == 0 else MARRON_OSCURO
            franja = Line(
                pos_target + np.array([off, -0.12, 0]),
                pos_target + np.array([off * 0.35, 0.18, 0]),
                color=col,
                stroke_width=0.8,
            )
            franjas.add(franja)
        franjas.set_z_index(11)

        brillo = Ellipse(width=0.018, height=0.08, color=WHITE, fill_opacity=0.6, stroke_width=0)
        brillo.move_to(pos_target + np.array([-0.025, 0.03, 0]))
        brillo.set_z_index(12)

        textura_semilla = VGroup(semilla_dibujo, franjas, brillo)

        self.play(Create(semilla_dibujo), run_time=1)
        self.play(Create(franjas), FadeIn(brillo), run_time=0.8)
        self.wait(1.2)

        self.play(
            self.camera.frame.animate.scale(4.55).move_to(ORIGIN),
            FadeOut(textura_semilla),
            FadeOut(girasol_completo),
            FadeOut(centro_flor),
            run_time=1.8,
        )

        # -------------------------------------------------------------
        # ESCENA: CONEJOS Y SECUENCIA DE FIBONACCI
        # -------------------------------------------------------------
        def crear_conejo_realista():
            sombra_suelo = Ellipse(width=1.8, height=0.3, color=BLACK, fill_opacity=0.4, stroke_width=0)
            sombra_suelo.move_to(DOWN * 0.55)

            cuerpo = Ellipse(width=1.1, height=0.82, color=GRIS_BOCETO, stroke_width=1.5,
                             fill_color=CREMA_CONEJO, fill_opacity=1)
            cuerpo.move_to(DOWN * 0.1)
            cuerpo.rotate(-PI / 12)

            cabeza = Circle(radius=0.34, color=GRIS_BOCETO, stroke_width=1.5,
                            fill_color=CREMA_CONEJO, fill_opacity=1)
            cabeza.move_to(UP * 0.45 + RIGHT * 0.35)

            def oreja_detallada(dx, angulo):
                o = Ellipse(width=0.17, height=0.62, color=GRIS_BOCETO, stroke_width=1.5,
                            fill_color=CREMA_CONEJO, fill_opacity=1)
                o.move_to(UP * 1.0 + RIGHT * (0.35 + dx))
                o.rotate(angulo)
                interior = Ellipse(width=0.08, height=0.38, color=SOMBRA_CONEJO,
                                   fill_color=SOMBRA_CONEJO, fill_opacity=1, stroke_width=0)
                interior.move_to(o.get_center())
                return VGroup(o, interior)

            oreja_1 = oreja_detallada(-0.12, -0.15)
            oreja_2 = oreja_detallada(0.1, 0.2)

            cola = Circle(radius=0.1, color=GRIS_BOCETO, stroke_width=1.2,
                          fill_color=WHITE, fill_opacity=1)
            cola.move_to(cuerpo.get_center() + LEFT * 0.58 + DOWN * 0.02)

            pata_trasera = Ellipse(width=0.4, height=0.22, color=GRIS_BOCETO, stroke_width=1.2,
                                   fill_color=SOMBRA_CONEJO, fill_opacity=1)
            pata_trasera.move_to(cuerpo.get_center() + DOWN * 0.38 + LEFT * 0.1)

            pata_delantera = Ellipse(width=0.18, height=0.28, color=GRIS_BOCETO, stroke_width=1.2,
                                     fill_color=CREMA_CONEJO, fill_opacity=1)
            pata_delantera.move_to(cuerpo.get_center() + DOWN * 0.38 + RIGHT * 0.32)

            ojo = Dot(point=cabeza.get_center() + RIGHT * 0.14 + UP * 0.04, radius=0.04, color=MARRON_PROFUNDO)
            brillo_ojo = Dot(point=cabeza.get_center() + RIGHT * 0.15 + UP * 0.05, radius=0.012, color=WHITE)
            nariz = Dot(point=cabeza.get_center() + RIGHT * 0.32, radius=0.028, color=ROSA_PETALO_OSCURO)

            estructura = VGroup(sombra_suelo, pata_trasera, cuerpo, pata_delantera, cola, oreja_1, oreja_2, cabeza)
            detalles = VGroup(ojo, brillo_ojo, nariz)
            return VGroup(estructura, detalles)

        conejo_izq = crear_conejo_realista().scale(1.1).move_to(LEFT * 2.3 + DOWN * 0.2)
        conejo_der = crear_conejo_realista().scale(1.1).move_to(RIGHT * 2.3 + DOWN * 0.2)
        conejo_der.flip(axis=UP)

        corazon = ParametricFunction(
            lambda t: np.array([
                0.22 * (16 * np.sin(t) ** 3),
                0.22 * (13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)),
                0,
            ]),
            t_range=[0, TAU],
            color=RED_B,
            fill_opacity=0.85,
        ).scale(0.2).move_to(UP * 0.2)

        self.play(
            Create(conejo_izq[0]),
            Create(conejo_der[0]),
            run_time=2.0,
        )
        self.play(
            FadeIn(conejo_izq[1]),
            FadeIn(conejo_der[1]),
            DrawBorderThenFill(corazon),
            run_time=0.8,
        )

        self.play(corazon.animate.scale(1.2), rate_func=there_and_back, run_time=0.45)
        self.play(corazon.animate.scale(1.2), rate_func=there_and_back, run_time=0.45)

        secuencia = MathTex("1", ",", "1", ",", "2", ",", "3", ",", "5", ",", "8", ",", "13", r", \dots",
                             font_size=42, color=DORADO_PETALO)
        secuencia.next_to(VGroup(conejo_izq, conejo_der), DOWN, buff=0.6)

        self.play(Write(secuencia), run_time=2.0)
        self.wait(2)